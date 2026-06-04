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

## Implementation via Bizzmod MCP

- Use `inventory-planning.orders.list` as the main data source.
- Use `module.kpis` for `inventory-planning` if the worker asks for a summary before the row review.
- Use `inventory-planning.mark_received` when the worker confirms an incoming order has been physically received.
- Use `inventory-planning.cancel_order` when the worker confirms the replenishment order should be cancelled.
- Use `inventory-planning.send_reminder` when the worker needs to flag an in-flight order for supplier follow-up.

## Output

- Planning summary.
- Risk list.
- Suggested operational checks.
