# Manage Incidents

## Profile

Support and customer care staff.

## Goal

Review tickets and cases, prioritize them, and prepare next actions.

## Modules

- `customer-care`
- `case-lifecycle`

## Backend capabilities

- Read KPIs.
- Read `tickets`, `cases`, `cases_by_status`, and `cases_by_type`.
- Upload and webhook support.

## Use this skill when

- You need a support queue summary.
- You want to identify stuck or urgent cases.

## What it should do

- Review open work.
- Group by urgency, status, or type.
- Highlight stale tickets and blocked cases.
- Recommend reply, escalation, or closure review.

## Implementation via Uproc MCP

- Use:
  - `customer-care.tickets.list`
  - `case-lifecycle.cases.list`
  - `case-lifecycle.cases_by_status.list`
  - `case-lifecycle.cases_by_type.list`
- Use `module.kpis` for either module when the worker first asks for volume and status overview.
- Filter by status or type with `filter_field` and `filter_value` where needed.
- Use `customer-care.create_ticket` when the worker needs to open a new support incident from the conversation.
- Use `customer-care.mark_resolved`, `customer-care.close_ticket`, and `customer-care.reopen_ticket` when the worker needs explicit resolution and closure actions after triage.
- Use `customer-care.update_ticket_status` only when the worker needs a less common status transition outside those explicit ticket verbs.
- Use `customer-care.assign_ticket` when the worker needs to route a ticket to a specific support owner.
- Use `customer-care.reply_to_ticket` when the worker needs to log an agent reply inside the customer-care workflow.
- Use `case-lifecycle.create_case_note` when the worker needs to record a follow-up, escalation summary, or customer update inside the case workflow.
- Use `case-lifecycle.close_case` and `case-lifecycle.reopen_case` when the worker needs to move an operational case into or out of closure.

## Output

- Queue summary.
- Priority incidents.
- Recommended next step per case.
