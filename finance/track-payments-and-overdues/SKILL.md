# Track Payments And Overdues

## Profile

Collections and finance staff.

## Goal

Review outstanding payments and decide the next communication or escalation step.

## Modules

- `debt-track`

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

## Implementation via Bizzmod MCP

- Use:
  - `debt-track.invoices.list`
  - `debt-track.payments.list`
  - `debt-track.reminders.list`
  - `debt-track.communications.list`
- Use `module.kpis` for `debt-track` when the worker wants a collections overview.
- If the worker needs a new ingestion event from an external system, use `debt-track.communications.webhook` or the generic `module.webhook` path.

## Output

- Collections summary.
- List of overdue items.
- Suggested follow-up actions.
