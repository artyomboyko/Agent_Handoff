---
type: github_workflow
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Coordinated GitHub Flow

Agent Handoff uses Coordinated GitHub Flow for medium repositories where humans, autonomous agents, and human-supervised agents may work in parallel.

This is a lightweight GitHub Flow with issue-driven planning, visible ownership, short-lived branches, early Draft PRs, checks, and compact handoffs.

## Roles

- Maintainer or coordinator — prioritizes, assigns, pauses, splits, or supersedes work.
- Human contributor — implements or reviews work directly.
- Autonomous agent — works from an Issue with visible claim and handoff.
- Human-supervised agent — works under a named human coordinator.
- Reviewer — reviews PR scope, risks, checks, and implementation.

## Work unit

One meaningful work item should have:

- one GitHub Issue;
- one clear scope;
- one short-lived branch;
- one Pull Request;
- one visible owner at a time.

## Status labels

Recommended workflow labels:

- `needs-triage`
- `ready`
- `in-progress`
- `blocked`
- `in-review`
- `changes-requested`
- `ready-to-merge`

Closed Issue or merged PR is the normal `done` state.

## Branch naming

Use branch names without `/` to reduce ambiguity in automation, shells, URLs, and tools.

Recommended format:

```text
<type>-issue-<number>-<short-slug>
```

Examples:

```text
work-issue-14-agent-identity
fix-issue-21-broken-template
docs-issue-33-readme-quickstart
research-issue-40-ci-options
```

## Workflow

1. Triage or create an Issue.
2. Mark it `ready` only when scope and acceptance criteria are clear.
3. Choose agent identity when an agent is involved.
4. Claim work in the Issue before editing.
5. Create a short-lived branch without `/` in the name.
6. Open a Draft PR early.
7. Keep discussion, blockers, and review in Issue or PR.
8. Run required checks and smoke tests.
9. Move to review only when scope is complete enough.
10. Merge only after checks, review, and risks are acceptable.
11. Delete the branch after merge.
12. Add a handoff when work is completed, paused, blocked, or transferred.

## Human coordination

A human coordinator may reassign, pause, split, or supersede agent work.

Agents must not overwrite or ignore human decisions written in Issue or PR comments.

If the work is human-supervised, the Work Claim should include:

```text
Coordinator: @username
Supervision: autonomous | human-supervised | human-driven
```
