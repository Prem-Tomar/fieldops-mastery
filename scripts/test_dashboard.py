"""Exercise reviewer writes and gate/forecast behavior in isolated temporary records."""
import copy
import json
import shutil
import tempfile
import threading
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from http.server import ThreadingHTTPServer

import dashboard_server as dashboard
from export_dashboard import export_dashboard
from forecast_roadmap import forecast

FIXED_DATE = date(2026, 10, 14)


class DashboardTests(unittest.TestCase):
    def setUp(self):
        workspace_temp = dashboard.ROOT / ".local"
        workspace_temp.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="dashboard-test-", dir=workspace_temp)
        self.root = Path(self.temp.name)
        for path in ["curriculum/roadmap.json", "curriculum/catalog.json",
                     "evidence/learner-5y/coverage.csv", "evidence/learner-10y/coverage.csv"]:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(dashboard.ROOT / path, target)
        (self.root / "curriculum/progress.json").write_text(json.dumps({"version": 1, "actualStartDate": None, "acceptedGates": []}))
        (self.root / "curriculum/reviews.json").write_text(json.dumps({"version": 1, "slices": []}))
        self.store = dashboard.Store(self.root)
        self.clock = patch("dashboard_server.today", return_value=FIXED_DATE)
        self.clock.start()

    def tearDown(self):
        self.clock.stop()
        self.root.resolve().relative_to((dashboard.ROOT / ".local").resolve())
        self.temp.cleanup()

    def payload(self, **values):
        return {"revision": self.store.revision(), **values}

    def assessment(self, login, score=2, number=1):
        return self.payload(slice=number, learner=login, status="ready-for-review",
            scores={dimension: score for dimension in dashboard.DIMENSIONS},
            evidence=f"Individual review for {login} / slice {number}", notes="Unseen variation demonstrated")

    def ready(self, number=1):
        for login in dashboard.FOLDERS:
            self.store.save_review(self.assessment(login, number=number), dashboard.OWNER)

    def gate(self, number=1, **changes):
        return self.payload(slice=number, actualStartDate="2026-10-11",
                            checks={"product": True, "concepts": True, "platforms": True}, **changes)

    def test_gate_persists_and_shrinks_forecast(self):
        self.ready()
        self.store.accept_gate(self.gate(), dashboard.OWNER)
        reloaded = dashboard.Store(self.root).state()
        self.assertEqual(reloaded["forecast"]["acceptedSlices"], 1)
        self.assertGreater(reloaded["forecast"]["daysEarlierThanPlan"], 0)
        self.assertEqual(reloaded["progress"]["acceptedGates"][0]["acceptedBy"], dashboard.OWNER)
        self.assertTrue(reloaded["forecast"]["issuePublicationPaused"])

    def test_missing_or_assisted_learner_blocks_acceptance(self):
        first, second = dashboard.FOLDERS
        self.store.save_review(self.assessment(first), dashboard.OWNER)
        with self.assertRaisesRegex(ValueError, "both contributors"):
            self.store.accept_gate(self.gate(), dashboard.OWNER)
        self.store.save_review(self.assessment(second, score=1), dashboard.OWNER)
        with self.assertRaisesRegex(ValueError, "independently pass"):
            self.store.accept_gate(self.gate(), dashboard.OWNER)
        self.assertEqual(self.store.state()["progress"]["acceptedGates"], [])

    def test_gate_order_duplicate_checks_and_dates(self):
        self.ready()
        with self.assertRaisesRegex(ValueError, "next consecutive"):
            self.store.accept_gate(self.gate(2), dashboard.OWNER)
        bad = self.gate(); bad["checks"]["platforms"] = False
        with self.assertRaisesRegex(ValueError, "platform"):
            self.store.accept_gate(bad, dashboard.OWNER)
        bad = self.gate(); bad["actualStartDate"] = "2027-01-01"
        with self.assertRaisesRegex(ValueError, "future"):
            self.store.accept_gate(bad, dashboard.OWNER)
        self.store.accept_gate(self.gate(), dashboard.OWNER)
        with self.assertRaisesRegex(ValueError, "next consecutive"):
            self.store.accept_gate(self.gate(), dashboard.OWNER)

    def test_owner_only_and_stale_edits(self):
        first = next(iter(dashboard.FOLDERS))
        stale = self.assessment(first)
        with self.assertRaisesRegex(ValueError, "reviewer"):
            self.store.save_review(stale, first)
        self.store.save_review(self.assessment(first), dashboard.OWNER)
        with self.assertRaisesRegex(ValueError, "STALE"):
            self.store.save_review(stale, dashboard.OWNER)

    def test_concept_evidence_is_individual_and_can_regress(self):
        first, second = dashboard.FOLDERS
        concept = self.store.state()["ledgers"][first][0]["concept"]
        missing = self.payload(learner=first, concept=concept, status="mastered", evidence="")
        with self.assertRaisesRegex(ValueError, "individual evidence"):
            self.store.save_concept(missing, dashboard.OWNER)
        self.store.save_concept(self.payload(learner=first, concept=concept, status="independent", evidence="Review session"), dashboard.OWNER)
        state = self.store.state()
        self.assertEqual(state["ledgers"][first][0]["status"], "independent")
        self.assertEqual(state["ledgers"][second][0]["status"], "not-started")
        self.store.save_concept(self.payload(learner=first, concept=concept, status="assisted", evidence="Retention gap"), dashboard.OWNER)
        self.assertEqual(self.store.state()["ledgers"][first][0]["status"], "assisted")

    def test_closed_issues_never_accept_gates(self):
        self.store.issues = {"syncedAt": "2026-10-14", "items": [{"number": 1, "state": "CLOSED"}]}
        self.assertEqual(self.store.state()["forecast"]["acceptedSlices"], 0)

    def test_snapshot_is_read_only_and_escapes_evidence(self):
        first = next(iter(dashboard.FOLDERS))
        record = self.assessment(first)
        record["evidence"] = "</script><script>alert('bad')</script>"
        self.store.save_review(record, dashboard.OWNER)
        path = export_dashboard(self.root)
        snapshot = path.read_text(encoding="utf-8")
        self.assertIn('"canReview": false', snapshot)
        self.assertIn('"token": null', snapshot)
        self.assertIn("\\u003c/script\\u003e", snapshot)
        self.assertNotIn(record["evidence"], snapshot)

    def test_forecast_stalls_and_final_audit(self):
        self.ready(); self.store.accept_gate(self.gate(), dashboard.OWNER)
        roadmap, progress, _, _, ledgers = self.store.models()
        later = forecast(roadmap, progress, ledgers, date(2027, 1, 1))
        self.assertLess(later["daysEarlierThanPlan"], 0)
        progress["acceptedGates"] = [dict(copy.deepcopy(progress["acceptedGates"][0]), slice=n) for n in range(1, 27)]
        result = forecast(roadmap, progress, ledgers, FIXED_DATE)
        self.assertEqual(result["status"], "concept-audit-pending")
        self.assertIsNone(result["projectedFinish"])

    def test_http_write_security_and_refresh(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), dashboard.Handler)
        server.store, server.actor, server.auth_error = self.store, dashboard.OWNER, None
        server.token = "test-token"
        server.host_header = f"127.0.0.1:{server.server_port}"
        server.origin = f"http://{server.host_header}"
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        login = next(iter(dashboard.FOLDERS))
        def request(headers):
            return urlopen(Request(server.origin + "/api/reviews", data=json.dumps(self.assessment(login)).encode(), headers=headers), timeout=5)
        try:
            with patch("dashboard_server.github", return_value={"login": dashboard.OWNER}):
                headers = {"Content-Type": "application/json", "X-Review-Token": server.token}
                with self.assertRaises(HTTPError) as error:
                    request(headers)
                self.assertEqual(error.exception.code, 403)
                headers["Origin"] = "http://malicious.example"
                with self.assertRaises(HTTPError): request(headers)
                headers["Origin"] = server.origin
                headers["X-Review-Token"] = "incorrect"
                with self.assertRaises(HTTPError): request(headers)
                headers["X-Review-Token"] = server.token
                with request(headers) as response: self.assertEqual(response.status, 200)
                with urlopen(server.origin + "/api/state") as response:
                    self.assertEqual(json.load(response)["reviews"]["slices"][0]["learners"][login]["scores"]["transfer"], 2)
            with patch("dashboard_server.github", return_value={"login": login}):
                with self.assertRaises(HTTPError) as error: request(headers)
                self.assertEqual(error.exception.code, 403)
        finally:
            server.shutdown(); server.server_close(); thread.join()


if __name__ == "__main__":
    unittest.main()
