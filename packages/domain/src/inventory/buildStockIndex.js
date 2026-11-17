export default function buildStockIndex(records) {
  if (!Array.isArray(records)) {
    return {
      ok: false,
      code: "INVALID_STOCK_LIST",
    };
  }

  const byId = new Map();

  for (const record of records) {
    if (
      record === null ||
      typeof record !== "object" ||
      Array.isArray(record) ||
      typeof record.partId !== "string" ||
      record.partId.trim() === "" ||
      record.partId !== record.partId.trim() ||
      !Number.isSafeInteger(record.available) ||
      record.available < 0 ||
      !isPlainObject(record.metadata) ||
      !Object.values(record.metadata).every(
        (value) => typeof value === "string",
      )
    ) {
      return {
        ok: false,
        code: "INVALID_STOCK",
      };
    }

    if (byId.has(record.partId)) {
      return {
        ok: false,
        code: "DUPLICATE_PART_ID",
      };
    }

    const copiedRecord = {
      partId: record.partId,
      available: record.available,
      metadata: { ...record.metadata },
    };

    byId.set(record.partId, copiedRecord);
  }

  return {
    ok: true,
    byId,
  };
}
