# REACT-03 — Use effects and custom hooks safely

Phase: P03 | Order: 11 | Prerequisite: REACT-02

## Precise task

Implement useJobSubscription(jobId) against a fake subscription service. Changing jobs replaces the subscription; unmount removes it. Fetch detail data with explicit stale-response protection and cleanup.

## Why we are doing this

Effects synchronize external systems and require correct dependency and lifetime reasoning.

## What you achieve

Reusable hooks without leaked subscriptions or stale updates.

## What this teaches

- useEffect
- dependency arrays
- closures
- useRef
- custom hooks
- StrictMode
- cleanup
- render versus commit

## Progressive hints

1. List the external resource each effect owns.
2. Simulate setup-cleanup-setup before assuming one mount.
3. Prefer deriving values during render when no external synchronization is needed.

## Acceptance criteria

- [ ] After changing job IDs exactly one current subscription remains.
- [ ] Unmount and StrictMode-style replay leave no active resource.
- [ ] Explain and repair missing-dependency and unnecessary-effect examples.

## Independent mastery challenge

Move a cross-component external store subscription to a concurrency-safe subscription API.

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
