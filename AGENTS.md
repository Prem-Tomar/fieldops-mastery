# Required contribution and review rules

Read [the mandatory learning rules](docs/LEARNING_RULES.md), [the roadmap](docs/ROADMAP.md), and [the review format](docs/REVIEW_GUIDE.md) before preparing tasks, implementing work or reviewing a PR.

- Treat these as requirements, not suggestions. Each learner task has one main idea, bounded product implementation, explicit exclusions, exact unit contracts, observable completion criteria and research hints. Do not substitute documentation for product behavior or provide the complete solution in a hint.
- Follow prerequisites. W1 D7 comes after W1 D1-D6, in order, for each contributor. Existing later work stays queued until its predecessors are reviewed; a draft or stacked branch does not count as a passed prerequisite.
- Both contributors cover every catalog concept independently through different product asks. Introduce only the abstractions needed now and reuse accepted units.
- Separate implementation acceptance from mastery assessment. A completed implementation may close its task; understanding and unseen variations are coaching evidence. Do not add surprise product requirements or mark mastery from issue closure. Both learners must still pass a mastery gate before the forecast advances.
- Review with a high-level summary and precise inline feedback: exact location, requested change, affected components, plain-language term explanation, observed/expected behavior or risk, and a research hint. Label implementation blockers, prerequisite blockers, optional feedback and mastery coaching separately.
- Tests and documentation are not standalone learner issues or mandatory authoring deliverables. Maintainers may own them. Report actual validation and its limits; turn failures into concrete gaps.
- Apply [Question of the Day](docs/QUESTION_OF_THE_DAY.md) from D2, revisiting concepts from earlier completed work (D2 revisits D1). Keep initial questions answer-free; require every part in the learner's own words in the review discussion, preserve original answers, give corrections and targeted follow-ups, and track understanding separately. Unanswered learning questions do not block otherwise correct implementations; actual code defects still do.
- Do not create, edit, close, relabel, reassign or automate GitHub issues without fresh explicit owner authorization. Current issues must remain untouched.
- Only Prem-Tomar merges to master. Do not merge on the owner's behalf or change governance.

Run `python scripts/validate_curriculum.py` before submitting curriculum changes. It enforces policy structure and coverage; it cannot prove teaching quality or individual understanding. Run other checks appropriate to code changes.
