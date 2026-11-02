# Seven open learning issues per contributor

## Owner authorisation and scope

On **1 November 2026**, Prem-Tomar instructed: “Any closes, we create replacement, keeping 7 issues at any given point in time.” This authorises bounded replacement publication. The target is **seven OPEN learning issues for Neha2212-vi and seven for madhavichauhan1995**, not seven in total. PRs, unrelated bugs and maintainer work do not count.

The structured policy is [queue-policy.json](../curriculum/queue-policy.json). It supersedes the earlier publication pause for this rolling queue only. It does not authorise bulk publication of the roadmap, changing existing task contracts/assignees, closing unfinished tasks, merging PRs, or marking mastery. Only Prem-Tomar merges to master.

## Refill the tail, preserve the next active task

The first batch contained sequences 1–7 per learner. Closing Neha's #1 leaves six open tasks: #2 remains next, while sequence 8 follows #7. Closing Madhavi's #8 and #9 leaves five: #10 remains next, while sequences 8 and 9 follow #14. A replacement is additional future product work, not another implementation of the immediate successor.

New tasks stay **queued** until their prerequisites are reviewed and integrated and any required mastery gate passes. W1 D1–D7 order remains mandatory. Seven open issues do not mean seven active tasks; keep one active curricular task per person. Both learners independently cover all 338 concepts through different product asks.

## Reconciliation procedure

1. Read the learning rules, roadmap, review guide and this policy. Fetch all live issues, including closed tasks; never rely on a stale dashboard snapshot.
2. Count recognised curriculum metadata with the correct single learner assignment. Run `python scripts/plan_issue_replacements.py --issues <snapshot.json>`. This planner reports deficits, the published tail and closure causes; it never creates or closes an issue.
3. For each deficit, author one coherent next product increment after that learner's tail. Use the roadmap, accepted contracts and individual coverage gaps; never publish a whole concept reference or copy the peer's ask.
4. Each issue needs one main idea, purpose/outcome, implementation location, exclusions, explained terms, exact per-function inputs/defaults/outputs/errors/validation order/mutation/timing, worked examples, observable completion, three research hints and separate mastery coaching. Frontend work includes real screen images and relevant states. No standalone tests/documentation tasks or complete solutions in hints.
5. Immediately before each create, refetch issues. Search all states by learner/sequence/task ID and closure cause. If the replacement exists or the queue is full, do not create another. Publish serially, assign only its learner, label it queued, and include metadata below. A creation timeout is ambiguous: search before retrying.
6. Refetch and verify the created issue, assignment, predecessor and count. Continue only until that learner has seven open issues. Record source/number in [queued-tasks.json](../curriculum/queued-tasks.json) and refresh the dated dashboard snapshot through a maintainer PR. Publication records no scores and accepts no gates.

Metadata example; use actual predecessor and closure numbers:

```json
{"schema":1,"kind":"curriculum","learner":"Neha2212-vi","sequence":8,"parentTask":"JS-04","task":"W02-D1-JOB","predecessorIssue":7,"replenishesIssue":1,"roadmapWeek":2}
```

`predecessorIssue` is the previous task at the tail. `replenishesIssue` is the closed task whose queue space this issue fills; they usually differ. Learner/sequence and replenished closure must be unique and stable on retries.

## Timing and exceptional states

During authorised closure handling, refill in the same work session. A recurring check every **15 minutes** is prepared to catch closures made elsewhere; activation requires the owner's pending automation confirmation. Its activation state is recorded in queue-policy.json. Until enabled, refill during authorised work sessions only. A recurring check is reconciliation, not an instantaneous webhook: counts can briefly fall below seven between a closure and a successful run. The computer and desktop app must be running for a local recurring check.

If reopening creates more than seven open issues, stop creating and report the excess; do not discard work or close an unfinished issue to hide it. Missing/duplicate metadata, unavailable access or an unexplainable deficit also needs attention. Failed publication stays retryable. At full roadmap and concept-audit completion, stop replenishing rather than invent filler.

Report replacement creation, failed publication, completion or required owner action; unchanged state produces no report. No duplicate monitor or automatic merge is authorised. Question of the Day stays in PR discussions from D2, answer-free initially and non-blocking for correct implementation; it is never a queue-filling issue.
