# SYNC-03 — Resolve offline completion versus cancellation

Phase: P07 | Order: 27 | Reference prerequisite: SYNC-02

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Explicit stale-write conflicts

## Precise task

Simulate a technician completing a job offline while a dispatcher cancels it online. Compare automatic overwrite, version-checked rejection, and human reconciliation. Choose a policy and implement its user flow.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Concurrent edits can express business conflicts that timestamps cannot resolve.

## What you achieve

A documented conflict policy that preserves evidence and intent.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **optimistic concurrency:** An operation checks that the stored version still matches the version it edited. Example: Reject completion based on an outdated cancelled-job version.
- **versions:** Versions identify revisions of data or contracts so changes can be detected and negotiated. Example: Include a job revision with an edit.
- **conflict detection:** Conflict detection recognizes incompatible concurrent intent rather than silently overwriting it. Example: Notice offline completion against online cancellation.
- **domain policy:** Domain policy states the business decision when several technically possible behaviors exist. Example: Decide whether cancellation requires reviewing captured evidence.
- **audit history:** An audit history preserves attributable changes and decisions for investigation. Example: Retain the cancellation and attempted completion.
- **clock skew:** Clock skew means device timestamps can disagree and cannot alone prove global order. Example: Do not choose a conflict winner solely by phone time.
- **reconciliation:** Reconciliation resolves differences between local and authoritative state through a defined policy. Example: Present a completion conflict for an authorized decision.

## Research hints

1. Search for "optimistic concurrency" and "Explicit stale-write conflicts"; find a small example and predict its observable result before trying it.
2. Investigate "versions" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] The conflict is detected rather than silently overwritten.
- [ ] Both histories and completion evidence remain traceable.
- [ ] A user can resolve or escalate the conflict, with authorization checked again.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Introduce delete-versus-edit and permission revocation during reconciliation.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
