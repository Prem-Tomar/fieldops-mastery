"""Forecast elapsed duration from jointly reviewed gates; never publish issues."""
import argparse
import csv
import json
import math
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = {"understanding", "implementation", "debugging", "tradeoffs", "transfer"}


def forecast(roadmap, progress, ledgers, as_of):
    """Return a forecast dict; reject unsupported gate or completion claims."""
    plan = roadmap["planning"]
    baseline = date.fromisoformat(plan["plannedEndDate"])
    total = len(roadmap["weeks"])
    gates = progress["acceptedGates"]
    if progress["version"] != 1:
        raise ValueError("Unsupported progress version")
    if [gate["slice"] for gate in gates] != list(range(1, len(gates) + 1)) or len(gates) > total:
        raise ValueError("Accepted slices must be consecutive from 1 without omissions")
    start = date.fromisoformat(progress["actualStartDate"]) if progress["actualStartDate"] else None
    if start and start > as_of:
        raise ValueError("Actual start cannot be in the future")
    previous = start
    for gate in gates:
        accepted = date.fromisoformat(gate["acceptedOn"])
        if not start or accepted < previous or accepted > as_of:
            raise ValueError("Gates need an actual start and chronological, nonfuture dates")
        previous = accepted
        if gate["acceptedBy"] != roadmap["reviewer"]:
            raise ValueError("Only the reviewer accepts a gate")
        if set(gate["learners"]) != set(roadmap["learners"]):
            raise ValueError("Each gate needs both learners")
        for learner, evidence in gate["learners"].items():
            scores = evidence["scores"]
            if not isinstance(evidence["evidence"], str) or not evidence["evidence"].strip():
                raise ValueError(f"{learner}: missing gate evidence")
            if set(scores) != DIMENSIONS or any(type(score) is not int or not 2 <= score <= 3 for score in scores.values()):
                raise ValueError(f"{learner}: every dimension must independently pass (2 or 3)")
    completed = len(gates)
    remaining = total - completed
    status = "planned" if not start else "awaiting-first-gate"
    projected = baseline if not start else None
    pace = None
    if completed:
        elapsed = (as_of - start).days + 1
        pace = elapsed / completed
        projected = as_of + timedelta(days=math.ceil(remaining * pace))
        status = "in-progress"
    if completed == total:
        verified = all(
            rows and all(row["status"] in {"independent", "mastered"}
                         and row["evidence"].strip() and row["assessor"].strip() for row in rows)
            for rows in ledgers.values()
        ) and set(ledgers) == set(roadmap["learners"])
        status = "complete" if verified else "concept-audit-pending"
        projected = previous if verified else None
    return {
        "asOf": as_of.isoformat(), "status": status,
        "acceptedSlices": completed, "remainingSlices": remaining,
        "planningEnd": baseline.isoformat(),
        "projectedFinish": projected.isoformat() if projected else None,
        "daysEarlierThanPlan": (baseline - projected).days if projected else None,
        "observedDaysPerSlice": round(pace, 2) if pace else None,
        "scopeUnchanged": True, "issuePublicationPaused": not roadmap["issueCreationAuthorized"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", type=date.fromisoformat,
                        default=datetime.now(timezone(timedelta(hours=5, minutes=30))).date())
    args = parser.parse_args()
    roadmap = json.loads((ROOT / "curriculum/roadmap.json").read_text(encoding="utf-8"))
    progress = json.loads((ROOT / "curriculum/progress.json").read_text(encoding="utf-8"))
    concepts = {concept for task in json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))["tasks"] for concept in task["concepts"]}
    ledgers = {}
    for login, folder in zip(roadmap["learners"], ["learner-5y", "learner-10y"]):
        with (ROOT / "evidence" / folder / "coverage.csv").open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source))
        if len(rows) != len(concepts) or {row["concept"] for row in rows} != concepts:
            raise ValueError(f"{login}: incomplete concept ledger")
        ledgers[login] = rows
    try:
        result = forecast(roadmap, progress, ledgers, args.as_of)
    except (KeyError, TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
