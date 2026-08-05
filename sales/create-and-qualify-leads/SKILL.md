# Create And Qualify Leads

## Profile

Sales and business development staff.

## Goal

Create new leads when needed and organize the first qualification pass.

## Modules

- `lead-management`
- `lead-intelligence`

## Backend capabilities

- Read KPIs and read `leads`.
- Create new records in `lead-management.leads`.
- Review `lead-intelligence` collections such as `leads`, `executions`, `sync_logs`, and `duplicates`.

## Use this skill when

- You need to register a new lead.
- You want to review duplicates or enrichment signals before follow-up.

## What it should do

- Ask for the minimum required fields.
- Create the lead when the user confirms.
- Highlight duplicates or missing enrichment context.

## Implementation via Uproc MCP

- Use `lead-management.leads.create` for new lead creation. This is one of the few generic external create shortcuts currently enabled.
- Read context with:
  - `lead-management.leads.list`
  - `lead-intelligence.leads.list`
  - `lead-intelligence.duplicates.list`
  - `lead-intelligence.executions.list`
- If the environment varies by customer, confirm create support with `module.capabilities` for `lead-management` before assuming write access.

## Output

- Lead creation summary.
- Qualification notes.
- Suggested next commercial step.
