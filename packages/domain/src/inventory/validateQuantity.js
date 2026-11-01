export default function validateQuantity(value) {
  if (
    typeof value === "number" &&
    Number.isFinite(value) &&
    Number.isInteger(value) &&
    Number.MAX_SAFE_INTEGER >= value &&
    value > 0
  ) {
    return { ok: true, quantity: value };
  }
  return { ok: false, code: "INVALID_QUANTITY" };
}


