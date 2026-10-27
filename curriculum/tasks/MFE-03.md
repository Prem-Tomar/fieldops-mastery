# MFE-03 — Version contracts and isolate remote failures

Phase: P09 | Order: 35 | Reference prerequisite: MFE-02

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Recovery from an incompatible remote

## Precise task

Define typed and runtime-validated shell/remote events without sharing a global mutable store. Simulate a missing remote, a render exception, and an incompatible contract. Keep shell navigation usable and provide retry or fallback.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Distributed UI releases must tolerate disagreement and partial failure.

## What you achieve

Observable remote loading with compatible contracts and bounded failure.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **event contracts:** An event contract defines a message's name, payload, version and meaning for producers and consumers.
- **schema validation:** A runtime schema checks actual data shapes; static types alone do not inspect incoming JSON. Example: Reject a quantity string at the API boundary.
- **version negotiation:** Version negotiation selects a contract version both communicating components can understand.
- **error boundaries:** A boundary renders a fallback for supported descendant render/lifecycle failures; it does not catch every async error. Example: Keep navigation working when a detail widget fails.
- **timeouts:** A timeout bounds waiting but may leave an uncertain outcome if work committed elsewhere. Example: A timed-out completion might still have succeeded.
- **cache invalidation:** Invalidation marks cached data as outdated after a relevant change. Example: Completing a job invalidates affected status lists.
- **rollbacks:** Rollback restores a safe earlier application or state version after failure; database reversal requires separate reasoning. Example: Revert a failed optimistic change without losing newer accepted data.
- **contract tests:** Contract tests check whether a producer and consumer agree on their shared inputs, outputs and errors.

## Research hints

1. Search for "event contracts" and "Recovery from an incompatible remote"; find a small example and predict its observable result before trying it.
2. Investigate "schema validation" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] All three injected failures leave unrelated routes usable.
- [ ] Supported previous/current contract fixtures demonstrate compatible behavior.
- [ ] A reporting rollback works without a synchronized shell release.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Change an event field and support old and new remotes during a staged rollout.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
