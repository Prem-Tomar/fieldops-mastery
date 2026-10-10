# FieldOps Mastery

A learning-to-mastery project for two developers with approximately 5 and 10 years of experience: **JavaScript, TypeScript, React, React Native, Node.js, offline synchronization, and micro frontends**.

Build a maintenance operations platform: dispatchers assign jobs on web, technicians complete work on mobile, and a Node.js backend manages jobs, inventory, access, and synchronization.

This repository currently contains curriculum, assessment ledgers, contribution templates, and governance configuration. Application code is implemented by learners as they complete tasks.

## Start here

1. Read the [problem statement](docs/PROBLEM_STATEMENT.md).
2. Follow the [22-week roadmap](docs/ROADMAP.md).
3. Use the [44 ordered task definitions](curriculum/tasks/README.md).
4. Read the [two-person collaboration agreement](docs/COLLABORATION.md) and [assessment rubric](docs/ASSESSMENT.md).
5. Track concepts separately: [5-year learner](evidence/learner-5y/coverage.csv), [10-year learner](evidence/learner-10y/coverage.csv).
6. Review [architecture and micro frontend scope](docs/ARCHITECTURE.md).

**No issues are created until Prem-Tomar explicitly authorizes the start.** Both learners receive all 44 tasks as separate personal instances: 88 instances over the roadmap, published incrementally. After authorization, start one task per learner; each eligible closure creates one successor in that learner's sequence. See [issue lifecycle](docs/ISSUE_LIFECYCLE.md).

## Knowledge coverage

The catalog maps 338 named concepts to tasks. Both learners demonstrate every catalog concept, including basics. Individual ledgers prevent shared implementation or experience level from hiding a gap. This is a broad curriculum, not a claim to cover every possible language or platform feature.

Every task contains a precise problem, purpose, expected outcome, concepts, progressive hints, acceptance criteria, independent mastery challenge, and coach checkpoint.

## Contribution and verification

Only **Prem-Tomar** may merge PRs to **master**. Collaborators work on branches or forks and submit PRs. See [governance](docs/GOVERNANCE.md) and [contribution guide](CONTRIBUTING.md).

Run the curriculum checks using Python 3.12 or newer:

```sh
python scripts/validate_curriculum.py
```

Initial CI validates tasks, dependencies, concept ledgers, internal links, and governance files. Application type checks, tests, and builds must be added as apps are implemented; documentation checks do not prove application correctness.
