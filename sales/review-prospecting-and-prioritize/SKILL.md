# Review Prospecting And Prioritize

## Profile

Sales development and outbound teams.

## Goal

Review prospecting results and focus effort on the best opportunities.

## Modules

- `leads.capture` · suite `sales`
- `leads.enrich` · suite `sales`
- `campaigns` · suite `sales`

## Backend capabilities

- Read `strategies`, `opportunities`, `prospects`, `executions`, `duplicates`, `sync_logs`, `campaigns`, and `audiences`.
- Upload and webhook support.

## Use this skill when

- You need to prioritize outreach.
- You want to review which prospecting actions generated the best opportunities.

## What it should do

- Summarize current opportunities and prospects.
- Flag duplicates or sync issues.
- Suggest prioritization criteria.

## Implementation via Uproc MCP

- Use:
  - `leads.capture.strategies.list`
  - `leads.capture.opportunities.list`
  - `leads.capture.prospects.list`
  - `leads.capture.executions.list`
  - `leads.enrich.duplicates.list`
  - `leads.enrich.sync_logs.list`
  - `campaigns.campaigns.list`
  - `campaigns.audiences.list`
- Trigger `leads.capture.run_discovery` when the worker wants to launch a new discovery run from an existing strategy.
- Use `leads.capture.send_opportunity_to_leads` when an opportunity should be converted into the lead workflow.
- Use `module.kpis` on prospecting or campaign modules when the worker wants a compact summary first.

## Implementation via Uproc CLI

- Read prospecting context with:
  - `uproc applications leads capture list-strategies [--page 1]`
  - `uproc applications leads capture list-opportunities [--page 1]`
  - `uproc applications leads capture list-prospects [--page 1]`
  - `uproc applications leads capture list-executions [--page 1]`
- Launch a discovery run with `uproc applications leads capture run-discovery <strategy_id> [company] [domain]`.
- Convert an opportunity into the lead workflow with `uproc applications leads capture send-to-leads <opportunity_id>`.
- Read campaign context with `uproc applications campaigns list [--page 1]` and `uproc applications campaigns list-audiences [--page 1]`.
- Lead-intelligence reads use the generic reader: `uproc applications module collection lead-intelligence duplicates [--page 1]` / `uproc applications module collection lead-intelligence sync_logs [--page 1]`.

- Enrichment runs: `module.action` on `leads.capture`-scope module `lead-prospecting` with `enrichment_settings_get|update`, `enrichment_run` (`prospect_ids`, optional `pipeline_keys`), `enrichment_runs` (`prospect_id`, `limit`) and `enrichment_cancel` (`run_id`).
- CLI equivalent: `uproc applications module action lead-prospecting enrichment-run '<json>'` (misma acción para settings/runs/cancel).

## Output

- Prospecting summary.
- High-priority leads to contact.
- Cleanup or follow-up suggestions.
