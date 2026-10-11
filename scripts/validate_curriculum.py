"""Validate curriculum integrity using Python's standard library only."""

import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


catalog = read_json("curriculum/catalog.json")
tasks = catalog["tasks"]
phases = catalog["phases"]
phase_ids = {phase["id"] for phase in phases}
check(len(phase_ids) == len(phases), "Duplicate phase IDs")
ids = [task["id"] for task in tasks]
check(len(ids) == len(set(ids)), "Duplicate task IDs")
check(catalog["owner"] == "Prem-Tomar", "Unexpected repository owner")
check(catalog["issueCreationAuthorized"] is False,
      "Issue creation must remain gated until the owner's explicit instruction")
fields = ["id", "phase", "title", "problem", "why", "outcome", "mastery", "workflow"]
concept_map = {}

for index, task in enumerate(tasks):
    task_id = task["id"]
    for field in fields:
        check(isinstance(task.get(field), str) and bool(task[field].strip()),
              f"{task_id}: missing {field}")
    check(task["phase"] in phase_ids, f"{task_id}: unknown phase")
    check(task["order"] == index + 1, f"{task_id}: invalid sequence")
    expected = [] if index == 0 else [tasks[index - 1]["id"]]
    check(task["dependsOn"] == expected, f"{task_id}: broken prerequisites")
    for field, minimum in [("concepts", 1), ("hints", 3), ("acceptance", 3)]:
        values = task.get(field, [])
        check(isinstance(values, list) and len(values) >= minimum,
              f"{task_id}: insufficient {field}")
        check(all(isinstance(value, str) and value.strip() for value in values),
              f"{task_id}: blank {field}")
        check(len(values) == len(set(values)), f"{task_id}: duplicate {field}")
    doc = ROOT / "curriculum" / "tasks" / f"{task_id}.md"
    check(doc.is_file(), f"{task_id}: missing task document")
    if doc.is_file():
        text = doc.read_text(encoding="utf-8")
        for field in ["title", "problem", "why", "outcome", "mastery"]:
            check(task[field] in text, f"{task_id}: document differs from catalog {field}")
        for field in ["concepts", "hints", "acceptance"]:
            for value in task[field]:
                check(value in text, f"{task_id}: undocumented {field}: {value}")
        for heading in ["Pair collaboration", "Evidence to submit", "Coach checkpoint"]:
            check(f"## {heading}" in text, f"{task_id}: missing {heading}")
    for concept in task["concepts"]:
        concept_map.setdefault(concept, []).append(task_id)

roadmap = read_json("curriculum/roadmap.json")
learners = ["Neha2212-vi", "madhavichauhan1995"]
check(roadmap["reviewer"] == catalog["owner"], "Unexpected roadmap reviewer")
check(roadmap["learners"] == learners, "Unexpected roadmap learners")
check(roadmap["issueCreationAuthorized"] is False,
      "Further roadmap issue publication must remain paused")
weeks = roadmap["weeks"]
check([week["week"] for week in weeks] == list(range(1, 27)),
      "Roadmap must contain exactly 26 consecutive learning slices")
plan = roadmap["planning"]
check(plan["durationMonths"] == 6 and plan["targetWeeks"] == 26,
      "Planning budget must be six months / 26 nominal weeks")
check(plan["mode"] == "mastery-gated", "Advancement must use mastery gates")
for field in ["advanceImmediatelyOnGatePass", "allowEarlyCompletion",
              "requireBothLearners", "requireAllConcepts"]:
    check(plan[field] is True, f"Missing mastery-gated planning rule: {field}")
check(plan["autoPublishIssues"] is False, "Automatic issue publication remains paused")
stage_ids = ["none", "foundation", "queries", "correctness",
             "sync", "delivery", "operations", "evolution"]
check([stage["id"] for stage in roadmap["postgresStages"]] == stage_ids,
      "PostgreSQL stages must preserve gradual depth")
for stage in roadmap["postgresStages"]:
    for field in ["label", "weeks", "focus", "checkpoint"]:
        check(isinstance(stage.get(field), str) and bool(stage[field].strip()),
              f"PostgreSQL stage {stage['id']}: missing {field}")
planned_tasks = {learner: set() for learner in learners}
deliverables = []
stage_order = []
for week in weeks:
    label = f"Week {week['week']}"
    for field in ["focus", "productOutcome"]:
        check(isinstance(week.get(field), str) and bool(week[field].strip()),
              f"{label}: missing {field}")
    asks = week.get("deliverables", {})
    check(set(asks) == set(learners), f"{label}: missing or extra learner ask")
    for learner in learners:
        ask = asks.get(learner, "")
        check(isinstance(ask, str) and bool(ask.strip()),
              f"{label}: missing product contribution for {learner}")
        deliverables.append(ask)
    references = week.get("referenceTaskIds", [])
    check(bool(references) and len(references) == len(set(references)),
          f"{label}: missing or duplicate concept references")
    check(set(references).issubset(ids), f"{label}: unknown concept reference")
    for learner in learners:
        planned_tasks[learner].update(references)
    stage = week.get("postgresStage")
    check(stage in stage_ids, f"{label}: unknown PostgreSQL stage")
    if stage in stage_ids:
        stage_order.append(stage_ids.index(stage))
check(len(deliverables) == len(set(deliverables)),
      "Learners must have distinct weekly product contributions")
check(stage_order == sorted(stage_order), "PostgreSQL depth moves backwards")
check(set(stage_order) == set(range(len(stage_ids))),
      "A PostgreSQL learning stage is missing")
for learner in learners:
    check(planned_tasks[learner] == set(ids),
          f"{learner}: roadmap omits a concept reference group")
    planned_concepts = {concept for task in tasks
                        if task["id"] in planned_tasks[learner]
                        for concept in task["concepts"]}
    check(planned_concepts == set(concept_map),
          f"{learner}: roadmap does not plan every catalog concept")

reviews = read_json("curriculum/reviews.json")
check(reviews["version"] == 1, "Unexpected dashboard review version")
review_ids = [entry["slice"] for entry in reviews["slices"]]
check(len(review_ids) == len(set(review_ids)), "Duplicate dashboard review slice")
dimensions = {"understanding", "implementation", "debugging", "tradeoffs", "transfer"}
for entry in reviews["slices"]:
    number = entry["slice"]
    check(type(number) is int and 1 <= number <= 26, "Unknown reviewed slice")
    check(bool(entry["learners"]) and set(entry["learners"]).issubset(learners),
          f"Slice {number}: unexpected assessment contributor")
    for login, review in entry["learners"].items():
        check(review["status"] in {"not-started", "in-progress", "ready-for-review", "needs-revision"},
              f"Slice {number} {login}: invalid review status")
        check(set(review["scores"]) == dimensions and all(
            type(score) is int and 0 <= score <= 3 for score in review["scores"].values()),
            f"Slice {number} {login}: invalid review scores")
        check(review["assessedBy"] == catalog["owner"],
              f"Slice {number} {login}: unexpected reviewer")
        check(isinstance(review["evidence"], str) and isinstance(review["notes"], str),
              f"Slice {number} {login}: invalid evidence or feedback")
        if review["status"] == "ready-for-review":
            check(bool(review["evidence"].strip()), f"Slice {number} {login}: missing individual evidence")

issue_snapshot = read_json("curriculum/issue-status.json")
numbers = [issue["number"] for issue in issue_snapshot["items"]]
check(len(numbers) == len(set(numbers)), "Duplicate issue in dashboard snapshot")
for issue in issue_snapshot["items"]:
    check(type(issue["number"]) is int and issue["number"] > 0, "Invalid issue number")
    check(issue["state"] in {"OPEN", "CLOSED"}, "Invalid dashboard issue state")
    check(issue["url"] == f"https://github.com/Prem-Tomar/fieldops-mastery/issues/{issue['number']}",
          "Unexpected dashboard issue URL")

states = {"not-started", "learning", "assisted", "independent", "mastered"}
for learner in ["learner-5y", "learner-10y"]:
    ledger = ROOT / "evidence" / learner / "coverage.csv"
    with ledger.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))
    names = [row["concept"] for row in rows]
    check(len(names) == len(set(names)), f"{learner}: duplicate concepts")
    check(set(names) == set(concept_map), f"{learner}: incomplete or extra concept coverage")
    for row in rows:
        concept = row["concept"]
        check(row["tasks"].split() == concept_map.get(concept, []),
              f"{learner}: incorrect task mapping for {concept}")
        check(row["status"] in states, f"{learner}: invalid status for {concept}")
        if row["status"] in {"independent", "mastered"}:
            check(bool(row["evidence"].strip() and row["assessor"].strip()),
                  f"{learner}: unsupported mastery claim for {concept}")

for path in ROOT.rglob("*.md"):
    if any(part in {".git", ".local", "node_modules", "dist", "build"}
           for part in path.relative_to(ROOT).parts):
        continue
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        if target:
            check((path.parent / target).exists(),
                  f"{path.relative_to(ROOT)}: broken link {target}")

owner_rule = read_json(".github/governance/owner-only-master.json")
quality_rule = read_json(".github/governance/master-quality.json")
check(owner_rule["bypass_actors"] == [
    {"actor_id": 6422761, "actor_type": "User", "bypass_mode": "pull_request"}
], "Owner-only rule has an unexpected bypass actor")
check(owner_rule["rules"] == [{"type": "update"}], "Missing update restriction")
check(quality_rule["bypass_actors"] == [], "Quality rules must not have bypass actors")
for rule in [owner_rule, quality_rule]:
    check(rule["target"] == "branch" and rule["enforcement"] == "active",
          "Rules must target branches and be active")
    check(rule["conditions"]["ref_name"] == {
        "include": ["refs/heads/master"], "exclude": []
    }, "Rules must target master")
rule_types = {rule["type"] for rule in quality_rule["rules"]}
check({"deletion", "non_fast_forward", "required_linear_history", "pull_request",
       "required_status_checks"}.issubset(rule_types), "Missing master safeguards")
checks = next(rule for rule in quality_rule["rules"]
              if rule["type"] == "required_status_checks")
check(checks["parameters"]["required_status_checks"] == [
    {"context": "curriculum-validation"}
], "Required check does not match workflow")
workflow = (ROOT / ".github/workflows/curriculum-validation.yml").read_text()
check("name: curriculum-validation" in workflow, "Missing matching CI job name")
check("python scripts/validate_curriculum.py" in workflow, "CI does not run validator")
check("python scripts/forecast_roadmap.py" in workflow, "CI does not recalculate forecast")
check("python scripts/test_dashboard.py" in workflow, "CI does not verify dashboard writes")
check("python scripts/export_dashboard.py" in workflow, "CI does not export progress dashboard")

if errors:
    print("Curriculum validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"Validated {len(phases)} reference areas, {len(tasks)} concept groups, "
      f"{len(weeks)} roadmap weeks, {len(deliverables)} distinct contributions, "
      f"{len(stage_ids)} PostgreSQL stages, "
      f"{len(concept_map)} planned concepts per learner, "
      "two ledgers, links, and governance. Actual mastery requires review evidence.")
