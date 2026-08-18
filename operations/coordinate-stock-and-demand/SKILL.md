# Coordinate Stock And Demand

## Profile

Operations and supply staff.

## Goal

Review inventory planning inputs and summarize replenishment pressure.

## Modules

- `inventory-planning`

## Backend capabilities

- Read KPIs.
- Read `orders`.
- Upload and webhook support.

## Use this skill when

- You need a quick stock planning summary.
- You want to identify risky order concentrations.

## What it should do

- Review the available planning orders.
- Point out likely stock pressure or operational concentration.
- Recommend where to check manually.

## Implementation via Uproc MCP

- Use `inventory-planning.orders.list` as the main data source.
- Use `module.kpis` for `inventory-planning` if the worker asks for a summary before the row review.
- Use `inventory-planning.mark_received` when the worker confirms an incoming order has been physically received.
- Use `inventory-planning.cancel_order` when the worker confirms the replenishment order should be cancelled.
- Use `inventory-planning.send_reminder` when the worker needs to flag an in-flight order for supplier follow-up.

## Implementation via Uproc CLI

- Read planning orders with `uproc applications inventory list [--page 1]`.
- KPIs: `uproc applications module overview inventory-planning kpis`.
- Act on orders with `uproc applications inventory mark-received <order_id>`, `uproc applications inventory cancel <order_id>`, and `uproc applications inventory send-reminder <order_id>`.

## Output

- Planning summary.
- Risk list.
- Suggested operational checks.
