---
name: "review-incoming-orders"
description: "Review newly ingested orders and decide what needs follow-up."
---

# Review Incoming Orders

## Profile

Operations staff.

## Goal

Review newly ingested orders and decide what needs follow-up.

## Modules

- `orders.intake` · suite `operations`
- `orders.tracking` · suite `operations`

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

## Implementation via Uproc MCP

- Use:
  - `orders.intake.orders.list`
  - `orders.intake.emails.list`
  - `orders.tracking.orders.list`
  - `orders.tracking.emails.list`
- Sort by recent creation when the worker asks for new activity.
- Use `orders.intake.reprocess_order` when the worker wants to retry parsing or processing for an ingested order.
- Use `orders.intake.validate_order` when the worker confirms an ingested order is ready for validation.
- Use `orders.intake.send_order_to_erp` when the worker wants to push a validated order into ERP sync.
- Use `orders.tracking.mark_received` when the worker confirms a tracked order has arrived.
- Use `orders.tracking.cancel_order` when the worker confirms the tracked order should be cancelled.
- Use `orders.tracking.send_reminder` when the worker needs to leave the order in follow-up and trigger reminder handling.
- Use upload shortcuts only when the worker is injecting source files or payloads.

## Implementation via Uproc CLI

- Read orders with:
  - `uproc applications orders intake list [--page 1]`
  - `uproc applications orders intake list-emails [--page 1]`
  - `uproc applications orders tracking list [--page 1]`
- Act on ingested orders with `uproc applications orders intake reprocess <order_id>`, `uproc applications orders intake validate <order_id>`, and `uproc applications orders intake send-to-erp <order_id>`.
- Act on tracked orders with `uproc applications orders tracking mark-received <order_id>`, `uproc applications orders tracking cancel <order_id>`, and `uproc applications orders tracking send-reminder <order_id>`.

## Output

- Order intake summary.
- Exception list.
- Suggested next action per issue.