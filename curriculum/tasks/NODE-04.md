# NODE-04 — Protect tenant and role boundaries

Phase: P06 | Order: 24 | Prerequisite: NODE-03

## Precise task

Implement dispatcher, technician, and administrator permissions. Scope list, detail, write, and attachment access to an organization. A technician can modify only their assigned jobs. Document session expiration and revocation.

## Why we are doing this

Authentication does not prove access to a particular resource.

## What you achieve

An API that enforces identity, tenant, role, and resource permissions.

## What this teaches

- authentication versus authorization
- sessions versus tokens
- password hashing when applicable
- RBAC and resource rules
- tenant isolation
- CSRF and CORS
- rate limiting

- TLS basics
- HTTP security headers

## Progressive hints

1. Build an actor-resource-operation matrix.
2. Change IDs in valid requests instead of testing only logged-out access.
3. Never trust a tenant ID merely because the client supplied it.

## Acceptance criteria

- [ ] Cross-tenant IDs fail for reads, writes, lists, and attachments.
- [ ] Role and assignment changes take effect according to a documented policy.
- [ ] Choose a credential transport and demonstrate its relevant CSRF/CORS behavior.

## Independent mastery challenge

Revoke a technician's permissions while an offline operation is waiting to synchronize.

The coach adds one undisclosed variation after both learners submit their own predictions and implementation evidence. Each learner explains every listed concept, predicts an observable behavior, and demonstrates it in code or an experiment. Fixing the shared product alone does not mark either learner's coverage complete.

## Pair collaboration

Both learners complete the same concepts and criteria. Alternate driver/reviewer on shared integration; use isolated spikes for individual alternatives. The second PR adds tests, a validated alternative, or personal evidence rather than duplicating production code. Review each other's reasoning only after independent predictions are recorded. Pairing is allowed; assisted work remains marked assisted until independently repeated.

## Evidence to submit

- Linked personal issue (only after the owner authorizes issue creation), task ID, learner handle, and PR.
- Predictions made before execution; observed output and explanation for every concept.
- Tests or reproducible experiment, runtime/device details, and failures encountered.
- Design alternatives, accepted tradeoffs, and the unseen challenge result.
- Per-concept assessment in the learner's coverage ledger; five-dimension mastery score.

## Coach checkpoint

Record expected behavior before inspecting the solution. Inject a changed constraint, request a diagnosis, and score understanding, implementation, debugging, tradeoffs, and transfer from 0–3. Every dimension must reach 2 independently. Failed concepts receive remediation; experience level never waives a basic concept.
