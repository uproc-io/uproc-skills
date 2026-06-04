# Revisar Documentos Entrantes

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

## Output

- Short summary.
- List of records needing attention.
- Recommended next step per record.
