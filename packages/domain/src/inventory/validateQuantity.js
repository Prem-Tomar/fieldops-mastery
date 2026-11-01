function validateQuantity(value) {
  if (
    typeof value === "number" &&
    Number.isFinite(value) &&
    Number.MAX_SAFE_INTEGER >= value &&
    value > 0
  ) {
    return { ok: true, quantity: value };
  }
  return { ok: false, code: "INVALID_QUANTITY" };
}

// Example
// console.log(validateQuantity(1), "testcase");
// console.log(validateQuantity(Number.MAX_SAFE_INTEGER), "testcase");
// console.log(validateQuantity(-1), "testcase");
// console.log(validateQuantity({}), "testcase");
// console.log(validateQuantity([]), "testcase");
// console.log(validateQuantity(true), "testcase");
// console.log(validateQuantity(undefined), "testcase");
// console.log(validateQuantity(null), "testcase");
// console.log(validateQuantity(Number.MAX_SAFE_INTEGER + 1), "testcase");
