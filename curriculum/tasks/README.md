# Concept reference index

These 44 definitions retain every catalog concept and provide reference scenarios, hints and mastery prompts. The [six-month roadmap](../../docs/ROADMAP.md) controls implementation order and gives each learner a different product contribution. The order/phase/prerequisite columns below are the original reference index, not the current publication sequence; Node and light PostgreSQL now precede React clients.

Both learners independently demonstrate every reference concept through their own features or bounded experiments. Do not assign the same definition to both as duplicate production work. Where legacy examples describe evidence documents or test deliverables, apply the current roadmap and assessment policy: PR/session evidence is sufficient, test-writing feedback is optional, and neither tests nor documentation is a standalone assigned issue.

Fourteen week-one issues already exist. No more issues are authorized by this index or roadmap update. Future issues need explained terms, unit input/output contracts, progressive hints, distinct product integration and frontend screen images where applicable.

| Order | Task | Phase | Prerequisite |
|---|---|---|---|
| 1 | [JS-01: Build pure job and inventory utilities](JS-01.md) | P01 | None |
| 2 | [JS-02: Predict scope, binding, prototypes, and module behavior](JS-02.md) | P01 | JS-01 |
| 3 | [JS-03: Debounce search and prevent stale responses](JS-03.md) | P01 | JS-02 |
| 4 | [JS-04: Implement bounded asynchronous work](JS-04.md) | P01 | JS-03 |
| 5 | [TS-01: Encode job-state invariants](TS-01.md) | P02 | JS-04 |
| 6 | [TS-02: Create reusable typed pagination and projections](TS-02.md) | P02 | TS-01 |
| 7 | [TS-03: Validate untrusted input and classify errors](TS-03.md) | P02 | TS-02 |
| 8 | [TS-04: Define versioned web and mobile contracts](TS-04.md) | P02 | TS-03 |
| 9 | [REACT-01: Build a predictable component and state model](REACT-01.md) | P03 | TS-04 |
| 10 | [REACT-02: Build an accessible assignment form](REACT-02.md) | P03 | REACT-01 |
| 11 | [REACT-03: Use effects and custom hooks safely](REACT-03.md) | P03 | REACT-02 |
| 12 | [REACT-04: Test user behavior and isolate UI failures](REACT-04.md) | P03 | REACT-03 |
| 13 | [REACT-05: Design server-state caching and invalidation](REACT-05.md) | P04 | REACT-04 |
| 14 | [REACT-06: Implement optimistic assignment with rollback](REACT-06.md) | P04 | REACT-05 |
| 15 | [REACT-07: Compare client rendering and streamed rendering](REACT-07.md) | P04 | REACT-06 |
| 16 | [REACT-08: Profile a busy dispatch board](REACT-08.md) | P04 | REACT-07 |
| 17 | [RN-01: Build navigation and adaptive technician screens](RN-01.md) | P05 | REACT-08 |
| 18 | [RN-02: Capture and retain completion evidence](RN-02.md) | P05 | RN-01 |
| 19 | [RN-03: Profile native lists and interaction](RN-03.md) | P05 | RN-02 |
| 20 | [RN-04: Implement and diagnose native integration](RN-04.md) | P05 | RN-03 |
| 21 | [NODE-01: Build validated HTTP job endpoints](NODE-01.md) | P06 | RN-04 |
| 22 | [NODE-02: Design schema and prevent inventory races](NODE-02.md) | P06 | NODE-01 |
| 23 | [NODE-03: Make completion idempotent](NODE-03.md) | P06 | NODE-02 |
| 24 | [NODE-04: Protect tenant and role boundaries](NODE-04.md) | P06 | NODE-03 |
| 25 | [SYNC-01: Persist a durable offline operation queue](SYNC-01.md) | P07 | NODE-04 |
| 26 | [SYNC-02: Synchronize 500 queued operations](SYNC-02.md) | P07 | SYNC-01 |
| 27 | [SYNC-03: Resolve offline completion versus cancellation](SYNC-03.md) | P07 | SYNC-02 |
| 28 | [SYNC-04: Resume attachments safely](SYNC-04.md) | P07 | SYNC-03 |
| 29 | [RT-01: Recover live updates after disconnection](RT-01.md) | P08 | SYNC-04 |
| 30 | [RT-02: Make background side effects recoverable](RT-02.md) | P08 | RT-01 |
| 31 | [RT-03: Stream a large report with backpressure](RT-03.md) | P08 | RT-02 |
| 32 | [RT-04: Offload CPU work and shut down gracefully](RT-04.md) | P08 | RT-03 |
| 33 | [MFE-01: Define and challenge micro frontend boundaries](MFE-01.md) | P09 | RT-04 |
| 34 | [MFE-02: Build independently deployable shell and remotes](MFE-02.md) | P09 | MFE-01 |
| 35 | [MFE-03: Version contracts and isolate remote failures](MFE-03.md) | P09 | MFE-02 |
| 36 | [MFE-04: Create mobile feature modules with clear boundaries](MFE-04.md) | P09 | MFE-03 |
| 37 | [OPS-01: Threat-model and test sensitive boundaries](OPS-01.md) | P10 | MFE-04 |
| 38 | [OPS-02: Measure end-to-end performance and capacity](OPS-02.md) | P10 | OPS-01 |
| 39 | [OPS-03: Trace and diagnose a failed workflow](OPS-03.md) | P10 | OPS-02 |
| 40 | [OPS-04: Rehearse deployment, rollback, and recovery](OPS-04.md) | P10 | OPS-03 |
| 41 | [CAP-01: Support an older client during domain evolution](CAP-01.md) | P11 | OPS-04 |
| 42 | [CAP-02: Handle disputed inventory and job evidence](CAP-02.md) | P11 | CAP-01 |
| 43 | [CAP-03: Run an unseen incident investigation](CAP-03.md) | P11 | CAP-02 |
| 44 | [CAP-04: Defend architecture and prove concept coverage](CAP-04.md) | P11 | CAP-03 |
