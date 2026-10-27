# CAP-01 — Support an older client during domain evolution

Phase: P11 | Order: 41 | Reference prerequisite: OPS-04

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Compatibility during a domain change

## Precise task

Add awaitingApproval to the completion workflow while retaining a declared supported v1 mobile contract. Preserve old queued commands and document how the old client presents jobs requiring approval.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Real deployments contain multiple client and data versions.

## What you achieve

A compatible rollout with explicit limitations.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **API compatibility:** API compatibility keeps existing clients working when request, response or business behavior changes.
- **domain migrations:** Migrations change stored schema or data in a controlled, versioned way. Example: Add approval state without corrupting existing jobs.
- **local migrations:** Local migrations evolve device storage while preserving supported old data. Example: Upgrade a queued v1 command record.
- **feature negotiation:** Feature negotiation determines which capabilities a client and server both support before using them.
- **deprecation:** Deprecation announces that a capability will be retired and gives consumers a supported transition path.
- **contract testing:** Contract testing verifies producer and consumer agreement at a versioned boundary.

## Research hints

1. Search for "API compatibility" and "Compatibility during a domain change"; find a small example and predict its observable result before trying it.
2. Investigate "domain migrations" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Previous-client fixtures and stored commands still work within the policy.
- [ ] New approval rules cannot be bypassed by the old client.
- [ ] The rollout and deprecation paths are documented and tested.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

The coach selects a previously unseen field removal or approval-policy change.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
