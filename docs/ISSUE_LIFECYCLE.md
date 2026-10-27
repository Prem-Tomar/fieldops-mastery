# Complementary learner issue lifecycle

## Current publication state

Fourteen week-one issues have been created and assigned: seven to Neha (@Neha2212-vi, #1–7) and seven to Madhavi (@madhavichauhan1995, #8–14). Both collaborators have accepted their invitations. Prem-Tomar is the reviewer, not an implementation assignee.

**Further issue creation and issue-generation automation are paused until Prem-Tomar explicitly authorizes them.** Updating the roadmap does not grant publication authorization. Keep curriculum/catalog.json and curriculum/roadmap.json creation gates false for further publication.

## Planning a future successor

Use the [six-month roadmap](ROADMAP.md) and current feature state. Give each learner a different ask that integrates with accepted units; both cover the same concept requirements independently. The 44 source definitions organize concept references; publication counts follow the complementary product slices. Do not publish a generic source task verbatim or create test/documentation assignments.

Future publication must satisfy the [mandatory learning rules](LEARNING_RULES.md): one primary idea, small product goal/context, explicit exclusions, reviewed predecessor, per-function inputs/outputs/errors and worked examples, explained concepts, three research-oriented hints, observable implementation completion and separate mastery coaching. Web/mobile implementation issues include reference screen images and important states. Test-writing feedback stays optional. Question of the Day starts from D2 and belongs in the review discussion, not a new daily issue. W1 D7 requires D1-D6 in order. No existing issue is edited by this update.

## Closure behavior after future authorization

1. Validate that the closed issue is a recognized learner task and identify its learner and predecessor metadata.
2. Confirm owner acceptance of the original bounded implementation and integrated behavior. Record implementation completion separately from learning/mastery. A missing coaching answer alone is not an implementation failure or a reason to keep adding product requirements.
3. First search for an existing successor in that learner's published batch. Reuse it instead of creating another. It becomes active only when its reviewed implementation prerequisites and any required mastery gate have passed; otherwise keep it queued.
4. If none exists and creation is explicitly authorized, create exactly one distinct product successor for that learner, with the predecessor and closure event recorded.
5. If understanding is incomplete, record targeted coaching in the existing review/ledger flow and revisit the concept. Do not invent an extra implementation issue just for an unanswered learning question. A defect in the original acceptance behavior must identify the concrete unmet requirement.
6. At the final gate, resolve concept gaps with focused coaching or bounded experiments; create a product successor only for a genuine new need with authorization. Never repeat an accepted capability wholesale or claim mastery from closure.

The requested one-successor-per-closure policy applies only when further publication is authorized and no planned successor already exists. The existing seven-day batch must not be duplicated.

## Idempotency, prerequisites and assignments

Before creation, search by learner, predecessor and closure event. Retries and reopen/reclose events must not create duplicate successors. Ignore unrelated discussion/bug closures. Use explicit metadata, not title matching.

Keep at most one active curricular issue per learner; future published issues remain queued until prerequisites pass. Cross-lane integrations may wait for the peer's accepted unit. Do not count a peer's completed work as the learner's mastery.

Assign implementation only to the specified collaborator. If the invitation is pending, record intended ownership and awaiting-acceptance status; never assign the reviewer instead. Do not invent usernames or send duplicate invitations.

## Monitor behavior when activated later

No monitor is activated by this change. When explicitly activated, remain quiet while unchanged and notify only for successor creation, failure, roadmap completion or required action. Failed creation stays retryable. Only Prem-Tomar merges to master; no automation merges.
