# REACT-01 — Build a predictable component and state model

Phase: P03 | Order: 9 | Reference prerequisite: TS-04

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Predictable component state ownership

## Precise task

Build job list, status filter, and job detail components using 20 fixtures. Selecting and filtering must retain the correct job identity. Add a draft notes editor whose reset behavior is explicitly tied to job selection. Compare useState with useReducer and Context for the same state ownership; demonstrate a Rules of Hooks violation and its correction.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Component identity and state ownership determine whether data survives the right interactions.

## What you achieve

A usable job browser with intentional state lifetime.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **JSX:** JSX describes UI elements using syntax transformed into JavaScript; it is not an HTML string. Example: Render a JobRow with properties inside a list.
- **components:** Components package UI behavior and presentation into reusable units. Example: JobDetails receives a selected job and renders its status.
- **props:** Props are inputs passed from a parent to a component. Example: Pass jobId rather than copying unrelated parent state.
- **composition:** Composition builds larger behavior by connecting smaller units through explicit interfaces. Example: A detail view composes a status badge and evidence panel.
- **events:** Events represent user or system actions; handlers decide how state changes. Example: A submit handler prevents default navigation and starts assignment.
- **state:** State is stored information that can change and influence behavior or rendering. Example: Store selectedJobId and an unsaved notes draft.
- **reconciliation:** Reconciliation resolves differences between local and authoritative state through a defined policy. Example: Present a completion conflict for an authorized decision.
- **keys:** Keys identify siblings across list changes; stable domain IDs avoid mismatched identity. Example: Use job.id rather than a changing array position.
- **derived state:** Derived state can be computed from other inputs instead of separately stored. Example: Compute selectedJob from selectedJobId and the job list.
- **immutable updates:** Treat existing data as unchanged and create new values when updating it. Example: Return a new stock object instead of decrementing the input object.
- **Rules of Hooks:** Hooks follow stable calling order and permitted call locations so React can associate state correctly. Example: Do not call useState only when a condition is true.
- **useReducer:** useReducer expresses state changes through actions and a reducer function. Example: An assignment reducer handles pending, success, and conflict.
- **Context:** Context distributes values through a component tree without passing each intermediate prop. Example: Provide the current organization to nested views.

## Research hints

1. Search for "JSX" and "Predictable component state ownership"; find a small example and predict its observable result before trying it.
2. Investigate "components" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Reordering and filtering never move one job's draft to another.
- [ ] Explain every stored value and why it cannot simply be derived.
- [ ] Fix an injected mutation and an unstable-key bug.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Add selection encoded in the URL without creating two conflicting sources of truth.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
