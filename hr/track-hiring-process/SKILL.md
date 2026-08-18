# Track Hiring Process

## Profile

HR and recruiting staff.

## Goal

Review recruitment progress and identify blocked stages or pending actions.

## Modules

- `candidate-evaluation`
- `email-assistant`

## Backend capabilities

- Read candidate pipeline collections.
- Draft communication support through `email-assistant`.

## Use this skill when

- You need a progress review by stage.
- You want to prepare the next recruiter communication.

## What it should do

- Review stage events and application status.
- Flag stalled candidates or missing evaluations.
- Prepare communication drafts if asked.

## Implementation via Uproc MCP

- Use `candidate-evaluation.stage_events.list`, `candidate-evaluation.applications.list`, and `candidate-evaluation.evaluations.list` to track process movement.
- Use `candidate-evaluation.create_job_opening` when the worker needs to create the opening first.
- Use `candidate-evaluation.create_profile` when the worker needs to add a candidate not yet present in the pipeline.
- Use `candidate-evaluation.create_application` when the worker needs to place a candidate into an opening before continuing stage follow-up.
- Use `candidate-evaluation.move_application_stage` when the worker needs to advance or reposition a candidate in the funnel.
- Use `candidate-evaluation.update_application_status` when the worker needs to mark the application as hired, rejected, archived, or still active.
- Use `candidate-evaluation.create_evaluation` when the worker needs to log a structured evaluation result.
- Use `email-assistant.emails.list` if previous recruiter communication is relevant.
- This skill remains conservative on candidate updates beyond the currently exposed opening/profile/application/evaluation and application stage/status actions.

## Implementation via Uproc CLI

- Track movement with `uproc applications candidate list-stage-events [--page 1]`, `uproc applications candidate list-applications [--page 1]`, and `uproc applications candidate list-evaluations [--page 1]`.
- Advance the funnel with `uproc applications candidate move-stage <application_id> <stage>` and `uproc applications candidate update-status <application_id> <status>`.
- Create records with `uproc applications candidate create-job-opening <item_json>`, `uproc applications candidate create-profile <item_json>`, `uproc applications candidate create-application <item_json>`, and `uproc applications candidate create-evaluation <item_json>`.
- Inspect recruiter communication with `uproc applications email list [--page 1]`.

## Output

- Recruitment progress summary.
- Blocked items.
- Optional communication draft.
