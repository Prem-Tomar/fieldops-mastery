# MFE-01 — Define and challenge micro frontend boundaries

Phase: P09 | Order: 33 | Prerequisite: RT-04

## Precise task

Compare a modular React application with a shell plus dispatch and reporting micro frontends. Define ownership of routes, authentication context, navigation, design tokens, data access, and deployment. Write an architecture decision record before implementation.

## Why we are doing this

Independent deployment can introduce costs that a two-person team must justify.

## What you achieve

A bounded experiment with explicit reasons for using or rejecting each boundary.

## What this teaches

- micro frontends versus modules
- build-time versus runtime integration
- ownership
- coupling
- shared dependencies
- architecture decisions

## Progressive hints

1. Choose a feature whose release can be independent.
2. List everything the shell must know about a remote.
3. Count deployment, testing, and runtime costs alongside benefits.

## Acceptance criteria

- [ ] Compare at least two integration approaches and a modular monolith.
- [ ] Document contracts and a measurable independence goal.
- [ ] Explain why code splitting alone does not demonstrate independent deployment.

## Independent mastery challenge

Add a third team requirement and identify which boundary would fail first.

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
