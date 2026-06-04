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
- Upload and webhook support.

## Use this skill when

- You need an editorial prioritization view.
- You want a concise content pipeline summary.

## What it should do

- Review editorial projects and opportunities.
- Surface articles needing attention.
- Suggest a priority order for work.

## Implementation via Bizzmod MCP

- Use:
  - `editorial-engine.projects.list`
  - `editorial-engine.opportunities.list`
  - `editorial-engine.articles.list`
  - `editorial-engine.combined.list`
- Use `module.kpis` for `editorial-engine` when the worker starts from a summary request.

## Output

- Editorial summary.
- Priority content list.
- Suggested next steps.
