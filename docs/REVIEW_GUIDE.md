# Mandatory review response format

Apply these requirements to every contributor PR. Review the agreed task and prerequisites before judging implementation. Preserve the [learning rules](LEARNING_RULES.md): code acceptance and mastery are different outcomes, and coaching cannot introduce surprise implementation requirements.

## High-level summary

State the implementation outcome (changes needed, ready for implementation acceptance, or blocked on prerequisites), the product behavior reviewed and any required predecessor still missing. Summarize the code findings and their consequences. Identify the exact revision reviewed, checks actually run, expected/actual results and what those checks do not establish. State mastery as unassessed, pending coaching or evidence-backed verified; do not infer it from working code or green CI.

For Week 1, explicitly check D1 through D6 before accepting D7 for either contributor. A later PR with no reviewed prerequisite is a sequence problem, even if its isolated function appears to work. Tell the contributor which earlier capability must be reviewed and why the dependent component needs it; preserve the branch while the correct sequence resumes.

## Precise inline guidance

Use this format for every actionable code finding:

- **Location and category:** exact file and smallest relevant line range; label implementation blocker, prerequisite blocker, optional feedback or mastery coaching.
- **Requested change:** describe the behavior to correct, not a complete replacement solution.
- **Components involved:** name the caller, unit, adapter/module or consumer affected.
- **Term explained:** briefly define any unfamiliar term used in the finding.
- **Behavior or risk:** show a concrete input/timing scenario, expected and observed results, and why the difference matters. Trace it to the original contract for a blocker.
- **Research hint:** provide a useful concept/search phrase or diagnostic question. Leave design decisions and implementation with the learner.

Keep the overall summary as well as inline guidance. Put sequence/process feedback in the summary when it has no meaningful changed code line. Do not attach a fabricated code location. A finding that spans unrelated problems must be split so each ask is independently understandable.

## Coaching and optional validation feedback

After implementation review, ask the contributor to explain a decision, walk through state transitions or predict an unseen input. Record assistance and remaining gaps in the existing review/ledger flow. A missing explanation is a coaching gap, not automatically a code defect. A failed original acceptance scenario is a code defect regardless of how well it is explained.

Optional test-writing feedback must state the scenario, expected result and a research hint, and remain labeled optional. Maintainers may supply the test. Formal reports and test authoring are not required learner deliverables. Never report an unrun check as passing or equate curriculum/dashboard CI with application verification.

## Question of the Day in review

From D2 onward, follow [Question of the Day](QUESTION_OF_THE_DAY.md): select previously completed work, ask one focused reasoning question without its answer, and require every part in the learner's own words in the intended review discussion. Preserve the original response, distinguish correct/partial/incorrect/missing parts, explain corrections and request only a targeted follow-up for the remaining gap. Record understanding separately; unanswered questions do not block otherwise correct implementation. Do not add daily issues or require tests/documents to answer.
