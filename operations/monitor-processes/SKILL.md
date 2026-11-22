# Monitor Processes

## Profile

Operations managers and process owners.

## Goal

Review process visibility signals and identify what needs intervention.

## Modules

- `processes` · suite `operations`
- `market` · suite `sales`

## Backend capabilities

- Read KPIs.
- Read `processes`, `signals`, `executions`, and `activations`.
- Upload and webhook support.

## Use this skill when

- You need an operational control view.
- You want to detect process anomalies or triggers.

## What it should do

- Summarize visible process state.
- Highlight signals and activations worth reviewing.
- Recommend operational escalations.

## Implementation via Uproc MCP

- Use:
  - `processes.processes.list`
  - `market.signals.list`
  - `market.executions.list`
  - `market.activations.list`
- Use `module.kpis` on `processes` or `market` for high-level monitoring first.
- Use `processes.retry_step` when the worker needs to restart the current blocked step.
- Use `processes.reassign_owner` when the worker needs to send the process back to the fallback owner flow.
- Use `processes.cancel_process` when the worker confirms the tracked process should be stopped.

## Implementation via Uproc CLI

- Read processes with `uproc applications processes list [--page 1]`.
- Read signals with `uproc applications market list [--page 1]`, `uproc applications market list-executions [--page 1]`, and `uproc applications market list-activations [--page 1]`.
- KPIs: `uproc applications module overview process-visibility kpis` and `uproc applications module overview market-signals kpis`.
- Act on processes with `uproc applications processes retry-step <process_id>`, `uproc applications processes reassign-owner <process_id>`, and `uproc applications processes cancel <process_id>`.

## Output

- Process overview.
- Alert list.
- Suggested actions.
