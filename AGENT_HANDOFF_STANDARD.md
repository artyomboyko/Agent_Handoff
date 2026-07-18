---
standard: Agent Handoff
version: "1.3"
status: active
updated: 2026-07-18
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

For projects that use or plan Docker or Docker Compose, `ai/CONTAINERIZATION.md` is also required.

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
11. `ai/CONTAINERIZATION.md` when Docker or Compose is used, planned, or being discussed
12. related GitHub Issue or Pull Request
13. relevant handoffs through `ai/handoffs/INDEX.md`

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

## Repository initialization and adoption decision gate

When Agent Handoff is initialized in a new repository or added to an existing repository, the agent MUST inspect the repository and ask the user a separate, explicit question about containerization before changing any Docker or Compose structure.

The question must confirm:

- whether Docker or Docker Compose is used now or planned;
- which container file layout the user wants;
- for an existing repository, whether the current layout must be preserved or may be migrated;
- whether production deployment configuration belongs in the same repository or a separate deployment repository.

The agent MUST NOT infer this decision from existing files, an empty repository, general best practices, or the recommended default.

Until the user answers, the agent must not create, move, rename, delete, or consolidate Dockerfiles, Compose files, build contexts, ignore files, container scripts, environment-file references, or container configuration.

For an unanswered new-repository decision, create no container infrastructure. For an unanswered existing-repository decision, preserve the current layout.

## Containerized project organization

Agent Handoff supports these approaches:

1. no repository-managed containerization;
2. Dockerfiles colocated with service code and primary Compose files at the root;
3. centralized Docker and Compose infrastructure under `docker/`;
4. a hybrid layout with root Compose files, service-local Dockerfiles, and shared infrastructure under `docker/`;
5. a modular monorepo layout with service-level container modules and explicit top-level orchestration;
6. a separate deployment repository for production orchestration;
7. preservation of an established or custom layout.

The hybrid layout is the recommended option to present for many small and medium multi-service repositories, but it must never be selected without explicit user confirmation.

The selected approach, canonical commands, build contexts, Compose file order, environment handling, and migration decision must be documented. Use `ai/CONTAINERIZATION.md` for the complete decision gate, layouts, migration rules, and verification requirements.

## GUI testing

Do not create brittle automated GUI tests that locate, interact with, or validate interface elements through absolute coordinates, screen position, pixel offsets, or incidental layout order.

Position-dependent GUI checks must be performed manually or as supervised exploratory checks with Codex. They must not be committed as part of the routine automated test suite.

Automated GUI tests should use stable semantic selectors such as roles, accessible names, labels, documented component identifiers, or dedicated test IDs.

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
- `ai/handoffs/INDEX.md` is updated when needed;
- mandatory initialization or adoption questions were answered when relevant;
- container layout and canonical commands are recorded when Docker or Compose is used;
- changed Compose configuration was rendered and checked, or the reason and risk are documented.

## Final rule

Code changes together with compact state for the next agent.

Large data stays in GitHub and Git.

`ai/` stores only what helps future agents continue development quickly and safely.
