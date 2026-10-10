# OPS-04 — Rehearse deployment, rollback, and recovery

Phase: P10 | Order: 40 | Prerequisite: OPS-03

## Precise task

Create CI for actual application type checking, tests, builds, and contract checks when those apps exist. Deploy a staged environment, perform an expand/contract database change, roll back an app release, restore a backup, and send termination during active work.

## Why we are doing this

Delivery is incomplete until failure recovery is demonstrated.

## What you achieve

A rehearsed release and recovery procedure with measured limits.

## What this teaches

- CI/CD
- artifact reproducibility
- configuration
- migration safety
- backups
- restore verification
- graceful shutdown
- recovery objectives

- unit versus integration versus end-to-end tests
- property-based testing

## Progressive hints

1. Keep application rollback separate from database rollback.
2. Declare recovery-time and data-loss objectives before rehearsal.
3. A backup exists only usefully if a restore succeeds.

## Acceptance criteria

- [ ] A failed required check blocks a PR and secrets are not in artifacts.
- [ ] Restore verifies domain invariants and reports actual recovery time/data loss.
- [ ] Shutdown preserves durably acknowledged work and releases resources.

## Independent mastery challenge

Recover from a faulty migration while an older mobile client continues synchronizing.

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
