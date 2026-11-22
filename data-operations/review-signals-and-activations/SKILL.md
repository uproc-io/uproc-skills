# Review Signals And Activations

## Profile

Advanced operations and strategy staff.

## Goal

Review external market signals and see which ones became activations or actions.

## Modules

- `market` · suite `sales`

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

## Implementation via Uproc MCP

- Use:
  - `market.signals.list`
  - `market.executions.list`
  - `market.activations.list`
- Use `market.approve_signal` when a reviewed signal should move forward.
- Use `market.discard_signal` when a signal should be closed out as not useful.
- Use `market.mark_pending_review` when the signal needs to go back into review.
- Use `market.activate_signal` when the worker is ready to trigger the activation path.
- Use `market.close_signal` when follow-up is complete and the signal should be finalized.
- Use `module.kpis` for `market` when the worker starts with a summary request.

## Implementation via Uproc CLI

- Read signals with `uproc applications market list [--page 1]`, `uproc applications market list-executions [--page 1]`, and `uproc applications market list-activations [--page 1]`.
- KPIs: `uproc applications module overview market-signals kpis`.
- Act on signals with `uproc applications market approve <signal_id>`, `uproc applications market discard <signal_id>`, `uproc applications market mark-pending-review <signal_id>`, `uproc applications market activate <signal_id>`, and `uproc applications market close <signal_id>`.

## Output

- Signal summary.
- Activation overview.
- Suggested business follow-up.
