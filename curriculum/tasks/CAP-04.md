# CAP-04 — Defend architecture and prove concept coverage

Phase: P11 | Order: 44 | Prerequisite: CAP-03

## Precise task

Each developer presents the complete system and answers one unseen basic and one advanced question for every curriculum phase. Compare modular monolith and service extraction, modular web and micro frontends, and shared versus platform-specific code. Audit the personal coverage ledger.

## Why we are doing this

Experience and shared commits do not prove individual mastery.

## What you achieve

An independently assessed portfolio with no unverified concept coverage.

## What this teaches

- architecture tradeoffs
- complexity analysis
- system boundaries
- cost
- communication
- fundamental recall
- knowledge transfer

## Progressive hints

1. Use measurements and concrete failure scenarios.
2. Identify conditions that would change a decision.
3. Acknowledge gaps and schedule remediation rather than marking them passed.

## Acceptance criteria

- [ ] All catalog concepts have independent evidence for both learners.
- [ ] Each phase has a score of at least 2/3 in understanding, implementation, debugging, tradeoffs, and transfer.
- [ ] Unpassed concepts receive remediation tasks before final completion.

## Independent mastery challenge

The coach changes team size, device constraints, or reliability requirements and asks for a revised architecture.

The coach adds one undisclosed variation after both learners submit their own predictions and implementation evidence. Each learner explains every listed concept, predicts an observable behavior, and demonstrates it in code or an experiment. Fixing the shared product alone does not mark either learner's coverage complete.

## Pair collaboration

Both learners complete the same concepts and criteria. Alternate driver/reviewer on shared integration; use isolated spikes for individual alternatives. The second PR adds tests, a validated alternative, or personal evidence rather than duplicating production code. Review each other's reasoning only after independent predictions are recorded. Pairing is allowed; assisted work remains marked assisted until independently repeated.

## Evidence to submit

- Linked personal issue (only after the owner authorizes issue creation), task ID, learner handle, and PR.
- Predictions made before execution; observed output and explanation for every concept.
- Tests or reproducible experiment, runtime/device details, and failures encountered.
- Design alternatives, accepted tradeoffs, and the unseen challenge result.
- Per-concept assessment in the learner's coverage ledger; five-dimension mastery score.

## Coach checkpoint

Record expected behavior before inspecting the solution. Inject a changed constraint, request a diagnosis, and score understanding, implementation, debugging, tradeoffs, and transfer from 0–3. Every dimension must reach 2 independently. Failed concepts receive remediation; experience level never waives a basic concept.
