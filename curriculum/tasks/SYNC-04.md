# SYNC-04 — Resume attachments safely

Phase: P07 | Order: 28 | Reference prerequisite: SYNC-03

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Resuming an interrupted attachment

## Precise task

Upload a 100 MB test attachment in resumable chunks. Persist upload identity and progress. Verify final integrity and associate the file with a job only after completion. Define cancellation and abandoned-upload cleanup.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Large uploads fail frequently on mobile networks and own server resources.

## What you achieve

A recoverable upload with explicit integrity and ownership.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **chunking:** Chunking divides a large payload into manageable pieces. Example: Send a large photo archive in resumable chunks.
- **checksums:** A checksum summarizes content so unexpected changes can be detected under its stated guarantees. Example: Verify uploaded chunks and the assembled file.
- **resumability:** Resumability continues from a durable checkpoint after interruption. Example: Restart an upload from accepted chunks.
- **file streams:** Streams process data incrementally instead of loading the entire payload at once. Example: Stream report rows or attachment bytes.
- **resource lifecycle:** A resource has creation, ownership, use, completion, and cleanup rules. Example: A partial upload expires and its temporary chunks are removed.
- **upload authorization:** Upload authorization checks who may create, continue, and attach a file to a resource. Example: Revalidate ownership before accepting a resumed chunk.
- **mobile background limits:** The OS can limit or stop background execution; clients must not rely on uninterrupted work. Example: Resume a persisted upload after the app restarts.

## Research hints

1. Search for "chunking" and "Resuming an interrupted attachment"; find a small example and predict its observable result before trying it.
2. Investigate "checksums" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Interrupt and restart after several chunks without uploading the whole file again.
- [ ] Corrupt content is rejected; partial files are not presented as complete.
- [ ] Cancellation and expiration clean up abandoned resources.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Revoke upload permission halfway through and define what happens to already-stored chunks.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
