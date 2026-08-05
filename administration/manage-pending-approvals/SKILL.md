# Manage Pending Approvals

## Profile

Administrative coordinators and approvers.

## Goal

Review pending approval requests and prepare a decision-ready summary.

## Modules

- `approval-management`

## Backend capabilities

- Read KPIs.
- Read `requests`.
- Upload and webhook support.

## Use this skill when

- You need to know what is still waiting for approval.
- You want to prioritize approval workload.

## What it should do

- List pending requests.
- Group by urgency, type, or requester when possible.
- Highlight blocked or stale requests.
- Recommend approve, reject, or escalate.

## Implementation via Uproc MCP

- Use `approval-management.requests.list` as the default queue query.
- Use `module.kpis` for `approval-management` if the worker asks for a summary view before record-level review.
- Apply `filter_field` and `filter_value` when the worker narrows by status or requester.
- Use `approval-management.approve_request` when the worker is ready to approve a request.
- Use `approval-management.reassign_request` when the worker needs to hand the request to another approver with context.
- Use `approval-management.reject_request` when the worker is ready to reject a request.
- Use `approval-management.cancel_request` when the worker needs to explicitly stop an approval flow that should no longer continue.

## Output

- Approval queue summary.
- Highest priority requests.
- Decision suggestions with rationale.
