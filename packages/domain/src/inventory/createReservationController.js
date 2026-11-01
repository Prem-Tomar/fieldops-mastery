function createReservationController({ submit, onState }) {
  if (typeof submit !== "function" || typeof onState !== "function") {
    throw new TypeError("INVALID_RESERVATION_CONFIG");
  }

  let disposed = false;
  let active = false;
  let operationId = 0;
  let activeAbortController = null;

  let state = {
    status: "idle",
    request: null,
    receipt: null,
    error: null,
  };

  function clone(value) {
    return value == null ? value : structuredClone(value);
  }

  function emit(next) {
    state = clone(next);
    onState(clone(state));
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

  emit(state);

  async function confirm(request) {
    if (disposed) {
      return { ok: false, code: "DISPOSED" };
    }

    if (active) {
      return { ok: false, code: "BUSY" };
    }

    if (!validateRequest(request)) {
      return { ok: false, code: "INVALID_REQUEST" };
    }

    const snapshot = clone(request);
    const id = ++operationId;
    const abortController = new AbortController();

    active = true;
    activeAbortController = abortController;

    emit({
      status: "submitting",
      request: snapshot,
      receipt: null,
      error: null,
    });

    try {
      const result = await submit(snapshot, abortController.signal);

      if (disposed || id !== operationId) {
        return { ok: false, code: "DISPOSED" };
      }

      if (!result.ok) {
        emit({
          status: "error",
          request: snapshot,
          receipt: null,
          error: result?.code || "SUBMIT_FAILED",
        });

        return result;
      }

      emit({
        status: "success",
        request: snapshot,
        receipt: result?.receipt ?? null,
        error: null,
      });

      return result;
    } catch (error) {
      if (disposed || id !== operationId) {
        return { ok: false, code: "DISPOSED" };
      }

      emit({
        status: "error",
        request: snapshot,
        receipt: null,
        error: "SUBMIT_FAILED",
      });

      return { ok: false, code: "SUBMIT_FAILED" };
    } finally {
      if (id === operationId) {
        active = false;
        activeAbortController = null;
      }
    }
  }

  function dispose() {
    if (disposed) return;

    disposed = true;
    operationId++;

    activeAbortController?.abort();
    activeAbortController = null;
    active = false;
  }

  async function retry() {
    if (!state.request) {
      return { ok: false, code: "NO_REQUEST" };
    }

    return confirm(state.request);
  }
  return { confirm, dispose, retry };
}
