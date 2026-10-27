# MFE-02 — Build independently deployable shell and remotes

Phase: P09 | Order: 34 | Reference prerequisite: MFE-01

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Independent deployment of one web feature

## Precise task

Build a web shell and separately built dispatch and reporting remotes. Load them at runtime with a documented integration mechanism. Deploy a reporting change without rebuilding the shell or dispatch remote.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Independent delivery must be demonstrated rather than inferred from folder structure.

## What you achieve

Two micro frontends with versioned build artifacts and reproducible loading.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **module federation or equivalent:** Module Federation lets separately built applications share code at runtime; alternatives must meet the same integration requirements.
- **runtime manifests:** A runtime manifest tells the shell which feature version to load and where its artifact is located.
- **shared React identity:** The shell and remotes must use compatible React runtime instances so component and Hook behavior remains valid.
- **bundler configuration:** Bundler settings determine how source code becomes executable artifacts, including imports, chunks and shared libraries.
- **lazy loading:** Lazy loading delays acquiring code or data until it is needed. Example: Load reporting UI only when the reporting route is opened.
- **CSS isolation:** CSS isolation prevents a feature's styles from accidentally changing another feature's interface.
- **routing:** Routing selects an endpoint; middleware applies cross-cutting request behavior around handlers. Example: Validate input and attach a request ID before domain work.

## Research hints

1. Search for "module federation or equivalent" and "Independent deployment of one web feature"; find a small example and predict its observable result before trying it.
2. Investigate "runtime manifests" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Record shell and dispatch artifact hashes before and after the reporting-only deployment; they stay unchanged.
- [ ] Direct navigation and browser back work.
- [ ] Styles and React dependencies do not cause cross-app breakage.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Inject an incompatible shared dependency and demonstrate a safe rejection or rollback.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
