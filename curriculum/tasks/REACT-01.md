# REACT-01 — Build a predictable component and state model

Phase: P03 | Order: 9 | Prerequisite: TS-04

## Precise task

Build job list, status filter, and job detail components using 20 fixtures. Selecting and filtering must retain the correct job identity. Add a draft notes editor whose reset behavior is explicitly tied to job selection. Compare useState with useReducer and Context for the same state ownership; demonstrate a Rules of Hooks violation and its correction.

## Why we are doing this

Component identity and state ownership determine whether data survives the right interactions.

## What you achieve

A usable job browser with intentional state lifetime.

## What this teaches

- JSX
- components
- props
- composition
- events
- state
- reconciliation
- keys
- derived state
- immutable updates

- Rules of Hooks
- useReducer
- Context

## Progressive hints

1. Draw the ownership of selected ID, filter, and draft.
2. Use stable job IDs and deliberately reorder fixtures.
3. Decide when a component should preserve or reset state.

## Acceptance criteria

- [ ] Reordering and filtering never move one job's draft to another.
- [ ] Explain every stored value and why it cannot simply be derived.
- [ ] Fix an injected mutation and an unstable-key bug.

## Independent mastery challenge

Add selection encoded in the URL without creating two conflicting sources of truth.

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
