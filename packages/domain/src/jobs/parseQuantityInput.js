export const parseQuantityInput = (value) => {
  const result = { ok: false, code: "INVALID_QUANTITY_INPUT" };

  if (typeof value !== "string") {
    return result;
  }

  const text = value.trim();

  if (!/^[0-9]+$/.test(text)) {
    return result;
  }

  const quantity = Number(text);

  if (!Number.isSafeInteger(quantity) || quantity <= 0) {
    return result;
  }

  return { ok: true, quantity };
};
