---
type: issue_claim_protocol
version: 1
status: active
updated: 2026-07-02
project: AI_Handoff
---

# Issue Claim Protocol

This file defines how an AI agent marks a GitHub Issue as being worked on.

Current ownership is written in the Issue itself. The `ai/` folder only stores the protocol.

## Before starting work

An agent must:

1. read the Issue and recent comments;
2. check linked Pull Requests;
3. check active handoffs;
4. choose `agent_name`, `agent_id`, and `run_id` using `ai/AGENT_IDENTITY.md`;
5. leave an Issue claim comment;
6. use the `in-progress` label when available;
7. create a branch and Draft PR as early as practical.

## Claim comment

```md
## AI Handoff Claim

Agent: <agent_name>
Agent ID: <agent_id>
Run ID: <run_id>
Started: YYYY-MM-DD HH:MM UTC
Branch: <branch-name>
Scope: <short scope>
Status: in-progress
Next update: <time or condition>
```

## Progress comments

For meaningful work, the agent should add short updates in the Issue or PR:

```md
## AI Handoff Update

Agent ID: <agent_id>
Run ID: <run_id>
Status: in-progress | blocked | completed
Changed:
Tested:
Risk:
Next:
```

## Completion comment

When work is finished, the Issue or linked PR should explain:

- what changed;
- what was tested;
- what risks remain;
- which PR, commits, or handoffs are related.

## Conflict rule

If an Issue already has a recent claim comment and no completion or release note, another agent must not silently take it over.

The second agent should comment, ask for status, narrow scope, or create a follow-up Issue.
