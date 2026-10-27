# REACT-08 — Profile a busy dispatch board

Phase: P04 | Order: 16 | Reference prerequisite: REACT-07

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

A measured rendering bottleneck

## Precise task

Render 10,000 fixture jobs using a list or table and simulate updates to 50 jobs per second for one minute. Keep filtering and selection usable. Record a baseline and improve the measured bottleneck.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Performance work should follow measurements.

## What you achieve

A responsive board with justified rendering changes.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **React Profiler:** Profiling measures where time and resources go so changes address actual bottlenecks. Example: Measure row renders before memoizing them.
- **memoization:** Memoization reuses a result when relevant inputs have not changed. Example: Cache an expensive derived summary when justified.
- **referential equality:** Referential equality compares object identity, not a deep comparison of contents. Example: Two separately created {id:1} objects are different references.
- **context propagation:** Changes in a context value can update consumers; placement and identity influence the scope. Example: Avoid changing an unrelated global value on every job update.
- **virtualization:** Virtualization renders a visible window of a large collection rather than every item. Example: Render only nearby rows in a 10,000-job list.
- **transitions:** Transitions mark suitable React updates as lower priority so urgent interaction can proceed. Example: Keep typing responsive while a large filter result updates.
- **bundle splitting:** Bundle splitting divides code into loadable chunks. Example: Separate reporting code from the initial dispatch bundle.
- **memory cleanup:** Cleanup releases resources your operation owns when it completes, fails, or is abandoned. Example: Clear timers, unsubscribe listeners, and close owned cursors.
- **useMemo versus useCallback:** useMemo caches a calculated value; useCallback retains a function identity between relevant changes. Example: Stabilize a callback only when its identity affects measured behavior.

## Research hints

1. Search for "React Profiler" and "A measured rendering bottleneck"; find a small example and predict its observable result before trying it.
2. Investigate "memoization" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Record hardware, dataset, render costs, and interaction latency before and after.
- [ ] No lost visible updates or selection corruption.
- [ ] Explain one optimization rejected because it added complexity without benefit.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Inject an expensive derived calculation and choose between scheduling, caching, or offloading it.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
