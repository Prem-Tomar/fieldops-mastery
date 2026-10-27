# Two-person learning agreement

Neha (@Neha2212-vi, 5 years) and Madhavi (@madhavichauhan1995, 10 years) build one FieldOps product. Both cover all 338 catalog concepts, including basics. Experience changes guidance and challenge depth, not coverage.

Follow the [mandatory learning rules](LEARNING_RULES.md) and [review format](REVIEW_GUIDE.md). Each actual task teaches one primary idea through a bounded product increment, with explicit exclusions and research hints.

## Complementary product work

Follow the [six-month roadmap](ROADMAP.md). Each learner owns a different integrated feature in each week; the 44 source definitions are concept references, not identical assignments to both people.

- Neha initially owns jobs; Madhavi initially owns inventory. Both implement web, mobile, Node and PostgreSQL behavior in their own feature lane.
- Import accepted domain utilities and shared contracts. Do not repeat an existing production unit merely to give the peer an assignment.
- Each PR adds its own behavior, correctness fix, measured improvement or recovery capability. A second PR is not assigned merely to produce tests or documentation.
- Integrate complementary branches and reciprocally review the other feature. Alternate the integration driver weekly, with Neha driving odd weeks and Madhavi even weeks; swap when availability requires it.
- Cross feature boundaries through integration and the final capstone; initial ownership is not a permanent knowledge silo.
- Submit separate PRs targeting master. Prem-Tomar is the reviewer and only merger, never an implementation assignee.

## Independent knowledge

For every named concept, each learner explains it, predicts a result, implements/adapts a bounded behavior, demonstrates it and solves an unseen variation. The peer's accepted feature can provide a case to discuss, but reviewing it alone cannot establish independent mastery.

Use a short experiment only when the product feature does not expose a concept sufficiently. Such experiments stay bounded; duplicate production implementations are not a task requirement. Assisted work remains assisted until independently demonstrated. The 5-year learner critiques senior assumptions; the 10-year learner implements and explains basics too.

Record evidence in the individual [Neha ledger](../evidence/learner-5y/coverage.csv) and [Madhavi ledger](../evidence/learner-10y/coverage.csv). The reviewer can use PR demonstrations and review-session results as evidence; learner-authored evidence documents are not mandatory deliverables. Tests and documentation are not standalone assigned issues. Test-writing suggestions belong in optional PR feedback with a scenario, hint and expected behavior.

## Dependencies and scope

Each feature names prior units and a concrete integration point. Coordinate cross-lane imports before closing; do not implement a duplicate substitute when the peer's dependency is still pending. Keep one active learning task per person; already published later issues remain queued.

The required first-week sequence is D1 → D2 → D3 → D4 → D5 → D6 → D7 for both contributors. D7 is not a starting task. Queue a later branch while predecessors are reviewed and their accepted units become available; do not erase work or bypass prerequisite gates.

No new issues or generation automation are authorized by this roadmap update. The existing 14 week-one issues retain their distinct job/inventory asks. Future issue publication must follow the [issue lifecycle](ISSUE_LIFECYCLE.md).

## Coach responsibilities

Explain unfamiliar terms plainly. State expected behavior before seeing solutions, then introduce one undisclosed input, timing or constraint change within scope. Reproduce findings, distinguish policy decisions from bugs and revise mistaken expectations.

Assess each learner using the same independent pass threshold. Assess the coach's scenario clarity, reproducibility, fairness and willingness to reconsider. Both learners must pass shared gates; a successful feature does not hide the other person's concept gaps.

Implementation completion and mastery are separate outcomes. Review an otherwise correct PR independently of unanswered learning questions. From D2, use [Question of the Day](QUESTION_OF_THE_DAY.md) to revisit earlier completed work in the review discussion. Both learners answer every part in their own words; the reviewer preserves the original response and gives specific corrections and targeted follow-ups. Concept gaps remain visible without becoming surprise implementation requirements.

## Pace and early advancement

The six-month plan uses 26 nominal one-week slices. Once both learners pass a slice and Prem-Tomar accepts its product behavior, start the next available slice immediately. The reviewer records accepted gates and evidence; the forecast recomputes automatically in CI. Speed shortens elapsed time, never coverage or independent mastery requirements. No new issue publication is authorized by faster progress.
