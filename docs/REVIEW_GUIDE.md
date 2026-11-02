# Mandatory review response format

Apply these requirements to every contributor PR. Review the agreed task and prerequisites before judging implementation. Preserve the [learning rules](LEARNING_RULES.md): code acceptance and mastery are different outcomes, and coaching cannot introduce surprise implementation requirements.

## Plain English is mandatory

Write for contributors who may use English as an additional language. Use short, direct sentences and familiar words. Keep the technical meaning precise; avoid idioms, unexplained abbreviations and several instructions packed into one sentence. Address the code respectfully. Do not make assumptions about a contributor's ability or mention their language background in public feedback.

Every bug comment must let the contributor answer these questions without guessing:

1. **Where is the problem?** Give the file, function and smallest useful line range. Point to the relevant code fragment when useful.
2. **What happens now?** Show one concrete input or action and the result actually observed.
3. **What should happen?** State the expected result, including the exact output/error and relevant call/event counts.
4. **Which task requirement does this affect?** Link the agreed issue and identify the specific input/output or behavior rule. For maintainer work, link the agreed policy. Explain how the bug prevents that ask from working; do not add a new requirement.
5. **What change is needed, and why?** Describe the behavior to correct and the caller/component affected. Keep separate bugs separate.
6. **What can help the contributor investigate?** Give a focused research hint without the full replacement implementation.

Use those plain labels in inline feedback. Keep inputs, observed outputs and expected outputs in separate language-tagged fenced blocks where code helps. Explain a new technical term once and record its shared glossary entry; link the entry later. Keep Question of the Day answer-free at first. A clear explanation does not replace actual validation, and automated format checks cannot prove that a comment is understandable.

## High-level summary

State the implementation outcome (changes needed, ready for implementation acceptance, or blocked on prerequisites), the product behavior reviewed and any required predecessor still missing. Summarize the code findings and their consequences. Identify the exact revision reviewed, checks actually run, expected/actual results and what those checks do not establish. State mastery as unassessed, pending coaching or evidence-backed verified; do not infer it from working code or green CI.

For Week 1, explicitly check D1 through D6 before accepting D7 for either contributor. A later PR with no reviewed prerequisite is a sequence problem, even if its isolated function appears to work. Tell the contributor which earlier capability must be reviewed and why the dependent component needs it; preserve the branch while the correct sequence resumes.

## Precise inline guidance

Use this format for every actionable code finding:

- **Location and category:** exact file and smallest relevant line range; label implementation blocker, prerequisite blocker, optional feedback or mastery coaching.
- **Requested change:** describe the behavior to correct, not a complete replacement solution.
- **Components involved:** name the caller, unit, adapter/module or consumer affected.
- **Term explained:** check the shared definitions first. Explain a new term briefly at its first project use and add a canonical entry; later reviews link to it instead of repeating the definition.
- **Behavior or risk:** show a concrete input/timing scenario, expected and observed results, and why the difference matters. Trace it to the original contract for a blocker.
- **Research hint:** provide a useful concept/search phrase or diagnostic question. Leave design decisions and implementation with the learner.

Keep the overall summary as well as inline guidance. Put sequence/process feedback in the summary when it has no meaningful changed code line. Do not attach a fabricated code location. A finding that spans unrelated problems must be split so each ask is independently understandable.

## Define terms once and link them thereafter

Do not assume that a phrase such as positive integer is already understood. Check the existing [concept explanations](../curriculum/concepts.json) and [review term glossary](REVIEW_TERMS.md) before adding an explanation. Define a new term in plain language with a small example at its first relevant project review, record the explanation link in [review-terms.json](../curriculum/review-terms.json), and maintain one canonical glossary entry. In later reviews, link the appropriate entry rather than copying the same definition again. Both contributors use the same glossary; a glossary link does not itself establish their understanding.

The [positive integer entry](REVIEW_TERMS.md#positive-integer), for example, includes examples and non-examples. Do not repeat that explanation in every review. Targeted corrections and worked examples are still appropriate when a learner's answer reveals a specific misunderstanding; preserve their original response.

## Make snippets stand out

Use fenced code blocks with a language such as js or json for runnable fragments, input examples and result objects. Label the scenario, observed result and expected result clearly. Keep inline code for short identifiers, not dense multi-part examples buried in prose. Show only enough code to reproduce the finding; do not supply the full replacement implementation.

For an initial Question of the Day, fence the question's example code when needed but keep answers and expected outcomes out of that initial prompt. Worked answer snippets belong in the correction after the learner responds.

## Coaching and optional validation feedback

After implementation review, ask the contributor to explain a decision, walk through state transitions or predict an unseen input. Record assistance and remaining gaps in the existing review/ledger flow. A missing explanation is a coaching gap, not automatically a code defect. A failed original acceptance scenario is a code defect regardless of how well it is explained.

Optional test-writing feedback must state the scenario, expected result and a research hint, and remain labeled optional. Maintainers may supply the test. Formal reports and test authoring are not required learner deliverables. Never report an unrun check as passing or equate curriculum/dashboard CI with application verification.

## Question of the Day in review

From D2 onward, follow [Question of the Day](QUESTION_OF_THE_DAY.md): select previously completed work, ask one focused reasoning question without its answer, and require every part in the learner's own words in the intended review discussion. Preserve the original response, distinguish correct/partial/incorrect/missing parts, explain corrections and request only a targeted follow-up for the remaining gap. Record understanding separately; unanswered questions do not block otherwise correct implementation. Do not add daily issues or require tests/documents to answer.
