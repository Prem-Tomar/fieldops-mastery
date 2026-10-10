# Incremental personal issue lifecycle

## Current state

**No issues or recurring issue-creation automation are started.** Prem-Tomar will explicitly say when to create issues. Separate issues for both learners are required; that scope does not waive the timing instruction.

## After start authorization

1. Map the two provided GitHub usernames to the learner folders.
2. Create one JS-01 issue per learner with the full task and individual evidence requirements.
3. Record task ID, learner, sequence, predecessor, and advancement/closure event in metadata.
4. Enable a closure monitor/webhook only after authorization; record a baseline.
5. Each newly closed recognized personal task produces exactly one successor in that person's sequence.
6. Owner/coach verifies criteria, independent concepts, mastery score, and PR before successful closure.
7. A closure without passing produces one remediation successor for the same task, preserving all missing concepts.
8. After all 44 tasks pass, the successor is a final retention/audit issue. Subsequent closures produce one targeted retention exercise each; do not blindly repeat identical completed work.

## Idempotency and prerequisites

Before creating, search for a successor containing the predecessor issue and closure timestamp. Retries do not create duplicates. Reopening/reclosing an issue with an existing successor does not advance the sequence again.

Prerequisites apply per learner. Keep at most one active curricular task per learner. Shared integration can wait at phase gates; isolated experiments continue.

Use explicit metadata rather than title matching. Ignore unrelated bug/discussion closures. There are 88 initial personal instances, published incrementally; remediation and retention can add more.

## Monitor behavior when activated later

Stay quiet when unchanged. Notify only on successor creation, failure, roadmap completion, or required user action. Failed creation remains retryable. No automatic merges; only Prem-Tomar merges.

No usernames, assignments, or invitations are invented. Issues include full task, why, outcome, concepts, progressive hints, acceptance criteria, mastery/coach checkpoint, prerequisites, and evidence path—not just a link.
