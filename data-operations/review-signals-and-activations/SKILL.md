# Review Signals And Activations

## Profile

Advanced operations and strategy staff.

## Goal

Review external market signals and see which ones became activations or actions.

## Modules

- `market-signals`

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
  - `market-signals.signals.list`
  - `market-signals.executions.list`
  - `market-signals.activations.list`
- Use `market-signals.approve_signal` when a reviewed signal should move forward.
- Use `market-signals.discard_signal` when a signal should be closed out as not useful.
- Use `market-signals.mark_pending_review` when the signal needs to go back into review.
- Use `market-signals.activate_signal` when the worker is ready to trigger the activation path.
- Use `market-signals.close_signal` when follow-up is complete and the signal should be finalized.
- Use `module.kpis` for `market-signals` when the worker starts with a summary request.

## Output

- Signal summary.
- Activation overview.
- Suggested business follow-up.
