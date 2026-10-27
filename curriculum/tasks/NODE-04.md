# NODE-04 — Protect tenant and role boundaries

Phase: P06 | Order: 24 | Reference prerequisite: NODE-03

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Resource authorization within a tenant

## Precise task

Implement the selected dispatcher, technician or administrator resource permission within an organization. A technician can modify only their assigned jobs. Demonstrate the selected access boundary and its session expiration/revocation behavior; extend other routes in later bounded increments.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Authentication does not prove access to a particular resource.

## What you achieve

An API that enforces identity, tenant, role, and resource permissions.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **authentication versus authorization:** Authentication establishes identity; authorization decides whether that identity may perform an action. Example: A logged-in technician still cannot edit another tenant's job.
- **sessions versus tokens:** Sessions and tokens are ways to carry identity; expiration, storage, and revocation depend on the design. Example: Define how a revoked mobile session stops queued commands.
- **password hashing when applicable:** Password hashing stores a one-way, deliberately expensive verifier instead of a recoverable password. Example: Use a suitable maintained password-hashing implementation if passwords are supported.
- **RBAC and resource rules:** Role permissions describe categories of actions; resource rules check the particular object's ownership or assignment. Example: Technician role alone does not permit changing every job.
- **tenant isolation:** Tenant isolation prevents one organization's data from leaking into another's operations. Example: Scope API queries, files, caches, and subscriptions by organization.
- **CSRF and CORS:** CSRF abuses ambient credentials for unwanted actions; CORS controls browser cross-origin response access, not API authorization. Example: Choose relevant protections for cookie-based mutation requests.
- **rate limiting:** Rate limiting bounds how often callers can consume a service. Example: Limit abusive upload or login traffic with a documented response.
- **TLS basics:** TLS protects transport confidentiality and integrity and authenticates endpoints through certificate validation. Example: Use validated HTTPS for mobile API calls.
- **HTTP security headers:** Security headers tell browsers about content, framing, transport, and related restrictions. Example: Choose content and framing policies for the web shell.

## Research hints

1. Search for "authentication versus authorization" and "Resource authorization within a tenant"; find a small example and predict its observable result before trying it.
2. Investigate "sessions versus tokens" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Cross-tenant IDs fail for reads, writes, lists, and attachments.
- [ ] Role and assignment changes take effect according to a documented policy.
- [ ] Choose a credential transport and demonstrate its relevant CSRF/CORS behavior.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Revoke a technician's permissions while an offline operation is waiting to synchronize.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
