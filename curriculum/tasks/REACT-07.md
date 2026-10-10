# REACT-07 — Compare client rendering and streamed rendering

Phase: P04 | Order: 15 | Prerequisite: REACT-06

## Precise task

Build a small read-only customer job page with slow history data. Compare client rendering with streamed server rendering using Suspense. Record shell delivery, content delivery, hydration, and error behavior.

## Why we are doing this

Rendering architecture changes user experience, caching, and deployment requirements.

## What you achieve

An evidence-based rendering decision for a specific route.

## What this teaches

- lazy loading
- Suspense
- transitions
- streaming SSR
- hydration
- server/client boundaries
- framework integration
- bundle size

## Progressive hints

1. Keep the dispatcher SPA separate from this focused experiment.
2. Measure when useful content appears and when it becomes interactive.
3. Identify which data sources actually integrate with Suspense.

## Acceptance criteria

- [ ] Demonstrate slow history without blocking the useful page shell.
- [ ] Reproduce and fix a hydration mismatch.
- [ ] Explain SSR versus Server Components and when this project benefits from each.

## Independent mastery challenge

Introduce a personalized field and explain how shared caching could leak it.

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
