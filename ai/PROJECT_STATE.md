---
type: project_state
version: 1
status: active
updated: 2026-06-29
project: AI_Handoff
---

# Project State

## Current phase

Standard repository setup for AI Handoff Standard 1.1.

## Architecture snapshot

This repository contains:

- the full AI Handoff Standard;
- root `AGENTS.md` entrypoint;
- compact `ai/` memory structure;
- GitHub Issue Forms;
- default Pull Request template.

## Main subsystems

- Standard document: `AI_HANDOFF_STANDARD.md`
- Agent entrypoint: `AGENTS.md`
- Project memory: `ai/`
- Run handoffs: `ai/handoffs/`
- GitHub workflow templates: `.github/`

## Implemented

- Versioned standard metadata.
- Source priority order.
- Handoff statuses and relevance values.
- Extended handoff index format.
- Parallel-work conflict protocol.
- Definition of Done with mandatory smoke tests.
- Increased size guidance.
- GitHub Issue Forms for bugs and standard changes.
- Pull Request template with smoke-test checklist.
- YAML front matter rules for AI memory files.
- Security and private access value rules.

## In progress

Initial PR for Standard 1.1.

## Known risks

- This repository is documentation-first; smoke tests are mostly structural Markdown/YAML checks.
- GitHub Issue Forms must remain valid YAML.

## Sensitive areas

- `AI_HANDOFF_STANDARD.md`
- `AGENTS.md`
- `ai/HANDOFF_PROTOCOL.md`
- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/pull_request_template.md`

## Current technical constraints

- Keep active `ai/` memory compact.
- Do not store bulky records, full discussions, generated artifacts, or private access values in `ai/`.

## Next likely milestones

1. Review and merge Standard 1.1.
2. Optionally add automated Markdown/YAML checks.
3. Optionally tag the first stable release.
