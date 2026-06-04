# Prepare Tax Reporting

## Profile

Finance and tax staff.

## Goal

Review available tax reports and identify what should be validated before filing or export.

## Modules

- `tax-reporting`
- `financial-reconciliation`

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

## Implementation via Bizzmod MCP

- Use `tax-reporting.reports.list` as the primary reporting source.
- Use `tax-reporting.generate_report` to trigger a draft generation run for an existing report.
- Use `tax-reporting.recalculate_report` when source figures changed and totals must be refreshed.
- Use `tax-reporting.validate_report` before filing or handoff.
- Use `tax-reporting.export_report` when the reviewed report is ready for export delivery.
- Use `financial-reconciliation.matches.list` or `financial-reconciliation.entries.list` as supporting evidence for unresolved mismatches.
- Use `module.kpis` for `tax-reporting` when the worker asks for a summary rather than a report list.

## Output

- Report status summary.
- Risks and pending checks.
- Suggested validation sequence.
