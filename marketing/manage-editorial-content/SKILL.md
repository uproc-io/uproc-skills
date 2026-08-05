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
- Use `module.kpis` for `editorial-engine` when the worker starts from a summary request.

## Output

- Editorial summary.
- Priority content list.
- Suggested next steps.
