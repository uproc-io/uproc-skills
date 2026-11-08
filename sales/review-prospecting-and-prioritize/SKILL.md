# Review Prospecting And Prioritize

## Profile

Sales development and outbound teams.

## Goal

Review prospecting results and focus effort on the best opportunities.

## Modules

- `lead-prospecting`
- `lead-intelligence`
- `campaign-automation`

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
  - `lead-prospecting.strategies.list`
  - `lead-prospecting.opportunities.list`
  - `lead-prospecting.prospects.list`
  - `lead-prospecting.executions.list`
  - `lead-intelligence.duplicates.list`
  - `lead-intelligence.sync_logs.list`
  - `campaign-automation.campaigns.list`
  - `campaign-automation.audiences.list`
- Trigger `lead-prospecting.run_discovery` when the worker wants to launch a new discovery run from an existing strategy.
- Use `lead-prospecting.send_opportunity_to_leads` when an opportunity should be converted into the lead workflow.
- Use `module.kpis` on prospecting or campaign modules when the worker wants a compact summary first.

## Implementation via Uproc CLI

- Read prospecting context with:
  - `uproc applications lead-prospecting list-strategies [--page 1]`
  - `uproc applications lead-prospecting list-opportunities [--page 1]`
  - `uproc applications lead-prospecting list-prospects [--page 1]`
  - `uproc applications lead-prospecting list-executions [--page 1]`
- Launch a discovery run with `uproc applications lead-prospecting run-discovery <strategy_id> [company] [domain]`.
- Convert an opportunity into the lead workflow with `uproc applications lead-prospecting send-to-leads <opportunity_id>`.
- Read campaign context with `uproc applications campaign-automation list [--page 1]` and `uproc applications campaign-automation list-audiences [--page 1]`.
- Lead-intelligence reads use the generic reader: `uproc applications module collection lead-intelligence duplicates [--page 1]` / `uproc applications module collection lead-intelligence sync_logs [--page 1]`.

## Output

- Prospecting summary.
- High-priority leads to contact.
- Cleanup or follow-up suggestions.
