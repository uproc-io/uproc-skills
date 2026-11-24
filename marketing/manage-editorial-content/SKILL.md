---
name: "manage-editorial-content"
description: "Review editorial work queues and focus on the highest-value content items."
---

# Manage Editorial Content

## Profile

Marketing and content teams.

## Goal

Review editorial work queues and focus on the highest-value content items.

## Modules

- `content` · suite `sales`

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
  - `content.projects.list`
  - `content.opportunities.list`
  - `content.articles.list`
  - `content.combined.list`
- Use these concrete editorial actions when workers need to move an opportunity forward:
  - `content.generate_proposal`
  - `content.generate_article`
  - `content.publish`
  - `content.schedule`
  - `content.discard`
- For the editorial planning flow, use `content.analyze_plan` to get an AI-generated editorial plan (calendar, cadence, content mix), `content.get_plan` / `content.list_plans` to review it, and `content.execute_plan` to create opportunities from the calendar. `content.regenerate_plan` rebuilds an existing plan with the current AI prompt.
- Use `module.kpis` for `content` when the worker starts from a summary request.

## Implementation via Uproc CLI

- Read editorial context with:
  - `uproc applications content list-opportunities [--page 1]`
  - `uproc applications content list-projects [--page 1]`
  - `uproc applications content list-articles [--page 1]`
  - `uproc applications content list-combined [--page 1]`
- Act on opportunities with `uproc applications content generate-proposal <opportunity_id>`, `uproc applications content generate-article <opportunity_id>`, `uproc applications content publish <opportunity_id>`, `uproc applications content schedule <opportunity_id>`, and `uproc applications content discard <opportunity_id>`.
- KPIs: `uproc applications module overview editorial-engine kpis`.
- Limit: the editorial AI plan flow (`analyze_plan`/`execute_plan`) is MCP-only.

## Output

- Editorial summary.
- Priority content list.
- Suggested next steps.