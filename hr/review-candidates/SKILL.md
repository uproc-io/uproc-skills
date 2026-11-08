# Review Candidates

## Profile

HR and recruiting staff.

## Goal

Review candidates, applications, and evaluations for current hiring processes.

## Modules

- `candidate-evaluation`

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
  - `candidate-evaluation.job_openings.list`
  - `candidate-evaluation.profiles.list`
  - `candidate-evaluation.applications.list`
  - `candidate-evaluation.evaluations.list`
  - `candidate-evaluation.stage_events.list`
- Use `module.kpis` for `candidate-evaluation` when the worker starts from a hiring overview.
- Use `candidate-evaluation.create_job_opening` when the worker needs to register a new opening before candidate intake starts.
- Use `candidate-evaluation.create_profile` when the worker needs to register a new candidate manually.
- Use `candidate-evaluation.create_application` when the worker needs to attach a candidate to a specific opening.
- Use `candidate-evaluation.create_evaluation` when the worker needs to record a new interview or review outcome.

## Implementation via Uproc CLI

- Read pipeline context with:
  - `uproc applications candidate-evaluation list-job-openings [--page 1]`
  - `uproc applications candidate-evaluation list-profiles [--page 1]`
  - `uproc applications candidate-evaluation list-applications [--page 1]`
  - `uproc applications candidate-evaluation list-evaluations [--page 1]`
  - `uproc applications candidate-evaluation list-stage-events [--page 1]`
- Create records with `uproc applications candidate-evaluation create-job-opening <item_json>`, `uproc applications candidate-evaluation create-profile <item_json>`, `uproc applications candidate-evaluation create-application <item_json>`, and `uproc applications candidate-evaluation create-evaluation <item_json>`.
- KPIs: `uproc applications module overview candidate-evaluation kpis`.

## Output

- Candidate pipeline summary.
- Shortlist candidates.
- Recommended next actions.
