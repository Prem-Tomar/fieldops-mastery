# MFE-03 — Version contracts and isolate remote failures

Phase: P09 | Order: 35 | Prerequisite: MFE-02

## Precise task

Define typed and runtime-validated shell/remote events without sharing a global mutable store. Simulate a missing remote, a render exception, and an incompatible contract. Keep shell navigation usable and provide retry or fallback.

## Why we are doing this

Distributed UI releases must tolerate disagreement and partial failure.

## What you achieve

Observable remote loading with compatible contracts and bounded failure.

## What this teaches

- event contracts
- schema validation
- version negotiation
- error boundaries
- timeouts
- cache invalidation
- rollbacks
- contract tests

## Progressive hints

1. Distinguish load errors, render errors, and asynchronous operation failures.
2. Publish the minimum event payload needed.
3. Verify compatibility with the previously deployed shell.

## Acceptance criteria

- [ ] All three injected failures leave unrelated routes usable.
- [ ] Contract tests cover supported previous/current versions.
- [ ] A reporting rollback works without a synchronized shell release.

## Independent mastery challenge

Change an event field and support old and new remotes during a staged rollout.

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
