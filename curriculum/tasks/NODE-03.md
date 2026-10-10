# NODE-03 — Make completion idempotent

Phase: P06 | Order: 23 | Prerequisite: NODE-02

## Precise task

Complete a job and deduct inventory in one transactional operation. Accept an idempotency key scoped to the tenant and operation. Send ten concurrent identical requests; reject key reuse with a different payload.

## Why we are doing this

Clients cannot know whether a timed-out response represents a committed operation.

## What you achieve

One completion and one stock movement despite retries.

## What this teaches

- idempotency
- transactions
- unique constraints
- atomicity
- request fingerprints
- concurrent promises
- business-state guards

## Progressive hints

1. Define key scope, retention, and response replay.
2. Enforce the guarantee in storage, not only an in-memory map.
3. Consider a crash after commit but before response.

## Acceptance criteria

- [ ] Concurrent duplicates have one effect and a consistent documented result.
- [ ] Different payload reuse is rejected.
- [ ] A new key cannot bypass the rule against completing an already-completed job.

## Independent mastery challenge

Retry after a lost response and after restarting the API process.

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
