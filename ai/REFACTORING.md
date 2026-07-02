---
type: refactoring_protocol
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Refactoring Workflow

This file is a compact entry point for code cleanup, code decomposition, renaming, and internal restructuring work.

Track concrete tasks in GitHub Issues. Keep this file as protocol, not as a long backlog.

## Use this workflow for

- splitting large files into smaller modules;
- removing unused or obsolete code;
- simplifying duplicated logic;
- renaming confusing internal names;
- moving responsibilities to clearer modules;
- reducing coupling between subsystems.

## Do not use this workflow for

- product features;
- research notes;
- ordinary bug reports;
- long implementation logs;
- full diffs or bulky command output.

## Issue fields

A code cleanup Issue should include:

- code area;
- current problem;
- target state;
- non-goals;
- risk;
- required checks;
- related files or PRs.

## Agent instruction

Perform the code cleanup task described in the related GitHub Issue.

Before editing, read `AGENTS.md`, `ai/README.md`, `ai/HANDOFF_PROTOCOL.md`, `ai/PROJECT_STATE.md`, `ai/DECISIONS.md`, `ai/REFACTORING.md`, the related Issue or PR, current branch, recent commits, and active handoffs.

Keep external behavior unchanged unless the Issue explicitly allows it. Prefer small reviewable steps. Preserve public APIs and compatibility boundaries unless the Issue says otherwise. Do not mix unrelated product features with cleanup work. Keep `ai/` compact.

Before finishing, run required checks, describe what changed and what was tested, list risks, and add a short handoff only when it helps the next agent.
