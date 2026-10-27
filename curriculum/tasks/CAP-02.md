# CAP-02 — Handle disputed inventory and job evidence

Phase: P11 | Order: 42 | Reference prerequisite: CAP-01

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

A traceable compensating business action

## Precise task

Introduce a returned-part workflow and a cancelled job with captured evidence. Define stock reversal rules, authorization, audit history, and user reconciliation. Implement one vertical slice on web, mobile, and API.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

New product rules test whether the domain model can evolve coherently.

## What you achieve

A traceable reversal and dispute-resolution flow.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **domain invariants:** Domain invariants are business rules that must remain true, such as accepted consumption never exceeding available stock.
- **state transitions:** A state transition changes an entity from one valid state to another according to business rules.
- **transactions:** A transaction groups changes that commit together or are rolled back. Example: Complete a job and record inventory movement atomically.
- **compensating actions:** A compensating action creates a new business operation to correct an accepted effect while preserving its history.
- **UX:** User experience includes how clearly a person can understand, complete and recover from a product workflow.
- **audit trails:** An audit history preserves attributable changes and decisions for investigation. Example: Retain the cancellation and attempted completion.
- **cross-platform contracts:** Cross-platform contracts preserve business meaning across web, mobile and server implementations.

## Research hints

1. Search for "domain invariants" and "A traceable compensating business action"; find a small example and predict its observable result before trying it.
2. Investigate "state transitions" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Retries cannot reverse stock twice.
- [ ] Both clients show the same accepted outcome and unresolved conflicts.
- [ ] Each developer defends a different proposed design before choosing the integrated solution.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

The coach introduces a partial return and a revoked technician permission.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
