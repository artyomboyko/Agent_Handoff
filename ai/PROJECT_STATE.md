---
type: project_state
version: 1
status: active
updated: 2026-07-24
project: Agent_Handoff
---

# Project State

## Current phase

Agent Handoff Standard 1.4 is the active standard.

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
- Security and evidence may block or expand scope only for verified High or Critical current-scope risks or exactly cited mandatory requirements.
- Suspected High or Critical risks permit only short, time-boxed investigation until confirmed.
- Low, Medium, unrated, and unverified risks remain non-blocking.
- Early smallest useful end-to-end scenario for MVPs, prototypes, and runtime spikes.
- Non-binding 10–15% security-and-evidence planning heuristic.

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
- `docs/releases/v1.4.md`

## Active decisions

- Container layout is selected by the user, not inferred by an agent.
- The hybrid layout may be recommended but cannot be selected automatically.
- Existing container infrastructure cannot be migrated without explicit approval.
- Position-dependent GUI tests stay outside the routine automated test suite.
- Automated GUI tests use stable semantic selectors.
- Blocking or scope-expanding security and evidence work requires a verified High or Critical current-scope risk or an exactly cited mandatory requirement.
- Existing security baselines stay intact unless the owner explicitly approves a change.
- Low, Medium, unrated, unverified, and otherwise unsupported hardening remains non-blocking and does not delay the smallest useful vertical slice.

## Current publication

- Standard version: `1.4`
- Status: active
- Publication date: 2026-07-24
- Issue: #14
- Pull Request: #15

## Next

1. Keep repository checks and public documentation synchronized with future standard changes.
2. Collect feedback from projects adopting the proportional-security and containerization decision rules.
3. Prepare a future version only through a focused Issue, branch, Pull Request, checks, and release handoff.
