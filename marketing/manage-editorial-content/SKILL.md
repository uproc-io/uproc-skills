# Manage Editorial Content

## Profile

Marketing and content teams.

## Goal

Review editorial work queues and focus on the highest-value content items.

## Modules

- `editorial-engine`

## Backend capabilities

- Read KPIs.
- Read `projects`, `opportunities`, `articles`, and `combined`.
- Trigger proposal, draft, publish, schedule, and discard actions for editorial opportunities.
- Upload and webhook support.

## Use this skill when

- You need an editorial prioritization view.
- You want a concise content pipeline summary.

## What it should do

- Review editorial projects and opportunities.
- Surface articles needing attention.
- Trigger the next editorial workflow step when an opportunity is ready.
- Suggest a priority order for work.

## Implementation via Uproc MCP

- Use:
  - `editorial-engine.projects.list`
  - `editorial-engine.opportunities.list`
  - `editorial-engine.articles.list`
  - `editorial-engine.combined.list`
- Use these concrete editorial actions when workers need to move an opportunity forward:
  - `editorial-engine.generate_proposal`
  - `editorial-engine.generate_article`
  - `editorial-engine.publish`
  - `editorial-engine.schedule`
  - `editorial-engine.discard`
- For the editorial planning flow, use `editorial-engine.analyze_plan` to get an AI-generated editorial plan (calendar, cadence, content mix), `editorial-engine.get_plan` / `editorial-engine.list_plans` to review it, and `editorial-engine.execute_plan` to create opportunities from the calendar. `editorial-engine.regenerate_plan` rebuilds an existing plan with the current AI prompt.
- Use `module.kpis` for `editorial-engine` when the worker starts from a summary request.

## Implementation via Uproc CLI

- Read editorial context with:
  - `uproc applications editorial list-opportunities [--page 1]`
  - `uproc applications editorial list-projects [--page 1]`
  - `uproc applications editorial list-articles [--page 1]`
  - `uproc applications editorial list-combined [--page 1]`
- Act on opportunities with `uproc applications editorial generate-proposal <opportunity_id>`, `uproc applications editorial generate-article <opportunity_id>`, `uproc applications editorial publish <opportunity_id>`, `uproc applications editorial schedule <opportunity_id>`, and `uproc applications editorial discard <opportunity_id>`.
- KPIs: `uproc applications module overview editorial-engine kpis`.
- Limit: the editorial AI plan flow (`analyze_plan`/`execute_plan`) is MCP-only.

## Output

- Editorial summary.
- Priority content list.
- Suggested next steps.
