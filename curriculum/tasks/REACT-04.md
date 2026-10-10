# REACT-04 — Test user behavior and isolate UI failures

Phase: P03 | Order: 12 | Prerequisite: REACT-03

## Precise task

Add component tests for assignment success, rejection, and job switching. Add one browser test through the full fixture workflow. A broken job detail widget must show a recovery fallback while navigation remains usable.

## Why we are doing this

Behavioral evidence matters more than snapshots of markup.

## What you achieve

A tested flow with intentional error boundaries.

## What this teaches

- component testing
- integration testing
- mock boundaries
- error boundaries
- async event errors
- render errors
- test isolation

## Progressive hints

1. Test visible outcomes and interactions.
2. Distinguish exceptions an error boundary catches from rejected async operations.
3. Use controllable failures rather than arbitrary sleeps.

## Acceptance criteria

- [ ] Tests expose an intentionally injected stale-response bug.
- [ ] A render failure is isolated; an API failure receives explicit handling.
- [ ] Recovery resets the failed widget without losing unrelated navigation.

## Independent mastery challenge

Remove an unnecessary mock and explain what confidence the more integrated test adds.

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
