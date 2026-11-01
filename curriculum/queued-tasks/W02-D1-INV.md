**Owner:** @madhavichauhan1995 (10 years) · **Peer:** @Neha2212-vi · **Reviewer:** @Prem-Tomar
**State:** queued · **Effort guide:** 4 hours, plus review

## Goal, main idea and purpose

Give a dispatcher a **batch stock preview**: show which requested reservations could succeed together without committing stock or sending writes. The main idea is **per-item failure isolation**: one invalid/unavailable line has its own result while independent lines continue. Earlier successful lines affect the remaining preview stock, so the batch cannot promise the same units twice.

**Location:** `packages/domain/src/inventory/previewReservationBatch.js`, exported through the inventory entrypoint. This adds a real multi-line preview to the existing single-reservation workflow.

## Prerequisites and explicit exclusions

Complete and integrate your W1 D1–D7 in order, ending with #14. This is sequence 8 and remains queued while those predecessors are incomplete. Reuse accepted `buildStockIndex`, `validateQuantity` and `reservePart`; do not reproduce their rules in another helper.

No reservation submission, persistence, currency changes, UI, transport, asynchronous concurrency, rollback service or all-or-nothing batch transaction. This preview does not reserve stock on a server. Exact supplier IDs belong to the next separate increment.

## Concepts explained

- **Batch:** a finite collection of lines processed by one call. Here the maximum is 100 requests; that bound limits synchronous work.
- **Failure isolation:** a line returning failure leaves preview stock unchanged; the next line can still be considered.
- **Sequential dependency:** a later request for P1 sees the preview remaining after earlier successful P1 lines. Reusing the original availability for every line would over-promise stock.
- **Map lookup:** a Map associates a part ID with its stock record. It gives the same key one current preview value.
- **Object identity and copies:** two equal-looking objects can be separate values. Caller inputs, historical line outputs and final-stock outputs must be independent. Use the existing [concept explanations](../concepts.json) and [numeric glossary](../../docs/REVIEW_TERMS.md) for previously introduced terms.

## Exact unit contract

Implement synchronous `previewReservationBatch(stockRecords, requests)`.

`stockRecords` follows the accepted `buildStockIndex` array/stock/duplicate-ID contract. Each stock is `{partId,available,metadata}` and metadata values are strings. `requests` is an array of at most 100 entries. Each valid entry is a plain record `{partId,quantity}` with an already-trimmed nonempty string partId; extra keys are ignored. Inputs are ordinary fixture data, without accessors or proxies. Neither argument has a default.

Global validation order: first call the accepted stock-index unit and forward its exact failure (`INVALID_STOCK_LIST`, `INVALID_STOCK` or `DUPLICATE_PART_ID`). Next reject a non-array or oversized requests list with `{ok:false,code:'INVALID_RESERVATION_BATCH'}`. These failures produce no partial preview. Empty request and stock arrays are valid.

For a globally valid call, return `{ok:true,results,stocks}`. Visit request entries from index 0 upward. For each entry, use this order:

1. Invalid entry shape/partId → `{index,ok:false,code:'INVALID_RESERVATION_REQUEST'}`.
2. Quantity fails accepted `validateQuantity` → `{index,ok:false,code:'INVALID_QUANTITY'}`.
3. No matching stock → `{index,ok:false,code:'UNKNOWN_PART'}`.
4. Otherwise apply accepted `reservePart` to that part's **current preview stock**. Forward its failure code in `{index,ok:false,code}`. On success return `{index,ok:true,stock}` and carry its remaining stock forward to later lines.

`results` has exactly one entry per input request, in input order. `stocks` contains the final preview stocks in original stock-record order. No quantity is changed by a failed line. Repeated part IDs in requests are allowed and consume preview availability cumulatively; duplicate stock IDs are not allowed. Copy stock and metadata so each successful historical line, final stocks array, caller input and separate batch call remain independent. Return only the stated fields. Ordinary invalid input returns a failure rather than throwing. No logs, mutation, network calls or outside state.

## Observable completion and examples

Input:

```js
previewReservationBatch(
  [{partId:'P1',available:5,metadata:{bin:'A'}}],
  [{partId:'P1',quantity:3},{partId:'P1',quantity:3},{partId:'P1',quantity:1}]
);
```

Expected:

```json
{"ok":true,"results":[{"index":0,"ok":true,"stock":{"partId":"P1","available":2,"metadata":{"bin":"A"}}},{"index":1,"ok":false,"code":"INSUFFICIENT_STOCK"},{"index":2,"ok":true,"stock":{"partId":"P1","available":1,"metadata":{"bin":"A"}}}],"stocks":[{"partId":"P1","available":1,"metadata":{"bin":"A"}}]}
```

```js
previewReservationBatch([], [{partId:'missing',quantity:'3'}]);
// {ok:true,results:[{index:0,ok:false,code:'INVALID_QUANTITY'}],stocks:[]}
previewReservationBatch([], null);
// {ok:false,code:'INVALID_RESERVATION_BATCH'}
```

Demonstrate mixed success/failure, repeated-part accumulation, error precedence, empty input and independent output objects. Use existing stock fixtures and accepted units; a runnable walkthrough is enough. Tests and formal reports are optional.

## Progressive research hints

1. Search “JavaScript reduce sequential state Map”; compare a running preview with independent calculations against the original stock.
2. Compare a failed line with a successful line: which one is allowed to replace the preview value for that part?
3. Search “JavaScript shallow copy object identity”; after processing two P1 lines, ask which metadata objects a caller could otherwise accidentally share.

## Separate mastery coaching

Predict the outcome when the coach changes line order, then explain which objects can be mutated independently. This is learning evidence, not a surprise production feature. Question of the Day recalls earlier completed work in the PR with no initial answers. Both implementation and individual understanding are assessed; an unanswered learning question alone does not block correct behavior or require a new issue.
