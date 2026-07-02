---
type: handoff_protocol
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Handoff Protocol

## Start

Read `AGENTS.md`, `AGENT_HANDOFF_STANDARD.md`, `ai/README.md`, `ai/GITHUB_WORKFLOW.md`, `ai/AGENT_IDENTITY.md`, `ai/WORK_CLAIM_PROTOCOL.md`, `ai/PROJECT_STATE.md`, `ai/DECISIONS.md`, the related Issue or PR, current branch, recent commits, and `ai/handoffs/INDEX.md`.

Choose `agent_name`, `agent_id`, and `run_id` before taking work.

If the task is code cleanup, file decomposition, renaming, dead-code removal, or internal restructuring, also read `ai/REFACTORING.md` before editing.

## Work claim

Before editing, leave a work claim comment using `ai/WORK_CLAIM_PROTOCOL.md`.

The claim comment must include agent name, agent id, run id, issue, branch, draft PR, scope, and current status.

Use workflow labels from `ai/GITHUB_WORKFLOW.md` when available.

## Scope

One meaningful work item should have one Issue, one branch, one PR, and one clear scope.

Use branch names without `/`; example: `work-agent-identity-a91f`.

Open a Draft PR early.

For meaningful refactoring work, use a GitHub Issue with the `refactoring` label and keep task details in GitHub.

## Smoke tests

Smoke tests are mandatory before marking work ready or setting a handoff to `completed`.

For this repository:

1. Required files exist.
2. Markdown links point to intended files.
3. Issue Forms are valid YAML.
4. PR template includes the smoke-test checklist.
5. Handoff index is updated when a handoff file is added.

If smoke tests cannot be run, document reason, risk, and next step.

## Done checklist

- [ ] Related Issue or PR is linked.
- [ ] Work claim comment exists for agent work.
- [ ] Agent ID and run ID are repeated in PR or handoff when relevant.
- [ ] Branch contains only intended changes.
- [ ] Smoke tests were run, or reason is documented.
- [ ] PR description is updated.
- [ ] Risks are listed.
- [ ] Handoff file is created for meaningful work.
- [ ] `ai/handoffs/INDEX.md` is updated when needed.
- [ ] `ai/PROJECT_STATE.md` is updated only if stable state changed.
- [ ] `ai/DECISIONS.md` is updated only if a durable architecture record was made.

## Parallel work

Before editing high-risk files, check open PRs, related Issues, recent commits, active handoffs, and recent work claim comments.

If overlap exists, coordinate in the related Issue or PR before continuing.
