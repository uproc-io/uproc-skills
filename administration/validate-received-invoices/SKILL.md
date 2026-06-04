# Validate Received Invoices

## Profile

Administrative staff handling supplier invoices.

## Goal

Review captured invoices and detect extraction problems, duplicates, or missing data before downstream processing.

## Modules

- `invoice-ingest`
- `document-classifier`
- `document-numbering`
- `document-archiving`

## Backend capabilities

- Direct read access is strongest on `invoice-ingest`.
- Document support modules are mainly supporting workflow modules and may expose limited collection detail.
- Upload and webhook support are available across modules.

## Use this skill when

- You need to validate newly received invoices.
- You suspect OCR or extraction issues.
- You need a manual review queue.

## What it should do

- Review recent invoices.
- Flag invoices missing supplier, date, amount, or identifier fields.
- Point out likely duplicates or ambiguous records.
- Recommend archive, correction, or escalation.

## Implementation via Bizzmod MCP

- Use `invoice-ingest.invoices.list` as the main source for captured invoice review.
- Optionally inspect `invoice-ingest.emails.list` for intake context.
- For document support modules, first call `module.collections` or `module.capabilities` because their exposed collections are narrower and may differ from internal workflow expectations.
- Use upload shortcuts only when the worker is adding new supporting files, not for validation itself.

## Output

- Validation summary.
- Problematic invoices.
- Recommended action per invoice.
