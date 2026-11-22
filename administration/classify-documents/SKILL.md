# Classify Documents

## Profile

Administrative staff.

## Goal

Keep the document classification pipeline healthy: review what has been classified, route or fix unprocessed documents, and upload new files for classification.

## Modules

- `treatments.classify` · suite `documents`

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

- Read the overview with `module.kpis` on `treatments.classify`.
- Read folder rows with `treatments.classify.folders.list` (or `.get` / `.search` with the same aliases).
- Upload a new file with `treatments.classify.folders.upload` (`file_name` + base64 `content`).
- Send a webhook payload with `treatments.classify.folders.webhook` (`raw`, `text`, `message`, `reply_callback`).
- Process a folder with `treatments.classify.start_upload_batch` (`process_id`) and retry a failed batch with `treatments.classify.retry_upload_batch` (`folder_id`).

## Implementation via Uproc CLI

- KPIs: `uproc applications module overview document-classifier kpis`.
- Read rows: `uproc applications module collection document-classifier folders [--page 1 --sort-field key --sort-order asc --filter-field key --filter-value val]`.
- Upload: `uproc applications module upload document-classifier folders <file_path>`.
- Webhook: `uproc applications module webhook document-classifier folders <payload_json>`.
- Process a folder with `uproc applications treatments classify process <process_id>` and retry it with `uproc applications treatments classify retry <folder_id>`.

## Output

- Classification summary.
- Failed or unprocessed document list.
- Recommended re-upload or reroute actions.
