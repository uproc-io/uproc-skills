# Load And Sync Data

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
- ERP and accounting integrations: Holded (API v2, Bearer token), Factura Directa (api-key + company id), Invoice Ninja (X-API-TOKEN), Xero (OAuth2 access token + tenant id), QuickBooks (OAuth2 access token + realmId), Pandle, QuickFile, ClearBooks, Bonsai and Capium (API key/token) are independent integrations, each with its own credential. A customer selects which integrations to use; each selected one syncs `invoices` (sales), `purchases` (expenses), `clients`, or `suppliers` to a destination module (`sales-invoices`, `purchase-invoices`, or `data-management`). Integrations can belong to several groups (e.g. `erp` + `accounting`); some accounting integrations (FreeAgent, Zoho Books, NetSuite, Odoo, Ember, FreshBooks, Dynamics 365 Business Central, Sage Intacct) are registered but not yet available (`available=false`).
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
  - `data-sync.runs.list`
  - `data-sync.workflows.list`
  - `data-sync.records.list`
  - `data-enrichment.executions.list`
  - `data-enrichment.runs.list`
- Use `data-sync.run_workflow` when the worker wants to execute a workflow immediately.
- Use `data-sync.preview_workflow` before running a workflow if the worker wants a low-risk sample of the records that would be processed.
- Use `data-sync.dry_run_workflow` when the worker wants a rehearsal without publishing changes.
- Use `module.get` (`data-sync`) or `module.collection` to inspect the ERP integration status (`erp_integrations`) when the worker needs to see which ERPs are configured for the customer.
- Use `module.action` (`data-sync` `test_source`) to validate a workflow's source connectivity before enabling it.
- Use the generic `module.create` (`data-sync` `workflows`) to set up an ERP sync workflow: provide `source_kind=erp`, a `source_resource` (`invoices`/`purchases`/`clients`/`suppliers`), and a `destination_kind` (`sales-invoices`/`purchase-invoices`/`data-management`).
- Use `data-management.preview_import` to validate a mapped file before ingesting it.
- Use `data-management.enqueue_import` to queue the actual mapped import.
- Use `data-management.get_upload_status` or `data-management.get_latest_upload` to monitor import progress.
- Use `data-management.list_tables`, `data-management.create_table`, and `data-management.update_table` for worker-facing table setup and maintenance.
- Use `data-management.list_columns`, `data-management.create_column`, `data-management.update_column`, and `data-management.reorder_columns` for column-level schema maintenance.
- For the data normalization flow, use `data-management.analyze_normalization` (entity ids + optional `custom_prompt` / `data_contract`; sends only structural metadata to AI) to get an AI-generated normalization plan, `data-management.get_plan` / `data-management.list_plans` to review it, `data-management.get_row_mappings` to see the exact row-level transformations, and `data-management.execute_normalization` to create the lookup/main entities and replace raw values with FK ids. `data-management.regenerate_plan` rebuilds an existing plan.
- Use `data-management.smart_import_preview` to match a raw upload against a normalized entity (confidence + column mapping) and `data-management.smart_import_execute` to map and insert unique rows (creating target columns when needed).
- Use `module.kpis` for `data-sync` or `data-enrichment` when the worker wants an overview first.
- Use `form-generator.publish_form` when the worker finishes preparing a form and wants to make it live.
- Use `form-generator.archive_form` when the worker needs to retire a form from active use.
- Use `form-generator.restore_form` when the worker needs to reopen an archived form as draft.
- Use `form-generator.mark_submission_processed` when the worker finishes handling a form submission.
- Use `form-generator.archive_submission` when the worker needs to remove a handled submission from the active queue.
- Treat `form-generator` as the more limited MCP surface; `data-management` now supports worker-facing import monitoring and table/column setup, but destructive deletes still require more advanced routes.

## Implementation via Uproc CLI

- Read sync context with `uproc applications sync list-workflows [--page 1]`, `uproc applications sync list-runs [--page 1]`, and `uproc applications sync list-records [--page 1]`.
- Run and rehearse workflows with `uproc applications sync run <workflow_id>`, `uproc applications sync preview <workflow_id> [limit]`, and `uproc applications sync dry-run <workflow_id> [limit]`.
- Push a record to an ERP with `uproc applications sync push-to-erp --credential <id> --resource <resource> --json '<payload>'`.
- Read data-management tables with the generic reader: `uproc applications module collection data-management entities [--page 1]` (and per-entity collections as configured).
- KPIs: `uproc applications module overview data-sync kpis`, `uproc applications module overview data-management kpis`.
- Forms lifecycle with `uproc applications forms list [--page 1]`, `uproc applications forms list-fields [--page 1]`, `uproc applications forms list-submissions [--page 1]`, `uproc applications forms publish <form_id>`, `uproc applications forms archive <form_id>`, `uproc applications forms archive-submission <submission_id>`, `uproc applications forms restore <form_id>`, and `uproc applications forms mark-submission-processed <submission_id>`.
- Limits: the data-management normalization/smart-import flow and `data-sync` ERP workflow creation (`module.create`) are MCP-only; the CLI covers workflow run/preview/dry-run and ERP push verbs.

## Output

- Pipeline health summary.
- Failing workflow list.
- Suggested corrective actions.
