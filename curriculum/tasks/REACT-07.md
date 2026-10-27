# REACT-07 — Compare client rendering and streamed rendering

Phase: P04 | Order: 15 | Reference prerequisite: REACT-06

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Useful page content during a slow render

## Precise task

Build a small read-only customer job page with slow history data. Compare client rendering with streamed server rendering using Suspense. Record shell delivery, content delivery, hydration, and error behavior.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Rendering architecture changes user experience, caching, and deployment requirements.

## What you achieve

An evidence-based rendering decision for a specific route.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **lazy loading:** Lazy loading delays acquiring code or data until it is needed. Example: Load reporting UI only when the reporting route is opened.
- **Suspense:** Suspense coordinates fallback UI for supported suspending work through React/framework integration. Example: Show a history fallback while streamed history is pending.
- **transitions:** Transitions mark suitable React updates as lower priority so urgent interaction can proceed. Example: Keep typing responsive while a large filter result updates.
- **streaming SSR:** Streaming server rendering sends useful HTML progressively rather than waiting for all sections. Example: Deliver the job summary before slow history finishes.
- **hydration:** Hydration connects client React behavior to existing server-rendered markup. Example: Match initial server/client content to avoid mismatch.
- **server/client boundaries:** Boundaries decide which work runs on the server and which requires browser interaction. Example: Keep credentialed data access on an appropriate server boundary.
- **framework integration:** A framework supplies routing, rendering, and data-loading conventions around React. Example: Use supported data loading for a Suspense experiment.
- **bundle size:** Bundle size affects transfer, parsing, and startup cost. Example: Measure the initial download before adding a large library.

## Research hints

1. Search for "lazy loading" and "Useful page content during a slow render"; find a small example and predict its observable result before trying it.
2. Investigate "Suspense" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Demonstrate slow history without blocking the useful page shell.
- [ ] Reproduce and fix a hydration mismatch.
- [ ] Explain SSR versus Server Components and when this project benefits from each.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Introduce a personalized field and explain how shared caching could leak it.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
