import validateQuantity from "./validateQuantity.js";

export default function reservePart(stock, requested) {
  if (
    stock === null ||
    typeof stock !== "object" ||
    Array.isArray(stock) ||
    typeof stock.partId !== "string" ||
    stock.partId.trim() === "" ||
    stock.partId !== stock.partId.trim() ||
    !Number.isSafeInteger(stock.available) ||
    stock.available < 0 ||
    !isPlainObject(stock.metadata) ||
    !Object.values(stock.metadata).every((value) => typeof value === "string")
  ) {
    return {
      ok: false,
      code: "INVALID_STOCK",
    };
  }

  const quantityResult = validateQuantity(requested);

  if (!quantityResult.ok) {
    return quantityResult;
  }

  if (requested > stock.available) {
    return {
      ok: false,
      code: "INSUFFICIENT_STOCK",
    };
  }

  return {
    ok: true,
    stock: {
      partId: stock.partId,
      available: stock.available - requested,
      metadata: { ...stock.metadata },
    },
  };
}
