---
type: handoff_protocol
version: 1
status: active
updated: 2026-06-29
project: AI_Handoff
---

# Handoff Protocol

## Start

Read `AGENTS.md`, `AI_HANDOFF_STANDARD.md`, `ai/README.md`, `ai/PROJECT_STATE.md`, `ai/DECISIONS.md`, the related Issue or PR, current branch, recent commits, and `ai/handoffs/INDEX.md`.

## Scope

One meaningful work item should have one Issue, one branch, one PR, and one clear scope.

Open a Draft PR early.

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
