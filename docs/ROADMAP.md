# Phases and roadmap

Target: **22 weeks at 20–25 hours per week per learner**, plus coach time. This estimate extends when remediation, unfamiliar native tooling, or unavailable platform hardware requires it. Advancement depends on evidence, not dates.

| Phase | Weeks | Focus | Tasks | Phase gate |
|---|---|---|---|---|
| P01 | 1–2 | JavaScript foundations | [JS-01](../curriculum/tasks/JS-01.md), [JS-02](../curriculum/tasks/JS-02.md), [JS-03](../curriculum/tasks/JS-03.md), [JS-04](../curriculum/tasks/JS-04.md) | Predict asynchronous behavior and implement correct domain utilities without assistance. |
| P02 | 3–4 | TypeScript and domain contracts | [TS-01](../curriculum/tasks/TS-01.md), [TS-02](../curriculum/tasks/TS-02.md), [TS-03](../curriculum/tasks/TS-03.md), [TS-04](../curriculum/tasks/TS-04.md) | Reject invalid states statically and untrusted data at runtime. |
| P03 | 5–6 | React fundamentals | [REACT-01](../curriculum/tasks/REACT-01.md), [REACT-02](../curriculum/tasks/REACT-02.md), [REACT-03](../curriculum/tasks/REACT-03.md), [REACT-04](../curriculum/tasks/REACT-04.md) | Build an accessible job workflow and explain render, state, and effect behavior. |
| P04 | 7–8 | Advanced React | [REACT-05](../curriculum/tasks/REACT-05.md), [REACT-06](../curriculum/tasks/REACT-06.md), [REACT-07](../curriculum/tasks/REACT-07.md), [REACT-08](../curriculum/tasks/REACT-08.md) | Demonstrate correct cache, optimistic, rendering, and recovery behavior. |
| P05 | 9–10 | React Native fundamentals | [RN-01](../curriculum/tasks/RN-01.md), [RN-02](../curriculum/tasks/RN-02.md), [RN-03](../curriculum/tasks/RN-03.md), [RN-04](../curriculum/tasks/RN-04.md) | Demonstrate platform behavior and persisted workflows on Android and iOS. |
| P06 | 11–12 | Node.js and data correctness | [NODE-01](../curriculum/tasks/NODE-01.md), [NODE-02](../curriculum/tasks/NODE-02.md), [NODE-03](../curriculum/tasks/NODE-03.md), [NODE-04](../curriculum/tasks/NODE-04.md) | Prove HTTP contracts, transaction correctness, and idempotent completion. |
| P07 | 13–14 | Offline mobile synchronization | [SYNC-01](../curriculum/tasks/SYNC-01.md), [SYNC-02](../curriculum/tasks/SYNC-02.md), [SYNC-03](../curriculum/tasks/SYNC-03.md), [SYNC-04](../curriculum/tasks/SYNC-04.md) | Recover drafts and synchronize under conflicts, app termination, and repeated requests. |
| P08 | 15–16 | Real-time delivery and Node depth | [RT-01](../curriculum/tasks/RT-01.md), [RT-02](../curriculum/tasks/RT-02.md), [RT-03](../curriculum/tasks/RT-03.md), [RT-04](../curriculum/tasks/RT-04.md) | Recover missed events and demonstrate bounded background and streaming work. |
| P09 | 17–18 | Micro frontends and mobile feature modules | [MFE-01](../curriculum/tasks/MFE-01.md), [MFE-02](../curriculum/tasks/MFE-02.md), [MFE-03](../curriculum/tasks/MFE-03.md), [MFE-04](../curriculum/tasks/MFE-04.md) | Deploy an independent web remote, isolate its failures, and defend mobile module boundaries. |
| P10 | 19–20 | Security, performance, and operations | [OPS-01](../curriculum/tasks/OPS-01.md), [OPS-02](../curriculum/tasks/OPS-02.md), [OPS-03](../curriculum/tasks/OPS-03.md), [OPS-04](../curriculum/tasks/OPS-04.md) | Prove tenant boundaries, profile real bottlenecks, and rehearse recovery. |
| P11 | 21–22 | Evolution and mastery capstone | [CAP-01](../curriculum/tasks/CAP-01.md), [CAP-02](../curriculum/tasks/CAP-02.md), [CAP-03](../curriculum/tasks/CAP-03.md), [CAP-04](../curriculum/tasks/CAP-04.md) | Both developers independently solve unseen changes and incidents using evidence. |

## Learning-to-mastery cycle

1. Clarify the problem; write examples, assumptions, and invariants.
2. Study listed concepts and reproduce them in isolated experiments.
3. Record individual predictions before comparing answers.
4. Implement shared behavior; alternate driver/reviewer.
5. Each learner submits individual evidence for every acceptance criterion and concept.
6. Coach introduces an unseen failure or change and scores independent understanding.
7. Update per-concept ledgers, remediate gaps, then advance.

Reveal hints progressively and record their use. The 10-year learner receives deeper variations; the 5-year learner can use more guided practice. Both have the same independent pass threshold and complete all basics.

## Dependencies and weekly rhythm

Tasks are sequential. A prerequisite is satisfied by that learner's evidence, not the other person's completion. Shared phase gates require both learners to pass. Isolated spikes avoid duplicating production work.

Use fixture-driven domain and client work before integrating real APIs. Security, accessibility, and testing start early; P10 consolidates them.

Each week: independent concept experiments; implementation and pair integration; reciprocal review; tests and unseen challenge; ledger and coaching. Revisit an earlier basic and advanced concept.

Micro frontend work begins only after the core platform and recovery flow exist. Two weeks are added to the original 20-week roadmap.

## Environment prerequisites

Pin supported runtime/tool versions and record them. Have Node.js/TypeScript tooling, PostgreSQL, web browser, Android tooling, and access to macOS/Xcode for iOS builds and native-module exercises. Mark unverified platforms pending; Android evidence is not an iOS pass.
