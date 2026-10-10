# NODE-01 — Build validated HTTP job endpoints

Phase: P06 | Order: 21 | Prerequisite: RN-04

## Precise task

Implement create, list, detail, assign, and complete job endpoints with runtime validation, stable error codes, pagination, request IDs, and centralized error handling. Document response behavior for malformed and missing resources. Include isolated experiments for a Buffer, a filesystem promise, EventEmitter subscription cleanup, headers/cookies, and an oversized JSON body.

## Why we are doing this

Clients need stable HTTP contracts under valid and invalid input.

## What you achieve

A documented API with integrated request-level tests.

## What this teaches

- HTTP semantics
- routing
- middleware
- request lifecycle
- async errors
- configuration
- logging
- dependency injection
- ESM

- headers and cookies
- JSON parsing limits
- Buffer
- filesystem promises
- EventEmitter
- package scripts and lockfiles

## Progressive hints

1. Separate transport validation from business rules.
2. Decide which errors are client conflicts versus internal failures.
3. Exercise thrown synchronous errors and rejected asynchronous operations.

## Acceptance criteria

- [ ] Invalid input, not-found resources, conflicts, and unexpected failures have tested responses.
- [ ] Logs correlate to a request without including credentials.
- [ ] Pagination ordering is deterministic when records share a timestamp.

## Independent mastery challenge

Disconnect a client mid-request and account for cleanup of owned resources.

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
