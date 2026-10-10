# REACT-02 — Build an accessible assignment form

Phase: P03 | Order: 10 | Prerequisite: REACT-01

## Precise task

Build technician selection, appointment date, and notes fields with validation. Prevent duplicate submission while pending. Show field errors, submission errors, success, loading, and empty-technician states.

## Why we are doing this

Forms connect browser behavior, domain validation, and accessibility.

## What you achieve

A keyboard-usable form with explicit feedback.

## What this teaches

- controlled and uncontrolled inputs
- form events
- validation
- refs
- focus
- routing
- URL state
- accessibility
- loading and empty states

- portals
- focus management

## Progressive hints

1. Start with labels and keyboard interactions.
2. Separate field validity from server acceptance.
3. Define where focus moves after an error and successful submission.

## Acceptance criteria

- [ ] All controls work by keyboard and have accessible names.
- [ ] Invalid fields preserve entered values; failed submission allows retry.
- [ ] Deep-link navigation and browser back restore the intended job.

## Independent mastery challenge

Introduce a slow validation request and prevent its result from overwriting validation for newer input.

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
