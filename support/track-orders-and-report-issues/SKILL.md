# Track Orders And Report Issues

## Profile

Support and operations staff.

## Goal

Review order status and prepare customer communication when delays or issues appear.

## Modules

- `order-track`
- `email-assistant`

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

## Implementation via Bizzmod MCP

- Use `order-track.orders.list` as the main order-status source.
- Use `order-track.emails.list` if intake or communication context matters.
- Use `order-track.mark_received` when the worker confirms delivery.
- Use `order-track.cancel_order` when the worker confirms the order should be cancelled.
- Use `order-track.send_reminder` when the worker needs to push order follow-up before customer communication.
- Use `email-assistant.emails.list` for drafting context if a previous customer conversation exists.

## Output

- Order status summary.
- Exception list.
- Draft communication if requested.
