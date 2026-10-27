# REACT-06 — Implement optimistic assignment with rollback

Phase: P04 | Order: 14 | Reference prerequisite: REACT-05

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Rollback of an optimistic change

## Precise task

Immediately show a selected technician and pending status before the API confirms. On failure restore the last confirmed value. Define behavior for overlapping assignments and a server-side competing update.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Optimistic UI requires a correctness policy under failure.

## What you achieve

Responsive assignment with recoverable disagreement.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **optimistic state:** Optimistic state displays expected success before the server confirms, with a recovery policy. Example: Show a technician assignment while its request is pending.
- **mutation ordering:** Mutation ordering decides which overlapping changes may update confirmed or displayed state. Example: A late first assignment cannot overwrite a newer accepted one.
- **rollback:** Rollback restores a safe earlier application or state version after failure; database reversal requires separate reasoning. Example: Revert a failed optimistic change without losing newer accepted data.
- **state machines:** A state machine defines allowed states and transitions rather than scattered flags. Example: A queued operation moves from pending to sending to accepted.
- **closures:** A function can retain access to bindings from the scope where it was created. Example: A counter function remembers its private count between calls.
- **accessible status feedback:** Status feedback must be perceivable without depending only on color or sight. Example: Announce pending assignment and errors with appropriate semantics.

## Research hints

1. Search for "optimistic state" and "Rollback of an optimistic change"; find a small example and predict its observable result before trying it.
2. Investigate "mutation ordering" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Success, rejection, reversed responses, and competing updates follow the written policy.
- [ ] Errors expose retry or conflict resolution.
- [ ] Rollback never restores a value made obsolete by a later accepted operation.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Cancel the current view while its mutation completes and keep the shared cache correct.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
