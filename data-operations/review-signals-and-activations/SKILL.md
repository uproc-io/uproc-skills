# Review Signals And Activations

## Profile

Advanced operations and strategy staff.

## Goal

Review external business signals and see which ones became activations or actions.

## Modules

- `business-signals`

## Backend capabilities

- Read KPIs.
- Read `signals`, `executions`, and `activations`.
- Upload and webhook support.

## Use this skill when

- You need to understand recent signal activity.
- You want to know which signals deserve action.

## What it should do

- Summarize recent signals.
- Identify which signals led to activations.
- Highlight unusual or high-impact signals.

## Implementation via Bizzmod MCP

- Use:
  - `business-signals.signals.list`
  - `business-signals.executions.list`
  - `business-signals.activations.list`
- Use `module.kpis` for `business-signals` when the worker starts with a summary request.

## Output

- Signal summary.
- Activation overview.
- Suggested business follow-up.
