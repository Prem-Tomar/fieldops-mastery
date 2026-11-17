**Owner:** @Neha2212-vi (5 years) · **Peer:** @madhavichauhan1995 · **Reviewer:** @Prem-Tomar
**State:** queued · **Effort guide:** 4–5 hours, plus review

## Goal, main idea and purpose

Add a bounded job-prefetch unit so the dispatcher can prepare several job details without starting every request at once. The main idea is **bounded concurrency**: permit several unfinished operations, but cap their number. This extends your accepted single-job loader; it does not replace the lookup controller.

**Location:** `packages/domain/src/jobs/prefetchJobs.js`, exported through the existing jobs entrypoint. The product gains a fixture-driven batch read that later web/mobile screens can share.

## Prerequisites and explicit exclusions

Complete and integrate your W1 D1–D7 in order, ending with issue #7. This is sequence 8, appended after the published tail; filling the queue does not make it active. Reuse D6 `loadJob` through an injected adapter. Do not copy its transport/response validation.

No cache, retries, progress callbacks, UI, HTTP server, database, framework, generic scheduler package or changes to the accepted single-job contracts. This issue does not pass the whole JavaScript gate.

## Concepts explained

- **Concurrency versus order:** two requests can be unfinished together and finish in reverse order. Starting J1 before J2 does not guarantee J1 finishes first.
- **Promise and await:** a Promise represents a later result; awaiting it pauses that function's continuation. It does not automatically limit how many operations other calls already started.
- **Result ordering:** retain each result beside the input that caused it, even when completion order differs. A failed J2 must not shift J3's position.
- **Cooperative cancellation:** a signal asks work to stop; a loader can ignore it. This unit must still stop dispatching queued work and classify late outcomes.
- **Independent snapshots:** returned result/job objects belong to this call, rather than sharing objects supplied by its loader or another batch. Refer to the existing [concept explanations](../concepts.json) for closures, copies and errors.

## Exact unit contract

Implement async `prefetchJobs(jobIds, load, options = {})`.

| Input | Contract |
|---|---|
| `jobIds` | Array of at most 100 unique nonempty string IDs, already trimmed. Preserve input order; never trim/coerce an ID. Empty array is valid. |
| `load` | Function `load(id, signal)` wrapping accepted D6 `loadJob(id, fetcher, signal)`. It returns a D6 result Promise. A well-formed D6 result is assumed; unexpected throws/rejections are handled below. |
| `options` | Non-null, non-array record; omitted means `{}`. `concurrency` defaults to 2, must be an integer number 1–8. Optional `signal` is assumed to be an AbortSignal when supplied. Extra option keys are ignored. |

Validate **before any load call**, in this order: dependency/options/concurrency → `{ok:false,code:'INVALID_PREFETCH_CONFIG'}`; array/size → `INVALID_JOB_ID_LIST`; scan IDs left to right, invalid ID syntax → `INVALID_JOB_ID`, otherwise previously seen ID → `DUPLICATE_JOB_ID`. These names mean the exact `{ok:false,code}` result. Invalid configuration/input resolves to failure; it does not reject.

Success is `{ok:true,results:[{jobId,result},...]}`. Each `result` is the D6 success/failure shape. Start work in input order, with no more than `concurrency` unsettled load calls. When a slot finishes, the next queued ID may start; one failure does not stop unrelated work. Retain results in **input order**, with fresh result/job copies. Snapshot IDs before the first asynchronous pause; never mutate the inputs or loader-owned records. No logging or outside state.

Pass the supplied signal to every dispatched load. If already aborted, make zero calls and return one `CANCELLED` result per ID. After abort, start no additional loads, mark queued items cancelled, and classify any in-flight outcome handled after abort as `CANCELLED`. Await already dispatched loads before the batch resolves. A loader that never settles can therefore keep the batch pending; no immediate-cancellation deadline is promised. An AbortError rejection becomes `CANCELLED`; other unexpected throws/rejections become `LOAD_FAILED`. Independent batches share no counters or pending state.

## Observable completion and examples

With concurrency 2, J1/J2 start first. J2 finishing allows J3 to start while J1 remains pending. Resolve J3 before J1; the output must still list J1, J2, J3. Use controlled fixture Promises, not wall-clock guesses.

```js
await prefetchJobs([], load); // {ok:true,results:[]}
await prefetchJobs(['J1', 'J1'], load);
// {ok:false,code:'DUPLICATE_JOB_ID'}, zero load calls
```

For J1 success and J2 `LOAD_FAILED`, expected shape:

```json
{"ok":true,"results":[{"jobId":"J1","result":{"ok":true,"job":{"id":"J1","status":"assigned"}}},{"jobId":"J2","result":{"ok":false,"code":"LOAD_FAILED"}}]}
```

Demonstrate the concurrency cap, failure isolation, stable ordering, input/result independence and cancellation dispatch rule using the accepted loader adapter. A runnable walkthrough is sufficient; automated test authoring and documents are optional.

## Progressive research hints

1. Search “JavaScript Promise concurrency limit active operations”; compare active calls with completed results.
2. Compare eagerly calling every item in `map` with starting only work that currently has capacity. Predict call counts before running a fixture.
3. Search “AbortSignal cooperative cancellation”; ask which queued calls remain eligible after the signal changes and which Promise still owns each result position.

## Separate mastery coaching

Explain a changed completion order and diagnose an unseen cancellation timing in discussion. The reviewer records assistance and independent understanding separately from code acceptance. From D2 onward, Question of the Day revisits earlier **completed** work in the PR; the initial question contains no answers and missing learning answers do not block correct implementation. No standalone test/documentation issue is created.
