---
type: agent_identity_protocol
version: 1
status: active
updated: 2026-07-02
project: AI_Handoff
---

# Agent Identity Protocol

This file defines how AI agents name themselves during parallel work.

Current work ownership lives in GitHub Issues, Pull Requests, labels, branches, and handoffs.

## Fields

Each agent run should use:

- `agent_name` — human-readable name chosen by the agent.
- `agent_id` — short slug for this repository context.
- `run_id` — unique id for the current session.

Example:

```text
Agent: North Fox
Agent ID: north-fox-7c2a
Run ID: 20260702-issue-14-a91f
```

## Agent ID

Recommended format:

```text
<two-words-slug>-<4-hex>
```

Examples:

```text
north-fox-7c2a
silver-owl-b91d
quiet-river-03af
```

## Run ID

Recommended format:

```text
YYYYMMDD-issue-<number>-<4-hex>
```

If there is no issue yet:

```text
YYYYMMDD-no-issue-<4-hex>
```
