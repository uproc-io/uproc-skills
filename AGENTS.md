# AGENTS.md

This file is the project-level guide for work inside `skills/`.

Scope
- `skills/` stores end-user skills written in Markdown.
- Follow this file first when creating, editing, or reviewing files under `skills/`.
- If a specific skill directory later adds its own `AGENTS.md`, that local guide overrides this one for that subtree.

Purpose
- Keep skills easy to discover, read, and maintain.
- Prefer small, explicit Markdown changes over inventing extra tooling.
- Treat each skill as user-facing documentation and instructions, not as application code.

Structure
- One skill per directory.
- Skill directories should use kebab-case names.
- The main entry file for a skill should be `SKILL.md`.
- Supporting assets should live next to the skill, using descriptive names.
- `README.md` documents the folder-level conventions and should stay in sync with the current structure.

Authoring rules
- Write clear, direct instructions.
- Keep examples realistic and minimal.
- Prefer ASCII unless the file already uses non-ASCII content or the language requires it.
- Do not include secrets, tokens, private URLs, or environment-specific credentials.
- Avoid repo-internal assumptions unless the skill is explicitly meant for this repository.
- Each `SKILL.md` should include an `Implementation via Uproc MCP` section that names the relevant MCP tools, semantic shortcuts, and known capability limits.

## Tracking policy (mandatory)

### TODO.md
- Before starting work, read `TODO.md` in the skills root.
- Use `TODO.md` to detect pending work, partially applied requirements, blockers, and follow-ups before making changes.
- When work leaves unfinished scope or reveals new follow-ups, update `TODO.md` in the same change set.
- When completing pending items, move them to `DONE.md` and remove from `TODO.md`.
- **Date grouping**: items within each section must be grouped under `## YYYY-MM-DD` headers.
- Treat `TODO.md` as the operational handoff and pending-work tracker for skills agent workflows.

### DONE.md
- Maintain `DONE.md` as the permanent record of completed skills work.
- When closing a TODO, move the entry to `DONE.md` under a `## YYYY-MM-DD` header.

### REVIEW.md
- Maintain `REVIEW.md` as the canonical log for skills items needing human review.
- A review item is any intentionally omitted or postponed scope decision, technical debt, or skill-content gap.
- Every review entry must include: date, area, item, reason, impact, and follow-up status.

When changing this folder
- Update `skills/README.md` when adding, renaming, or removing skills.
- Update `skills/USER_MANUAL.md` whenever any `SKILL.md` changes so the catalog summary and expected outcomes stay aligned with the current skill behavior.
- If conventions change, update this file in the same change set.
- Keep folder references aligned with the repo root `AGENTS.md`.
- When backend capabilities change, update the MCP implementation section of affected skills so the documented tools stay accurate.

Validation
- Check that referenced files and directories actually exist.
- Check that Markdown headings and fenced code blocks render cleanly.
- For new skills, verify the expected entry file is `SKILL.md` and is placed in the correct directory.
