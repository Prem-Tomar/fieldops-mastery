# MFE-04 — Create mobile feature modules with clear boundaries

Phase: P09 | Order: 36 | Prerequisite: MFE-03

## Precise task

Split the technician app into jobs, evidence, and sync feature packages with explicit public interfaces. Give each feature a focused test harness. Share contracts/domain rules with web where useful, while keeping native UI and lifecycle behavior platform-specific.

## Why we are doing this

Mobile teams benefit from modular ownership, but web runtime loading assumptions cannot simply be copied.

## What you achieve

A modular mobile app and a comparison with web micro frontend deployment.

## What this teaches

- package boundaries
- dependency graphs
- navigation contracts
- shared domain code
- dependency injection
- native build compatibility
- mobile release constraints

## Progressive hints

1. Inspect accidental imports across feature internals.
2. Treat sync as an explicit service boundary.
3. Separate independent testing from independent native app delivery.

## Acceptance criteria

- [ ] Feature tests run through public interfaces.
- [ ] A dependency rule detects imports into another feature's internals.
- [ ] Document what requires a native rebuild/release and what the selected update mechanism can actually change.

## Independent mastery challenge

Replace the evidence implementation without changing job-domain rules or breaking stored drafts.

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
