# REACT-04 — Isolate UI failures and recover the affected widget

Phase: P03 | Order: 12 | Reference prerequisite: REACT-03

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Recoverable widget failure isolation

## Precise task

Make a broken job-detail or inventory widget show a recoverable fallback while unrelated navigation remains usable. Handle an asynchronous request failure explicitly. Demonstrate assignment, rejection and feature-switching behavior with controlled fixtures; maintainers may supply component/browser checks.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Behavioral evidence matters more than snapshots of markup.

## What you achieve

A tested flow with intentional error boundaries.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **component testing:** Component testing exercises a UI unit's observable behavior with controlled inputs. Example: Discuss how an assignment widget should react to rejection.
- **integration testing:** Integration testing exercises connected parts and their boundaries. Example: Verify the API and database agree on inventory reservations.
- **mock boundaries:** A mock replaces a dependency; the chosen boundary determines which real behavior is verified. Example: Control a network response without replacing all UI behavior.
- **error boundaries:** A boundary renders a fallback for supported descendant render/lifecycle failures; it does not catch every async error. Example: Keep navigation working when a detail widget fails.
- **async event errors:** An async event operation can reject outside render-error boundary handling. Example: Handle a failed assignment request explicitly.
- **render errors:** Render errors occur while calculating or processing a component's UI. Example: A broken detail widget throws before it can display.
- **test isolation:** Isolation prevents one verification scenario's state from contaminating another. Example: Reset database fixtures between independent scenarios.

## Research hints

1. Search for "component testing" and "Recoverable widget failure isolation"; find a small example and predict its observable result before trying it.
2. Investigate "integration testing" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] An injected stale response cannot replace the current feature state.
- [ ] A render failure is isolated; an API failure receives explicit handling.
- [ ] Recovery resets the failed widget without losing unrelated navigation.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Remove an unnecessary mock and explain what confidence the more integrated test adds.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
