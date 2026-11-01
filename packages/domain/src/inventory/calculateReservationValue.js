import validateQuantity from "./validateQuantity.js";

export default function calculateReservationValue(
  unitPriceCents,
  quantity,
  discountPercent = 0,
) {
  if (!Number.isSafeInteger(unitPriceCents) || unitPriceCents < 0) {
    return {
      ok: false,
      code: "INVALID_PRICE",
    };
  }

  if (!validateQuantity(quantity)) {
    return {
      ok: false,
      code: "INVALID_QUANTITY",
    };
  }

  if (
    !Number.isInteger(discountPercent) ||
    discountPercent < 0 ||
    discountPercent > 100
  ) {
    return {
      ok: false,
      code: "INVALID_DISCOUNT",
    };
  }

  const grossCents = unitPriceCents * quantity;

  if (!Number.isSafeInteger(grossCents)) {
    return {
      ok: false,
      code: "AMOUNT_OUT_OF_RANGE",
    };
  }

  const netCents = Math.round(grossCents * ((100 - discountPercent) / 100));

  return {
    ok: true,
    grossCents,
    netCents,
  };
}
