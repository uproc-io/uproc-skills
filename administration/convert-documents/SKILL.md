# Convert Documents

## Profile

Administrative staff.

## Goal

Monitor the document conversion pipeline: review processed and failed conversions, and submit new files for conversion.

## Modules

- `treatments.convert` · suite `documents`

## Backend capabilities

- Read KPIs and charts for the conversion overview.
- Read the `folders` collection.
- Upload files for conversion.
- Receive webhook payloads.

## Use this skill when

- You need a quick control of how many documents have been converted, processed, or failed.
- You want to review conversion folders and decide what to re-upload or reroute.
- You need to submit a new document (or a webhook payload) into the conversion flow.

## What it should do

- Query the conversion KPIs and folder rows.
- Surface documents that failed or were not processed.
- Upload missing files or forward payloads for conversion.

## Implementation via Uproc MCP

- Read the overview with `module.kpis` on `treatments.convert`.
- Read folder rows with `treatments.convert.folders.list` (or `.get` / `.search` with the same aliases).
- Upload a new file with `treatments.convert.folders.upload` (`file_name` + base64 `content`).
- Send a webhook payload with `treatments.convert.folders.webhook` (`raw`, `text`, `message`, `reply_callback`).
- Limit: the conversion module exposes the single `folders` collection (read/upload/webhook); there are no dedicated conversion action tools in MCP yet.

## Implementation via Uproc CLI

- KPIs: `uproc applications module overview document-conversion kpis`.
- Read rows: `uproc applications module collection document-conversion folders [--page 1 --sort-field key --sort-order asc --filter-field key --filter-value val]`.
- Upload: `uproc applications module upload document-conversion folders <file_path>`.
- Webhook: `uproc applications module webhook document-conversion folders <payload_json>`.
- Upload files with `uproc applications treatments convert upload <process_id> <files...>`, process the folder with `uproc applications treatments convert process <process_id>` and retry it with `uproc applications treatments convert retry <folder_id>`.

## Output

- Conversion summary.
- Failed or unprocessed document list.
- Recommended upload or reroute actions.
