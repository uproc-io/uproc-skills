# Track Orders And Report Issues

## Profile

Support and operations staff.

## Goal

Review order status and prepare customer communication when delays or issues appear.

## Modules

- `orders.tracking` · suite `operations`
- `mail` · suite `operations`

## Backend capabilities

- Read KPIs.
- Read `orders` and `emails`.
- Upload and webhook support.

## Use this skill when

- You need to check the latest order situation.
- You need to notify a customer about an issue.

## What it should do

- Review order state.
- Flag delayed or incomplete orders.
- Prepare a communication draft if needed.

## Implementation via Uproc MCP

- Use `orders.tracking.orders.list` as the main order-status source.
- Use `orders.tracking.emails.list` if intake or communication context matters.
- Use `orders.tracking.mark_received` when the worker confirms delivery.
- Use `orders.tracking.cancel_order` when the worker confirms the order should be cancelled.
- Use `orders.tracking.send_reminder` when the worker needs to push order follow-up before customer communication.
- Use `mail.emails.list` for drafting context if a previous customer conversation exists.

## Implementation via Uproc CLI

- Read orders with `uproc applications orders tracking list [--page 1]`.
- Read tracked orders context with `uproc applications orders tracking list [--page 1]`.
- Act on orders with `uproc applications orders tracking mark-received <order_id>`, `uproc applications orders tracking cancel <order_id>`, and `uproc applications orders tracking send-reminder <order_id>`.
- Inspect email context for the draft with `uproc applications mail list [--page 1]`.

## Output

- Order status summary.
- Exception list.
- Draft communication if requested.
