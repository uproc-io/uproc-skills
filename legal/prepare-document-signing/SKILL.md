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

## Implementation via Uproc MCP

- Use `document-signing.requests.list` as the main signing queue source.
- Use `document-generator.documents.list` to inspect document context.
- Use `document-signing.send_reminder`, `document-signing.sync_status`, `document-signing.reopen_request`, and `document-signing.cancel_request` for the routine signing follow-up actions already exposed by MCP.
- Use `document-generator.mark_ready`, `document-generator.mark_review`, `document-generator.regenerate_document`, `document-generator.archive_document`, and `document-generator.restore_document` to move the draft through the internal preparation queue before signature.
- Use `document-archiving.folders.list` only if the worker needs archival context and that collection is exposed in the current environment.
- If the signing preparation depends on a contract record, use `contract-lifecycle.upload_contract_document` to attach the latest draft or annex before triggering the external signature workflow.
- If a new signature request must be injected from an external workflow, use `module.webhook` or `document-signing.requests.webhook` when the integration path supports it.

## Implementation via Uproc CLI

- Read the signing queue with `uproc applications signing list [--page 1]`.
- Signing follow-up with `uproc applications signing send-reminder <request_id>`, `uproc applications signing sync-status <request_id>`, `uproc applications signing reopen <request_id>`, and `uproc applications signing cancel <request_id>`.
- Move the draft through the internal preparation queue with `uproc applications document-ingest list [--page 1]`, `uproc applications document-ingest mark-ready <document_id>`, `uproc applications document-ingest mark-review <document_id>`, `uproc applications document-ingest regenerate <document_id>`, `uproc applications document-ingest archive <document_id>`, and `uproc applications document-ingest restore <document_id>`.
- Read archival context with `uproc applications module collection document-archiving folders [--page 1]`.
- Limits: `contract-lifecycle.upload_contract_document` and `document-signing.requests.webhook` are MCP-only; the CLI covers queue management verbs.

## Output

- Signing workflow summary.
- Pending request list.
- Readiness checklist.
