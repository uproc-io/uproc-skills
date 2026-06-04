# Monitor Processes

## Profile

Operations managers and process owners.

## Goal

Review process visibility signals and identify what needs intervention.

## Modules

- `process-visibility`
- `business-signals`

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

## Implementation via Bizzmod MCP

- Use:
  - `process-visibility.processes.list`
  - `business-signals.signals.list`
  - `business-signals.executions.list`
  - `business-signals.activations.list`
- Use `module.kpis` on `process-visibility` or `business-signals` for high-level monitoring first.
- Use `process-visibility.retry_step` when the worker needs to restart the current blocked step.
- Use `process-visibility.reassign_owner` when the worker needs to send the process back to the fallback owner flow.
- Use `process-visibility.cancel_process` when the worker confirms the tracked process should be stopped.

## Output

- Process overview.
- Alert list.
- Suggested actions.
