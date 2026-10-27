# MFE-04 — Create mobile feature modules with clear boundaries

Phase: P09 | Order: 36 | Reference prerequisite: MFE-03

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

An explicit mobile feature interface

## Precise task

Split the technician app into jobs, evidence and sync feature packages with explicit public interfaces. Integrate each through its consumer and demonstrate the flow using controlled fixtures. Share contracts/domain rules where useful while preserving native UI and lifecycle behavior; maintainers may supply focused package checks.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Mobile teams benefit from modular ownership, but web runtime loading assumptions cannot simply be copied.

## What you achieve

A modular mobile app and a comparison with web micro frontend deployment.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **package boundaries:** Package boundaries define public imports and prevent consumers from relying on private implementation details.
- **dependency graphs:** A dependency graph shows which packages rely on others; cycles and hidden dependencies make change harder.
- **navigation contracts:** Navigation contracts define route names, parameters and expected destination behavior across mobile features.
- **shared domain code:** Shared domain code contains platform-independent business rules reused by web, mobile and server features.
- **dependency injection:** Dependency injection supplies collaborators through interfaces rather than hardcoded global imports. Example: Inject a fake subscription service into an isolated exercise.
- **native build compatibility:** Native build compatibility means feature code and native dependencies work with the application's platform toolchain and binary.
- **mobile release constraints:** Mobile changes must respect native binary compatibility, platform requirements and the chosen release/update mechanism.

## Research hints

1. Search for "package boundaries" and "An explicit mobile feature interface"; find a small example and predict its observable result before trying it.
2. Investigate "dependency graphs" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Product consumers work through public feature interfaces.
- [ ] A dependency rule detects imports into another feature's internals.
- [ ] Demonstrate which changes require a native rebuild/release and which the selected update mechanism can apply.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Replace the evidence implementation without changing job-domain rules or breaking stored drafts.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
