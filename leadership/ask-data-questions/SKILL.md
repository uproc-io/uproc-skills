# Ask Data Questions

## Profile

Managers and business users.

## Goal

Answer business questions in natural language and ground them in available data context.

## Modules

- `data-chatbot`
- `data-management`

## Backend capabilities

- Read `queries` from `data-chatbot`.
- `data-management` currently has limited generic collection exposure, so use it as supporting context, not as a broad promise.

## Use this skill when

- A worker asks a business question rather than a record lookup.
- You need a short analytical answer, not a raw table dump.

## What it should do

- Clarify the question if too broad.
- Return a short answer grounded in the available context.
- State uncertainty when the backend exposure is limited.

## Implementation via Bizzmod MCP

- Use `data-chatbot.queries.list` to inspect prior analytical queries when relevant.
- Send the business question with `data-chatbot.send_chat_query` when the worker wants an answer instead of only browsing past queries.
- Use `modules.resolve` to find the most relevant business module if the question is not clearly tied to one dataset.
- Use `module.kpis` and `module.data` as supporting evidence, but do not overpromise raw dataset access for `data-management` until the external metadata is normalized.

## Output

- Direct answer.
- Supporting context.
- Any caveat or missing data note.
