# Mandatory learning and implementation rules

These rules are non-negotiable for both contributors, the reviewer and anyone preparing tasks or review feedback. They apply to repository reference material and future assignments. Existing GitHub issues are left unchanged; apply the method in review without widening an issue's agreed implementation scope. The six-month roadmap and all 338 concepts per contributor remain required.

Apply these cumulatively with the existing curriculum, technology scope, governance, screen-design requirements, exact task contracts and publication restrictions. A new coaching rule does not waive an earlier requirement.

## Tasks build the product one idea at a time

Every learner task must have one primary learning idea and one bounded implementation goal in the real product path. Supporting concepts may be explained, but a long concept list is not permission to bundle unrelated capabilities. Split a broad roadmap slice into small coherent tasks; later tasks extend earlier accepted units. The 44 catalog entries are reference groups, not ready-to-publish assignments or duplicate work for both learners.

Each task must state:

1. **Goal and main idea:** the capability being added and the one idea it primarily teaches.
2. **Context and purpose:** why the capability matters now, what existing behavior it extends and what the contributor achieves.
3. **Bounded implementation:** the affected unit/component and its integration point. For every named function, specify inputs/types/defaults, success and error outputs, validation order, mutation rules and worked valid/invalid examples. Async units also specify cancellation, timing, freshness and recovery.
4. **Out of scope:** name adjacent features, abstractions and optimizations that belong in later tasks. Introduce a boundary only when this task needs it.
5. **Observable completion:** demonstrate accepted behavior and relevant failures in the product path. A written explanation alone cannot substitute for implementation. Screens are accompanied by actual reference images and relevant states when frontend work is assigned.
6. **Explained concepts and research hints:** explain unfamiliar terms with target-project examples. Give three progressive, search-oriented hints: a concept/search phrase, a useful comparison, and a diagnostic question. A hint must help investigation without dictating the full architecture or solution steps.
7. **Separate mastery coaching:** identify the explanation, walkthrough or unseen variation used to assess understanding. These are learning checks, not undisclosed implementation acceptance criteria.

Each learner must be able to trace and explain the task's input, state changes and output. A task that needs a new subsystem merely to demonstrate a basic idea must be reduced to the necessary product increment. Reading a peer's PR does not waive independent coverage; use a short bounded experiment only for a genuine concept gap, not a duplicate production feature.

## Prerequisite order is mandatory

For both contributors the first week is **W1 D1 → D2 → D3 → D4 → D5 → D6 → D7**. D7 request orchestration consumes the earlier domain rules, feature modules and submission adapter; it must not be treated as an independent starting task.

| Contributor | Day 1 through Day 6 prerequisites | Day 7 |
|---|---|---|
| Neha | Existing issues 1 through 6, in order | Existing issue 7 |
| Madhavi | Existing issues 8 through 13, in order | Existing issue 14 |

Prerequisite completion must be reviewed and its integration available before a dependent task becomes active. Preserve already-started later work on its branch and queue it while returning to the earliest unreviewed predecessor. A clearly declared draft/stacked PR may preserve dependent work, but cannot bypass predecessor acceptance or a required mastery gate. Keep one active curricular task per person.

## Implementation completion and mastery are different outcomes

**Implementation complete** means the original bounded goal, stated contracts and product acceptance behavior are met and reviewed. Close that task on its implementation outcome when normal issue handling is authorized; do not keep it open merely to add an unseen product feature or require a formal report.

**Mastery verified** means that contributor independently explains/predicts the behavior and handles the planned walkthrough or unseen variation at the required rubric threshold. Record assistance and gaps honestly. Coaching may remain pending after implementation completion. An unseen variation can be a discussion or disposable experiment; it must not silently expand the accepted product requirement.

If an unseen check reveals a defect in the original acceptance behavior, point to that original requirement and explain the concrete defect. If it introduces a genuinely new product capability, it belongs to an appropriately scoped successor only after publication authorization. If it reveals only a concept gap, record and coach that gap without inventing a new implementation blocker.

Closing an issue or merging a PR does not pass a mastery gate. Both contributors must independently pass every gate and eventually cover all concepts before the finish forecast advances or completion is claimed. Product correctness, security and required platform/recovery checks remain mandatory.

## Reviews coach through precise evidence

Every review must have a high-level outcome, affected product behavior, prerequisite status, validation performed/limits and a separately identified mastery status. Each actionable code finding must identify an exact file/line, requested change, affected components, a brief explanation of unfamiliar terms, observed versus expected behavior or risk, and a research hint. Use the [review guide](REVIEW_GUIDE.md); give enough direction to investigate without supplying the complete implementation.

Distinguish an implementation blocker from a prerequisite blocker, optional suggestion or mastery coaching. Do not request unrelated architecture, mandatory test authoring or documentation as a condition of accepting a bounded learner feature. Review the target skill at the contributor's demonstrated level; years of experience waive neither basics nor independent assessment.

## Question of the Day starts from D2

Follow the [Question of the Day rules](QUESTION_OF_THE_DAY.md). From D2, revisit only concepts encountered in that learner's earlier completed work; D2 reviews D1 learning. Rotate focused reasoning questions across already-covered areas without assuming future topics. Keep answers out of the initial question. The learner answers every part in their own words in the review discussion; preserve the original answer, mark correct/partial/incorrect/missing parts, explain corrections and ask a targeted follow-up. Track and revisit weak understanding independently of task completion. Unanswered learning questions do not block an otherwise correct implementation; actual code defects remain implementation findings. No extra learner-written tests/documents or daily issues are required.

## Validation and successor discipline

Maintainers may own routine test authoring, formatting and documentation. Learners still demonstrate behavior and learn testing concepts in the product context. Report checks actually run, observed results and anything not covered. When a check fails, identify the input/scenario, expected/actual behavior and concrete gap; do not assign a generic testing or documentation issue.

After future explicit publication authorization, implementation closure selects **one** coherent successor for that contributor. Reuse an already published successor, keep prerequisite/mastery gates respected, and deduplicate reopen/reclose events. No unrelated backlog growth or repeated accepted product capability. Current issue creation and editing remain paused: this rule does not authorize any issue mutation or automation. Only Prem-Tomar merges to master.
