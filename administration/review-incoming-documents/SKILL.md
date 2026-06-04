# Review Incoming Documents

## Profile

Administrative staff.

## Goal

Review incoming business documents and identify what needs validation, correction, or routing.

## Modules

- `invoice-ingest`
- `order-ingest`
- `document-ingest`

## Backend capabilities

- Read KPIs.
- Read collections such as `emails`, `invoices`, `orders`, `documents`, and `uploads`.
- Upload files and receive webhooks.

## Use this skill when

- You want to review what entered today.
- You need to detect missing or malformed extracted records.
- You need a triage summary before manual processing.

## What it should do

- Check the relevant incoming collections.
- Sort recent items first when the user asks for the latest records.
- Group records by type and status.
- Highlight missing fields, suspicious parsing, or records that require manual review.

## Implementation via Bizzmod MCP

- Start with `module.capabilities` for `invoice-ingest`, `order-ingest`, and `document-ingest` if the environment may differ by customer.
- Read recent records with `module.data` or the semantic shortcuts:
  - `invoice-ingest.emails.list`
  - `invoice-ingest.invoices.list`
  - `order-ingest.orders.list`
  - `order-ingest.emails.list`
  - `document-ingest.documents.list`
  - `document-ingest.uploads.list`
  - `document-ingest.emails.list`
- Use `sort_field=created_at` and `sort_order=desc` when the user asks for latest activity.
- If the worker needs to inject new files, use `module.upload` or the matching `*.upload` shortcut.

## Output

- Short summary.
- List of records needing attention.
- Recommended next step per record.
