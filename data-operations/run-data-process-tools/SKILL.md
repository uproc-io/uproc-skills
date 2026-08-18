# Run Data Process Tools

## Profile

Data operations staff.

## Goal

Validate, clean, or enrich a dataset by running data-process tools on a single record or in batch over a data-management entity.

## Modules

- `data-process`

## Backend capabilities

- Search the data-process tool catalog.
- Inspect the full spec of a tool (params, accepted values, format, cost).
- Execute a tool inline (real-time single call).
- Queue a background batch run over a data-management entity.
- Read batch run history.

## Use this skill when

- You need to validate a single value (for example, an IBAN, a credit card checksum, or a mobile number) and only have the value.
- You need to enrich a set of records already loaded into a data-management table with a background batch run.
- You want to know which tools exist and what their parameters and cost are before executing.

## What it should do

- Search the catalog and pick the right tool.
- Inspect the tool spec to build a correct parameter payload.
- Execute the tool inline for a one-off value.
- Queue a batch run over a source entity when many rows must be processed.
- Report the resulting outputs and any failed rows.

## Implementation via Uproc MCP

- Search the catalog with `data-process.search` (optional query text) and open a full spec with `data-process.tool` (tool key) to see params, accepted values, format, and cost.
- Run a single tool call with `data-process.execute` (argument `processor` = tool key, `params` = parameter object).
- Queue a background run with `data-process.batch`: provide `tool`, `source_entity_id` (the data-management entity holding the rows), optional `column_mapping`, `fixed_values`, and `output_name`.
- Read past runs with `module.data` on `data-process` / `runs`.

## Implementation via Uproc CLI

- `uproc applications data-process search [query]` — search the catalog.
- `uproc applications data-process tool <key>` — show the full tool spec.
- `uproc applications data-process execute <tool> [params_json]` — run a tool inline.
- `uproc applications data-process batch <tool> <source_entity_id> [column_mapping_json] [fixed_values_json] [output_name]` — queue a background batch run.
- `uproc applications data-process runs` — read past batch runs.

## Output

- Tool result for the single call.
- Batch run summary with processed/failed rows and the generated output entity.
