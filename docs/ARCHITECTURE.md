# Architecture and micro app scope

Start with React web, React Native mobile, a modular Node.js backend, PostgreSQL, and file storage. Share justified domain/contracts code; keep platform UI explicit. Add outbox/workers when delivery and CPU exercises require them.

Implement in the [roadmap's order](ROADMAP.md): shared JavaScript/TypeScript domain units, a small Node/PostgreSQL API, web clients, then native clients and deeper product behavior. Jobs and inventory have distinct owners; both learners implement every platform and demonstrate all concepts.

Suggested target layout (learners implement it):

```text
apps/
  web-shell/
  web-dispatch/
  web-reporting/
  mobile-technician/
  api/
  worker/
packages/
  domain/
  contracts/
  design-tokens/
  mobile-jobs/
  mobile-inventory/
  mobile-evidence/
  mobile-sync/
experiments/
evidence/
```

## Web micro frontend experiment

After the core workflow works, create a shell and separately built dispatch/reporting remotes using Module Federation or a justified alternative. Demonstrate independent artifacts/deployment, contract compatibility, routing, dependency sharing, CSS isolation, failure recovery, and rollback.

Define trusted remote locations. Loaded remote JavaScript executes with host privileges; an error boundary is not a security sandbox. Backend authorization remains mandatory. Prefer explicit versioned contracts to shared global mutable state.

Compare micro frontends with a modular application and quantify costs for a two-person team. Service extraction is a separate backend decision, not a prerequisite.

## React Native feature modules

Use jobs/evidence/sync packages with public interfaces and test harnesses. Independent feature testing does not prove independent native delivery. Evaluate runtime/OTA tooling against platform and native-build constraints before claiming separate releases.

## Primary references

- [Webpack Module Federation](https://webpack.js.org/concepts/module-federation/) — independent builds and runtime integration.
- [React Suspense](https://react.dev/reference/react/Suspense) — supported loading and streaming.
- [React Native architecture](https://reactnative.dev/architecture/overview) — native integration and rendering.
- [React Native security](https://reactnative.dev/docs/security) — storage/networking considerations.
- [Node event-loop guidance](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop) — CPU/blocking behavior.
