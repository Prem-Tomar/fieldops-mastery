# OPS-03 — Trace and diagnose a failed workflow

Phase: P10 | Order: 39 | Reference prerequisite: OPS-02

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Tracing a failed product operation

## Precise task

Propagate correlation across mobile command, API transaction, outbox, and worker. Add structured logs, latency/error metrics, and traces. Reproduce a delayed notification and identify its cause from telemetry.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

An incident must be explainable beyond one process's logs.

## What you achieve

A diagnostic path from user action to final side effect.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **structured logging:** Structured logging records consistent named fields so events can be searched and compared reliably.
- **metrics:** Metrics are numeric measurements over time, such as request count, latency or queue depth.
- **tracing:** Tracing connects the steps of one operation across components to show where time or failure occurred.
- **context propagation:** Changes in a context value can update consumers; placement and identity influence the scope. Example: Avoid changing an unrelated global value on every job update.
- **AsyncLocalStorage:** Node's AsyncLocalStorage associates context with an asynchronous operation, such as its request or correlation ID.
- **SLIs and SLOs:** A service-level indicator measures behavior; a service-level objective sets a target for that measurement.
- **alert design:** Alert design identifies a meaningful failure condition, threshold and response without generating unnecessary noise.
- **privacy:** Privacy limits collection, use and exposure of personal or sensitive data, including logs and reports.

## Research hints

1. Search for "structured logging" and "Tracing a failed product operation"; find a small example and predict its observable result before trying it.
2. Investigate "metrics" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] A command can be traced through the worker using a stable correlation.
- [ ] An injected queue delay and an API error are distinguishable.
- [ ] No tenant PII or credentials are added to diagnostic payloads.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Diagnose an incident using only telemetry and the runbook, without opening the source first.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
