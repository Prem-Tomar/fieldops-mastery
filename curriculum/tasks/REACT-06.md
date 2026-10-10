# REACT-06 — Implement optimistic assignment with rollback

Phase: P04 | Order: 14 | Prerequisite: REACT-05

## Precise task

Immediately show a selected technician and pending status before the API confirms. On failure restore the last confirmed value. Define behavior for overlapping assignments and a server-side competing update.

## Why we are doing this

Optimistic UI requires a correctness policy under failure.

## What you achieve

Responsive assignment with recoverable disagreement.

## What this teaches

- optimistic state
- mutation ordering
- rollback
- state machines
- closures
- accessible status feedback

## Progressive hints

1. Separate confirmed state from local intent.
2. Choose whether overlapping commands are queued, blocked, or superseded.
3. Consider which response is still allowed to update the UI.

## Acceptance criteria

- [ ] Success, rejection, reversed responses, and competing updates follow the written policy.
- [ ] Errors expose retry or conflict resolution.
- [ ] Rollback never restores a value made obsolete by a later accepted operation.

## Independent mastery challenge

Cancel the current view while its mutation completes and keep the shared cache correct.

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
