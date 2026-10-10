# MFE-02 — Build independently deployable shell and remotes

Phase: P09 | Order: 34 | Prerequisite: MFE-01

## Precise task

Build a web shell and separately built dispatch and reporting remotes. Load them at runtime with a documented integration mechanism. Deploy a reporting change without rebuilding the shell or dispatch remote.

## Why we are doing this

Independent delivery must be demonstrated rather than inferred from folder structure.

## What you achieve

Two micro frontends with versioned build artifacts and reproducible loading.

## What this teaches

- module federation or equivalent
- runtime manifests
- shared React identity
- bundler configuration
- lazy loading
- CSS isolation
- routing

## Progressive hints

1. Use a supported integration tool and pin compatible versions.
2. Inspect whether host and remote load incompatible React runtimes.
3. Treat a remote URL as trusted executable code configuration.

## Acceptance criteria

- [ ] Record shell and dispatch artifact hashes before and after the reporting-only deployment; they stay unchanged.
- [ ] Direct navigation and browser back work.
- [ ] Styles and React dependencies do not cause cross-app breakage.

## Independent mastery challenge

Inject an incompatible shared dependency and demonstrate a safe rejection or rollback.

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
