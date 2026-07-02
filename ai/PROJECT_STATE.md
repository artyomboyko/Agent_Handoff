---
type: project_state
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Project State

## Current phase

Agent Handoff Standard 1.2 is implemented in the repository and the documentation now includes usage quick starts, issue labels, agent identity, work claim, and refactoring workflow.

## Architecture snapshot

This repository contains:

- the Agent Handoff Standard;
- root `AGENTS.md` entrypoint;
- compact `ai/` memory structure;
- GitHub Issue Forms;
- default Pull Request template;
- agent identity and work claim protocols;
- code cleanup and refactoring workflow entry point.

## Main subsystems

- Standard document: `AGENT_HANDOFF_STANDARD.md`
- Agent entrypoint: `AGENTS.md`
- Project memory: `ai/`
- Agent identity: `ai/AGENT_IDENTITY.md`
- Work claim protocol: `ai/WORK_CLAIM_PROTOCOL.md`
- Refactoring workflow: `ai/REFACTORING.md`
- Run handoffs: `ai/handoffs/`
- GitHub workflow templates: `.github/`
- Language docs: `docs/en/`, `docs/ru/`

## Implemented

- Versioned standard metadata.
- Source priority order.
- Agent identity and run IDs.
- Work claim protocol for Issues and Pull Requests.
- Handoff statuses and relevance values.
- Extended handoff index format.
- Parallel-work conflict protocol.
- Definition of Done with mandatory smoke tests.
- Issue labels and GitHub Issue Forms.
- Pull Request template with smoke-test checklist.
- YAML front matter rules for agent memory files.
- Security and private access value rules.
- Bilingual README links and usage quick starts.
- Refactoring workflow and agent instruction.

## In progress

Repository rename from `AI_Handoff` to `Agent_Handoff` must be completed in GitHub settings.

## Known risks

- This repository is documentation-first; smoke tests are mostly structural Markdown/YAML checks.
- GitHub Issue Forms must remain valid YAML.
- Universal labels may need to be created manually in GitHub if missing.

## Sensitive areas

- `AGENT_HANDOFF_STANDARD.md`
- `AGENTS.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/AGENT_IDENTITY.md`
- `ai/WORK_CLAIM_PROTOCOL.md`
- `ai/REFACTORING.md`
- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/pull_request_template.md`

## Current technical constraints

- Keep active `ai/` memory compact.
- Do not store bulky records, full discussions, generated artifacts, or private access values in `ai/`.
- Track actual refactoring tasks in GitHub Issues, not as a long backlog in `ai/REFACTORING.md`.

## Next likely milestones

1. Rename the GitHub repository to `Agent_Handoff` or `agent-handoff`.
2. Review all issue forms in GitHub UI.
3. Optionally add automated Markdown/YAML checks.
