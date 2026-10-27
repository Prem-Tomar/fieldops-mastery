# NODE-01 — Build validated HTTP job endpoints

Phase: P06 | Order: 21 | Reference prerequisite: RN-04

**Concept reference, not a ready learner assignment.** The [mandatory learning rules](../../docs/LEARNING_RULES.md) and [roadmap](../../docs/ROADMAP.md) control actual scope and implementation order. Split this capability into small product increments before future publication. Existing GitHub issues remain unchanged.

## Primary learning idea

A validated HTTP boundary

## Precise task

Implement the selected job or inventory endpoint with runtime validation, stable error codes and the existing repository boundary. Demonstrate malformed and missing-resource responses. Separate create, list, detail and transactional writes into bounded increments at their roadmap gates; use small runtime experiments only where a listed concept is not exposed by the selected endpoint.

This reference scenario may span several tasks. Each actual assignment must select one bounded implementation goal, name the existing product integration, give exact function input/output/error contracts and worked examples, and state its observable completion criteria before work starts.

## Why we are doing this

Clients need stable HTTP contracts under valid and invalid input.

## What you achieve

Validated API behavior with consistent request, response and failure boundaries.

## Out of scope

- Do not publish this whole reference group as one learner task; select one bounded increment from the current roadmap slice.
- Do not add a new subsystem or abstraction without a need in that selected increment; defer adjacent capabilities to their own successor.
- Do not assign standalone tests, documentation or a duplicate accepted product capability.

## What this teaches

- **HTTP semantics:** HTTP methods, status codes, headers, and bodies describe requests and their outcomes. Example: Use a stable conflict response for a rejected assignment.
- **routing:** Routing selects an endpoint; middleware applies cross-cutting request behavior around handlers. Example: Validate input and attach a request ID before domain work.
- **middleware:** Routing selects an endpoint; middleware applies cross-cutting request behavior around handlers. Example: Validate input and attach a request ID before domain work.
- **request lifecycle:** A request passes through admission, handling, response, and cleanup, including disconnects. Example: Release owned resources if a downloading client leaves.
- **async errors:** A thrown error or rejected Promise must reach a handler that owns the failure policy. Example: Await worker results so rejected jobs do not become unhandled failures.
- **configuration:** Configuration supplies environment-specific behavior without hardcoding secrets. Example: Read a database URL from a controlled environment setting.
- **logging:** Logging records diagnostic events with relevant context. Example: Log a request ID and failure category without credentials.
- **dependency injection:** Dependency injection supplies collaborators through interfaces rather than hardcoded global imports. Example: Inject a fake subscription service into an isolated exercise.
- **ESM:** JavaScript modules use import/export with explicit dependencies and live exported bindings. Example: An imported counter binding reflects updates made by its exporting module.
- **headers and cookies:** Headers carry request/response metadata; cookies can store browser session identifiers with access rules. Example: Explain HttpOnly and SameSite for a chosen session transport.
- **JSON parsing limits:** Parsing limits bound untrusted body size and complexity before expensive processing. Example: Reject an oversized job command.
- **Buffer:** A Buffer represents binary bytes in Node.js. Example: Stream attachment chunks rather than treating bytes as a text string.
- **filesystem promises:** Promise-based filesystem APIs provide asynchronous file operations with explicit errors. Example: Await a file write and handle permission failure.
- **EventEmitter:** EventEmitter lets producers emit named events and listeners subscribe; listener lifetime needs management. Example: Remove a job listener when its owner is disposed.
- **package scripts and lockfiles:** Scripts name repeatable commands; lockfiles record resolved dependency versions. Example: Run a consistent build and install from a committed lockfile.

## Research hints

1. Search for "HTTP semantics" and "A validated HTTP boundary"; find a small example and predict its observable result before trying it.
2. Investigate "routing" in the current product unit; compare the valid and failing paths without copying a complete solution.
3. Search the relevant runtime or framework guide for the observed failure; trace one input through the existing caller and boundary before choosing a change.

## Acceptance criteria

- [ ] The selected endpoint returns the agreed valid, invalid, missing-resource and failure responses.
- [ ] Logs correlate to a request without including credentials.
- [ ] Its consumer receives the agreed data/error shape and can handle the demonstrated failure.

Use these reference scenarios to choose observable criteria for the selected product increment. Maintainers may supply routine checks; a demonstration is required, while learner-authored tests or formal reports are not.

## Independent mastery challenge

Disconnect a client mid-request and account for cleanup of owned resources.

This is separate coaching, not a surprise product requirement. A short explanation, walkthrough or bounded unseen variation establishes understanding; any genuinely new product capability needs its own authorized successor. A failure of the original implementation contract remains an implementation defect. Both learners must independently cover every referenced concept before the relevant mastery gate passes.

## Pair collaboration

Both learners independently cover these reference concepts through different product asks. Split broad capabilities into bounded single-idea tasks in roadmap order; reuse accepted units. Implementation completion and mastery acceptance are separate outcomes.

Each PR adds a different integrated behavior, correctness fix, measured improvement or recovery capability. Do not create a second PR merely for tests, documentation or personal evidence. Review the peer's decisions and use a small experiment only for an individual concept gap. Assistance remains recorded until independent verification.

## Evidence to submit

A runnable product demonstration and short PR/review-session walkthrough are sufficient. Identify the learner, existing task/PR, relevant input and observed output. The reviewer records individual concept evidence, assistance and scores in the existing ledgers; the optional submission template is not a required document.

Report the checks actually run and the concrete gap exposed by any failure. Keep implementation completion separate from mastery assessment. No new issue publication or issue editing is authorized by this reference.

## Coach checkpoint

State expected behavior before inspecting the solution. Use the [review format](../../docs/REVIEW_GUIDE.md): exact code location, requested change, components, unfamiliar terms explained briefly, behavior/risk and a research hint. Keep a high-level summary and distinguish implementation blockers, prerequisite blockers, optional feedback and mastery coaching. For mastery, score understanding, implementation, debugging, tradeoffs and transfer independently; every dimension must reach 2. Years of experience waive no concept.
