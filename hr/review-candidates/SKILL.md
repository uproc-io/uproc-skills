# Review Candidates

## Profile

HR and recruiting staff.

## Goal

Review candidates, applications, and evaluations for current hiring processes.

## Modules

- `candidates` · suite `operations`

## Backend capabilities

- Read KPIs.
- Read `job_openings`, `profiles`, `applications`, `evaluations`, and `stage_events`.
- Upload and webhook support.

## Use this skill when

- You need a shortlist view.
- You want to compare active candidates quickly.

## What it should do

- Review candidates by opening.
- Summarize stage, status, and evaluations.
- Highlight candidates needing decision or movement.

## Implementation via Uproc MCP

- Use:
  - `candidates.job_openings.list`
  - `candidates.profiles.list`
  - `candidates.applications.list`
  - `candidates.evaluations.list`
  - `candidates.stage_events.list`
- Use `module.kpis` for `candidates` when the worker starts from a hiring overview.
- Use `candidates.create_job_opening` when the worker needs to register a new opening before candidate intake starts.
- Use `candidates.create_profile` when the worker needs to register a new candidate manually.
- Use `candidates.create_application` when the worker needs to attach a candidate to a specific opening.
- Use `candidates.create_evaluation` when the worker needs to record a new interview or review outcome.

## Implementation via Uproc CLI

- Read pipeline context with:
  - `uproc applications candidates list-job-openings [--page 1]`
  - `uproc applications candidates list-profiles [--page 1]`
  - `uproc applications candidates list-applications [--page 1]`
  - `uproc applications candidates list-evaluations [--page 1]`
  - `uproc applications candidates list-stage-events [--page 1]`
- Create records with `uproc applications candidates create-job-opening <item_json>`, `uproc applications candidates create-profile <item_json>`, `uproc applications candidates create-application <item_json>`, and `uproc applications candidates create-evaluation <item_json>`.
- KPIs: `uproc applications module overview candidate-evaluation kpis`.

## Output

- Candidate pipeline summary.
- Shortlist candidates.
- Recommended next actions.
