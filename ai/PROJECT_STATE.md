---
type: project_state
version: 1
status: active
updated: 2026-07-02
project: AI_Handoff
---

# Project State

## Current phase

AI Handoff Standard 1.1 is implemented in the repository and the documentation now includes usage quick starts and a refactoring workflow.

## Architecture snapshot

This repository contains:

- the full AI Handoff Standard;
- root `AGENTS.md` entrypoint;
- compact `ai/` memory structure;
- GitHub Issue Forms;
- default Pull Request template;
- code cleanup and refactoring workflow entry point.

## Main subsystems

- Standard document: `AI_HANDOFF_STANDARD.md`
- Agent entrypoint: `AGENTS.md`
- Project memory: `ai/`
- Refactoring workflow: `ai/REFACTORING.md`
- Run handoffs: `ai/handoffs/`
- GitHub workflow templates: `.github/`
- Language docs: `docs/en/`, `docs/ru/`

## Implemented

- Versioned standard metadata.
- Source priority order.
- Handoff statuses and relevance values.
- Extended handoff index format.
- Parallel-work conflict protocol.
- Definition of Done with mandatory smoke tests.
- Increased size guidance.
- GitHub Issue Forms for bugs, standard changes, and refactoring.
- Pull Request template with smoke-test checklist.
- YAML front matter rules for AI memory files.
- Security and private access value rules.
- Bilingual README links and usage quick starts.
- Refactoring workflow and agent instruction.

## In progress

No active standard migration task.

## Known risks

- This repository is documentation-first; smoke tests are mostly structural Markdown/YAML checks.
- GitHub Issue Forms must remain valid YAML.
- The `refactoring` label may need to be created manually if GitHub does not create it from the issue form.

## Sensitive areas

- `AI_HANDOFF_STANDARD.md`
- `AGENTS.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/REFACTORING.md`
- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/pull_request_template.md`

## Current technical constraints

- Keep active `ai/` memory compact.
- Do not store bulky records, full discussions, generated artifacts, or private access values in `ai/`.
- Track actual refactoring tasks in GitHub Issues, not as a long backlog in `ai/REFACTORING.md`.

## Next likely milestones

1. Review the refactoring issue form in GitHub UI.
2. Optionally add automated Markdown/YAML checks.
3. Optionally tag the first stable release.
