---
name: "review-invoices-and-capture"
description: "Compare received invoice capture with issued invoice records and identify gaps or inconsistencies."
---

# Review Invoices And Capture

## Profile

Finance and accounting staff.

## Goal

Compare received invoice capture with issued invoice records and identify gaps or inconsistencies.

## Modules

- `invoice-ingest`
- `sales` · suite `finance`

## Backend capabilities

- Read KPIs.
- Read `emails`, `invoices`, `invoice_lines`, `series`, and `recurring_invoices`.
- Upload and webhook support.

## Use this skill when

- You need a quick control of incoming versus managed invoices.
- You want to detect missing records before reconciliation.

## What it should do

- Review incoming and issued invoice data.
- Surface mismatches in dates, totals, series, or basic identifiers.
- Point out what should be checked manually.

## Implementation via Uproc MCP

- Query incoming data with `invoice-ingest.invoices.list` and `invoice-ingest.emails.list` when needed.
- Query issued invoice context with:
  - `sales.invoices.list`
  - `sales.invoice_lines.list`
  - `sales.series.list`
  - `sales.recurring_invoices.list`
- Use `sales.preview_invoice_pdf` before issuing or correcting a draft invoice.
- Use `sales.get_invoice_pdf` when the worker needs the final generated PDF for an existing invoice.
- Use `sales.issue_invoice` when the worker is ready to move a draft invoice into the issuing workflow.
- Use `sales.add_invoice_line`, `sales.update_invoice_line`, and `sales.delete_invoice_line` when the worker needs to fix invoice composition before issuing or correcting the document.
- Use `sales.rectify_invoice` when an issued invoice must be corrected; use `sales.cancel_invoice` to cancel an issued/rectified invoice (creates the F2 cancellation rectificative and the original becomes immutable).
- For recurring billing, use `sales.recurring_invoices.create` (or `sales.create_recurring_from_invoice` to turn an existing invoice into a template) and `sales.generate_recurring_invoice` to create the next draft now. Generated drafts stay in `draft` status for review unless `auto_issue` is enabled.
- Use `sales.send_invoice` when the worker is ready to send the final invoice.
- Use `sales.export_to_erp` to send a specific issued invoice to the configured ERP (only works when `erp_sync_mode` is `full` or `push`; otherwise a warning is returned). `sales.configure_erp_sync` (set the mode) and `sales.run_erp_sync` (run the linked data-sync workflows now) cover the activation flow.
- Use `sales.run_verifactu` to send pending VeriFactu registrations to the AEAT now (enabling `verifactu_enabled` creates the scheduled `VeriFactu AEAT` data-sync workflow).
- Use `sales.get_verifactu_xml`, `sales.resubmit_verifactu`, and `sales.backfill_verifactu` to manage VeriFactu (Spain) registrations: download the AEAT SF v1.1 file, retry a registration, or register already-issued invoices into the chain.
- Use `module.kpis` for both modules if the worker asks for a quick control summary before drilling into rows.

## Implementation via Uproc CLI

- Read incoming data with the generic reader (invoice-ingest has no dedicated CLI verbs): `uproc applications invoice-ingest list-invoices [--page 1]` and `uproc applications invoice-ingest list-emails [--page 1]`.
- Read issued invoice context with `uproc applications purchases list [--page 1]`, and the generic readers `uproc applications module collection sales-invoices series [--page 1]` / `uproc applications module collection sales-invoices recurring_invoices [--page 1]`.
- Fix invoice composition with `uproc applications purchases add <invoice_id> <concept> [quantity] [unit_price] [tax_rate] [sort_order]`, `uproc applications purchases update <invoice_id> <line_id> [...]`, and `uproc applications purchases delete <invoice_id> <line_id>`.
- Move the invoice forward with `uproc applications sales issue <invoice_id>`, `uproc applications sales send <invoice_id> [email] [subject] [message]`, `uproc applications sales rectify <invoice_id> [reason]`, and `uproc applications sales get-pdf <invoice_id>`.
- Manage VeriFactu with `uproc applications sales verifactu resubmit <invoice_id>`, `uproc applications sales verifactu backfill`, and `uproc applications sales verifactu xml <invoice_id>`.
- KPIs: `uproc applications module overview invoice-ingest kpis` and `uproc applications module overview sales-invoices kpis`.
- Limits: `preview_invoice_pdf`, `cancel_invoice`, recurring creation/generation, and the ERP sync verbs (`export_to_erp`, `configure_erp_sync`, `run_erp_sync`, `run_verifactu`) have no CLI command and are MCP-only (or web UI).

## Output

- Comparison summary.
- Suspect invoice list.
- Recommended review actions.