# Complementary learner issue lifecycle

## Current publication state

Fourteen week-one issues have been created and assigned: seven to Neha (@Neha2212-vi, #1–7) and seven to Madhavi (@madhavichauhan1995, #8–14). Both collaborators have accepted their invitations. Prem-Tomar is the reviewer, not an implementation assignee.

**Further issue creation and issue-generation automation are paused until Prem-Tomar explicitly authorizes them.** Updating the roadmap does not grant publication authorization. Keep curriculum/catalog.json and curriculum/roadmap.json creation gates false for further publication.

## Planning a future successor

Use the [22-week roadmap](ROADMAP.md) and current feature state. Give each learner a different ask that integrates with accepted units; both cover the same concept requirements independently. The 44 source definitions organize concept references; publication counts follow the complementary product slices. Do not publish a generic source task verbatim or create test/documentation assignments.

Every issue must include learner, distinct task ID, roadmap week, predecessor, product integration, plain-language concept explanations, per-function inputs/outputs/errors, worked examples, progressive hints, acceptance and mastery/coach criteria. Web/mobile implementation issues also include reference screen images and important states. Test-writing feedback remains optional in the PR.

## Closure behavior after future authorization

1. Validate that the closed issue is a recognized learner task and identify its learner and predecessor metadata.
2. Require owner review of behavior, independent concept evidence, mastery result and integrated PR before successful advancement.
3. First search for an existing successor in that learner's published batch. If present, make that queued issue ready instead of creating another.
4. If none exists and creation is explicitly authorized, create exactly one distinct product successor for that learner, with the predecessor and closure event recorded.
5. If the gate failed, choose one targeted remediation slice/experiment with precise missing concepts and hints; do not advance or repeat an accepted capability wholesale.
6. At the final roadmap gate, use concept gaps and product needs to choose a retention/remediation successor rather than copying a completed task.

The requested one-successor-per-closure policy applies only when further publication is authorized and no planned successor already exists. The existing seven-day batch must not be duplicated.

## Idempotency, prerequisites and assignments

Before creation, search by learner, predecessor and closure event. Retries and reopen/reclose events must not create duplicate successors. Ignore unrelated discussion/bug closures. Use explicit metadata, not title matching.

Keep at most one active curricular issue per learner; future published issues remain queued until prerequisites pass. Cross-lane integrations may wait for the peer's accepted unit. Do not count a peer's completed work as the learner's mastery.

Assign implementation only to the specified collaborator. If the invitation is pending, record intended ownership and awaiting-acceptance status; never assign the reviewer instead. Do not invent usernames or send duplicate invitations.

## Monitor behavior when activated later

No monitor is activated by this change. When explicitly activated, remain quiet while unchanged and notify only for successor creation, failure, roadmap completion or required action. Failed creation stays retryable. Only Prem-Tomar merges to master; no automation merges.
