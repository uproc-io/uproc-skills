# Revisar Facturas Y Captura

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

## Output

- Comparison summary.
- Suspect invoice list.
- Recommended review actions.
