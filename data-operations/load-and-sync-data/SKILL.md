# Load And Sync Data

## Profile

Advanced operations and data staff.

## Goal

Review synchronization and enrichment activity and prepare the next operational step.

## Modules

- `connectors` · suite `data`
- `data-enrichment` · suite `data`
- `tables` · suite `data`
- `forms` · suite `operations`

## Backend capabilities

- Read `runs`, `workflows`, `records`, `executions`, and `runs`.
- Upload and webhook support.
- `tables` and `forms` need careful handling because their generic collection exposure is not as complete as other modules.
- ERP and accounting integrations: Holded (API v2, Bearer token), Factura Directa (api-key + company id), Invoice Ninja (X-API-TOKEN), Xero (OAuth2 access token + tenant id), QuickBooks (OAuth2 access token + realmId), Pandle, QuickFile, ClearBooks, Bonsai and Capium (API key/token) are independent integrations, each with its own credential. A customer selects which integrations to use; each selected one syncs `invoices` (sales), `purchases` (expenses), `clients`, or `suppliers` to a destination module (`sales`, `purchases`, or `tables`). Integrations can belong to several groups (e.g. `erp` + `accounting`); some accounting integrations (FreeAgent, Zoho Books, NetSuite, Odoo, Ember, FreshBooks, Dynamics 365 Business Central, Sage Intacct) are registered but not yet available (`available=false`).
- Postiz (social media scheduling, category/group `social`, read-only) is a data-sync source that can fetch `integrations`/`posts` — not accounting/ERP.

## Use this skill when

- You need to review data pipeline status.
- You want to detect failing syncs or ingestion bottlenecks.

## What it should do

- Review recent runs and executions.
- Highlight failing or stale workflows.
- Separate what can be retried directly from what needs manual investigation.

## Implementation via Uproc MCP

- Use:
  - `connectors.runs.list`
  - `connectors.workflows.list`
  - `connectors.records.list`
  - `data-enrichment.executions.list`
  - `data-enrichment.runs.list`
- Use `connectors.run_workflow` when the worker wants to execute a workflow immediately.
- Use `connectors.preview_workflow` before running a workflow if the worker wants a low-risk sample of the records that would be processed.
- Use `connectors.dry_run_workflow` when the worker wants a rehearsal without publishing changes.
- Use `module.get` (`connectors`) or `module.collection` to inspect the ERP integration status (`erp_integrations`) when the worker needs to see which ERPs are configured for the customer.
- Use `module.action` (`connectors` `test_source`) to validate a workflow's source connectivity before enabling it.
- Use the generic `module.create` (`connectors` `workflows`) to set up an ERP sync workflow: provide `source_kind=erp`, a `source_resource` (`invoices`/`purchases`/`clients`/`suppliers`), and a `destination_kind` (`sales`/`purchases`/`tables`).
- Use `tables.preview_import` to validate a mapped file before ingesting it.
- Use `tables.enqueue_import` to queue the actual mapped import.
- Use `tables.get_upload_status` or `tables.get_latest_upload` to monitor import progress.
- Use `tables.list_tables`, `tables.create_table`, and `tables.update_table` for worker-facing table setup and maintenance.
- Use `tables.list_columns`, `tables.create_column`, `tables.update_column`, and `tables.reorder_columns` for column-level schema maintenance.
- For the data normalization flow, use `tables.analyze_normalization` (entity ids + optional `custom_prompt` / `data_contract`; sends only structural metadata to AI) to get an AI-generated normalization plan, `tables.get_plan` / `tables.list_plans` to review it, `tables.get_row_mappings` to see the exact row-level transformations, and `tables.execute_normalization` to create the lookup/main entities and replace raw values with FK ids. `tables.regenerate_plan` rebuilds an existing plan.
- Use `tables.smart_import_preview` to match a raw upload against a normalized entity (confidence + column mapping) and `tables.smart_import_execute` to map and insert unique rows (creating target columns when needed).
- Use `module.kpis` for `connectors` or `data-enrichment` when the worker wants an overview first.
- Use `forms.publish_form` when the worker finishes preparing a form and wants to make it live.
- Use `forms.archive_form` when the worker needs to retire a form from active use.
- Use `forms.restore_form` when the worker needs to reopen an archived form as draft.
- Use `forms.mark_submission_processed` when the worker finishes handling a form submission.
- Use `forms.archive_submission` when the worker needs to remove a handled submission from the active queue.
- Treat `forms` as the more limited MCP surface; `tables` now supports worker-facing import monitoring and table/column setup, but destructive deletes still require more advanced routes.

## Implementation via Uproc CLI

- Read sync context with `uproc applications connectors list-workflows [--page 1]`, `uproc applications connectors list-runs [--page 1]`, and `uproc applications connectors list-records [--page 1]`.
- Run and rehearse workflows with `uproc applications connectors run <workflow_id>`, `uproc applications connectors preview <workflow_id> [limit]`, and `uproc applications connectors dry-run <workflow_id> [limit]`.
- Push a record to an ERP with `uproc applications connectors push-to-erp --credential <id> --resource <resource> --json '<payload>'`.
- Read data-management tables with the generic reader: `uproc applications module collection data-management entities [--page 1]` (and per-entity collections as configured).
- KPIs: `uproc applications module overview data-sync kpis`, `uproc applications module overview data-management kpis`.
- Forms lifecycle with `uproc applications forms list [--page 1]`, `uproc applications forms list-fields [--page 1]`, `uproc applications forms list-submissions [--page 1]`, `uproc applications forms publish <form_id>`, `uproc applications forms archive <form_id>`, `uproc applications forms archive-submission <submission_id>`, `uproc applications forms restore <form_id>`, and `uproc applications forms mark-submission-processed <submission_id>`.
- Normalization operations and limits: `module.action` on `tables` with `operations_list`, `operation_get`, `settings_limits`, `merge_entities` and `execute_bulk_delete` (preview first with `preview_bulk_delete`).
- CLI equivalent: `uproc applications module action data-management <action> '<json>'`; `connectors` ERP workflow creation still uses the generic `module.create` contract.

## Output

- Pipeline health summary.
- Failing workflow list.
- Suggested corrective actions.
