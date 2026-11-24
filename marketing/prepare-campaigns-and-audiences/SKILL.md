---
name: "prepare-campaigns-and-audiences"
description: "Review campaign and audience data before activation or optimization."
---

# Prepare Campaigns And Audiences

## Profile

Marketing and growth teams.

## Goal

Review campaign and audience data before activation or optimization.

## Modules

- `campaigns` · suite `sales`
- `leads.capture` · suite `sales`

## Backend capabilities

- Read KPIs.
- Read `campaigns`, `audiences`, `opportunities`, `prospects`, and `executions`.
- Upload and webhook support.

## Use this skill when

- You need a campaign readiness review.
- You want to align audiences with available opportunities.

## What it should do

- Review available campaigns and audiences.
- Highlight gaps between targeting and available prospects.
- Recommend what to activate or refine.

## Implementation via Uproc MCP

- Use:
  - `campaigns.campaigns.list`
  - `campaigns.audiences.list`
  - `leads.capture.opportunities.list`
  - `leads.capture.prospects.list`
- Preview enrollment with `campaigns.preview_audience` before activating changes.
- Persist the audience definition with `campaigns.add_audience`.
- Use `campaigns.import_audience_csv` when the audience source is an external CSV file.
- To build an audience from a Data Management table, create the audience with the generic create contract (`create` on `campaigns` / `audiences`) using `source: "data_management"`, `source_entity_id: <entity id>` and, optionally, `source_column_map` (`{email, mobile, phone, first_name, last_name} -> column key`). Columns are auto-detected when the map is omitted; set `auto_refresh_from_entity: true` so members re-sync from the table on read. The table stays the single source of truth (it can be produced by Data Process or a file upload).
- Use `campaigns.record_execution_event` when an external delivery system must push campaign execution events back into Uproc.
- Use `campaigns.get_execution_stats` when the worker needs aggregated channel results for a campaign.
- Use `campaigns.pause_campaign` when a campaign must be stopped without deleting its setup.
- Use `campaigns.activate_campaign` when the reviewed campaign is ready to resume.
- Use `campaigns.sync_audience` to sync a campaign audience to the configured external platforms as subscribers.
- Use `campaigns.launch_platforms` to create and launch the campaign on its configured external platforms.
- For the campaign planning flow, use `campaigns.analyze_plan` to get an AI-generated campaign plan (campaigns, audiences, channels, merge tags), `campaigns.get_plan` / `campaigns.list_plans` to review it, and `campaigns.execute_plan` to create the proposed campaigns, audiences, and channels. `campaigns.regenerate_plan` rebuilds an existing plan with the current AI prompt.
- Use `module.kpis` for `campaigns` when the worker asks for a quick campaign summary.

## Implementation via Uproc CLI

- Read campaigns and audiences with `uproc applications campaigns list [--page 1]` and `uproc applications campaigns list-audiences [--page 1]`.
- Preview enrollment with `uproc applications campaigns preview-audience <campaign_id> [limit]`.
- Persist the audience definition with `uproc applications campaigns add-audience <campaign_id> [mode]`.
- Act on campaigns with `uproc applications campaigns pause <campaign_id>`, `uproc applications campaigns activate <campaign_id>`, `uproc applications campaigns sync-audience <campaign_id> <audience_id>`, and `uproc applications campaigns launch-platforms <campaign_id>`.
- Read prospecting context with `uproc applications leads capture list-opportunities [--page 1]` and `uproc applications leads capture list-prospects [--page 1]`.
- Schedule recurring runs: `uproc applications campaigns schedule-add <campaign_id> --recurrence '{"freq":"weekly","weekday":"mon","hour":8}' [--name weekly --stop-after 5]`, then `schedule-list`, `schedule-update <schedule_id> [--active true]`, `schedule-delete <schedule_id>`.
- Review suppressions and provider sync: `suppressions [--channel email]`, `suppression-add <channel> <recipient> --reason manual`, `sync-push <campaign_id>` (creates provider drafts), `sync-pull <campaign_id>`, `sync-status <campaign_id>`, and `sms-report <campaign_id>`.
- Generate channel content with `module.action` (`campaigns` `content_generate`: `campaign_id`, `brief`, optional `tone`/`channels`), review it with `content_get` and approve it with `content_approve` (`channel`, `approved`). AI content must be approved by a human before dispatch.
- Inspect audience sources with `module.action` (`campaigns` `data_sources`) and preview a table mapping with `preview_audience` (`entity_id`, `column_map`).
- Provider sync and reports: `sync_push`, `sync_pull`, `sync_status` and `sms_report` (+ `sms_report_csv`) per campaign.
- CLI equivalent: `uproc applications module action campaign-automation <action> '<json>'` for all of the above; the dedicated verbs cover lifecycle, schedules, suppressions and sync.

## Output

- Campaign readiness summary.
- Audience review notes.
- Prioritized recommendations.