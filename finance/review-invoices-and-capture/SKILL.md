# Review Invoices And Capture

## Profile

Finance and accounting staff.

## Goal

Compare received invoice capture with issued invoice records and identify gaps or inconsistencies.

## Modules

- `invoice-ingest`
- `invoice-generator`

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
  - `invoice-generator.invoices.list`
  - `invoice-generator.invoice_lines.list`
  - `invoice-generator.series.list`
- Use `invoice-generator.preview_invoice_pdf` before issuing or correcting a draft invoice.
- Use `invoice-generator.get_invoice_pdf` when the worker needs the final generated PDF for an existing invoice.
- Use `invoice-generator.issue_invoice` when the worker is ready to move a draft invoice into the issuing workflow.
- Use `invoice-generator.add_invoice_line`, `invoice-generator.update_invoice_line`, and `invoice-generator.delete_invoice_line` when the worker needs to fix invoice composition before issuing or correcting the document.
- Use `invoice-generator.rectify_invoice` when an issued invoice must be corrected.
- Use `invoice-generator.send_invoice` when the worker is ready to send the final invoice.
- Use `module.kpis` for both modules if the worker asks for a quick control summary before drilling into rows.

## Output

- Comparison summary.
- Suspect invoice list.
- Recommended review actions.
