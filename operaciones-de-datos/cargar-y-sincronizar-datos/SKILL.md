# Cargar Y Sincronizar Datos

## Profile

Advanced operations and data staff.

## Goal

Review synchronization and enrichment activity and prepare the next operational step.

## Modules

- `data-sync`
- `data-enrichment`
- `data-management`
- `form-generator`

## Backend capabilities

- Read `runs`, `workflows`, `records`, `executions`, and `runs`.
- Upload and webhook support.
- `data-management` and `form-generator` need careful handling because their generic collection exposure is not as complete as other modules.

## Use this skill when

- You need to review data pipeline status.
- You want to detect failing syncs or ingestion bottlenecks.

## What it should do

- Review recent runs and executions.
- Highlight failing or stale workflows.
- Separate what can be retried directly from what needs manual investigation.

## Output

- Pipeline health summary.
- Failing workflow list.
- Suggested corrective actions.
