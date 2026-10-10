# SYNC-01 — Persist a durable offline operation queue

Phase: P07 | Order: 25 | Prerequisite: NODE-04

## Precise task

Queue job edits locally with stable operation IDs, tenant, job, payload version, creation time, and pending/sending/accepted/rejected state. Persist before acknowledging locally. Restore after process termination.

## Why we are doing this

Offline usability depends on durable intent rather than in-memory state.

## What you achieve

A restart-safe queue with clear local versus server acknowledgement.

## What this teaches

- local transactions
- state machines
- durability
- serialization
- local database migrations
- app lifecycle

## Progressive hints

1. Specify crash behavior around each state transition.
2. Keep local ordering independent from device wall-clock accuracy.
3. Separate immutable command intent from current UI state.

## Acceptance criteria

- [ ] Termination after local acknowledgement loses no operation.
- [ ] A sending operation is recoverable on restart.
- [ ] Migration preserves previously queued commands and malformed records are surfaced.

## Independent mastery challenge

Fill local storage and explain how the UI avoids reporting an unsaved operation as saved.

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
