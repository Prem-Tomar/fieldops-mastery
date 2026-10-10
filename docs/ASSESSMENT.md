# Learning and mastery assessment

Both learners cover every catalog concept through different product features. For each concept assess a plain-language explanation, pre-run prediction, independent implementation/adaptation, observed result and an unseen variation. PR demonstrations and review-session evidence are valid; a separate formal report is not required.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Understanding | Cannot explain | Needs prompts | Explains and predicts independently | Explains edge cases and limits |
| Implementation | Incorrect | Needs assistance | Correct independently | Adapts to changed constraints |
| Debugging | Cannot localize | Needs hints | Diagnoses using evidence | Solves unfamiliar cross-layer failure |
| Tradeoffs | Cannot compare | Repeats advice | Defends alternatives | Identifies evidence that changes the decision |
| Transfer | Cannot apply | Copies recipe | Solves new variation | Generalizes and teaches accurately |

Pass requires every dimension >=2, demonstrated acceptance behavior and individual evidence for every assigned concept. Mastery additionally requires the unseen variation and explanation of limits. Correctness/security failures prevent passing. Peer review or a shared demo alone cannot pass either learner.

The [Neha ledger](../evidence/learner-5y/coverage.csv) and [Madhavi ledger](../evidence/learner-10y/coverage.csv) retain all 338 concepts. The reviewer records the evidence link and assessor. States are not-started, learning, assisted, independent and mastered; a failed retention check may regress a state. Each independently implemented feature contributes its own evidence, while bounded experiments fill gaps without duplicating product units.

Demonstrate invalid inputs, races, recovery and invariants using reproducible scenarios. Optional test-writing PR feedback includes a scenario, hint and expected result. Testing concepts remain part of coverage: learners explain strategies, boundaries and failure examples, and may demonstrate them with reviewer-supplied examples. Automated test authoring and formal documentation are not mandatory task deliverables, and neither is a standalone assigned issue.

Performance evidence identifies workload, hardware, runtime/build mode, duration, baseline and result. Native evidence identifies OS/device; unverified platforms stay pending. Database evidence includes real SQL/result, concurrency scenario or query plan as appropriate to the roadmap's current depth.

Weekly, revisit an earlier basic and advanced concept through a changed input or failure in an existing feature. Remediate gaps in a relevant product slice or bounded experiment; do not assign a repeated accepted feature. The final gate requires both ledgers fully independent or mastered and an unseen cross-feature product improvement from each learner.

Before reviewing code, the coach states expected outcomes and the assumptions behind them. Score scenario clarity, fairness and reproducibility, and revise an incorrect expectation. Years of experience waive nothing.
