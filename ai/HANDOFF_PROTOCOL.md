---
type: handoff_protocol
version: 1
status: active
updated: 2026-07-02
project: AI_Handoff
---

# Handoff Protocol

## Start

Read `AGENTS.md`, `AI_HANDOFF_STANDARD.md`, `ai/README.md`, `ai/PROJECT_STATE.md`, `ai/DECISIONS.md`, the related Issue or PR, current branch, recent commits, and `ai/handoffs/INDEX.md`.

If the task is code cleanup, file decomposition, renaming, dead-code removal, or internal restructuring, also read `ai/REFACTORING.md` before editing.

## Scope

One meaningful work item should have one Issue, one branch, one PR, and one clear scope.

Open a Draft PR early.

For meaningful refactoring work, use a GitHub Issue with the `refactoring` label and keep task details in GitHub, not as a long backlog in `ai/REFACTORING.md`.

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
- [ ] Branch contains only intended changes.
- [ ] Smoke tests were run, or reason is documented.
- [ ] PR description is updated.
- [ ] Risks are listed.
- [ ] Handoff file is created for meaningful work.
- [ ] `ai/handoffs/INDEX.md` is updated when needed.
- [ ] `ai/PROJECT_STATE.md` is updated only if stable state changed.
- [ ] `ai/DECISIONS.md` is updated only if a durable architecture record was made.

## Parallel work

Before editing high-risk files, check open PRs, related Issues, recent commits, and active handoffs.

If overlap exists, coordinate in the related Issue or PR before continuing.
