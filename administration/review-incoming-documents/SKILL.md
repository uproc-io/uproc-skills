# Review Incoming Documents

## Profile

Administrative staff.

## Goal

Review incoming business documents and identify what needs validation, correction, or routing.

## Modules

- `invoice-ingest`
- `order-ingest`
- `document-ingest`
- `document-numbering`

## Backend capabilities

- Read KPIs.
- Read collections such as `emails`, `invoices`, `orders`, `documents`, and `uploads`.
- Upload files and receive webhooks.
- Review the document numbering configuration (`document-numbering.folders`).

## Use this skill when

- You want to review what entered today.
- You need to detect missing or malformed extracted records.
- You need a triage summary before manual processing.

## What it should do

- Check the relevant incoming collections.
- Sort recent items first when the user asks for the latest records.
- Group records by type and status.
- Highlight missing fields, suspicious parsing, or records that require manual review.

## Implementation via Uproc MCP

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

### Document numbering

- Review the document numbering configuration with `module.data` on `document-numbering` / `folders` (or `module.kpis` for the overview).
- Upload new numbering definitions with `module.upload` on `document-numbering` / `folders`.
- Limit: numbering is configuration data exposed as the single `folders` collection (read/upload/webhook); there are no dedicated numbering action tools in MCP yet.

## Implementation via Uproc CLI

- Read incoming records with the generic CLI reader (there are no dedicated commands for `invoice-ingest`, `order-ingest`, `document-ingest`, or `document-numbering`):
  - `uproc applications module invoice-ingest invoices [--page 1 --sort-field created_at --sort-order desc]`
  - `uproc applications module order-ingest orders [--page 1 --sort-field created_at --sort-order desc]`
  - `uproc applications module document-ingest documents [--page 1 --sort-field created_at --sort-order desc]`
  - `uproc applications module document-numbering folders [--page 1]`
- KPIs: `uproc applications module overview invoice-ingest kpis` (and the same for `order-ingest`, `document-ingest`, `document-numbering`).
- Upload files: `uproc applications module upload <module_slug> <collection> <file_path>`.
- Webhook: `uproc applications module webhook <module_slug> <collection> <payload_json>`.

## Output

- Short summary.
- List of records needing attention.
- Recommended next step per record.
