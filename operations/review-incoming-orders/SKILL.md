# Review Incoming Orders

## Profile

Operations staff.

## Goal

Review newly ingested orders and decide what needs follow-up.

## Modules

- `order-ingest`
- `order-track`

## Backend capabilities

- Read KPIs.
- Read `orders` and `emails`.
- Upload and webhook support.

## Use this skill when

- You need the latest incoming order picture.
- You want to detect missing, malformed, or delayed order records.

## What it should do

- Review recent orders first.
- Compare ingest and tracking views when useful.
- Flag exceptions needing manual review.

## Implementation via Bizzmod MCP

- Use:
  - `order-ingest.orders.list`
  - `order-ingest.emails.list`
  - `order-track.orders.list`
  - `order-track.emails.list`
- Sort by recent creation when the worker asks for new activity.
- Use `order-ingest.reprocess_order` when the worker wants to retry parsing or processing for an ingested order.
- Use `order-ingest.validate_order` when the worker confirms an ingested order is ready for validation.
- Use `order-ingest.send_order_to_erp` when the worker wants to push a validated order into ERP sync.
- Use `order-track.mark_received` when the worker confirms a tracked order has arrived.
- Use `order-track.cancel_order` when the worker confirms the tracked order should be cancelled.
- Use `order-track.send_reminder` when the worker needs to leave the order in follow-up and trigger reminder handling.
- Use upload shortcuts only when the worker is injecting source files or payloads.

## Output

- Order intake summary.
- Exception list.
- Suggested next action per issue.
