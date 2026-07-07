---
type: handoff_protocol
version: 1
status: active
updated: 2026-07-07
project: Agent_Handoff
---

# Handoff Protocol

## Start

Read the required Agent Handoff files, the related Issue or PR, current branch, recent commits, and relevant handoffs.

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

## Smoke tests

Run smoke tests before marking work ready or setting a handoff to `completed`.

Current checks cover required files, YAML, PR template checklist, social preview size, and English-only active files.

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
