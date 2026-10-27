# NODE-03 — Make completion idempotent

Phase: P06 | Order: 23 | Reference prerequisite: NODE-02

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Replay-safe accepted operations

## Precise task

Complete a job and deduct inventory in one transactional operation. Accept an idempotency key scoped to the tenant and operation. Send ten concurrent identical requests; reject key reuse with a different payload.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Clients cannot know whether a timed-out response represents a committed operation.

## What you achieve

One completion and one stock movement despite retries.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **idempotency:** An idempotent operation has no extra business effect when repeated according to its contract. Example: Retry completion without deducting stock twice.
- **transactions:** A transaction groups changes that commit together or are rolled back. Example: Complete a job and record inventory movement atomically.
- **unique constraints:** Database constraints enforce rules even under concurrent application access. Example: Reject duplicate completion keys and negative available stock.
- **atomicity:** Atomicity means grouped changes succeed together or do not take effect. Example: Avoid a completed job without its required stock movement.
- **request fingerprints:** A fingerprint identifies the relevant contents of a request for repeat comparison. Example: Reject the same idempotency key with a different quantity.
- **concurrent promises:** Multiple Promise-producing operations can be in flight at once, requiring bounded admission and error handling. Example: Limit a batch to three active jobs.
- **business-state guards:** State guards reject operations that are not legal for the current business state. Example: A new key cannot complete an already-completed job twice.

## Research hints

1. Search for "idempotency" and "Replay-safe accepted operations"; find a small example and predict its observable result before trying it.
2. Investigate "transactions" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Concurrent duplicates have one effect and a consistent documented result.
- [ ] Different payload reuse is rejected.
- [ ] A new key cannot bypass the rule against completing an already-completed job.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Retry after a lost response and after restarting the API process.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
