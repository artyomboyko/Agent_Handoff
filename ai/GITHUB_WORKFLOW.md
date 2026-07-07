---
type: github_workflow
version: 1
status: active
updated: 2026-07-07
project: Agent_Handoff
---

# Coordinated GitHub Flow

Agent Handoff uses Coordinated GitHub Flow for medium repositories.

## Work unit

One work item should have one Issue, one scope, one short-lived branch, one Pull Request, one visible owner, and required result reporting.

## Status labels

- `needs-triage`
- `ready`
- `in-progress`
- `blocked`
- `in-review`
- `changes-requested`
- `ready-to-merge`

Closed Issue or merged PR is the normal `done` state.

## Branch naming

Use meaningful branch names without `/`, Issue numbers, or random identifiers by default.

Issue linkage belongs in the Work Claim comment, PR description, GitHub links, and handoff metadata.

## Result reports

Every meaningful Issue must have a result comment.

Large or multi-stage Issues use stage result comments after stable stages.

Small Issues use one final result comment.

Use `ai/TASK_REPORT_PROTOCOL.md`.

## Workflow

1. Create or select an Issue.
2. Mark it `ready` when scope is clear.
3. Choose agent identity when an agent is involved.
4. Claim work before editing.
5. Create a short-lived branch.
6. Open a Draft PR early.
7. Link the PR to the Issue.
8. Keep discussion and result reports in Issue or PR.
9. Run checks and smoke tests.
10. Finish only after checks, review, and result report.
11. Add a handoff when needed.
