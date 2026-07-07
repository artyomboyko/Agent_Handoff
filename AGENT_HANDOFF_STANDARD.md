---
standard: Agent Handoff
version: "1.2"
status: active
updated: 2026-07-07
---

# Agent Handoff Standard

Agent Handoff is a compact standard for passing development state between humans, AI agents, and human-supervised agents through GitHub, Git, and small repository-tracked memory files.

This repository is maintained in English. Downstream projects may adapt the standard to another project language, but the canonical files in this repository stay English-only.

## Core model

```text
GitHub manages work: Issues, Pull Requests, reviews, checks, labels, comments, and current ownership.
Git stores code: branches, commits, diffs, tags, and history.
ai/ stores compact durable memory and agent protocols.
ai/handoffs/ stores short snapshots of agent runs.
```

## Required files

```text
AGENTS.md
AGENT_HANDOFF_STANDARD.md
ISSUE_LABELS.md
ISSUE_STATUS.md
ai/README.md
ai/PROJECT_STATE.md
ai/DECISIONS.md
ai/GITHUB_WORKFLOW.md
ai/HANDOFF_PROTOCOL.md
ai/AGENT_IDENTITY.md
ai/WORK_CLAIM_PROTOCOL.md
ai/TASK_REPORT_PROTOCOL.md
ai/REFACTORING.md
ai/handoffs/INDEX.md
.github/ISSUE_TEMPLATE/
.github/pull_request_template.md
docs/en/
```

## Start order

Before meaningful work, read:

1. `AGENTS.md`
2. `AGENT_HANDOFF_STANDARD.md`
3. `ai/README.md`
4. `ai/GITHUB_WORKFLOW.md`
5. `ai/HANDOFF_PROTOCOL.md`
6. `ai/AGENT_IDENTITY.md`
7. `ai/WORK_CLAIM_PROTOCOL.md`
8. `ai/TASK_REPORT_PROTOCOL.md`
9. `ai/PROJECT_STATE.md`
10. `ai/DECISIONS.md`
11. related GitHub Issue or Pull Request
12. relevant handoffs through `ai/handoffs/INDEX.md`

## Task result reports

Task result comments are mandatory for meaningful Issues.

Large or multi-stage Issues must have a stage result comment after each stable stage.

Small single-stage Issues must have one final result comment before the work is marked done.

Use `ai/TASK_REPORT_PROTOCOL.md` for the required comment templates.

## Workflow

1. Select or create a GitHub Issue.
2. Check existing work claims, linked PRs, active handoffs, and recent comments.
3. Choose agent identity.
4. Claim the work.
5. Define scope and stages when the task is large.
6. Create a meaningful short-lived branch.
7. Open a Draft PR early.
8. Write required stage or final result comments in the Issue or PR.
9. Commit changes.
10. Run checks and smoke tests.
11. Update PR description.
12. Leave a handoff when work is completed or interrupted.

## Definition of Done

- related Issue or PR is linked;
- work claim comment exists for agent work;
- agent id and run id are repeated in PR or handoff when relevant;
- required stage or final result comment exists;
- changes are committed;
- smoke tests were run or reason is documented;
- PR description is updated;
- risks are listed;
- handoff exists for meaningful work;
- `ai/handoffs/INDEX.md` is updated when needed.

## Final rule

Code changes together with compact state for the next agent.

Large data stays in GitHub and Git.

`ai/` stores only what helps future agents continue development quickly and safely.
