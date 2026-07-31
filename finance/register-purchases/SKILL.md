# Register Purchases

## Profile

Finance and accounting staff.

## Goal

Register supplier invoices (purchases), assign received invoices from invoice-ingest, and track the purchase lifecycle until payment.

## Modules

- `purchase-invoices`
- `invoice-ingest`

## Backend capabilities

- Create purchase invoices (alta directa) with supplier, invoice number, dates, currency, base / IVA / total, notes and PDF.
- Assign a received invoice from `invoice-ingest` into a purchase (`assign_from_ingest`), cloning the data before saving.
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

## Implementation via Bizzmod MCP

- List/create purchases with:
  - `module.data` on `purchase-invoices` / `purchase_invoices`
  - `module.create` on `purchase-invoices` / `purchase_invoices`
- Add line items with `module.create` on `purchase-invoices` / `purchase_invoice_lines`.
- Record payments with `module.create` on `purchase-invoices` / `purchase_invoice_payments`.
- Advance the lifecycle with `purchase-invoices.change_status` (arguments `item_id`, `status` `validated` or `paid`, optional `reason`).
- Assign a received invoice to a purchase with `purchase-invoices.assign_from_ingest` (argument `invoice_id` = the received invoice id).
- Find received invoices to assign with `module.data` on `invoice-ingest` / `invoices`.
- Query the purchase detail (lines, payments, events, PDFs) with `module.data` on `purchase-invoices` / `purchase_invoices` (item id).
- Manage VeriFactu registrations with `purchase-invoices.resubmit_verifactu` and `purchase-invoices.backfill_verifactu`.
- Send a purchase to the configured ERP with `purchase-invoices.export_to_erp` (requires `erp_sync_mode` `full` or `push`); `purchase-invoices.configure_erp_sync` sets the mode and `purchase-invoices.run_erp_sync` runs the linked data-sync workflows.

## Output

- Registered purchase record with its lifecycle status and payment history.
