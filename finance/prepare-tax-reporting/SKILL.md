---
name: "prepare-tax-reporting"
description: "Review available tax reports and identify what should be validated before filing or export."
---

# Prepare Tax Reporting

## Profile

Finance and tax staff.

## Goal

Review available tax reports and identify what should be validated before filing or export.

## Modules

- `taxes` · suite `finance`
- `reconciliation` · suite `finance`

## Backend capabilities

- Read KPIs.
- Read `reports` in tax reporting and reconciliation collections for support context.

## Use this skill when

- You need a pre-submission review of tax reporting.
- You want to detect missing source checks.

## What it should do

- Review available tax reports.
- Point out missing supporting checks or unresolved financial mismatches.
- Prepare a concise validation checklist.

## Implementation via Uproc MCP

- Use `taxes.reports.list` as the primary reporting source.
- Use `taxes.generate_report` to trigger a draft generation run for an existing report.
- Use `taxes.recalculate_report` when source figures changed and totals must be refreshed.
- Use `taxes.validate_report` before filing or handoff.
- Use `taxes.export_report` when the reviewed report is ready for export delivery.
- Use `reconciliation.matches.list` or `reconciliation.entries.list` as supporting evidence for unresolved mismatches.
- Use `module.kpis` for `tax-reporting` when the worker asks for a summary rather than a report list.

## Implementation via Uproc CLI

- Read reports with `uproc applications taxes list [--page 1]`.
- Run lifecycle actions with `uproc applications taxes generate <report_id>`, `uproc applications taxes recalculate <report_id>`, `uproc applications taxes validate <report_id>`, and `uproc applications taxes export <report_id>`.
- Read reconciliation support context with `uproc applications reconciliation list-matches [--page 1]` and `uproc applications reconciliation list-entries [--page 1]`.
- KPIs: `uproc applications module overview tax-reporting kpis`.

## Output

- Report status summary.
- Risks and pending checks.
- Suggested validation sequence.