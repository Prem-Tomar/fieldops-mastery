# REACT-08 — Profile a busy dispatch board

Phase: P04 | Order: 16 | Prerequisite: REACT-07

## Precise task

Render 10,000 fixture jobs using a list or table and simulate updates to 50 jobs per second for one minute. Keep filtering and selection usable. Record a baseline and improve the measured bottleneck.

## Why we are doing this

Performance work should follow measurements.

## What you achieve

A responsive board with justified rendering changes.

## What this teaches

- React Profiler
- memoization
- referential equality
- context propagation
- virtualization
- transitions
- bundle splitting
- memory cleanup

- useMemo versus useCallback

## Progressive hints

1. Profile before adding useMemo or memo.
2. Separate update ingestion from visible rendering.
3. Test whether a high-level context update rerenders unrelated rows.

## Acceptance criteria

- [ ] Record hardware, dataset, render costs, and interaction latency before and after.
- [ ] No lost visible updates or selection corruption.
- [ ] Explain one optimization rejected because it added complexity without benefit.

## Independent mastery challenge

Inject an expensive derived calculation and choose between scheduling, caching, or offloading it.

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
