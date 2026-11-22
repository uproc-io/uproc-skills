# Draft Customer Replies

## Profile

Support, administration, and account teams.

## Goal

Draft clear emails for confirmations, requests for information, follow-ups, and issue responses.

## Modules

- `mail` · suite `operations`
- `support` · suite `operations`

## Backend capabilities

- Read `emails` and support context.
- Upload and webhook support.

## Use this skill when

- You need a professional customer reply.
- You want a concise summary and draft before sending.

## What it should do

- Ask for tone, language, and objective if missing.
- Use the case or ticket context when available.
- Produce a ready-to-review draft.

## Implementation via Uproc MCP

- Use `mail.emails.list` to inspect recent email context when available.
- Pull case context from `support.tickets.list` or `cases.cases.list` before drafting if the worker references a specific incident.
- Use `mail.mark_processed` when the worker finishes handling a reviewed email.
- Use `mail.archive_email` when the worker wants to remove a handled email from the active queue.
- This skill is guidance-first: the MCP layer helps fetch context and manage queue state, but message drafting remains the main worker-facing output.

## Implementation via Uproc CLI

- Inspect recent emails with `uproc applications mail list [--page 1]`.
- Pull support context with `uproc applications support list [--page 1]` or `uproc applications cases list [--page 1]` when the worker references a specific incident.
- Manage the email queue with `uproc applications mail mark-processed <email_id>` and `uproc applications mail archive <email_id>`.
- This skill is guidance-first: the CLI helps fetch context and manage queue state, but message drafting remains the main worker-facing output.

## Output

- Email subject.
- Email body.
- Short sending notes if needed.
