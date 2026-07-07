---
type: task_report_protocol
version: 1
status: active
updated: 2026-07-07
project: Agent_Handoff
---

# Task Report Protocol

This file defines required result comments for GitHub Issues and Pull Requests.

Task reports are written in the related Issue or PR so humans and agents can follow progress without reading chat history.

## Rule

Every meaningful Issue needs a result comment.

Large or multi-stage Issues need one result comment after each stable stage.

Small Issues may have one final result comment.

## Stage work

For each stage, an agent records findings, makes a small focused change, runs targeted tests or documents why they were not run, updates docs when relevant, continues after a stable layer, and leaves a stage result comment.

## Stage result comment

```md
## Agent Handoff Stage Result

Stage: <number or name>
Agent ID: <agent_id>
Run ID: <run_id>
Status: completed | blocked | partial

Findings:
- <what was found>

Changed:
- <small focused change>

Not changed:
- <explicit non-changes or preserved behavior>

Tests:
- <targeted tests and result, or reason not run>

Docs:
- <docs updated or not needed>

Commit:
- <commit sha or not committed yet>

Risks:
- <remaining risks>

Next:
- <next stage or handoff target>
```

## Final result comment

```md
## Agent Handoff Final Result

Agent ID: <agent_id>
Run ID: <run_id>
Status: completed | blocked | partial

Summary:
- <what was done>

Changed:
- <files, modules, docs, or behavior changed>

Not changed:
- <explicit non-changes or preserved behavior>

Tests:
- <checks and smoke tests, or reason not run>

Docs:
- <docs updated or not needed>

Commits:
- <commit shas>

Risks:
- <remaining risks>

Follow-up:
- <next work, if any>
```

## Stability gate

A multi-stage Issue moves to the next stage after the current stage has a result comment and the stage checks are stable or the blocker is documented.
