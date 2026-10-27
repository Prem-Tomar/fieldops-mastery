# MFE-01 — Define and challenge micro frontend boundaries

Phase: P09 | Order: 33 | Reference prerequisite: RT-04

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

A product route behind an explicit feature boundary

## Precise task

Place one existing dispatch or reporting route behind an explicit public feature boundary and integrate it with the current shell. Keep navigation and authorization working. Compare a modular build with runtime composition in review; introduce deployment boundaries only when a concrete product task requires them.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Independent deployment can introduce costs that a two-person team must justify.

## What you achieve

A working product route uses an explicit feature boundary whose costs can be demonstrated.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **micro frontends versus modules:** Micro frontends compose separately built web features; modules can share one build and release.
- **build-time versus runtime integration:** Build-time integration bundles features together; runtime integration loads or connects separately built features during execution.
- **ownership:** Ownership identifies who maintains a feature, its public contracts and its recovery behavior.
- **coupling:** Coupling is how strongly one component depends on another; stronger dependencies make independent change harder.
- **shared dependencies:** Shared dependencies are libraries used by multiple features; their versions and runtime instances must remain compatible.
- **architecture decisions:** An architecture decision explains a system choice, alternatives, evidence and consequences for future change.

## Research hints

1. Search for "micro frontends versus modules" and "A product route behind an explicit feature boundary"; find a small example and predict its observable result before trying it.
2. Investigate "build-time versus runtime integration" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] The selected route remains usable through the shell after extraction.
- [ ] The consumer uses only the declared public feature interface.
- [ ] The change preserves the existing navigation and authorization behavior.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Add a third team requirement and identify which boundary would fail first.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
