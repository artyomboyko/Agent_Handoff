---
type: work_claim_protocol
version: 1
status: active
updated: 2026-07-07
project: Agent_Handoff
---

# Work Claim Protocol

This file defines current work ownership in GitHub Issues and Pull Requests.

## Before starting work

1. Read the Issue.
2. Check linked Pull Requests.
3. Check active handoffs.
4. Choose `agent_name`, `agent_id`, and `run_id`.
5. Leave a work claim comment.
6. Plan stage or final result reports using `ai/TASK_REPORT_PROTOCOL.md`.
7. Create a branch and Draft PR early.

## Claim comment

```md
## Agent Handoff Work Claim

Agent: <agent_name>
Agent ID: <agent_id>
Run ID: <run_id>
Coordinator: <coordinator>
Supervision: autonomous | human-supervised | human-driven
Started: YYYY-MM-DD HH:MM UTC
Issue: #<issue-number>
Branch: <branch-name>
Draft PR: #<pr-number or TBD>
Scope: <short scope>
Status: in-progress
Next update: <time or condition>
```

## Update comment

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

## Result comments

Every meaningful Issue must have result comments.

Large or multi-stage Issues use stage result comments after each stable stage.

Small Issues use one final result comment before completion.

Use `ai/TASK_REPORT_PROTOCOL.md` for templates.

## Done

When work is finished, write what changed, what was tested, remaining risks, related PR or handoff, and the required result comment.

If an Issue or PR already has a recent work claim, coordinate before continuing.
