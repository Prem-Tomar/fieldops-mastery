# Contributor progress dashboard

The dashboard tracks both contributors' distinct product work, all 338 concepts each, individual review scores, accepted gates and the finish forecast. It reads the existing curriculum; it is reviewer tooling, not a learner implementation assignment.

## Open and review

Use Python 3.12+ and the GitHub CLI. Sign in with `gh auth login` as Prem-Tomar, then run from the repository root:

```sh
python scripts/dashboard_server.py
```

Open **http://127.0.0.1:8765**. The server reads the trusted GitHub identity and existing issue statuses at startup; it rechecks the owner identity before each save. Other identities or an unavailable GitHub login make the dashboard read-only. Use `--skip-issue-sync` to view the last task snapshot when offline; saving still requires the owner identity to be verified online. It listens only on this computer's loopback address.

1. **Product tasks:** inspect all 52 complementary contributions and the existing GitHub issue statuses. Refresh GitHub status using the read-only sync operation. A closed issue never automatically passes a gate.
2. **Concept mastery:** search/filter concepts, then update each contributor's status and individual PR/session evidence. Independent/mastered status requires evidence. Retention failures can regress a status.
3. **Reviews & gates:** choose a slice and save separate assessments for Neha and Madhavi. Save assisted or incomplete scores truthfully; they remain visible. Set each task to ready for review only when it has evidence.
4. **Accept:** for the next consecutive gate, both assessments must be ready with at least 2 in every dimension. Confirm integrated product behavior, independently assessed concepts, and required platform/security/recovery checks. Enter the actual start date at the first acceptance, then select **Accept gate & update forecast**.

The dashboard saves acceptance and recalculates the forecast immediately. Reloading preserves the records; no browser-local storage is used. The overview also refreshes once a minute when visible, without overwriting a review form. On the review page, use Refresh when records changed elsewhere. Stale saves are rejected rather than overwriting another tab's work. Gate acceptance is a slice-level review; closing individual issues alone does not shrink the forecast.

## Authoritative records and sharing

| Record | Purpose |
|---|---|
| [roadmap.json](../curriculum/roadmap.json) | Ordered slices, two distinct asks and planning baseline |
| [reviews.json](../curriculum/reviews.json) | Per-contributor task status, all five review scores, notes and individual evidence |
| [progress.json](../curriculum/progress.json) | Actual start and immutable accepted gate evidence |
| [Neha's ledger](../evidence/learner-5y/coverage.csv), [Madhavi's ledger](../evidence/learner-10y/coverage.csv) | Separate concept statuses, evidence and assessor |
| [issue-status.json](../curriculum/issue-status.json) | Dated snapshot of existing GitHub issues, not mastery evidence |

Saves modify the local checkout. Commit the changed records, submit them through a PR and merge as Prem-Tomar to share verified progress. The dashboard does not commit, push, merge, change GitHub issues or create successors. The existing governance and issue publication pause remain in effect. No record has been marked passed just to demonstrate the dashboard.

CI validates records, recalculates the forecast, exercises dashboard write/security behavior and produces a read-only **mastery-dashboard** artifact containing `index.html`. Download it from the relevant successful Actions run and open the file in a browser. It reflects that run's records and date; it has no write controls or session credentials. The master-branch artifact reflects merged progress, while a PR artifact is a preview of its branch's records.

To generate the same portable snapshot locally:

```sh
python scripts/export_dashboard.py
```

Open `output/dashboard/index.html`. Regenerate after saving progress for an updated snapshot. The local reviewer dashboard is the live acceptance interface; this HTML artifact is a dated read-only view, not a hosted multi-user service. Stop the local server with Ctrl+C when finished.

## Verification and limits

The finish calculation reuses [forecast_roadmap.py](../scripts/forecast_roadmap.py). It shortens elapsed duration when jointly verified pace is faster; it can extend when work stalls. All slices and concepts remain required. Final completion stays pending while either concept ledger has gaps, even if all product gates were accepted. Platform and concept acceptance confirmations are reviewer judgments backed by actual evidence; the dashboard cannot infer learning or device correctness from a checkbox or issue closure.

Run:

```sh
python scripts/validate_curriculum.py
python scripts/test_dashboard.py
python scripts/forecast_roadmap.py
```

Tests use isolated temporary records and localhost, including an acceptance that moves the forecast earlier, incomplete/assisted assessment rejection, stale edits, unauthorized/cross-origin writes, missing concept evidence, persistence and the final audit. These checks are maintenance for the dashboard and are not assigned learner issues.
