# CAP-02 — Handle disputed inventory and job evidence

Phase: P11 | Order: 42 | Prerequisite: CAP-01

## Precise task

Introduce a returned-part workflow and a cancelled job with captured evidence. Define stock reversal rules, authorization, audit history, and user reconciliation. Implement one vertical slice on web, mobile, and API.

## Why we are doing this

New product rules test whether the domain model can evolve coherently.

## What you achieve

A traceable reversal and dispute-resolution flow.

## What this teaches

- domain invariants
- state transitions
- transactions
- compensating actions
- UX
- audit trails
- cross-platform contracts

## Progressive hints

1. Do not edit historical stock movements silently.
2. Separate evidence preservation from job status.
3. Compare compensating entries with destructive updates.

## Acceptance criteria

- [ ] Retries cannot reverse stock twice.
- [ ] Both clients show the same accepted outcome and unresolved conflicts.
- [ ] Each developer defends a different proposed design before choosing the integrated solution.

## Independent mastery challenge

The coach introduces a partial return and a revoked technician permission.

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
