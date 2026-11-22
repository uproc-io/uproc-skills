# Review Investments

## Profile

Finance and leadership staff.

## Goal

Review investment scenarios and their reports, compare expected returns and risk, and prepare the next decision.

## Modules

- `investments` · suite `finance`

## Backend capabilities

- Scenarios with capital, horizon, expected return, risk profile and allocation assumptions.
- Reports generated from a scenario, including performance and risk outputs.
- Read access to both collections; creation/update follows the generic module contract.

## Use this skill when

- A worker must review the current investment scenarios or the latest reports.
- Leadership asks for expected ROI, risk or capital allocation before a decision.
- A scenario needs to be created or updated from a business case.

## What it should do

- List scenarios and reports for the customer.
- Summarize capital, expected return, risk and the latest report.
- Recommend whether to keep, adjust or create a scenario.

## Implementation via Uproc MCP

- List scenarios with `module.data` on `investments` / `scenarios`.
- List reports with `module.data` on `investments` / `reports`.
- Read one record with `module.collection` on the same module/collection and its id.
- Create or update a scenario with `module.create` / `module.update` on `investments` / `scenarios` (respect the schema returned by `module.collections`).

## Implementation via Uproc CLI

- List scenarios with `uproc applications investments list-scenarios [--page 1]`.
- List reports with `uproc applications investments list-reports [--page 1]`.
- Limit: there are no dedicated CLI verbs to create scenarios or generate reports; use the MCP tools or the web UI.

## Output

- Scenario and report summary.
- Expected return, risk and open differences.
- Recommended next action (keep, adjust, create or request a report).
