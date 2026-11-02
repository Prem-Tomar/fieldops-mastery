"""Maintainer checks for queue counts, retry safety and prerequisite metadata."""
import copy
import json
import unittest
from pathlib import Path
from plan_issue_replacements import plan_replacements

POLICY = json.loads((Path(__file__).resolve().parents[1] / "curriculum/queue-policy.json").read_text())


def task(login, sequence, number, state="OPEN", **extra):
    meta = {"kind": "curriculum", "learner": login, "sequence": sequence, **extra}
    return {"number": number, "state": state, "body": "<!-- fieldops-task " + json.dumps(meta) + " -->",
            "assignees": [{"login": login}], "labels": [{"name": "learning"}]}


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.issues = [task(login, n, n + index * 7) for index, login in enumerate(POLICY["learners"]) for n in range(1, 8)]

    def test_full_queues_do_nothing(self):
        self.assertEqual(plan_replacements(self.issues, POLICY)["replacements"], [])

    def test_three_closures_refill_only_the_affected_learners(self):
        for item in self.issues:
            if item["number"] in {1, 8, 9}:
                item["state"] = "CLOSED"
        before = copy.deepcopy(self.issues)
        result = plan_replacements(self.issues, POLICY)
        self.assertEqual([(item["learner"], item["sequence"], item["replenishesIssue"]) for item in result["replacements"]],
                         [("Neha2212-vi", 8, 1), ("madhavichauhan1995", 8, 8), ("madhavichauhan1995", 9, 9)])
        self.assertEqual([item["predecessorIssue"] for item in result["replacements"]], [7, 14, None])
        self.assertEqual(self.issues, before)

    def test_retry_and_reopen_do_not_repeat_a_replacement(self):
        self.issues[0]["state"] = "CLOSED"
        self.issues.append(task("Neha2212-vi", 8, 24, replenishesIssue=1))
        self.assertEqual(plan_replacements(self.issues, POLICY)["replacements"], [])
        self.issues[0]["state"] = "OPEN"
        result = plan_replacements(self.issues, POLICY)
        self.assertEqual(result["replacements"], [])
        self.assertEqual(len(result["attention"]), 1)

    def test_later_closure_appends_after_the_published_tail(self):
        self.issues[0]["state"] = "CLOSED"
        self.issues[1]["state"] = "CLOSED"
        self.issues.append(task("Neha2212-vi", 8, 24, replenishesIssue=1))
        result = plan_replacements(self.issues, POLICY)["replacements"]
        self.assertEqual(len(result), 1)
        self.assertEqual((result[0]["sequence"], result[0]["predecessorIssue"], result[0]["replenishesIssue"]), (9, 24, 2))

    def test_unrelated_closure_is_ignored(self):
        self.issues.append({"number": 100, "state": "CLOSED", "body": "discussion", "assignees": []})
        self.assertEqual(plan_replacements(self.issues, POLICY)["replacements"], [])

    def test_invalid_learning_metadata_stops_publication(self):
        self.issues[0]["body"] = "Missing marker"
        with self.assertRaises(ValueError):
            plan_replacements(self.issues, POLICY)

    def test_duplicate_sequence_is_rejected(self):
        self.issues.append(copy.deepcopy(self.issues[0]))
        with self.assertRaises(ValueError):
            plan_replacements(self.issues, POLICY)

    def test_completed_roadmap_does_not_create_filler(self):
        for item in self.issues:
            item["state"] = "CLOSED"
        self.assertEqual(plan_replacements(self.issues, POLICY, roadmap_complete=True)["replacements"], [])


if __name__ == "__main__":
    unittest.main()
