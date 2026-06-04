# Prepare Document Signing

## Profile

Legal and administrative staff.

## Goal

Prepare a signing workflow and review pending signature requests.

## Modules

- `document-signing`
- `document-generator`
- `document-archiving`

## Backend capabilities

- Read KPIs.
- Read `requests` in `document-signing` and `documents` in `document-generator`.
- Upload and webhook support.

## Use this skill when

- A document must be prepared for signature.
- You need to review pending signing requests.

## What it should do

- Review the current signing request status.
- Confirm whether the document is ready.
- Highlight missing business information before signature.

## Implementation via Bizzmod MCP

- Use `document-signing.requests.list` as the main signing queue source.
- Use `document-generator.documents.list` to inspect document context.
- Use `document-signing.send_reminder`, `document-signing.sync_status`, `document-signing.reopen_request`, and `document-signing.cancel_request` for the routine signing follow-up actions already exposed by MCP.
- Use `document-generator.mark_ready`, `document-generator.mark_review`, `document-generator.regenerate_document`, `document-generator.archive_document`, and `document-generator.restore_document` to move the draft through the internal preparation queue before signature.
- Use `document-archiving.folders.list` only if the worker needs archival context and that collection is exposed in the current environment.
- If the signing preparation depends on a contract record, use `contract-lifecycle.upload_contract_document` to attach the latest draft or annex before triggering the external signature workflow.
- If a new signature request must be injected from an external workflow, use `module.webhook` or `document-signing.requests.webhook` when the integration path supports it.

## Output

- Signing workflow summary.
- Pending request list.
- Readiness checklist.
