# OPS-01 — Threat-model and test sensitive boundaries

Phase: P10 | Order: 37 | Prerequisite: MFE-04

## Precise task

Threat-model tenant access, file uploads, credentials, and offline cached data. Add focused checks for malicious uploads, request flooding, leaked logs, revoked sessions, and unauthorized cached-data exposure after logout.

## Why we are doing this

Security depends on several layers agreeing on access and data lifetime.

## What you achieve

An attack-to-control matrix with reproducible regression tests.

## What this teaches

- threat modelling
- secure storage
- input and upload limits
- content validation
- credential lifecycle
- CSRF CORS CSP
- least privilege
- dependency security

## Progressive hints

1. Start from what an authenticated attacker can change.
2. Do not assume a client bundle can keep a server secret.
3. Test cached data and local files as well as API endpoints.

## Acceptance criteria

- [ ] Each listed threat has an explicit control and verification.
- [ ] Logout and tenant switching follow documented offline-data retention rules.
- [ ] Logs and public fixtures contain no tokens, credentials, or real customer data.

## Independent mastery challenge

Exploit an injected insecure attachment lookup, then prove the fix covers both metadata and file access.

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
