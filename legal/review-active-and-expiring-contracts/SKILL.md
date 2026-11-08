# Review Active And Expiring Contracts

## Profile

Legal and contract management staff.

## Goal

Review contracts, identify upcoming expirations, and prepare the next action.

## Modules

- `contract-lifecycle`

## Backend capabilities

- Read KPIs.
- Read `contracts`, `expiring_contracts`, and `contracts_by_counterparty`.
- Upload and webhook support.

## Use this skill when

- You need a contract status overview.
- You want to spot contracts close to expiry.

## What it should do

- Summarize active and expiring contracts.
- Group by counterparty when useful.
- Highlight contracts requiring renewal, review, or escalation.

## Implementation via Uproc MCP

- Use:
  - `contract-lifecycle.contracts.list`
  - `contract-lifecycle.expiring_contracts.list`
  - `contract-lifecycle.contracts_by_counterparty.list`
- Use `module.kpis` for `contract-lifecycle` when the worker wants a broad contract overview.
- Use `contract-lifecycle.update_contract` when the worker is ready to apply the agreed renewal or status updates to a contract.
- Use `contract-lifecycle.upload_contract_document` when a new contract version, annex, or supporting document must be attached to the contract record.
- Use `contract-lifecycle.renew_contract` when the worker is ready to execute the contract renewal flow directly.
- Use `contract-lifecycle.terminate_contract` when the worker is ready to end the contract and record that state explicitly.

## Implementation via Uproc CLI

- Read contracts with `uproc applications contract-lifecycle list [--page 1]`, `uproc applications contract-lifecycle list-expiring [--page 1]`, and `uproc applications contract-lifecycle list-by-counterparty [--page 1]`.
- KPIs: `uproc applications module overview contract-lifecycle kpis`.
- Act on contracts with `uproc applications contract-lifecycle update <contract_id> <data_json>`, `uproc applications contract-lifecycle renew <contract_id>`, and `uproc applications contract-lifecycle terminate <contract_id>`.
- Limit: `contract-lifecycle.upload_contract_document` has no CLI command and is MCP-only (or web UI).

## Output

- Contract overview.
- Expiration watchlist.
- Recommended next actions.
