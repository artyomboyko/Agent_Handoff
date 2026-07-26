---
type: project_state
version: 1
status: active
updated: 2026-07-26
project: Agent_Handoff
---

# Project State

## Current phase

Agent Handoff Standard 1.5 is prepared as the active release candidate.

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
- Required primary outcome, smallest acceptance proof, and execution envelope for meaningful work.
- Supporting work remains minimum sufficient and subordinate to the primary outcome.
- Localized reversible supporting-work fixes and bounded post-fix verification remain inside the current authorization and execution envelope.
- Outcome-based stage and handoff boundaries.
- `progress-stalled` recovery after two consecutive supporting-only updates without outcome progress.
- Structural checks for the outcome fields without automated semantic progress scoring.

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
- `docs/releases/v1.5.md`

## Active decisions

- Container layout is selected by the user, not inferred by an agent.
- The hybrid layout may be recommended but cannot be selected automatically.
- Existing container infrastructure cannot be migrated without explicit approval.
- Position-dependent GUI tests stay outside the routine automated test suite.
- Automated GUI tests use stable semantic selectors.
- Blocking or scope-expanding security and evidence work requires a verified High or Critical current-scope risk or an exactly cited mandatory requirement.
- Existing security baselines stay intact unless the owner explicitly approves a change.
- Low, Medium, unrated, unverified, and otherwise unsupported hardening remains non-blocking and does not delay the smallest useful vertical slice.
- Meaningful work records a primary outcome, smallest acceptance proof, and execution envelope before implementation.
- Supporting-tool failures do not create separate stages, handoffs, completion targets, or approval gates unless an explicit outcome or approval boundary is crossed.
- One bounded post-fix verification rerun is permitted after each relevant fix unless the execution envelope is stricter.
- Two consecutive supporting-only updates without outcome progress trigger `progress-stalled` and shortest-path replanning.

## Current publication

- Standard version: `1.5`
- Status: release candidate
- Publication date: 2026-07-26
- Issue: #16
- Pull Request: TBD

## Next

1. Complete owner review and GitHub Actions for the Standard 1.5 Draft Pull Request.
2. Merge only after the owner accepts the outcome-oriented execution and approval-boundary semantics.
3. Create tag `v1.5` and the GitHub Release from the verified merge commit only after merge.
