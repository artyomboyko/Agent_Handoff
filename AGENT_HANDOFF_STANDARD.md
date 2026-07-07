---
standard: Agent Handoff
version: "1.2"
status: active
updated: 2026-07-04
---

# Agent Handoff Standard

Agent Handoff is a compact standard for passing development state between humans, AI agents, and human-supervised agents through GitHub, Git, and small repository-tracked memory files.

## Core model

```text
GitHub manages work: Issues, Pull Requests, reviews, checks, labels, comments, and current ownership.
Git stores code: branches, commits, diffs, tags, and history.
ai/ stores compact durable memory and agent protocols.
ai/handoffs/ stores short snapshots of agent runs.
```

## Language model

The standard can be applied to English and Russian repositories.

For an English repository, agents should work in English.

For a Russian repository, agents should work in Russian.

English and Russian documentation should keep matching structure and meaning.

Issue Forms and Pull Request templates should support language selection or bilingual field names.

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
docs/ru/
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

## Agent identity

Each agent run should use `agent_name`, `agent_id`, and `run_id`.

Recommended formats:

```text
agent_id: <two-words-slug>-<4-hex>
run_id: YYYYMMDD-issue-<number>-<4-hex>
```

## Work claim

Before changing code or docs for a meaningful task, claim the work in GitHub.

Use this comment in the related Issue and repeat identity values in the Draft PR:

```md
## Agent Handoff Work Claim

Agent: <agent_name>
Agent ID: <agent_id>
Run ID: <run_id>
Coordinator: <username or none>
Supervision: autonomous | human-supervised | human-driven
Started: YYYY-MM-DD HH:MM UTC
Issue: #<issue-number>
Branch: <branch-name>
Draft PR: #<pr-number or TBD>
Scope: <short scope>
Status: in-progress
Next update: <time or condition>
```

For updates:

```md
## Agent Handoff Work Update

Agent ID: <agent_id>
Run ID: <run_id>
Status: in-progress | blocked | completed
Changed:
Tested:
Risk:
Next:
```

If an Issue or PR already has a recent work claim, coordinate in the related Issue or PR before continuing.

## Task result reports

Task result comments are mandatory for meaningful Issues.

Large or multi-stage Issues must have a stage result comment after each stable stage.

Small single-stage Issues must have one final result comment before the work is marked done.

For each large-task stage, an agent must record findings, make a small focused change, run targeted tests or explain why they were not run, update AI or project docs when relevant, make a bilingual commit when the repository is bilingual, and continue only after the layer is stable.

Use `ai/TASK_REPORT_PROTOCOL.md` for the required comment templates.

## Branch naming

Use meaningful branch names without `/`, Issue numbers, or random identifiers by default.

Recommended formats:

```text
<type>-<topic>
<type>-<scope>-<topic>
```

Examples:

```text
workflow-branch-naming
protocol-work-claim
docs-readme-quickstart
refactor-handoff-index
research-github-flow
fix-issue-template-yaml
```

Issue linkage belongs in the Work Claim comment, PR description, GitHub links, and handoff metadata, not in the branch name.

## Labels

Type labels: `bug`, `enhancement`, `refactoring`, `research`, `backlog`, `testing`, `docs`.

Status labels: `needs-triage`, `ready`, `in-progress`, `blocked`, `in-review`, `changes-requested`, `ready-to-merge`.

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
