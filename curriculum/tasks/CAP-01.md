# CAP-01 — Support an older client during domain evolution

Phase: P11 | Order: 41 | Prerequisite: OPS-04

## Precise task

Add awaitingApproval to the completion workflow while retaining a declared supported v1 mobile contract. Preserve old queued commands and document how the old client presents jobs requiring approval.

## Why we are doing this

Real deployments contain multiple client and data versions.

## What you achieve

A compatible rollout with explicit limitations.

## What this teaches

- API compatibility
- domain migrations
- local migrations
- feature negotiation
- deprecation
- contract testing

## Progressive hints

1. Compare wire compatibility with business-semantic compatibility.
2. Replay old serialized commands.
3. Write the supported-version policy before adapting the response.

## Acceptance criteria

- [ ] Previous-client fixtures and stored commands still work within the policy.
- [ ] New approval rules cannot be bypassed by the old client.
- [ ] The rollout and deprecation paths are documented and tested.

## Independent mastery challenge

The coach selects a previously unseen field removal or approval-policy change.

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
