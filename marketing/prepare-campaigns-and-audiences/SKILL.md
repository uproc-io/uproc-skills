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

## Implementation via Bizzmod MCP

- Use:
  - `campaign-automation.campaigns.list`
  - `campaign-automation.audiences.list`
  - `lead-prospecting.opportunities.list`
  - `lead-prospecting.prospects.list`
- Preview enrollment with `campaign-automation.preview_audience` before activating changes.
- Persist the audience definition with `campaign-automation.add_audience`.
- Use `campaign-automation.import_audience_csv` when the audience source is an external CSV file.
- Use `campaign-automation.record_execution_event` when an external delivery system must push campaign execution events back into Bizzmod.
- Use `campaign-automation.get_execution_stats` when the worker needs aggregated channel results for a campaign.
- Use `campaign-automation.pause_campaign` when a campaign must be stopped without deleting its setup.
- Use `campaign-automation.activate_campaign` when the reviewed campaign is ready to resume.
- Use `module.kpis` for `campaign-automation` when the worker asks for a quick campaign summary.

## Output

- Campaign readiness summary.
- Audience review notes.
- Prioritized recommendations.
