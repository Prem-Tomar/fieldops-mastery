# SYNC-03 — Resolve offline completion versus cancellation

Phase: P07 | Order: 27 | Prerequisite: SYNC-02

## Precise task

Simulate a technician completing a job offline while a dispatcher cancels it online. Compare automatic overwrite, version-checked rejection, and human reconciliation. Choose a policy and implement its user flow.

## Why we are doing this

Concurrent edits can express business conflicts that timestamps cannot resolve.

## What you achieve

A documented conflict policy that preserves evidence and intent.

## What this teaches

- optimistic concurrency
- versions
- conflict detection
- domain policy
- audit history
- clock skew
- reconciliation

## Progressive hints

1. Identify which fields can merge independently.
2. Ask whether completion evidence should survive cancellation.
3. Consider why latest timestamp is unreliable across devices.

## Acceptance criteria

- [ ] The conflict is detected rather than silently overwritten.
- [ ] Both histories and completion evidence remain traceable.
- [ ] A user can resolve or escalate the conflict, with authorization checked again.

## Independent mastery challenge

Introduce delete-versus-edit and permission revocation during reconciliation.

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
