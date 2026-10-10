# REACT-05 — Design server-state caching and invalidation

Phase: P04 | Order: 13 | Prerequisite: REACT-04

## Precise task

Cache paginated jobs by organization, status, and page. Navigate between filters and update one job. Define freshness, refetch, cancellation, and which queries must change after mutation.

## Why we are doing this

Incorrect cache keys and invalidation can display stale or cross-tenant data.

## What you achieve

Correct cache ownership with observable fetch behavior.

## What this teaches

- server state versus client state
- query keys
- pagination
- freshness
- invalidation
- request deduplication
- race conditions

## Progressive hints

1. List every input that changes the response.
2. Separate cached remote data from unsaved local drafts.
3. Inspect actual requests during filter and tenant changes.

## Acceptance criteria

- [ ] Different tenants and filters never share results.
- [ ] The documented mutations refresh or update all affected views.
- [ ] Fast navigation never displays a late result from another query.

## Independent mastery challenge

Switch organizations with in-flight requests and prove old data cannot reappear.

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
