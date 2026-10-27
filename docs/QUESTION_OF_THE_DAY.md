# Question of the Day rules

Question of the Day is mandatory coaching from **D2 onward**, using concepts encountered in earlier completed work. D2 revisits D1; D3 may revisit D1 or D2. D1 has no question requiring prior project learning. This does not change the implementation order: D1 through D6 must precede D7 for each contributor. Do not edit existing issues to add questions; use the relevant review discussion.

## Select and ask the question

On an active learning day from D2, select a concept from that contributor's completed work and link the implementation/review evidence. If no earlier work has been completed, first resolve that prerequisite rather than assuming it has been taught. Rotate among already covered language/framework fundamentals, system behavior, design tradeoffs, operational concerns and domain rules; do not introduce a future roadmap topic as a recall expectation.

Ask one focused reasoning question that can be answered in a short discussion. Ground it in a small example, earlier implementation or realistic failure. Where useful, ask the learner to predict an outcome, explain the mechanism, identify a consequence or reason about a changed condition. Explain unfamiliar terms. Make every requested part explicit; the initial question and research hint must not reveal the answer or dictate a complete solution.

The [queued prompt bank](../curriculum/qotd-prompts.json) prepares one different question for each contributor on D2-D7: 12 prompts, none on D1. Each identifies the earlier source day, existing task number, concept and research hint. These are prepared prompts, not a claim that the earlier work is complete or the question has been asked. The reviewer verifies eligibility, posts the selected question in the relevant review discussion, then indexes the actual discussion in qotd.json. Leave issue bodies, comments, states and assignments untouched.

## Answer and coach in the review discussion

The learner answers every requested part in their own words in the intended PR/review discussion. Preserve the original answer. The reviewer identifies each part as correct, partially correct, incorrect or missing, then explains any correction with a short worked example or authoritative reference where needed. State the behavior and reasoning clearly; ask a targeted follow-up about the actual misunderstanding rather than repeating the entire question.

If an answer was posted elsewhere, link that original answer and ask for the corrected answer in the intended discussion. Do not silently replace or rewrite the learner's original response. Revisit a weak concept later with a different example to check transfer rather than memorization.

## Record understanding independently

Use [qotd.json](../curriculum/qotd.json) as a reviewer-maintained index of questions, original answers, corrections and follow-ups. The review discussion holds the actual conversation; reference it from the individual concept ledger when it provides relevant evidence. A question alone does not prove mastery of an entire concept or all rubric dimensions.

Each index entry records `id`, `learner`, `day`, `concept`, `sourceEvidence`, `questionDiscussion`, `originalAnswerDiscussion` (null until answered), `status` and `followUpDiscussion` (null until needed). Status is `pending`, `partial`, `needs-correction`, `demonstrated` or `revisit`. Pending answers must stay pending; empty records are not evidence. No questions or answers are fabricated to populate the tracker.

An unanswered or incomplete learning answer is a **non-blocking coaching follow-up for an otherwise correct implementation**. It does not reopen a completed implementation task or require extra learner-written tests/documents. If discussion exposes a real defect in the original code contract, review that concrete defect normally and distinguish it from the learning answer.

Implementation PRs may be accepted independently of unanswered questions, but the original mastery gates and full individual concept coverage remain required. A coaching gap may keep mastery pending and therefore affect mastery-based advancement/forecasting. An issue closure, answer submission or one good question does not automatically pass a mastery gate.

This is a review practice and evidence format, not authorization to create daily issues, activate a scheduler, change issue states or publish successor tasks.
