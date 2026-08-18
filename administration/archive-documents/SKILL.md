# Archive Documents

## Profile

Administrative staff.

## Goal

Manage the document archiving folders: review what has been archived, detect failed or unarchived documents, and upload new files into the archive flow.

## Modules

- `document-archiving`

## Backend capabilities

- Read KPIs and charts for the archiving overview.
- Read the `folders` collection.
- Upload files for archiving.
- Receive webhook payloads.

## Use this skill when

- You need a quick control of how many documents have been archived, processed, or failed.
- You want to review archive folders and decide what needs to be uploaded or re-processed.
- You need to submit a new document (or a webhook payload) into the archiving flow.

## What it should do

- Query the archiving KPIs and folder rows.
- Surface documents that failed or were not processed.
- Upload missing files or forward payloads for archiving.

## Implementation via Uproc MCP

- Read the overview with `module.kpis` on `document-archiving`.
- Read folder rows with `document-archiving.folders.list` (or `.get` / `.search` with the same aliases).
- Upload a new file with `document-archiving.folders.upload` (`file_name` + base64 `content`).
- Send a webhook payload with `document-archiving.folders.webhook` (`raw`, `text`, `message`, `reply_callback`).
- Limit: the archiving module exposes the single `folders` collection (read/upload/webhook); there are no dedicated archive action tools in MCP yet.

## Implementation via Uproc CLI

- KPIs: `uproc applications module overview document-archiving kpis`.
- Read rows: `uproc applications module document-archiving folders [--page 1 --sort-field key --sort-order asc --filter-field key --filter-value val]`.
- Upload: `uproc applications module upload document-archiving folders <file_path>`.
- Webhook: `uproc applications module webhook document-archiving folders <payload_json>`.
- Limit: the CLI can only read/upload/webhook this collection; there is no dedicated archiving command.

## Output

- Archive status summary.
- Failed or unarchived document list.
- Recommended upload or reroute actions.
