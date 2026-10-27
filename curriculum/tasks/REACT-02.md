# REACT-02 — Build an accessible assignment form

Phase: P03 | Order: 10 | Reference prerequisite: REACT-01

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Accessible form submission

## Precise task

Build technician selection, appointment date, and notes fields with validation. Prevent duplicate submission while pending. Show field errors, submission errors, success, loading, and empty-technician states.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Forms connect browser behavior, domain validation, and accessibility.

## What you achieve

A keyboard-usable form with explicit feedback.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **controlled and uncontrolled inputs:** Controlled inputs take their current value from React state; uncontrolled inputs retain it in the host input. Example: Choose a controlled notes field for live validation.
- **form events:** Events represent user or system actions; handlers decide how state changes. Example: A submit handler prevents default navigation and starts assignment.
- **validation:** Validation checks incoming data against explicit rules before business code accepts or changes it.
- **refs:** A ref retains a mutable value across renders without its changes causing a render. Example: Keep a timer handle or input reference in useRef.
- **focus:** Focus determines where keyboard input goes; intentional movement makes recovery and navigation usable. Example: Move focus to an invalid field after submission.
- **routing:** Routing selects an endpoint; middleware applies cross-cutting request behavior around handlers. Example: Validate input and attach a request ID before domain work.
- **URL state:** URL state represents shareable navigation/filter values in the address. Example: Encode selected job and status filter in query parameters.
- **accessibility:** Accessibility makes interactions understandable and usable with different input methods and assistive technology. Example: Label controls and support keyboard navigation.
- **loading and empty states:** Loading means data is pending; empty means loading completed without matching data. Example: Show a loading indicator separately from no matching jobs.
- **portals:** A portal renders UI into another host container while retaining its React relationship. Example: Render an assignment dialog above the main page layout.
- **focus management:** Focus determines where keyboard input goes; intentional movement makes recovery and navigation usable. Example: Move focus to an invalid field after submission.

## Research hints

1. Search for "controlled and uncontrolled inputs" and "Accessible form submission"; find a small example and predict its observable result before trying it.
2. Investigate "form events" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] All controls work by keyboard and have accessible names.
- [ ] Invalid fields preserve entered values; failed submission allows retry.
- [ ] Deep-link navigation and browser back restore the intended job.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Introduce a slow validation request and prevent its result from overwriting validation for newer input.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
