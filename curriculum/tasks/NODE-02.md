# NODE-02 — Design schema and prevent inventory races

Phase: P06 | Order: 22 | Prerequisite: NODE-01

## Precise task

Model organizations, users, jobs, technicians, inventory, and stock movements in PostgreSQL. Reserve the final available part using two concurrent requests. Add a migration and inspect the job-list query plan.

## Why we are doing this

Application checks alone cannot preserve invariants during concurrent writes.

## What you achieve

A constrained schema with demonstrated transactional correctness.

## What this teaches

- relational modelling
- foreign keys
- unique and check constraints
- SQL
- indexes
- transactions
- locking
- isolation
- migrations
- query plans

## Progressive hints

1. Write stock and tenant invariants before choosing tables.
2. Force requests to overlap at the read/write boundary.
3. Compare optimistic updates and locks; document any transaction retry policy.

## Acceptance criteria

- [ ] Exactly one of two final-part reservations succeeds.
- [ ] Stock never becomes negative; required relationships are enforced.
- [ ] Show an EXPLAIN plan before and after a justified index and test migration behavior.

## Independent mastery challenge

Generate a deadlock or serialization conflict and retry the complete transaction safely.

The coach adds one undisclosed variation after both learners submit their own predictions and implementation evidence. Each learner explains every listed concept, predicts an observable behavior, and demonstrates it in code or an experiment. Fixing the shared product alone does not mark either learner's coverage complete.

## Pair collaboration

Both learners complete the same concepts and criteria. Alternate driver/reviewer on shared integration; use isolated spikes for individual alternatives. The second PR adds tests, a validated alternative, or personal evidence rather than duplicating production code. Review each other's reasoning only after independent predictions are recorded. Pairing is allowed; assisted work remains marked assisted until independently repeated.

## Evidence to submit

- Linked personal issue (only after the owner authorizes issue creation), task ID, learner handle, and PR.
- Predictions made before execution; observed output and explanation for every concept.
- Tests or reproducible experiment, runtime/device details, and failures encountered.
- Design alternatives, accepted tradeoffs, and the unseen challenge result.
- Per-concept assessment in the learner's coverage ledger; five-dimension mastery score.

## Coach checkpoint

Record expected behavior before inspecting the solution. Inject a changed constraint, request a diagnosis, and score understanding, implementation, debugging, tradeoffs, and transfer from 0–3. Every dimension must reach 2 independently. Failed concepts receive remediation; experience level never waives a basic concept.
