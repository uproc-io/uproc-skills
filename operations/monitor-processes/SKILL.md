# Monitor Processes

## Profile

Operations managers and process owners.

## Goal

Review process visibility signals and identify what needs intervention.

## Modules

- `process-visibility`
- `market-signals`

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
  - `process-visibility.processes.list`
  - `market-signals.signals.list`
  - `market-signals.executions.list`
  - `market-signals.activations.list`
- Use `module.kpis` on `process-visibility` or `market-signals` for high-level monitoring first.
- Use `process-visibility.retry_step` when the worker needs to restart the current blocked step.
- Use `process-visibility.reassign_owner` when the worker needs to send the process back to the fallback owner flow.
- Use `process-visibility.cancel_process` when the worker confirms the tracked process should be stopped.

## Implementation via Uproc CLI

- Read processes with `uproc applications process-visibility list [--page 1]`.
- Read signals with `uproc applications market-signals list [--page 1]`, `uproc applications market-signals list-executions [--page 1]`, and `uproc applications market-signals list-activations [--page 1]`.
- KPIs: `uproc applications module overview process-visibility kpis` and `uproc applications module overview market-signals kpis`.
- Act on processes with `uproc applications process-visibility retry-step <process_id>`, `uproc applications process-visibility reassign-owner <process_id>`, and `uproc applications process-visibility cancel <process_id>`.

## Output

- Process overview.
- Alert list.
- Suggested actions.
