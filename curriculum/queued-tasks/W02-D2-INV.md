**Owner:** @madhavichauhan1995 (10 years) · **Peer:** @Neha2212-vi · **Reviewer:** @Prem-Tomar
**State:** queued · **Effort guide:** 3 hours, plus review

## Goal, main idea and purpose

Normalize supplier part IDs without changing their numeric identity. Suppliers can send identifiers larger than JavaScript Number's safe integer range. The main idea is **exact integer identity with BigInt**; a rounded ID could select the wrong part even when the quantity is valid.

**Location:** `packages/domain/src/inventory/normalizeSupplierPartId.js`, exported through the inventory entrypoint. The result feeds the existing stock partId field and the new batch preview. This is a supplier-boundary adapter, not a new quantity rule.

## Prerequisites and explicit exclusions

Complete your own published sequences 1–8 in order. The direct predecessor is your W2 D1 batch-preview task (sequence 8); the published issue metadata links its actual issue number. Filling the seven-open-task queue does not waive this prerequisite or any mastery gate.

No supplier HTTP integration, import batch, database, React/mobile screen, arithmetic on prices/quantities, generic ID framework or changes to existing internal IDs. Do not replace accepted `validateQuantity`; quantities remain Number-based under their existing safe-integer contract.

## Concepts explained

- **Identifier versus quantity:** an identifier names a record; it is not a count to add or multiply. P1 and supplier:123 are names of parts.
- **BigInt:** JavaScript's integer type for exact whole-number values beyond Number's safe integer range. For example, `9007199254740993n` retains that integer identity. It is a different type from Number.
- **Canonical representation:** one agreed spelling for equivalent IDs. Here leading zeros disappear, so supplier text `000123` and BigInt `123n` name `supplier:123`.
- **Serialization boundary:** values crossing a text/JSON boundary need a supported representation. This function returns a string rather than putting a BigInt in a result that a later client may serialize.
- The [safe-integer definition](../../docs/REVIEW_TERMS.md#safe-integer), strings/numbers and strict type checks were introduced earlier; link their explanation when reviewing rather than repeating it.

## Exact unit contract

Implement synchronous `normalizeSupplierPartId(value)` with no default. Accept **only** a primitive string or primitive BigInt.

For strings, trim outer whitespace. Require 1–128 ASCII decimal digits (0–9), counting digits **before** removing leading zeros. Reject an empty string, signs, decimal points, exponent/hex notation, internal whitespace and non-ASCII digit characters. The resulting integer must be greater than zero. Leading zeros are allowed within the 128-digit input limit.

For BigInt, require a value greater than zero whose base-10 representation has at most 128 digits. Reject every Number, including a small safe Number such as 123: this boundary never guesses whether a supplier number was already rounded. Also reject boxed strings/BigInts, arrays, objects, booleans, null, undefined and symbols without calling their conversion methods.

Success is exactly `{ok:true,partId:'supplier:' + canonicalDigits}`. Failure is exactly `{ok:false,code:'INVALID_SUPPLIER_PART_ID'}`. Validate the primitive type, then its text/length rules, then positivity; malformed input must not escape as a thrown conversion exception. Do not use Number as an intermediate representation of the ID. Return no BigInt field. No input mutation, logging, outside state or I/O.

## Observable completion and examples

```js
normalizeSupplierPartId(' 0009007199254740993 ');
// {ok:true,partId:'supplier:9007199254740993'}
normalizeSupplierPartId(9007199254740993n);
// {ok:true,partId:'supplier:9007199254740993'}
normalizeSupplierPartId(123);
normalizeSupplierPartId('1e3');
normalizeSupplierPartId('0');
// Each: {ok:false,code:'INVALID_SUPPLIER_PART_ID'}
```

Demonstrate the distinct outputs for two adjacent supplier IDs beyond the safe Number range. A 129-digit string fails even if most digits are leading zeros. Show that serializing a success result yields ordinary JSON with its partId intact.

Compose a normalized ID into an existing valid stock fixture with available 5 and metadata `{bin:'A'}`, then pass the same ID and quantity 2 to the accepted batch-preview unit. Expected: that part is found and its preview remaining is 3; the original stock is unchanged. Use the stock/quantity contracts rather than modifying them for larger IDs.

## Progressive research hints

1. Search “JavaScript BigInt exact integers Number safe range”; compare constructing an integer from original decimal text with converting an already-created Number.
2. Compare the responsibilities of a supplier identifier parser and the accepted quantity validator. Which information is irrecoverable after rounding?
3. Search “JavaScript BigInt JSON serialization string”; ask which public result representation preserves the ID across a text boundary without special client support.

## Separate mastery coaching

The coach changes the input representation or length boundary and asks you to predict identity and failure behavior before running it. No new supplier integration is added as an unseen requirement. The reviewer records understanding separately, preserves original answers and uses targeted follow-ups. Question of the Day revisits a previously completed concept in the PR; its initial prompt has no answers and is non-blocking for an otherwise correct implementation. Tests and documentation are not required authoring deliverables or separate issues.
