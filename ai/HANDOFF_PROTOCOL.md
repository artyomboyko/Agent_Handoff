---
type: handoff_protocol
version: 1
status: active
updated: 2026-07-18
project: Agent_Handoff
---

# Handoff Protocol

## Start

Read the required Agent Handoff files, the related Issue or PR, current branch, recent commits, and relevant handoffs.

Read `ai/CONTAINERIZATION.md` when Docker or Docker Compose is used, planned, present in the repository, or part of the requested work.

Choose `agent_name`, `agent_id`, and `run_id` before taking work.

## Work claim

Leave a work claim comment with `ai/WORK_CLAIM_PROTOCOL.md` before changing code or docs.

## Task reports

Meaningful Issues require result comments.

Large or multi-stage Issues use stage result comments after stable stages.

Small Issues use one final result comment before completion.

Use `ai/TASK_REPORT_PROTOCOL.md`.

## Scope

One meaningful work item should have one Issue, one branch, one PR, and one clear scope.

Use meaningful branch names without `/`, Issue numbers, or random identifiers by default.

Open a Draft PR early.

## Initialization and adoption decision gate

When initializing Agent Handoff in a new repository or adding it to an existing repository, ask the user a separate, explicit question about Docker and Compose organization.

The user must confirm:

- whether containerization is used or planned;
- which supported layout should be used;
- whether an existing layout must be preserved or may be migrated;
- whether production deployment configuration belongs in the same repository or a separate repository.

Do not infer the answer from repository contents or choose the recommended layout automatically.

Until the user answers, do not create, move, rename, delete, or consolidate Dockerfiles, Compose files, build contexts, ignore files, container scripts, environment-file references, or container configuration.

For a new repository, leave containerization unresolved and create no container infrastructure. For an existing repository, preserve the current layout.

## Docker and Compose

Before changing container infrastructure:

1. identify the user-confirmed layout in `ai/PROJECT_STATE.md` or the related Issue;
2. inspect the primary Compose file, project directory, override order, build contexts, Dockerfile paths, ignore files, environment references, scripts, and CI commands;
3. check whether production orchestration is stored in this repository or elsewhere;
4. keep layout migration separate from unrelated application refactoring;
5. validate the effective Compose model with `docker compose config` when Compose is used;
6. build and start the affected scope, or document why this was not possible;
7. record changed commands, paths, images, services, ports, volumes, networks, health checks, environment variables, risks, and compatibility notes.

Migration between container layouts requires explicit user approval even when another approach appears cleaner.

## GUI testing

Do not commit automated GUI tests that depend on absolute coordinates, screen position, pixel offsets, or incidental layout order.

Perform position-dependent GUI checks manually or as supervised exploratory checks with Codex.

Automated GUI tests should use stable semantic selectors.

## Smoke tests

Run smoke tests before marking work ready or setting a handoff to `completed`.

Current checks cover required files, YAML, PR template checklist, social preview size, and English-only active files.

For container changes, also run the applicable Compose rendering, image build, service startup, health, and focused smoke checks defined in `ai/CONTAINERIZATION.md`.

## Done checklist

- Related Issue or PR is linked.
- Work claim comment exists.
- Required stage or final result comment exists.
- Branch contains only intended changes.
- Smoke tests were run or reason is documented.
- PR description is updated.
- Risks are listed.
- Handoff file is created when needed.
- `ai/handoffs/INDEX.md` is updated when needed.
- Mandatory initialization or adoption questions were answered when relevant.
- User-confirmed container layout is recorded when Docker or Compose is used.
- Container migration has explicit user approval when applicable.
