"""Serve the local reviewer dashboard; read GitHub tasks, never create issues."""
import argparse
import csv
import hashlib
import io
import json
import os
import secrets
import shutil
import subprocess
import threading
from datetime import date, datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from forecast_roadmap import DIMENSIONS, forecast

ROOT = Path(__file__).resolve().parents[1]
OWNER = "Prem-Tomar"
REPOSITORY = "Prem-Tomar/fieldops-mastery"
STATES = {"not-started", "learning", "assisted", "independent", "mastered"}
TASK_STATES = {"not-started", "in-progress", "ready-for-review", "needs-revision"}
FOLDERS = {"Neha2212-vi": "learner-5y", "madhavichauhan1995": "learner-10y"}


def today():
    return datetime.now(timezone(timedelta(hours=5, minutes=30))).date()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_atomic(path, text):
    temporary = path.with_name(path.name + ".pending")
    try:
        with temporary.open("w", encoding="utf-8", newline="") as output:
            output.write(text)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def github(args):
    executable = shutil.which("gh")
    if not executable:
        raise ValueError("GitHub CLI is unavailable. Dashboard is read-only until gh is installed and signed in.")
    result = subprocess.run([executable, *args], capture_output=True, text=True,
                            encoding="utf-8", timeout=25, check=False)
    if result.returncode:
        raise ValueError("GitHub could not be read. Check gh auth status and network access.")
    return json.loads(result.stdout)


class Store:
    def __init__(self, root=ROOT):
        self.root = Path(root)
        self.lock = threading.RLock()
        self.issue_error = None
        self.issues = {"syncedAt": None, "items": []}
        snapshot = self.root / "curriculum/issue-status.json"
        if snapshot.exists():
            self.issues = read_json(snapshot)

    def models(self):
        roadmap = read_json(self.root / "curriculum/roadmap.json")
        progress = read_json(self.root / "curriculum/progress.json")
        reviews = read_json(self.root / "curriculum/reviews.json")
        catalog = read_json(self.root / "curriculum/catalog.json")
        ledgers = {}
        concepts = {concept for task in catalog["tasks"] for concept in task["concepts"]}
        for login, folder in FOLDERS.items():
            with (self.root / "evidence" / folder / "coverage.csv").open(encoding="utf-8", newline="") as source:
                rows = list(csv.DictReader(source))
            if len(rows) != len(concepts) or {row["concept"] for row in rows} != concepts:
                raise ValueError(f"{login}: invalid concept ledger")
            ledgers[login] = rows
        return roadmap, progress, reviews, catalog, ledgers

    def revision(self):
        paths = ["curriculum/progress.json", "curriculum/reviews.json",
                 *[f"evidence/{folder}/coverage.csv" for folder in FOLDERS.values()]]
        digest = hashlib.sha256()
        for path in paths:
            digest.update((self.root / path).read_bytes())
        return digest.hexdigest()

    def state(self):
        with self.lock:
            roadmap, progress, reviews, catalog, ledgers = self.models()
            return {"roadmap": roadmap, "progress": progress, "reviews": reviews,
                    "catalog": catalog, "ledgers": ledgers,
                    "forecast": forecast(roadmap, progress, ledgers, today()),
                    "issues": self.issues, "issueError": self.issue_error,
                    "revision": self.revision()}

    def check_revision(self, payload):
        if payload.get("revision") != self.revision():
            raise ValueError("STALE: Records changed in another tab or outside the dashboard. Refresh before saving.")

    def save_review(self, payload, actor):
        with self.lock:
            if actor != OWNER:
                raise ValueError("Only the repository reviewer saves assessments")
            self.check_revision(payload)
            roadmap, progress, reviews, _, _ = self.models()
            number, login = payload.get("slice"), payload.get("learner")
            if type(number) is not int or not 1 <= number <= len(roadmap["weeks"]) or login not in FOLDERS:
                raise ValueError("Unknown slice or contributor")
            if number <= len(progress["acceptedGates"]):
                raise ValueError("Accepted gate evidence is immutable. Record retention changes in the concept ledger.")
            scores = payload.get("scores", {})
            if set(scores) != DIMENSIONS or any(type(value) is not int or not 0 <= value <= 3 for value in scores.values()):
                raise ValueError("All five scores must be integers from 0 to 3")
            status = payload.get("status")
            if status not in TASK_STATES:
                raise ValueError("Unknown task review status")
            evidence, notes = payload.get("evidence", ""), payload.get("notes", "")
            if not isinstance(evidence, str) or not isinstance(notes, str) or len(evidence) > 2000 or len(notes) > 4000:
                raise ValueError("Evidence or notes are too long or invalid")
            if status == "ready-for-review" and not evidence.strip():
                raise ValueError("Ready-for-review work requires an individual evidence reference")
            entry = next((entry for entry in reviews["slices"] if entry["slice"] == number), None)
            if entry is None:
                entry = {"slice": number, "learners": {}}
                reviews["slices"].append(entry)
                reviews["slices"].sort(key=lambda item: item["slice"])
            entry["learners"][login] = {"status": status, "scores": scores,
                "evidence": evidence.strip(), "notes": notes.strip(),
                "assessedOn": today().isoformat(), "assessedBy": actor}
            write_atomic(self.root / "curriculum/reviews.json", json.dumps(reviews, indent=2) + "\n")

    def save_concept(self, payload, actor):
        with self.lock:
            if actor != OWNER:
                raise ValueError("Only the repository reviewer updates concept evidence")
            self.check_revision(payload)
            login, concept, status = payload.get("learner"), payload.get("concept"), payload.get("status")
            evidence = payload.get("evidence", "")
            if login not in FOLDERS or status not in STATES or not isinstance(evidence, str) or len(evidence) > 2000:
                raise ValueError("Invalid contributor, concept status or evidence")
            if status in {"independent", "mastered"} and not evidence.strip():
                raise ValueError("Independent/mastered concepts need individual evidence")
            _, _, _, _, ledgers = self.models()
            row = next((row for row in ledgers[login] if row["concept"] == concept), None)
            if row is None:
                raise ValueError("Unknown catalog concept")
            row.update(status=status, evidence=evidence.strip(), assessor=actor)
            output = io.StringIO(newline="")
            writer = csv.DictWriter(output, fieldnames=["concept", "tasks", "status", "evidence", "assessor"])
            writer.writeheader()
            writer.writerows(ledgers[login])
            write_atomic(self.root / "evidence" / FOLDERS[login] / "coverage.csv", output.getvalue())

    def accept_gate(self, payload, actor):
        with self.lock:
            self.check_revision(payload)
            roadmap, progress, reviews, _, ledgers = self.models()
            number = len(progress["acceptedGates"]) + 1
            if actor != roadmap["reviewer"]:
                raise ValueError("Only the repository reviewer accepts gates")
            if type(payload.get("slice")) is not int or payload["slice"] != number or number > len(roadmap["weeks"]):
                raise ValueError("Accept only the next consecutive slice")
            checks = payload.get("checks", {})
            if set(checks) != {"product", "concepts", "platforms"} or not all(value is True for value in checks.values()):
                raise ValueError("Confirm integrated product behavior, individual concepts and required platform/recovery checks")
            entry = next((entry for entry in reviews["slices"] if entry["slice"] == number), None)
            if not entry or set(entry["learners"]) != set(FOLDERS):
                raise ValueError("Save separate assessments for both contributors first")
            for login, review in entry["learners"].items():
                if review["status"] != "ready-for-review" or not review["evidence"].strip():
                    raise ValueError(f"{login}: work must be ready and have individual evidence")
                if any(type(value) is not int or value < 2 for value in review["scores"].values()):
                    raise ValueError(f"{login}: every dimension must independently pass with 2 or 3")
            start_text = progress["actualStartDate"] or payload.get("actualStartDate")
            try:
                started = date.fromisoformat(start_text)
            except (TypeError, ValueError):
                raise ValueError("Enter the actual start date") from None
            if started > today():
                raise ValueError("Actual start cannot be in the future")
            progress["actualStartDate"] = started.isoformat()
            progress["acceptedGates"].append({"slice": number, "acceptedOn": today().isoformat(),
                "acceptedBy": actor, "checks": checks,
                "learners": {login: {"evidence": review["evidence"], "scores": review["scores"],
                                     "notes": review["notes"]} for login, review in entry["learners"].items()}})
            forecast(roadmap, progress, ledgers, today())
            write_atomic(self.root / "curriculum/progress.json", json.dumps(progress, indent=2) + "\n")

    def sync_issues(self):
        items = github(["issue", "list", "--repo", REPOSITORY, "--state", "all", "--limit", "1000",
                        "--json", "number,title,state,assignees,url,updatedAt"])
        snapshot = {"syncedAt": datetime.now(timezone.utc).isoformat(), "items": sorted(items, key=lambda item: item["number"])}
        with self.lock:
            write_atomic(self.root / "curriculum/issue-status.json", json.dumps(snapshot, indent=2) + "\n")
            self.issues, self.issue_error = snapshot, None


class Handler(BaseHTTPRequestHandler):
    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def send(self, status, body, content_type="application/json; charset=utf-8"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode()
        elif isinstance(body, str):
            body = body.encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
        self.end_headers()
        self.wfile.write(body)

    def valid_host(self):
        return self.headers.get("Host") == self.server.host_header

    def do_GET(self):
        if not self.valid_host():
            return self.send(403, {"error": "Use the printed local dashboard address"})
        if self.path == "/api/state":
            try:
                state = self.server.store.state()
                state["session"] = {"login": self.server.actor, "canReview": self.server.actor == OWNER,
                                    "token": self.server.token, "authError": self.server.auth_error}
                return self.send(200, state)
            except (ValueError, KeyError, OSError) as error:
                return self.send(500, {"error": str(error)})
        files = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"),
                 "/style.css": ("style.css", "text/css")}
        if self.path in files:
            name, kind = files[self.path]
            return self.send(200, (ROOT / "dashboard" / name).read_bytes(), kind + "; charset=utf-8")
        return self.send(404, {"error": "Not found"})

    def do_POST(self):
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self.send(413, {"error": "Invalid request size"})
        if not 0 < size <= 20000:
            return self.send(413, {"error": "Invalid request size"})
        # Consume bounded bodies before rejecting: closing with unread bytes can reset TCP on Windows.
        raw_body = self.rfile.read(size)
        if not self.valid_host() or self.headers.get("Origin") != self.server.origin:
            return self.send(403, {"error": "Reviewer changes must come from this dashboard"})
        if self.server.actor != OWNER or not secrets.compare_digest(self.headers.get("X-Review-Token", ""), self.server.token):
            return self.send(403, {"error": "Only the authenticated repository owner can save assessments"})
        if self.headers.get("Content-Type") != "application/json":
            return self.send(415, {"error": "Expected JSON"})
        try:
            payload = json.loads(raw_body)
            if not isinstance(payload, dict):
                raise ValueError("Expected an object")
            # Recheck trusted GitHub identity on every write; a form value never establishes authority.
            actor = github(["api", "user"])["login"]
            if actor != OWNER:
                return self.send(403, {"error": "Sign in to gh as the repository owner"})
            actions = {"/api/reviews": self.server.store.save_review,
                       "/api/concepts": self.server.store.save_concept,
                       "/api/gates": self.server.store.accept_gate}
            if self.path == "/api/issues/refresh":
                self.server.store.sync_issues()
            elif self.path in actions:
                actions[self.path](payload, actor)
            else:
                return self.send(404, {"error": "Unknown operation"})
            self.send(200, {"saved": True})
        except (ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
            self.send(409 if str(error).startswith("STALE:") else 400, {"error": str(error)})
        except OSError:
            self.send(500, {"error": "Could not save the record. Check filesystem permissions and retry."})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--skip-issue-sync", action="store_true", help="Use the last GitHub task snapshot")
    args = parser.parse_args()
    store = Store()
    actor, auth_error = None, None
    try:
        actor = github(["api", "user"])["login"]
    except (ValueError, subprocess.TimeoutExpired) as error:
        auth_error = str(error)
    if not args.skip_issue_sync:
        try:
            store.sync_issues()
        except (ValueError, subprocess.TimeoutExpired) as error:
            store.issue_error = str(error)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    server.store, server.actor, server.auth_error = store, actor, auth_error
    server.token = secrets.token_urlsafe(32)
    server.host_header = f"127.0.0.1:{args.port}"
    server.origin = f"http://{server.host_header}"
    print(f"FieldOps dashboard: {server.origin}", flush=True)
    print(f"Reviewer: {actor or 'not signed in'}; records stay in this checkout until committed and merged.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
