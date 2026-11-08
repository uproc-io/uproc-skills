# Send Proposal And Follow Up

## Profile

Sales staff.

## Goal

Send a proposal with the right message and define the immediate follow-up plan.

## Modules

- `lead-management`
- `email-assistant`

## Backend capabilities

- Use the special `send_lead_proposal` action in `lead-management`.
- Draft communication support from `email-assistant`.

## Use this skill when

- A proposal is ready and the team needs to send it.
- A follow-up sequence should be defined after sending.

## What it should do

- Confirm recipient, mailbox, subject, and message.
- Prepare or refine the sending draft.
- Trigger sending when the user confirms.
- Suggest the next follow-up date or action.

## Implementation via Uproc MCP

- Read lead context with `lead-management.leads.list`.
- Use `email-assistant.emails.list` for communication context if prior emails exist.
- Send the proposal with `lead-management.send_lead_proposal`.
- Use `module.actions` or `module.action` only as an advanced fallback if the client is operating at the generic MCP layer.

## Implementation via Uproc CLI

- Read lead context with `uproc applications lead-management list [--page 1]`.
- Read communication context with `uproc applications email list [--page 1]`.
- Send the proposal with `uproc applications lead-management send-proposal <lead_id> <mailbox_id> <to_email> <subject> <body> [proposal_url]`.
- Manage the email queue with `uproc applications email mark-processed <email_id>` / `uproc applications email archive <email_id>` if needed.

## Output

- Sending summary.
- Final email draft.
- Follow-up recommendations.
