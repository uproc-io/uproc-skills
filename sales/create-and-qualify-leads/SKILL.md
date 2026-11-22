# Create And Qualify Leads

## Profile

Sales and business development staff.

## Goal

Create new leads when needed and organize the first qualification pass.

## Modules

- `leads.manage` · suite `sales`
- `leads.enrich` · suite `sales`

## Backend capabilities

- Read KPIs and read `leads`.
- Create new records in `leads.manage.leads`.
- Review `leads.enrich` collections such as `leads`, `executions`, `sync_logs`, and `duplicates`.

## Use this skill when

- You need to register a new lead.
- You want to review duplicates or enrichment signals before follow-up.

## What it should do

- Ask for the minimum required fields.
- Create the lead when the user confirms.
- Highlight duplicates or missing enrichment context.

## Implementation via Uproc MCP

- Use `leads.manage.leads.create` for new lead creation. This is one of the few generic external create shortcuts currently enabled.
- Read context with:
  - `leads.manage.leads.list`
  - `leads.enrich.leads.list`
  - `leads.enrich.duplicates.list`
  - `leads.enrich.executions.list`
- If the environment varies by customer, confirm create support with `module.capabilities` for `leads.manage` before assuming write access.
- For the lead-intelligence planning flow, use `leads.enrich.analyze_plan` to get an AI-generated enrichment/scoring plan, `leads.enrich.get_plan` / `leads.enrich.list_plans` to review it, and `leads.enrich.execute_plan` to apply the accepted plan (enrichment steps, scoring rules, and configuration). `leads.enrich.regenerate_plan` rebuilds an existing plan with the current AI prompt.

## Implementation via Uproc CLI

- Read leads with `uproc applications leads manage list [--page 1 --sort-field created_at --sort-order desc --filter-field status --filter-value <status>]`.
- Rerun enrichment for a lead with `uproc applications leads enrich rerun-intelligence <lead_id>`.
- Lead-intelligence reads use the generic reader (no dedicated CLI verb): `uproc applications module collection lead-intelligence leads [--page 1]`, `uproc applications module collection lead-intelligence duplicates [--page 1]`, `uproc applications module collection lead-intelligence executions [--page 1]`.
- Limit: the CLI cannot create leads (no `leads create`); lead creation requires the MCP `leads.manage.leads.create` tool or the web UI.

## Output

- Lead creation summary.
- Qualification notes.
- Suggested next commercial step.
