# CAP-03 — Run an unseen incident investigation

Phase: P11 | Order: 43 | Prerequisite: CAP-02

## Precise task

The coach selects two undisclosed incidents from duplicate delivery, lost response, stale cache, worker crash, remote failure, or database contention. Each developer independently records hypotheses, identifies the cause, proposes a fix, and verifies recovery.

## Why we are doing this

Mastery includes diagnosing unfamiliar behavior without following a recipe.

## What you achieve

Independent incident reports with reproducible evidence.

## What this teaches

- debugging
- distributed failure
- observability
- hypothesis testing
- regression testing
- incident communication

## Progressive hints

1. Identify the earliest violated invariant.
2. Use telemetry to falsify hypotheses.
3. Reduce the reproduction before changing multiple layers.

## Acceptance criteria

- [ ] Each developer explains cause versus symptom and demonstrates a regression check.
- [ ] The fix preserves earlier invariants.
- [ ] The coach states expected outcomes before seeing the solution and accepts justified alternatives.

## Independent mastery challenge

Investigate a second incident where the first proposed fix is plausible but incorrect.

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
