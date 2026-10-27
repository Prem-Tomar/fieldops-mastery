# REACT-03 — Use effects and custom hooks safely

Phase: P03 | Order: 11 | Reference prerequisite: REACT-02

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Effect resource lifetime

## Precise task

Implement useJobSubscription(jobId) against a fake subscription service. Changing jobs replaces the subscription; unmount removes it. Fetch detail data with explicit stale-response protection and cleanup.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Effects synchronize external systems and require correct dependency and lifetime reasoning.

## What you achieve

Reusable hooks without leaked subscriptions or stale updates.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **useEffect:** An effect synchronizes a component with an external system after rendering. Example: Subscribe to job updates and return unsubscribe cleanup.
- **dependency arrays:** Effect dependencies describe reactive values used by the effect and when synchronization changes. Example: Changing jobId replaces its subscription.
- **closures:** A function can retain access to bindings from the scope where it was created. Example: A counter function remembers its private count between calls.
- **useRef:** A ref retains a mutable value across renders without its changes causing a render. Example: Keep a timer handle or input reference in useRef.
- **custom hooks:** A custom hook extracts reusable React behavior while retaining normal hook rules. Example: useJobSubscription owns connection setup and cleanup.
- **StrictMode:** StrictMode adds development checks that expose unsafe behavior, including effect lifecycle problems. Example: A setup-cleanup-setup check reveals a leaked subscription.
- **cleanup:** Cleanup releases resources your operation owns when it completes, fails, or is abandoned. Example: Clear timers, unsubscribe listeners, and close owned cursors.
- **render versus commit:** Rendering calculates UI; committing applies an accepted result to the host environment. Example: Avoid opening a subscription during render calculation.

## Research hints

1. Search for "useEffect" and "Effect resource lifetime"; find a small example and predict its observable result before trying it.
2. Investigate "dependency arrays" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] After changing job IDs exactly one current subscription remains.
- [ ] Unmount and StrictMode-style replay leave no active resource.
- [ ] Explain and repair missing-dependency and unnecessary-effect examples.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Move a cross-component external store subscription to a concurrency-safe subscription API.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
