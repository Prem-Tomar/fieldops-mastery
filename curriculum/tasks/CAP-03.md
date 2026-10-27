# CAP-03 — Run an unseen incident investigation

Phase: P11 | Order: 43 | Reference prerequisite: CAP-02

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Diagnosis of an unfamiliar failure

## Precise task

The coach selects two undisclosed incidents from duplicate delivery, lost response, stale cache, worker crash, remote failure, or database contention. Each developer independently records hypotheses, identifies the cause, proposes a fix, and verifies recovery.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Mastery includes diagnosing unfamiliar behavior without following a recipe.

## What you achieve

Independent incident reports with reproducible evidence.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **debugging:** Debugging uses observations and controlled experiments to identify the cause of incorrect behavior.
- **distributed failure:** Distributed failure occurs when connected components fail or disagree independently, including partial success and lost responses.
- **observability:** Observability uses logs, metrics and traces to understand a system's internal behavior from its outputs.
- **hypothesis testing:** In debugging, hypothesis testing proposes a cause, predicts evidence and runs an experiment to confirm or reject it.
- **regression testing:** Regression testing checks that a change has not broken behavior that previously worked.
- **incident communication:** Incident communication describes the observed impact, evidence, response and recovery status clearly to the relevant people.

## Research hints

1. Search for "debugging" and "Diagnosis of an unfamiliar failure"; find a small example and predict its observable result before trying it.
2. Investigate "distributed failure" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Each developer explains cause versus symptom and demonstrates a regression check.
- [ ] The fix preserves earlier invariants.
- [ ] The coach states expected outcomes before seeing the solution and accepts justified alternatives.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Investigate a second incident where the first proposed fix is plausible but incorrect.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
