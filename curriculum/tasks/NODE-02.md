# NODE-02 — Design schema and prevent inventory races

Phase: P06 | Order: 22 | Reference prerequisite: NODE-01

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Atomic concurrent stock protection

## Precise task

Model organizations, users, jobs, technicians, inventory, and stock movements in PostgreSQL. Reserve the final available part using two concurrent requests. Add a migration and inspect the job-list query plan.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Application checks alone cannot preserve invariants during concurrent writes.

## What you achieve

A constrained schema with demonstrated transactional correctness.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **relational modelling:** Relational modelling organizes entities and relationships into constrained tables. Example: Link stock movements to jobs and organizations.
- **foreign keys:** A foreign key constrains a reference to a valid related record. Example: A job assignment must reference an existing technician.
- **unique and check constraints:** Database constraints enforce rules even under concurrent application access. Example: Reject duplicate completion keys and negative available stock.
- **SQL:** SQL queries and changes relational data through declared statements. Example: Select jobs in a stable order within an organization.
- **indexes:** Indexes organize data to accelerate selected access patterns, at a write/storage cost. Example: Index the tenant and status columns for a common job query.
- **transactions:** A transaction groups changes that commit together or are rolled back. Example: Complete a job and record inventory movement atomically.
- **locking:** Locks coordinate access when concurrent work would violate a rule. Example: Protect the final stock unit during reservation.
- **isolation:** Isolation determines how concurrent transactions observe and affect one another. Example: Compare update behavior under competing reservations.
- **migrations:** Migrations change stored schema or data in a controlled, versioned way. Example: Add approval state without corrupting existing jobs.
- **query plans:** A query plan shows how the database intends to execute a query. Example: Inspect whether a job list scans all rows or uses an index.

## Research hints

1. Search for "relational modelling" and "Atomic concurrent stock protection"; find a small example and predict its observable result before trying it.
2. Investigate "foreign keys" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Exactly one of two final-part reservations succeeds.
- [ ] Stock never becomes negative; required relationships are enforced.
- [ ] Show an EXPLAIN plan before and after a justified index and test migration behavior.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Generate a deadlock or serialization conflict and retry the complete transaction safely.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
