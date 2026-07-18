---
type: project_state
version: 1
status: active
updated: 2026-07-18
project: Agent_Handoff
---

# Project State

## Current phase

Agent Handoff Standard 1.3 is in draft development on branch `standard-1.3`.

The repository is maintained as an English-only canonical version.

## Implemented

- Landing README and GitHub Pages site.
- English canonical standard document.
- GitHub Issue Forms and Pull Request template.
- Coordinated GitHub Flow.
- Agent identity protocol.
- Work claim protocol.
- Task report protocol for stage and final result comments.
- Refactoring workflow.
- FAQ and examples.
- GitHub Actions checks workflow.
- Citation metadata.
- Standard 1.3 draft GUI testing rule against position-dependent automated tests.
- Standard 1.3 draft containerization protocol with explicit user-controlled layout selection.
- Mandatory separate containerization question for new-repository initialization and existing-repository adoption.

## Main files

- `AGENT_HANDOFF_STANDARD.md`
- `AGENTS.md`
- `ai/README.md`
- `ai/GITHUB_WORKFLOW.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/AGENT_IDENTITY.md`
- `ai/WORK_CLAIM_PROTOCOL.md`
- `ai/TASK_REPORT_PROTOCOL.md`
- `ai/REFACTORING.md`
- `ai/CONTAINERIZATION.md`
- `.github/pull_request_template.md`
- `scripts/check_agent_handoff.py`

## Current draft decisions

- Container layout is selected by the user, not inferred by an agent.
- Supported approaches include no containerization, colocated, centralized, hybrid, modular monorepo, separate deployment repository, and preserved custom layouts.
- The hybrid layout may be recommended to the user but cannot be selected automatically.
- Existing container infrastructure cannot be migrated without explicit approval.

## Next

1. Review Standard 1.3 wording and examples.
2. Decide whether repository checks should require or validate the new containerization protocol.
3. Add a focused Issue and Draft Pull Request before publication.
4. Complete a release handoff and publish `v1.3` only after review and green checks.
