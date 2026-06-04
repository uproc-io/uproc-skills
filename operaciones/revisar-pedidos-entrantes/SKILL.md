# Revisar Pedidos Entrantes

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

## Output

- Order intake summary.
- Exception list.
- Suggested next action per issue.
