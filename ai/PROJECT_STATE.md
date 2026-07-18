---
type: project_state
version: 1
status: active
updated: 2026-07-18
project: Agent_Handoff
---

# Project State

## Current phase

Agent Handoff Standard 1.3 is the active published standard.

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
- GUI testing rule against position-dependent automated tests.
- Containerization protocol with explicit user-controlled layout selection.
- Mandatory separate containerization question for new-repository initialization and existing-repository adoption.
- Supported no-containerization, colocated, centralized, hybrid, modular monorepo, separate deployment repository, and preserved custom layouts.
- Container migration, Compose path, verification, project-memory, and handoff requirements.

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
- `docs/releases/v1.3.md`

## Active decisions

- Container layout is selected by the user, not inferred by an agent.
- The hybrid layout may be recommended but cannot be selected automatically.
- Existing container infrastructure cannot be migrated without explicit approval.
- Position-dependent GUI tests stay outside the routine automated test suite.
- Automated GUI tests use stable semantic selectors.

## Current publication

- Standard version: `1.3`
- Status: active
- Publication date: 2026-07-18
- Issue: #12
- Pull Request: #13

## Next

1. Keep repository checks and public documentation synchronized with future standard changes.
2. Collect feedback from projects adopting the containerization decision gate.
3. Prepare a future version only through a focused Issue, branch, Pull Request, checks, and release handoff.
