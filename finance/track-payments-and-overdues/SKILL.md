---
name: "track-payments-and-overdues"
description: "Review outstanding payments and decide the next communication or escalation step."
---

# Track Payments And Overdues

## Profile

Collections and finance staff.

## Goal

Review outstanding payments and decide the next communication or escalation step.

## Modules

- `collections` · suite `finance`

## Backend capabilities

- Read KPIs.
- Read `invoices`, `payments`, `reminders`, and `communications`.
- Upload and webhook support.

## Use this skill when

- You need a pending collections overview.
- You want to know which clients need a reminder.

## What it should do

- Review unpaid invoices and recent payments.
- Show which reminders or communications already exist.
- Suggest who should be contacted next and why.

## Implementation via Uproc MCP

- Use:
  - `collections.invoices.list`
  - `collections.payments.list`
  - `collections.reminders.list`
  - `collections.communications.list`
- Use `module.kpis` for `collections` when the worker wants a collections overview.
- If the worker needs a new ingestion event from an external system, use `collections.communications.webhook` or the generic `module.webhook` path.
- For the collection strategy flow, use `collections.analyze_plan` to get an AI-generated collection plan (reminder intervals, escalation rules, segment strategies), `collections.get_plan` / `collections.list_plans` to review it, and `collections.execute_plan` to apply the accepted plan. `collections.regenerate_plan` rebuilds an existing plan with the current AI prompt.

## Implementation via Uproc CLI

- Read debt data with the generic reader (debt-track has no dedicated CLI verbs):
  - `uproc applications collections list-invoices [--page 1]`
  - `uproc applications collections list-payments [--page 1]`
  - `uproc applications collections list-reminders [--page 1]`
  - `uproc applications collections list-communications [--page 1]`
- KPIs: `uproc applications module overview debt-track kpis`.
- Webhook: `uproc applications module webhook debt-track communications <payload_json>`.
- Limit: the debt-track AI plan flow (`analyze_plan`/`execute_plan`) is MCP-only.

## Output

- Collections summary.
- List of overdue items.
- Suggested follow-up actions.