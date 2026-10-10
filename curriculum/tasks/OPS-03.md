# OPS-03 — Trace and diagnose a failed workflow

Phase: P10 | Order: 39 | Prerequisite: OPS-02

## Precise task

Propagate correlation across mobile command, API transaction, outbox, and worker. Add structured logs, latency/error metrics, and traces. Reproduce a delayed notification and identify its cause from telemetry.

## Why we are doing this

An incident must be explainable beyond one process's logs.

## What you achieve

A diagnostic path from user action to final side effect.

## What this teaches

- structured logging
- metrics
- tracing
- context propagation
- AsyncLocalStorage
- SLIs and SLOs
- alert design
- privacy

## Progressive hints

1. Trace a single operation through all boundaries.
2. Use low-cardinality metric labels.
3. Choose alerts that indicate user impact rather than every retry.

## Acceptance criteria

- [ ] A command can be traced through the worker using a stable correlation.
- [ ] An injected queue delay and an API error are distinguishable.
- [ ] No tenant PII or credentials are added to diagnostic payloads.

## Independent mastery challenge

Diagnose an incident using only telemetry and the runbook, without opening the source first.

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
