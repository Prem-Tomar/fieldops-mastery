# OPS-02 — Measure end-to-end performance and capacity

Phase: P10 | Order: 38 | Reference prerequisite: OPS-01

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

A measured end-to-end capacity limit

## Precise task

Define a workload of 100 concurrent API users, a 10,000-job web board, and a 5,000-job mobile list. Agree budgets before measuring; an initial API target is p95 below 300 ms for lightweight endpoints on recorded hardware. Diagnose one web, one mobile, and one backend bottleneck.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Latency budgets and capacity claims need reproducible context.

## What you achieve

Baseline and improved performance evidence across all three runtimes.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **load models:** A load model describes realistic request rates, users and workloads for a performance measurement.
- **percentiles:** A percentile describes how much of a measured distribution falls below a value; p95 latency includes 95 percent of requests.
- **profiling:** Profiling measures where time and resources go so changes address actual bottlenecks. Example: Measure row renders before memoizing them.
- **event-loop delay:** Event-loop delay measures how long scheduled JS work is delayed by runtime load. Example: Compare API responsiveness during a synchronous calculation.
- **database plans:** A query plan shows how the database intends to execute a query. Example: Inspect whether a job list scans all rows or uses an index.
- **network cost:** Network cost includes transferred bytes, request overhead and delay between the client and server.
- **memory leaks:** A memory leak retains data that is no longer needed, increasing memory use as the application runs.
- **capacity and cost:** Capacity and cost relate required throughput, resource limits and operating expense under a defined workload.

## Research hints

1. Search for "load models" and "A measured end-to-end capacity limit"; find a small example and predict its observable result before trying it.
2. Investigate "percentiles" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Publish dataset, hardware, build mode, load script, duration, and results.
- [ ] Both developers independently diagnose a different injected bottleneck.
- [ ] Explain any missed budget and the measured limiting resource.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Double the workload and predict the first failure before running the experiment.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
