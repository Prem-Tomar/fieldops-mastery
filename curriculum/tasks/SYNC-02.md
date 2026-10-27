# SYNC-02 — Synchronize 500 queued operations

Phase: P07 | Order: 26 | Reference prerequisite: SYNC-01

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Bounded retry of pending work

## Precise task

Replay 500 offline operations with bounded concurrency. Preserve required order for operations on the same job while allowing independent jobs to proceed. Classify retryable, permanently rejected, and authorization failures.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Large reconnect batches must not overload servers or silently discard work.

## What you achieve

A resumable synchronizer with visible progress and failures.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **retry and backoff:** Retry transient failures with increasing delays and a bounded stopping policy. Example: Retry an upload after a temporary timeout, not a validation error.
- **jitter:** Jitter adds randomized delay so many clients do not retry at the same instant. Example: Spread reconnect retries after a network outage.
- **idempotency:** An idempotent operation has no extra business effect when repeated according to its contract. Example: Retry completion without deducting stock twice.
- **per-entity ordering:** Ordering is preserved for operations that depend on the same entity while independent entities can proceed. Example: A job start must not overtake its earlier assignment.
- **batching:** Batching combines work to reduce overhead while preserving limits and error visibility. Example: Send bounded groups of queued changes after reconnect.
- **cancellation:** Cancellation defines how unfinished work stops and how owned resources are released. Example: Disposed search must not publish a later response.
- **connectivity signals:** A device connection signal is a hint, not proof that a particular service is reachable. Example: Handle API failure even when the phone reports Wi-Fi.

## Research hints

1. Search for "retry and backoff" and "Bounded retry of pending work"; find a small example and predict its observable result before trying it.
2. Investigate "jitter" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Network loss and restart resume from durable state.
- [ ] Retryable responses follow bounded backoff; permanent errors remain inspectable.
- [ ] No same-job dependent command overtakes its prerequisite.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Return rate-limit responses and verify the client respects server retry guidance.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
