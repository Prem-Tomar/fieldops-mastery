# FieldOps Mastery

A learning-to-mastery project for two developers with approximately 5 and 10 years of experience: **JavaScript, TypeScript, React, React Native, Node.js, PostgreSQL, offline synchronization, and micro frontends**.

Build a maintenance operations platform: dispatchers assign jobs on web, technicians complete work on mobile, and a Node.js backend manages jobs, inventory, access, and synchronization.

This repository currently contains curriculum, assessment ledgers, contribution templates, and governance configuration. Application code is implemented by learners as they complete tasks.

## Start here

1. Read the [problem statement](docs/PROBLEM_STATEMENT.md).
2. Follow the [22-week roadmap](docs/ROADMAP.md).
3. Use the [44 concept reference definitions](curriculum/tasks/README.md) alongside the roadmap's implementation order.
4. Read the [two-person collaboration agreement](docs/COLLABORATION.md) and [assessment rubric](docs/ASSESSMENT.md).
5. Track concepts separately: [5-year learner](evidence/learner-5y/coverage.csv), [10-year learner](evidence/learner-10y/coverage.csv).
6. Review [architecture and micro frontend scope](docs/ARCHITECTURE.md).

**The existing 14 week-one issues are the authorized batch; further issue creation is paused.** Neha builds job features and Madhavi builds complementary inventory features. Each planned task adds integrated behavior, a correctness fix, a measured improvement or a recovery capability. Both independently demonstrate every concept, while accepted production units are reused. See the [22-week roadmap](docs/ROADMAP.md), its [structured schedule](curriculum/roadmap.json), and the [issue lifecycle](docs/ISSUE_LIFECYCLE.md).

PostgreSQL starts with a small Node API and basic SQL in week 5, before React clients. Its focus grows through real queries, concurrent transactions, offline reconciliation, reliable delivery, performance, migration safety and verified recovery.

## Knowledge coverage

The catalog maps 338 named concepts to tasks. Both learners demonstrate every catalog concept, including basics. Individual ledgers prevent shared implementation or experience level from hiding a gap. This is a broad curriculum, not a claim to cover every possible language or platform feature.

Every published task has a distinct product ask, purpose, explained concepts, function input/output/error contracts, worked examples, progressive hints, acceptance criteria, an independent mastery challenge and a coach checkpoint. Frontend tasks include screen references. Tests and documentation are not standalone assignments; test-writing suggestions are optional PR feedback.

## Contribution and verification

Only **Prem-Tomar** may merge PRs to **master**. Collaborators work on branches or forks and submit PRs. See [governance](docs/GOVERNANCE.md) and [contribution guide](CONTRIBUTING.md).

Run the curriculum checks using Python 3.12 or newer:

```sh
python scripts/validate_curriculum.py
```

CI validates the concept references, roadmap sequence, complementary deliverables, gradual PostgreSQL stages, planned coverage for both learners, ledgers, internal links and governance. It checks curriculum integrity, not completed learning or application correctness. As tooling exists, run appropriate application checks/builds and demonstrate behavior; optional test-writing feedback stays within feature PRs.
