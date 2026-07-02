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

One meaningful work item should have one GitHub Issue, one clear scope, one short-lived branch, one Pull Request, and one visible owner at a time.

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

Use branch names without `/` and without mandatory Issue numbers.

Recommended format:

```text
<type>-<short-slug>-<short-id>
```

Examples:

```text
work-agent-identity-a91f
fix-broken-template-7c2a
docs-readme-quickstart-b91d
research-ci-options-03af
```

The branch is not the source of truth for Issue linkage. Link the Issue in the Work Claim comment, PR description, and handoff metadata.

## Workflow

1. Triage or create an Issue.
2. Mark it `ready` only when scope and acceptance criteria are clear.
3. Choose agent identity when an agent is involved.
4. Claim work in the Issue before editing.
5. Create a short-lived branch.
6. Open a Draft PR early.
7. Link the PR to the Issue.
8. Keep discussion, blockers, and review in Issue or PR.
9. Run required checks and smoke tests.
10. Move to review only when scope is complete enough.
11. Merge only after checks, review, and risks are acceptable.
12. Delete the branch after merge.
13. Add a handoff when work is completed, paused, blocked, or transferred.

## Human coordination

A human coordinator may reassign, pause, split, or supersede agent work.

Agents must not overwrite or ignore human decisions written in Issue or PR comments.

If the work is human-supervised, the Work Claim should include:

```text
Coordinator: @username
Supervision: autonomous | human-supervised | human-driven
```
