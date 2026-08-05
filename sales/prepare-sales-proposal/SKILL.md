# Prepare Sales Proposal

## Profile

Sales staff.

## Goal

Prepare a proposal workflow from an existing lead using the backend actions available in lead management.

## Modules

- `lead-management`
- `document-generator`

## Backend capabilities

- Read lead data.
- Use special lead-management actions for proposal generation.
- Read generated document context when available.

## Use this skill when

- You already have a lead and need a commercial proposal.
- You want a proposal-ready package before sending.

## What it should do

- Confirm the target lead.
- Gather proposal title, description, and desired output format.
- Trigger proposal preparation when the worker confirms.

## Implementation via Uproc MCP

- Read the target lead with `lead-management.leads.list`.
- Generate the proposal directly with `lead-management.generate_lead_proposal`.
- Use `module.actions` or `module.action` only as an advanced fallback if the client is operating at the generic MCP layer.
- Use `document-generator.documents.list` to review generated document context when available.
- Use `document-generator.mark_review`, `document-generator.mark_ready`, and `document-generator.regenerate_document` when the generated proposal needs another internal drafting pass before it is sent.

## Output

- Proposal request summary.
- Generated proposal status.
- Recommended review checklist before sending.
