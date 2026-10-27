# OPS-01 — Threat-model and test sensitive boundaries

Phase: P10 | Order: 37 | Reference prerequisite: MFE-04

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

An enforced sensitive-resource boundary

## Precise task

Threat-model tenant access, file uploads, credentials, and offline cached data. Add focused checks for malicious uploads, request flooding, leaked logs, revoked sessions, and unauthorized cached-data exposure after logout.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Security depends on several layers agreeing on access and data lifetime.

## What you achieve

Sensitive product paths reject hostile inputs and unauthorized operations in reproducible scenarios.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **threat modelling:** Threat modelling identifies assets, possible attackers and abuse paths so protections address actual product risks.
- **secure storage:** Sensitive credentials need protected storage appropriate to the platform; ordinary preferences are not a secret store. Example: Keep session credentials out of unencrypted draft storage.
- **input and upload limits:** Size, count and format limits bound incoming data so requests cannot exhaust resources or bypass rules.
- **content validation:** Content validation inspects the actual data or file, rather than trusting its name or declared type.
- **credential lifecycle:** Credential lifecycle covers creation, storage, use, rotation, expiry and revocation of secrets or access credentials.
- **CSRF CORS CSP:** CSRF protects authenticated actions, CORS governs browser cross-origin access, and CSP limits allowed content execution. Example: Apply the controls relevant to the deployed browser architecture.
- **least privilege:** Least privilege grants only the permissions needed for a person, service or database operation.
- **dependency security:** Dependency security examines third-party packages, known vulnerabilities and update risks in the application's dependencies.

## Research hints

1. Search for "threat modelling" and "An enforced sensitive-resource boundary"; find a small example and predict its observable result before trying it.
2. Investigate "secure storage" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Each listed threat has an explicit control and verification.
- [ ] Logout and tenant switching follow documented offline-data retention rules.
- [ ] Logs and public fixtures contain no tokens, credentials, or real customer data.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Exploit an injected insecure attachment lookup, then prove the fix covers both metadata and file access.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
