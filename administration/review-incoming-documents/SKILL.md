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
- Read collections such as `emails`, `invoices`, `orders`, `documents`, `uploads`, and `templates`.
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
- Use the document-ingest `validation` summary (`errors`, `warnings`, `total`) and the
  structured `notifications` to prioritise documents that need manual review.
- For cancelled documents, read `document_type` and the notification's
  `detection_reason` to explain why the type was rejected.

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
  - `document-ingest.templates` via `module.data` (read the customer's selected extraction templates)
- Use `sort_field=created_at` and `sort_order=desc` when the user asks for latest activity.
- If the worker needs to inject new files, use `module.upload` or the matching `*.upload` shortcut.
- Template management: read the global catalog with `module.data` on `document-ingest` / `templates` (system rows have no `customer_id`); a customer authorizes a type by adding the catalog template. Do not edit system templates from the worker; system rows are read-only. Customer templates expose `prompt_exceptions`, which are extraction-only instructions appended to the type-specific prompt.

### Document numbering

- Review the document numbering configuration with `module.data` on `document-numbering` / `folders` (or `module.kpis` for the overview).
- Upload new numbering definitions with `module.upload` on `document-numbering` / `folders`.
- Limit: numbering is configuration data exposed as the single `folders` collection (read/upload/webhook); there are no dedicated numbering action tools in MCP yet.

## Implementation via Uproc CLI

- Read incoming records with the generic CLI reader (there are no dedicated commands for `invoice-ingest`, `order-ingest`, `document-ingest`, or `document-numbering`):
  - `uproc applications invoice-ingest list-invoices [--page 1 --sort-field created_at --sort-order desc]`
  - `uproc applications order-track list [--page 1 --sort-field created_at --sort-order desc]`
  - `uproc applications module collection document-ingest documents [--page 1 --sort-field created_at --sort-order desc]`
  - `uproc applications module collection document-ingest templates [--page 1]`
  - `uproc applications module collection document-numbering folders [--page 1]`
- KPIs: `uproc applications module overview invoice-ingest kpis` (and the same for `order-ingest`, `document-ingest`, `document-numbering`).
- Upload files: `uproc applications module upload <module_slug> <collection> <file_path>`.
- Templates: the CLI has no dedicated template management for document-ingest; use the app.
- Webhook: `uproc applications module webhook <module_slug> <collection> <payload_json>`.
- Reprocessing a document is an in-app session action (`POST /api/v1/modules/document-ingest/actions/reprocess`); it is not exposed as an MCP/CLI tool yet.

## Output

- Short summary.
- List of records needing attention.
- Recommended next step per record.
