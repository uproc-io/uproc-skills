# Skills User Manual

This manual explains what each skill in `skills/` is for, when to use it, and which worker profile it serves.

## How To Use This Catalog

- Start from the worker profile folder.
- Pick the skill whose task name best matches the job to be done.
- Open the `SKILL.md` file inside that folder.
- Follow the `Implementation via Uproc MCP` section to execute the task with the correct MCP tools.
- Alternatively, follow the `Implementation via Uproc CLI` section to execute the same task with the `uproc applications` CLI.
- Prefer the concrete MCP tools / CLI commands named in the skill before falling back to generic helpers such as `module.actions`, `module.action`, or `request`.

## Profiles

### Administration

#### `administration/review-incoming-documents`

- Use for: reviewing newly received business documents.
- Typical outcome: a quick intake summary, exceptions, and next routing decision.

#### `administration/validate-received-invoices`

- Use for: checking invoice intake quality before downstream finance processing.
- Typical outcome: validation summary, capture issues, and recommended fixes.

#### `administration/manage-pending-approvals`

- Use for: reviewing the approval queue and deciding whether to approve, reject, or reassign requests.
- Typical outcome: prioritized approval summary and action-ready decision list.

#### `administration/classify-documents`

- Use for: reviewing the document classifier folders and keeping the classification pipeline healthy.
- Typical outcome: classification status summary and next routing/upload actions.

#### `administration/archive-documents`

- Use for: managing document archiving folders and organizing stored documents.
- Typical outcome: archive status summary and next archive/upload actions.

#### `administration/convert-documents`

- Use for: reviewing document conversion folders and checking conversion processing health.
- Typical outcome: conversion summary, failures, and next upload/rerun actions.

#### `administration/unify-documents`

- Use for: reviewing document unification folders and the deduplication pipeline.
- Typical outcome: unification summary, pending duplicates, and next actions.

### Finance

#### `finance/review-invoices-and-capture`

- Use for: reviewing received invoices and their extraction/capture state.
- Typical outcome: invoice intake summary and list of records needing manual review.
- Also covers: sending issued invoices to an ERP (`sales-invoices.export_to_erp`) and VeriFactu (Spain) registration management (download XML, resubmit, backfill).

#### `finance/register-purchases`

- Use for: registering supplier invoices (purchases), assigning received invoices from invoice-ingest, and tracking the purchase lifecycle (received → validated → paid).
- Typical outcome: purchase records with lines, payments, and current status.
- Also covers: sending purchases to an ERP (`purchase-invoices.export_to_erp`).

#### `finance/reconcile-transactions`

- Use for: reconciling entries, extracts, and matches.
- Typical outcome: reconciliation summary, mismatch list, and next finance actions.

#### `finance/track-payments-and-overdues`

- Use for: monitoring collections, reminders, and unpaid invoices.
- Typical outcome: overdue list and recommended follow-up actions.

#### `finance/prepare-tax-reporting`

- Use for: reviewing tax reporting readiness and reporting outputs.
- Typical outcome: reporting summary, missing pieces, filing preparation notes, and action-ready next steps such as generate, recalculate, validate, or export.

### Support

#### `support/manage-incidents`

- Use for: triaging support queues, customer-care tickets, and related cases.
- Typical outcome: queue summary, priorities, and next handling actions.

#### `support/draft-customer-replies`

- Use for: preparing customer-facing responses from prior email context.
- Typical outcome: a structured draft reply or response outline.

#### `support/track-orders-and-report-issues`

- Use for: monitoring tracked orders and preparing issue communication.
- Typical outcome: order status summary, exception list, and draft customer update.

### Sales

#### `sales/create-and-qualify-leads`

- Use for: creating leads, checking qualification, and reviewing lead records.
- Typical outcome: qualified lead list and recommended follow-up steps.

#### `sales/prepare-sales-proposal`

- Use for: creating a proposal draft for an existing lead.
- Typical outcome: proposal summary and generated proposal workflow.

#### `sales/send-proposal-and-follow-up`

- Use for: sending proposals and tracking next steps after delivery.
- Typical outcome: sent proposal action and follow-up reminder plan.

#### `sales/review-prospecting-and-prioritize`

- Use for: reviewing prospecting output and deciding what should enter lead management.
- Typical outcome: prioritized opportunities and recommended actions.

### Operations

#### `operations/review-incoming-orders`

- Use for: checking newly ingested or tracked orders and deciding follow-up.
- Typical outcome: order intake summary, exceptions, and next operational action.

#### `operations/coordinate-stock-and-demand`

- Use for: reviewing inventory planning pressure and receipt status.
- Typical outcome: stock-risk summary and suggested coordination actions.

#### `operations/monitor-processes`

- Use for: reviewing operational process visibility and detecting blocked flows.
- Typical outcome: process status summary and escalation list.

#### `operations/file-sync`

- Use for: copying files between storage providers (SFTP / S3 / Dropbox / Google Drive) with overwrite.
- Typical outcome: configured transfers and run logs with copied/failed files.

### Legal

#### `legal/review-active-and-expiring-contracts`

- Use for: reviewing contract status, counterparties, and expiring agreements.
- Typical outcome: active/expiring contract summary and contract action list.

#### `legal/prepare-document-signing`

- Use for: preparing signature requests and following signing progress.
- Typical outcome: signing summary and required next signature step.

### HR

#### `hr/review-candidates`

- Use for: reviewing openings, candidates, applications, evaluations, and stage movement.
- Typical outcome: pipeline summary, shortlist, and recommended candidate actions.

#### `hr/track-hiring-process`

- Use for: monitoring hiring progress and identifying stalled applications or missing evaluations.
- Typical outcome: progress summary, blocked candidates, and optional communication draft.

### Marketing

#### `marketing/prepare-campaigns-and-audiences`

- Use for: reviewing campaigns, defining audiences, and preparing campaign execution.
- Typical outcome: campaign readiness summary, audience action plan, and a clear decision on whether to pause or activate a campaign.

#### `marketing/manage-editorial-content`

- Use for: reviewing editorial opportunities, projects, and article pipelines.
- Typical outcome: editorial backlog summary plus clear next actions such as generate proposal, generate article, publish, schedule, or discard.

### Leadership

#### `leadership/review-kpis-and-executive-summary`

- Use for: obtaining executive KPI snapshots across modules.
- Typical outcome: concise summary of the most relevant market signals and metrics.

#### `leadership/ask-data-questions`

- Use for: asking natural-language business questions to the data chatbot.
- Typical outcome: answer summary plus any recommended follow-up query.
- Supports: follow-up questions that build on a previous question (pass the prior question as `context`).

### Data Operations

#### `data-operations/load-and-sync-data`

- Use for: reviewing sync health, imports, workflows, form publishing readiness, and setting up ERP/accounting sync integrations (Holded, Factura Directa, Invoice Ninja, Xero, QuickBooks, and other accounting software grouped by `erp`/`accounting`; Postiz for social media, group `social`).
- Typical outcome: pipeline health summary, recommended corrective actions, and configured/validated sync workflows.

#### `data-operations/run-data-process-tools`

- Use for: searching the data-process tool catalog, inspecting tool specs, executing validation/cleaning/enrichment tools inline, and queueing background batch runs over a data-management entity.
- Typical outcome: executed tool results and batch runs with per-record outcomes.

#### `data-operations/review-signals-and-activations`

- Use for: reviewing market signals, activations, and execution trends.
- Typical outcome: signal summary and activation follow-up list.

## Notes

- Skills are worker-facing. They describe business tasks, not raw module architecture.
- Concrete MCP tools should be preferred when the skill lists them.
- Concrete Uproc CLI commands (`uproc applications ...`) should be preferred when the skill lists them.
- Generic tools such as `module.actions`, `module.action`, and `request` are fallback options for advanced workflows.
- Recent concrete additions include campaign pause/activate flows, tax reporting generate/recalculate/validate/export flows, and editorial proposal/article/publish/schedule/discard flows, so the related skills now support direct action execution instead of review-only guidance.
