# SYNC-04 — Resume attachments safely

Phase: P07 | Order: 28 | Prerequisite: SYNC-03

## Precise task

Upload a 100 MB test attachment in resumable chunks. Persist upload identity and progress. Verify final integrity and associate the file with a job only after completion. Define cancellation and abandoned-upload cleanup.

## Why we are doing this

Large uploads fail frequently on mobile networks and own server resources.

## What you achieve

A recoverable upload with explicit integrity and ownership.

## What this teaches

- chunking
- checksums
- resumability
- file streams
- resource lifecycle
- upload authorization
- mobile background limits

## Progressive hints

1. Choose a protocol before choosing a library.
2. Do not assume background execution will finish.
3. Make retried chunks safe and verify tenant/job ownership on each relevant step.

## Acceptance criteria

- [ ] Interrupt and restart after several chunks without uploading the whole file again.
- [ ] Corrupt content is rejected; partial files are not presented as complete.
- [ ] Cancellation and expiration clean up abandoned resources.

## Independent mastery challenge

Revoke upload permission halfway through and define what happens to already-stored chunks.

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
