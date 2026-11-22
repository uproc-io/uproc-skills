# Ask Data Questions

## Profile

Managers and business users.

## Goal

Answer business questions in natural language and ground them in available data context.

## Modules

- `queries` · suite `cross`
- `tables` · suite `data`

## Backend capabilities

- Read `queries` from `queries`.
- List the available data domains (channels) with their sample questions.
- Ask natural-language questions and continue the same conversation (follow-ups) with a session id.
- Switch channel/domain while keeping the conversation flow.
- `tables` currently has limited generic collection exposure, so use it as supporting context, not as a broad promise.

## Use this skill when

- A worker asks a business question rather than a record lookup.
- You need a short analytical answer, not a raw table dump.
- You want to see which questions can be asked on a domain, or continue an earlier conversation.

## What it should do

- Clarify the question if too broad.
- List the available domains/sample questions first when the worker is not sure where to ask.
- Return a short answer grounded in the available context, capturing the `session_id` to continue.
- State uncertainty when the backend exposure is limited.

## Implementation via Uproc MCP

- Use `queries.list_domains` to see the available domains (channels) and their sample questions before asking.
- Use `queries.queries.list` to inspect prior analytical queries when relevant.
- Send the business question with `queries.send_chat_query` (arguments `domain`, `question`, optional `channel`/`context`); the response includes the `session_id`.
- For follow-up questions that depend on a previous answer (e.g. "and last month?"), use `queries.follow_up` with the previous `session_id`; the channel, domain and previous question are reused automatically.
- Use `modules.resolve` to find the most relevant business module if the question is not clearly tied to one dataset.
- Use `module.kpis` and `module.data` as supporting evidence, but do not overpromise raw dataset access for `tables` until the external metadata is normalized.

## Implementation via Uproc CLI

- List the available domains with `uproc applications queries domains`.
- Ask a question with `uproc applications queries ask <domain> <question> [context] [channel] [sender_id] [origin_session_id]`; the response includes the `session_id` to resume.
- Continue a conversation with `uproc applications queries follow-up <origin_session_id> <question> [channel] [domain] [origin_user_id]`.
- Inspect prior queries with `uproc applications queries list [--page 1]`.
- Use the guided flow with `uproc applications queries interactive`.
- Supporting evidence: `uproc applications module overview <slug> kpis` and `uproc applications module collection data-management <collection> [--page 1]`.

## Output

- Direct answer.
- Supporting context.
- Any caveat or missing data note.
