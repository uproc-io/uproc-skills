# Skills

This directory contains end-user skills organized by worker profile and day-to-day task.

## Design rules

- The primary entry point is the worker profile, not the Uproc module name.
- Each skill is named after a real task the worker wants to complete.
- Module names are documented inside each skill as implementation detail.
- Skills reflect the backend reality: most modules support reading, KPIs, uploads, and webhooks; generic create operations are currently rare.
- In this catalog, `form-generator` is the canonical name used for forms.
- Every worker task can be executed through two access paths, and both are documented inside each `SKILL.md`:
  - `Implementation via Uproc MCP` — concrete MCP tools and semantic shortcuts.
  - `Implementation via Uproc CLI` — concrete `uproc applications` commands (dedicated business-verb commands when available, generic `module <slug> <collection>` / `module overview <slug> kpis` / `module upload` / `module webhook` otherwise).
- Prefer the concrete MCP tools / CLI commands named in the skill before falling back to generic helpers such as `module.actions`, `module.action`, or `request`.

## Access

- Every task can be executed through **Uproc MCP** (AI clients such as OpenCode, Claude Code, or Codex) or the **Uproc CLI** (`uproc applications`).
- How to configure both paths and where the required values (user email and user API key) come from is explained in `USER_MANUAL.md` → "Setting up access (MCP and CLI)".

## Structure

```text
skills/
  AGENTS.md
  README.md
  USER_MANUAL.md
  administration/
    review-incoming-documents/
      SKILL.md
```

## Priority model

- `P0`: immediate value for common worker workflows.
- `P1`: important area-specific workflows.
- `P2`: advanced or more specialized workflows.

## Catalog

### administration

- `P0` `administration/review-incoming-documents`
- `P0` `administration/validate-received-invoices`
- `P1` `administration/manage-pending-approvals`
- `P1` `administration/classify-documents`
- `P1` `administration/archive-documents`
- `P2` `administration/convert-documents`
- `P2` `administration/unify-documents`

### finance

- `P1` `finance/review-invoices-and-capture`
- `P1` `finance/register-purchases`
- `P0` `finance/reconcile-transactions`
- `P0` `finance/track-payments-and-overdues`
- `P1` `finance/prepare-tax-reporting`

### support

- `P0` `support/manage-incidents`
- `P0` `support/draft-customer-replies`
- `P1` `support/track-orders-and-report-issues`

### sales

- `P0` `sales/create-and-qualify-leads`
- `P0` `sales/prepare-sales-proposal`
- `P1` `sales/send-proposal-and-follow-up`
- `P1` `sales/review-prospecting-and-prioritize`

### operations

- `P1` `operations/review-incoming-orders`
- `P2` `operations/coordinate-stock-and-demand`
- `P2` `operations/monitor-processes`
- `P2` `operations/file-sync`

### legal

- `P0` `legal/review-active-and-expiring-contracts`
- `P1` `legal/prepare-document-signing`

### hr

- `P1` `hr/review-candidates`
- `P1` `hr/track-hiring-process`

### marketing

- `P2` `marketing/prepare-campaigns-and-audiences`
- `P2` `marketing/manage-editorial-content`

### leadership

- `P0` `leadership/review-kpis-and-executive-summary`
- `P1` `leadership/ask-data-questions`

### data-operations

- `P2` `data-operations/load-and-sync-data`
- `P1` `data-operations/run-data-process-tools`
- `P2` `data-operations/review-signals-and-activations`

## Backend notes

- Most backend-exposed capabilities are `read_kpis`, `list_collections`, `read_collection_data`, `upload_files`, and `receive_webhooks`.
- Generic external `create_collection_data` is currently available for `lead-management.leads`, `candidate-evaluation.job_openings`, `candidate-evaluation.profiles`, `candidate-evaluation.applications`, `candidate-evaluation.evaluations`, `form-generator.forms`, `form-generator.fields`, and `form-generator.submissions`.
- Generic action discovery and execution are available through `module.actions` and `module.action` as the advanced MCP layer.
- Concrete business MCP tools are the preferred worker-facing layer when available. The current concrete catalog also includes support and approval actions, order-ingest and order-track status actions, candidate profile/application creation, form publishing, email queue status actions, and process-visibility actions.
- Skills should prefer concrete tool names first and mention generic `module.actions` or `module.action` only as fallback for advanced clients.
- The Uproc CLI (`uproc applications`) exposes the same external API with dedicated business-verb commands for most modules: `email`, `order`, `orders-ingest`, `data-chatbot`, `forms`, `candidate`, `support`, `approval`, `campaign`, `contract`, `process`, `signals`, `editorial`, `signing`, `tax`, `documents`, `inventory`, `cases`, `invoice` (+ `invoice-lines` and `sales-invoices verifactu`), `purchase-invoices`, `sync`, `leads`, `prospecting`, `reconciliation`, and `data-process`.
- Modules without dedicated CLI business verbs are still reachable through the generic CLI reader `uproc applications module <slug> <collection>` plus `module overview <slug> kpis`, `module upload`, and `module webhook` (this covers `invoice-ingest`, `debt-track`, the `document-*` family, `lead-intelligence`, `data-management`, `investment-analysis`, and `file-sync`).
- The CLI has no `module create`: record creation covered by skills (for example `file-sync` transfers) is MCP-only (or via the web UI) and each affected skill documents that limit.

## Working in this directory

- Add one directory per skill.
- Keep each `SKILL.md` short, operational, and worker-facing.
- Include an `Implementation via Uproc MCP` section with the exact tools or shortcuts to use and any capability gaps.
- When backend capabilities change, update the affected skills and this catalog in the same change set.
- Keep `USER_MANUAL.md` aligned with the current catalog so end users have a single overview of all available skills.
