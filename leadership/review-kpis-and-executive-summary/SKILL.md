# Review KPIs And Executive Summary

## Profile

Managers and leadership.

## Goal

Summarize business KPIs across relevant modules and highlight where attention is needed.

## Modules

- `process-visibility`
- `data-chatbot`
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
- Use `data-chatbot.queries.list` if the worker wants visibility into recent analytical questions.

## Output

- Executive summary.
- Key metrics.
- Risks and recommended follow-ups.
