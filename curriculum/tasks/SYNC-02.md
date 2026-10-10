# SYNC-02 — Synchronize 500 queued operations

Phase: P07 | Order: 26 | Prerequisite: SYNC-01

## Precise task

Replay 500 offline operations with bounded concurrency. Preserve required order for operations on the same job while allowing independent jobs to proceed. Classify retryable, permanently rejected, and authorization failures.

## Why we are doing this

Large reconnect batches must not overload servers or silently discard work.

## What you achieve

A resumable synchronizer with visible progress and failures.

## What this teaches

- retry and backoff
- jitter
- idempotency
- per-entity ordering
- batching
- cancellation
- connectivity signals

## Progressive hints

1. A connectivity indicator does not prove the API is reachable.
2. Do not let one permanently invalid item block unrelated work forever.
3. Reuse durable operation IDs across retries.

## Acceptance criteria

- [ ] Network loss and restart resume from durable state.
- [ ] Retryable responses follow bounded backoff; permanent errors remain inspectable.
- [ ] No same-job dependent command overtakes its prerequisite.

## Independent mastery challenge

Return rate-limit responses and verify the client respects server retry guidance.

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
