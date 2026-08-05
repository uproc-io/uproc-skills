# Reconcile Transactions

## Profile

Finance and accounting staff.

## Goal

Review reconciliation activity, detect unmatched movements, and focus manual effort where needed.

## Modules

- `financial-reconciliation`

## Backend capabilities

- Read KPIs.
- Read `entries`, `extracts`, `exports`, and `matches`.
- Upload and webhook support.

## Use this skill when

- You need to review reconciliation status.
- You want to identify unmatched or suspicious items.

## What it should do

- Summarize reconciliation status.
- Highlight unmatched or low-confidence matches.
- Separate items ready to export from items needing manual review.

## Implementation via Uproc MCP

- Use the reconciliation shortcuts directly:
  - `financial-reconciliation.entries.list`
  - `financial-reconciliation.extracts.list`
  - `financial-reconciliation.exports.list`
  - `financial-reconciliation.matches.list`
- Use `financial-reconciliation.reconcile` when the worker wants to trigger a reconciliation run for the current process.
- Use `module.kpis` for `financial-reconciliation` when the worker wants an overview first.
- For recent activity, sort descending by `created_at` when that field exists in the target collection.

## Output

- Reconciliation summary.
- Manual review queue.
- Next actions by priority.
