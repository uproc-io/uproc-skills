# Prepare Campaigns And Audiences

## Profile

Marketing and growth teams.

## Goal

Review campaign and audience data before activation or optimization.

## Modules

- `campaign-automation`
- `lead-prospecting`

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
  - `campaign-automation.campaigns.list`
  - `campaign-automation.audiences.list`
  - `lead-prospecting.opportunities.list`
  - `lead-prospecting.prospects.list`
- Preview enrollment with `campaign-automation.preview_audience` before activating changes.
- Persist the audience definition with `campaign-automation.add_audience`.
- Use `campaign-automation.import_audience_csv` when the audience source is an external CSV file.
- Use `campaign-automation.record_execution_event` when an external delivery system must push campaign execution events back into Uproc.
- Use `campaign-automation.get_execution_stats` when the worker needs aggregated channel results for a campaign.
- Use `campaign-automation.pause_campaign` when a campaign must be stopped without deleting its setup.
- Use `campaign-automation.activate_campaign` when the reviewed campaign is ready to resume.
- Use `campaign-automation.sync_audience` to sync a campaign audience to the configured external platforms as subscribers.
- Use `campaign-automation.launch_platforms` to create and launch the campaign on its configured external platforms.
- For the campaign planning flow, use `campaign-automation.analyze_plan` to get an AI-generated campaign plan (campaigns, audiences, channels, merge tags), `campaign-automation.get_plan` / `campaign-automation.list_plans` to review it, and `campaign-automation.execute_plan` to create the proposed campaigns, audiences, and channels. `campaign-automation.regenerate_plan` rebuilds an existing plan with the current AI prompt.
- Use `module.kpis` for `campaign-automation` when the worker asks for a quick campaign summary.

## Implementation via Uproc CLI

- Read campaigns and audiences with `uproc applications campaign-automation list [--page 1]` and `uproc applications campaign-automation list-audiences [--page 1]`.
- Preview enrollment with `uproc applications campaign-automation preview-audience <campaign_id> [limit]`.
- Persist the audience definition with `uproc applications campaign-automation add-audience <campaign_id> [mode]`.
- Act on campaigns with `uproc applications campaign-automation pause <campaign_id>`, `uproc applications campaign-automation activate <campaign_id>`, `uproc applications campaign-automation sync-audience <campaign_id> <audience_id>`, and `uproc applications campaign-automation launch-platforms <campaign_id>`.
- Read prospecting context with `uproc applications lead-prospecting list-opportunities [--page 1]` and `uproc applications lead-prospecting list-prospects [--page 1]`.
- Limit: the campaign AI plan flow (`analyze_plan`/`execute_plan`) and `import_audience_csv` / `record_execution_event` are MCP-only; the CLI covers campaign lifecycle verbs.

## Output

- Campaign readiness summary.
- Audience review notes.
- Prioritized recommendations.
