# CAP-04 — Defend architecture and prove concept coverage

Phase: P11 | Order: 44 | Reference prerequisite: CAP-03

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

An independently defended cross-feature change

## Precise task

Deliver one agreed bounded change outside the contributor's usual feature lane, using the existing public contracts. Demonstrate its product behavior, then explain the decision and its limits in review. The separate final mastery audit revisits every catalog concept and compares the system's architectural choices; it does not require a duplicate implementation or a formal portfolio report.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Experience and shared commits do not prove individual mastery.

## What you achieve

An accepted cross-feature product improvement with independently explained decisions and separately tracked concept coverage.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **architecture tradeoffs:** Architecture tradeoffs compare the benefits and costs of a design under the product's actual constraints.
- **complexity analysis:** Describe how time and memory requirements grow with input size, rather than relying only on one timing. Example: Repeated linear searches may cost more than building an index once.
- **system boundaries:** System boundaries identify responsibilities and interfaces between components, including where failures and trust assumptions change.
- **cost:** Cost includes implementation effort, operating resources, maintenance burden and the effect of failure.
- **communication:** Communication expresses a problem, evidence, decision and expected behavior clearly enough for others to act.
- **fundamental recall:** Fundamental recall means explaining and applying basic concepts again without relying on memorized recipes.
- **knowledge transfer:** Knowledge transfer enables another person to understand and apply a concept, while checking their independent reasoning.

## Research hints

1. Search for "architecture tradeoffs" and "An independently defended cross-feature change"; find a small example and predict its observable result before trying it.
2. Investigate "complexity analysis" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] The bounded change meets its agreed function and product behavior.
- [ ] The existing consumer integrates the change without an unrelated regression.
- [ ] Relevant authorization, platform and recovery checks demonstrate the accepted behavior.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

The coach changes team size, device constraints, or reliability requirements and asks for a revised architecture.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
