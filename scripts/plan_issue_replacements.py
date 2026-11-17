"""Plan a bounded queue refill from a GitHub issue snapshot; never mutate GitHub."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = re.compile(r"<!--\s*fieldops-task\s+(\{.*?\})\s*-->", re.DOTALL)


def plan_replacements(issues, policy, roadmap_complete=False):
    learners = policy["learners"]
    target = policy["targetOpenPerLearner"]
    if policy["mode"] != "rolling-open-queue" or type(target) is not int or target != 7:
        raise ValueError("Expected the owner-authorised seven-issue rolling queue")
    grouped = {login: [] for login in learners}
    for issue in issues:
        if "pull_request" in issue:
            continue
        body = issue.get("body") or ""
        match = MARKER.search(body)
        labels = {label if isinstance(label, str) else label["name"] for label in issue.get("labels", [])}
        assignees = {person["login"] for person in issue.get("assignees", [])}
        if not match:
            if "learning" in labels and assignees.intersection(learners):
                raise ValueError(f"Issue {issue['number']}: learning task has no valid metadata")
            continue
        meta = json.loads(match.group(1))
        login = meta.get("learner")
        if meta.get("kind") != "curriculum" or login not in grouped:
            continue
        sequence = meta.get("sequence")
        if type(sequence) is not int or sequence < 1 or assignees != {login}:
            raise ValueError(f"Issue {issue['number']}: invalid sequence or learner assignment")
        if issue["state"].upper() not in {"OPEN", "CLOSED"}:
            raise ValueError(f"Issue {issue['number']}: unsupported state")
        grouped[login].append({**meta, "number": issue["number"], "state": issue["state"].upper()})
    result = {"targetOpenPerLearner": target, "openCounts": {}, "replacements": [], "attention": []}
    for login, tasks in grouped.items():
        tasks.sort(key=lambda item: item["sequence"])
        sequences = [item["sequence"] for item in tasks]
        if not tasks or sequences != list(range(1, len(tasks) + 1)):
            raise ValueError(f"{login}: missing or duplicate published sequence")
        used = [item["replenishesIssue"] for item in tasks if "replenishesIssue" in item]
        numbers = {item["number"] for item in tasks}
        if any(type(number) is not int for number in used) or len(set(used)) != len(used) or not set(used).issubset(numbers):
            raise ValueError(f"{login}: duplicate or unknown replacement cause")
        opened = sum(item["state"] == "OPEN" for item in tasks)
        result["openCounts"][login] = opened
        if roadmap_complete:
            continue
        if opened > target:
            result["attention"].append(f"{login}: {opened} open tasks; do not discard work to reduce the queue")
            continue
        causes = [item for item in tasks if item["state"] == "CLOSED" and item["number"] not in used]
        deficit = target - opened
        if len(causes) < deficit:
            result["attention"].append(f"{login}: insufficient recognised closures to explain the deficit")
            continue
        for offset, cause in enumerate(causes[:deficit], 1):
            result["replacements"].append({
                "learner": login,
                "sequence": tasks[-1]["sequence"] + offset,
                "predecessorSequence": tasks[-1]["sequence"] + offset - 1,
                "predecessorIssue": tasks[-1]["number"] if offset == 1 else None,
                "replenishesIssue": cause["number"],
            })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issues", type=Path, required=True)
    parser.add_argument("--policy", type=Path, default=ROOT / "curriculum/queue-policy.json")
    parser.add_argument("--roadmap-complete", action="store_true")
    args = parser.parse_args()
    issues = json.loads(args.issues.read_text(encoding="utf-8-sig"))
    policy = json.loads(args.policy.read_text(encoding="utf-8"))
    print(json.dumps(plan_replacements(issues, policy, args.roadmap_complete), indent=2))


if __name__ == "__main__":
    main()
