# Register Purchases

## Profile

Finance and accounting staff.

## Goal

Register supplier invoices and PDF/JPG tiquets (purchases), assign received invoices from ingestion, and track the purchase lifecycle until payment.

## Modules

- `purchase-invoices`

## Backend capabilities

- Create purchase invoices (alta directa) with supplier, invoice number, dates, currency, base / IVA / total, notes and PDF.
- Assign a received invoice (from email/upload, including tiquets) into a purchase (`assign_from_ingest`), cloning the data before saving.
- Upload PDF/JPG/PNG tiquets: receipts are parsed (OCR + AI) and considered complete with just the total amount (`document_type=receipt`), then assigned as purchases; batch-assign with `assign_multiple_from_ingest` (`parsed_invoice_ids`).
- Manage line items (`purchase_invoice_lines`) with automatic totals recalculation.
- Manage payments (`purchase_invoice_payments`).
- Move statuses `received → validated → paid` (a paid purchase is immutable).
- Resolve supplier display fields from a `proveedores` data-management entity.

## Use this skill when

- A supplier invoice arrives and must be recorded as a purchase.
- A received invoice (from email/API) must be converted into a purchase.
- You need to validate, mark as paid, or track the lifecycle of a purchase.

## What it should do

- Register the purchase with the supplier identity and invoice data.
- Assign received invoices from `invoice-ingest` to a purchase when they match.
- Validate data and advance the status when appropriate.
- Record payments against the purchase.

## Implementation via Uproc MCP

- List/create purchases with:
  - `module.data` on `purchase-invoices` / `purchase_invoices`
  - `module.create` on `purchase-invoices` / `purchase_invoices`
- Add line items with `module.create` on `purchase-invoices` / `purchase_invoice_lines`.
- Record payments with `module.create` on `purchase-invoices` / `purchase_invoice_payments`.
- For recurring supplier bills (e.g. rent, subscriptions), create a template with `module.create` on `purchase-invoices` / `recurring_invoices` (or `purchase-invoices.create_recurring_from_invoice` from an existing purchase) and trigger the next draft with `purchase-invoices.generate_recurring_invoice`. Generated drafts arrive as `received`.
- Advance the lifecycle with `purchase-invoices.change_status` (arguments `item_id`, `status` `validated` or `paid`, optional `reason`).
- Assign a received invoice to a purchase with `purchase-invoices.assign_from_ingest` (argument `invoice_id` = the received invoice id).
- Assign several received invoices (e.g. a batch of tiquets) at once with `purchase-invoices.assign_multiple_from_ingest` (argument `parsed_invoice_ids`).
- Find received invoices (including parsed tiquets) to assign with `module.data` on `purchase-invoices` / `invoices`.
- Query the purchase detail (lines, payments, events, PDFs) with `module.data` on `purchase-invoices` / `purchase_invoices` (item id).
- Send a purchase to the configured ERP with `purchase-invoices.export_to_erp` (requires `erp_sync_mode` `full` or `push`); `purchase-invoices.configure_erp_sync` sets the mode and `purchase-invoices.run_erp_sync` runs the linked data-sync workflows.

## Implementation via Uproc CLI

- Read purchases with `uproc applications purchase-invoices list [--page 1]`, `uproc applications purchase-invoices list-lines [--page 1]`, and `uproc applications purchase-invoices list-payments [--page 1]`.
- Advance the lifecycle with `uproc applications purchase-invoices validate <id> [reason]` and `uproc applications purchase-invoices pay <id> [reason]`.
- Assign a received invoice with `uproc applications purchase-invoices assign-from-ingest <invoice_id> [payload_json]`.
- Find received invoices (including tiquets) with the generic reader `uproc applications invoice-ingest list-invoices [--page 1]`.
- Limit: the CLI has no `module create`, so registering a new purchase, adding lines, recording payments, or batch-assigning tiquets requires the MCP `module.create` / action tools (or the web UI). ERP sync commands are MCP-only (`configure_erp_sync` / `run_erp_sync`).

## Output

- Registered purchase record with its lifecycle status and payment history.
