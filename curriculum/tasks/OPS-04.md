# OPS-04 — Rehearse deployment, rollback, and recovery

Phase: P10 | Order: 40 | Reference prerequisite: OPS-03

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Recovery of an accepted deployment

## Precise task

Create CI for actual application type checking, tests, builds, and contract checks when those apps exist. Deploy a staged environment, perform an expand/contract database change, roll back an app release, restore a backup, and send termination during active work.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Delivery is incomplete until failure recovery is demonstrated.

## What you achieve

A rehearsed release and recovery procedure with measured limits.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **CI/CD:** Continuous integration validates changes; continuous delivery or deployment prepares or releases reproducible application artifacts.
- **artifact reproducibility:** Artifact reproducibility means the same declared source, dependencies and build settings produce a repeatable release.
- **configuration:** Configuration supplies environment-specific behavior without hardcoding secrets. Example: Read a database URL from a controlled environment setting.
- **migration safety:** Migration safety preserves valid data and compatible clients while changing database structures or stored values.
- **backups:** A backup is a preserved copy of data that can be used to recover from loss or corruption.
- **restore verification:** Restore verification checks recovered data and business behavior; possessing a backup alone does not prove recovery works.
- **graceful shutdown:** Graceful shutdown stops new work and safely finishes or persists accepted work before exiting. Example: Do not lose acknowledged worker jobs during deployment.
- **recovery objectives:** Recovery objectives specify acceptable data loss and acceptable time to restore a working service.
- **unit versus integration versus end-to-end tests:** Unit checks isolate a small behavior; integration checks connected parts; end-to-end checks exercise a complete user workflow.
- **property-based testing:** Property-based testing generates varied inputs and checks general rules, such as stock never becoming negative.

## Research hints

1. Search for "CI/CD" and "Recovery of an accepted deployment"; find a small example and predict its observable result before trying it.
2. Investigate "artifact reproducibility" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] A failed required check blocks a PR and secrets are not in artifacts.
- [ ] Restore verifies domain invariants and reports actual recovery time/data loss.
- [ ] Shutdown preserves durably acknowledged work and releases resources.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Recover from a faulty migration while an older mobile client continues synchronizing.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
