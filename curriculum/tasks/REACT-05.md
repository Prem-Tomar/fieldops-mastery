# REACT-05 — Design server-state caching and invalidation

Phase: P04 | Order: 13 | Reference prerequisite: REACT-04

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

Server-state cache identity

## Precise task

Cache paginated jobs by organization, status, and page. Navigate between filters and update one job. Define freshness, refetch, cancellation, and which queries must change after mutation.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Incorrect cache keys and invalidation can display stale or cross-tenant data.

## What you achieve

Correct cache ownership with observable fetch behavior.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **server state versus client state:** Server state is remote authoritative data; client state includes local interaction and unsaved intent. Example: Keep a draft separate from the cached confirmed job.
- **query keys:** Query keys identify which remote result is cached and must include relevant inputs. Example: Include tenant, status, and page in a jobs key.
- **pagination:** Pagination divides a large result into ordered portions with a continuation strategy. Example: Return jobs with a cursor for the next stable page.
- **freshness:** Freshness describes how current cached data must be for a use case. Example: A dispatch view may refresh sooner than a historical report.
- **invalidation:** Invalidation marks cached data as outdated after a relevant change. Example: Completing a job invalidates affected status lists.
- **request deduplication:** Deduplication shares identical in-flight work rather than issuing redundant requests. Example: Two widgets use one current-job request.
- **race conditions:** An outcome depends on timing or ordering between operations that overlap. Example: An old search response arrives after the current query's response.

## Research hints

1. Search for "server state versus client state" and "Server-state cache identity"; find a small example and predict its observable result before trying it.
2. Investigate "query keys" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] Different tenants and filters never share results.
- [ ] The documented mutations refresh or update all affected views.
- [ ] Fast navigation never displays a late result from another query.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Switch organizations with in-flight requests and prove old data cannot reappear.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
