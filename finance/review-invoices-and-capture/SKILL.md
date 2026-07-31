# Review Invoices And Capture

## Profile

Finance and accounting staff.

## Goal

Compare received invoice capture with issued invoice records and identify gaps or inconsistencies.

## Modules

- `invoice-ingest`
- `sales-invoices`

## Backend capabilities

- Read KPIs.
- Read `emails`, `invoices`, `invoice_lines`, and `series`.
- Upload and webhook support.

## Use this skill when

- You need a quick control of incoming versus managed invoices.
- You want to detect missing records before reconciliation.

## What it should do

- Review incoming and issued invoice data.
- Surface mismatches in dates, totals, series, or basic identifiers.
- Point out what should be checked manually.

## Implementation via Bizzmod MCP

- Query incoming data with `invoice-ingest.invoices.list` and `invoice-ingest.emails.list` when needed.
- Query issued invoice context with:
  - `sales-invoices.invoices.list`
  - `sales-invoices.invoice_lines.list`
  - `sales-invoices.series.list`
- Use `sales-invoices.preview_invoice_pdf` before issuing or correcting a draft invoice.
- Use `sales-invoices.get_invoice_pdf` when the worker needs the final generated PDF for an existing invoice.
- Use `sales-invoices.issue_invoice` when the worker is ready to move a draft invoice into the issuing workflow.
- Use `sales-invoices.add_invoice_line`, `sales-invoices.update_invoice_line`, and `sales-invoices.delete_invoice_line` when the worker needs to fix invoice composition before issuing or correcting the document.
- Use `sales-invoices.rectify_invoice` when an issued invoice must be corrected.
- Use `sales-invoices.send_invoice` when the worker is ready to send the final invoice.
- Use `sales-invoices.export_to_erp` to send a specific issued invoice to the configured ERP (only works when `erp_sync_mode` is `full` or `push`; otherwise a warning is returned). `sales-invoices.configure_erp_sync` (set the mode) and `sales-invoices.run_erp_sync` (run the linked data-sync workflows now) cover the activation flow.
- Use `sales-invoices.get_verifactu_xml`, `sales-invoices.resubmit_verifactu`, and `sales-invoices.backfill_verifactu` to manage VeriFactu (Spain) registrations: download the AEAT SF v1.1 file, retry a registration, or register already-issued invoices into the chain.
- Use `module.kpis` for both modules if the worker asks for a quick control summary before drilling into rows.

## Output

- Comparison summary.
- Suspect invoice list.
- Recommended review actions.
