# Classify Documents

## Profile

Administrative staff.

## Goal

Keep the document classification pipeline healthy: review what has been classified, route or fix unprocessed documents, and upload new files for classification.

## Modules

- `document-classifier`

## Backend capabilities

- Read KPIs and charts for the classifier overview.
- Read the `folders` collection.
- Upload files for processing.
- Receive webhook payloads.

## Use this skill when

- You need a quick control of how many documents have been classified, processed, or failed.
- You want to review the documents sitting in the classifier folders and decide what to reroute or re-upload.
- You need to submit a new document (or a webhook payload) into the classification flow.

## What it should do

- Query the classifier KPIs and folder rows.
- Surface documents that failed or were not processed.
- Upload missing files or forward payloads for reclassification.

## Implementation via Uproc MCP

- Read the overview with `module.kpis` on `document-classifier`.
- Read folder rows with `document-classifier.folders.list` (or `.get` / `.search` with the same aliases).
- Upload a new file with `document-classifier.folders.upload` (`file_name` + base64 `content`).
- Send a webhook payload with `document-classifier.folders.webhook` (`raw`, `text`, `message`, `reply_callback`).
- Limit: the classifier exposes the single `folders` collection (read/upload/webhook); there are no dedicated classification action tools in MCP yet.

## Implementation via Uproc CLI

- KPIs: `uproc applications module overview document-classifier kpis`.
- Read rows: `uproc applications module collection document-classifier folders [--page 1 --sort-field key --sort-order asc --filter-field key --filter-value val]`.
- Upload: `uproc applications module upload document-classifier folders <file_path>`.
- Webhook: `uproc applications module webhook document-classifier folders <payload_json>`.
- Limit: the CLI can only read/upload/webhook this collection; there is no dedicated classifier command.

## Output

- Classification summary.
- Failed or unprocessed document list.
- Recommended re-upload or reroute actions.
