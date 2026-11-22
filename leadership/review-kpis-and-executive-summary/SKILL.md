# Review KPIs And Executive Summary

## Profile

Managers and leadership.

## Goal

Summarize business KPIs across relevant modules and highlight where attention is needed.

## Modules

- `processes` · suite `operations`
- `queries` · suite `cross`
- `reports` · suite `cross`
- Any business module with KPIs relevant to the request

## Backend capabilities

- Read KPIs across modules.
- Read supporting collections when needed.

## Use this skill when

- Leadership needs a concise operational summary.
- A manager asks for the current status of an area.

## What it should do

- Select the relevant modules for the request.
- Summarize KPIs and the few records that explain them.
- Highlight risks, blockers, or unusual changes.

## Implementation via Uproc MCP

- Use `modules.resolve` or `modules.search` when the worker asks a broad business question and the relevant module is not obvious.
- Query summaries with `module.kpis` on the resolved modules.
- Use `module.data` only for the few supporting collections needed to explain a KPI change.
- Use `queries.queries.list` if the worker wants visibility into recent analytical questions.
- Read the weekly business/system report with `reports.weekly.get` (`kind`) and list available periods with `reports.weekly.periods`.

## Implementation via Uproc CLI

- Discover the relevant module with `uproc applications module list` (or the raw `uproc applications request GET /api/v1/external/modules`).
- Query summaries with `uproc applications module overview <module_slug> kpis` for each resolved module.
- Drill into the few supporting collections with `uproc applications module collection <module_slug> <collection> [--page 1]`.
- Inspect recent analytical questions with `uproc applications queries list [--page 1]`.
- Read the weekly report with `uproc applications reports weekly [--kind system|customer]` and list periods with `uproc applications reports weekly-periods`.

## Output

- Executive summary.
- Key metrics.
- Risks and recommended follow-ups.
