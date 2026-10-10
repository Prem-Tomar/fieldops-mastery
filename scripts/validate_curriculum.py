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

if errors:
    print("Curriculum validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"Validated {len(phases)} phases, {len(tasks)} tasks, "
      f"{len(concept_map)} concepts per learner, two ledgers, links, and governance.")
