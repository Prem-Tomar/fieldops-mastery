function createReservationController({ submit, onState }) {
  if (typeof submit !== "function" || typeof onState !== "function") {
    throw new TypeError("INVALID_RESERVATION_CONFIG");
  }

  let disposed = false;
  let activeOperation = null;

  let state = {
    status: "idle",
    request: null,
    receipt: null,
    error: null,
  };

  function snapshot(value) {
    return structuredClone(value);
  }

  function emit(nextState) {
    state = snapshot(nextState);

    try {
      onState(snapshot(state));
    } catch {}
  }

  function validateRequest(request) {
    if (!request || typeof request !== "object" || Array.isArray(request)) {
      return { ok: false, code: "INVALID_REQUEST" };
    }

    const { requestId, productId, quantity } = request;

    if (
      typeof requestId !== "string" ||
      !requestId.trim() ||
      typeof productId !== "string" ||
      !productId.trim() ||
      !Number.isInteger(quantity) ||
      quantity <= 0
    ) {
      return { ok: false, code: "INVALID_REQUEST" };
    }

    return null;
  }
  emit({
    status: "idle",
    request: null,
    receipt: null,
    error: null,
  });

  async function confirm(request) {
    if (disposed) {
      return { ok: false, code: "DISPOSED" };
    }

    if (activeOperation !== null) {
      return { ok: false, code: "BUSY" };
    }

    const validationFailure = validateRequest(request);

    if (validationFailure) {
      return validationFailure;
    }

    const requestCopy = snapshot(request);

    const operation = {
      abortController: new AbortController(),
    };

    activeOperation = operation;

    emit({
      status: "submitting",
      request: requestCopy,
      receipt: null,
      error: null,
    });

    try {
      let result;

      try {
        result = await submit(
          snapshot(requestCopy),
          operation.abortController.signal,
        );
      } catch {
        result = { ok: false, code: "SUBMIT_FAILED" };
      }

      if (disposed || activeOperation !== operation) {
        return { ok: false, code: "DISPOSED" };
      }

      if (result && result.ok === true) {
        emit({
          status: "success",
          request: requestCopy,
          receipt: result.receipt,
          error: null,
        });
      } else {
        const failure =
          result && result.ok === false
            ? result
            : { ok: false, code: "SUBMIT_FAILED" };

        emit({
          status: "error",
          request: requestCopy,
          receipt: null,
          error: failure.code,
        });

        return snapshot(failure);
      }

      return snapshot(result);
    } finally {
      if (activeOperation === operation) {
        activeOperation = null;
      }
    }
  }

  function dispose() {
    if (disposed) {
      return;
    }

    disposed = true;

    const operation = activeOperation;
    activeOperation = null;

    if (operation !== null) {
      operation.abortController.abort();
    }
  }

  return { confirm, dispose };
}
