# OPS-02 — Measure end-to-end performance and capacity

Phase: P10 | Order: 38 | Prerequisite: OPS-01

## Precise task

Define a workload of 100 concurrent API users, a 10,000-job web board, and a 5,000-job mobile list. Agree budgets before measuring; an initial API target is p95 below 300 ms for lightweight endpoints on recorded hardware. Diagnose one web, one mobile, and one backend bottleneck.

## Why we are doing this

Latency budgets and capacity claims need reproducible context.

## What you achieve

Baseline and improved performance evidence across all three runtimes.

## What this teaches

- load models
- percentiles
- profiling
- event-loop delay
- database plans
- network cost
- memory leaks
- capacity and cost

## Progressive hints

1. Separate end-to-end latency from server processing time.
2. Use release builds for native measurements.
3. Change one suspected bottleneck at a time.

## Acceptance criteria

- [ ] Publish dataset, hardware, build mode, load script, duration, and results.
- [ ] Both developers independently diagnose a different injected bottleneck.
- [ ] Explain any missed budget and the measured limiting resource.

## Independent mastery challenge

Double the workload and predict the first failure before running the experiment.

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
