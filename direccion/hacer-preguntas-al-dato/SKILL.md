# Hacer Preguntas Al Dato

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

## Output

- Direct answer.
- Supporting context.
- Any caveat or missing data note.
