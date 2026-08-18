# Unify Documents

## Profile

Administrative staff.

## Goal

Monitor the document unification pipeline: review how documents are being matched and deduplicated, detect failures, and submit new files for unification.

## Modules

- `document-unification`

## Backend capabilities

- Read KPIs and charts for the unification overview.
- Read the `folders` collection.
- Upload files for unification.
- Receive webhook payloads.

## Use this skill when

- You need a quick control of how many documents have been unified, processed, or failed.
- You want to review unification folders and decide what to re-upload or reroute.
- You need to submit a new document (or a webhook payload) into the unification flow.

## What it should do

- Query the unification KPIs and folder rows.
- Surface documents that failed or were not processed.
- Upload missing files or forward payloads for unification.

## Implementation via Uproc MCP

- Read the overview with `module.kpis` on `document-unification`.
- Read folder rows with `document-unification.folders.list` (or `.get` / `.search` with the same aliases).
- Upload a new file with `document-unification.folders.upload` (`file_name` + base64 `content`).
- Send a webhook payload with `document-unification.folders.webhook` (`raw`, `text`, `message`, `reply_callback`).
- Limit: the unification module exposes the single `folders` collection (read/upload/webhook); there are no dedicated unification action tools in MCP yet.

## Implementation via Uproc CLI

- KPIs: `uproc applications module overview document-unification kpis`.
- Read rows: `uproc applications module document-unification folders [--page 1 --sort-field key --sort-order asc --filter-field key --filter-value val]`.
- Upload: `uproc applications module upload document-unification folders <file_path>`.
- Webhook: `uproc applications module webhook document-unification folders <payload_json>`.
- Limit: the CLI can only read/upload/webhook this collection; there is no dedicated unification command.

## Output

- Unification summary.
- Failed or unprocessed document list.
- Recommended upload or reroute actions.
