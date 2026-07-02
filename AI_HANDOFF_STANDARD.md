---
standard: AI Handoff
version: "1.2"
status: active
updated: 2026-07-02
---

# AI Handoff Standard

## 1. Purpose

AI Handoff is a compact standard for passing development state between AI coding agents through GitHub, Git, and small repository-tracked memory files.

Core formula:

```text
GitHub manages the work.
Git stores code and history.
ai/ stores compact durable project memory.
handoffs/ stores short snapshots of AI agent runs.
```

## 2. Sources of truth

GitHub is the primary workflow system. It stores Issues, Pull Requests, PR comments, labels, reviews, CI status, task discussions, and links between tasks, branches, agents, and PRs.

Git stores source code, commits, branches, diffs, tags, and history.

`ai/` stores compact project memory and workflow protocols. It does not replace GitHub or Git.

## 3. Source priority

If information conflicts:

1. Git working tree and current branch.
2. GitHub Pull Request.
3. GitHub Issue.
4. GitHub Issue or PR work claim comments.
5. `ai/PROJECT_STATE.md`.
6. `ai/DECISIONS.md`.
7. `ai/handoffs/*.md`.

A handoff can be stale. Code, PR state, and current GitHub discussion have higher priority.

## 4. Required repository structure

```text
AGENTS.md
AI_HANDOFF_STANDARD.md
ISSUE_LABELS.md
ai/
  README.md
  PROJECT_STATE.md
  DECISIONS.md
  HANDOFF_PROTOCOL.md
  AGENT_IDENTITY.md
  WORK_CLAIM_PROTOCOL.md
  REFACTORING.md
  handoffs/
    INDEX.md
    YYYY-MM-DD_issue-123_pr-45_run-abc123.md
  archive/
    README.md
.github/
  ISSUE_TEMPLATE/
    bug_report.yml
    standard_change.yml
    refactoring.yml
    research.yml
    backlog.yml
    testing.yml
    doc.yml
    config.yml
  pull_request_template.md
```

## 5. Start order

Before meaningful work, an agent should read:

1. `AGENTS.md`
2. `AI_HANDOFF_STANDARD.md`
3. `ai/README.md`
4. `ai/HANDOFF_PROTOCOL.md`
5. `ai/AGENT_IDENTITY.md`
6. `ai/WORK_CLAIM_PROTOCOL.md`
7. `ai/PROJECT_STATE.md`
8. `ai/DECISIONS.md`
9. related GitHub Issue or Pull Request
10. `ai/REFACTORING.md` when the task is cleanup or decomposition
11. `ai/handoffs/INDEX.md`
12. relevant handoff files only

The agent must not read every handoff file blindly.

## 6. Agent identity

Each AI agent run should use:

- `agent_name` — a human-readable name chosen by the agent;
- `agent_id` — a short stable slug for this repository context;
- `run_id` — a unique id for the current run or session.

Recommended example:

```text
Agent: North Fox
Agent ID: north-fox-7c2a
Run ID: 20260702-issue-14-a91f
```

Recommended `agent_id` format:

```text
<two-words-slug>-<4-hex>
```

Recommended `run_id` format:

```text
YYYYMMDD-issue-<number>-<4-hex>
```

If there is no Issue yet:

```text
YYYYMMDD-no-issue-<4-hex>
```

The agent may choose its own name, but `agent_id` must be short, readable, and unlikely to collide.

## 7. Work claim protocol

Before changing code or documentation for a meaningful task, an agent must claim the work in GitHub.

The claim belongs in the related GitHub Issue. If work is already centered on a Pull Request, the same identity values must also appear in the PR description or PR comments.

Required claim comment:

```md
## AI Handoff Work Claim

Agent: <agent_name>
Agent ID: <agent_id>
Run ID: <run_id>
Started: YYYY-MM-DD HH:MM UTC
Issue: #<issue-number>
Branch: <branch-name>
Draft PR: #<pr-number or TBD>
Scope: <short scope>
Status: in-progress
Next update: <time or condition>
```

For meaningful updates:

```md
## AI Handoff Work Update

Agent ID: <agent_id>
Run ID: <run_id>
Status: in-progress | blocked | completed
Changed:
Tested:
Risk:
Next:
```

If an Issue or PR already has a recent work claim and no completion note, another agent must not silently take it over. The second agent should comment, ask for status, narrow scope, or create a follow-up Issue.

## 8. Issue labels

Recommended universal type labels:

| Label | Use for |
|---|---|
| `bug` | A confirmed or suspected problem in behavior, structure, documentation, templates, or the standard. |
| `enhancement` | A proposed improvement to the standard, workflow, templates, or repository structure. |
| `refactoring` | Code cleanup, file decomposition, renaming, dead-code removal, or internal restructuring without intended behavior change. |
| `research` | Investigation, comparison, feasibility analysis, or design exploration before implementation. |
| `backlog` | Future work that is useful to keep, but not ready for immediate implementation. |
| `testing` | Test coverage gaps, failing checks, flaky checks, smoke-test improvements, or validation tasks. |
| `docs` | Documentation fixes, missing docs, unclear docs, examples, guides, README updates, or translation updates. |

Recommended status labels:

| Label | Use for |
|---|---|
| `in-progress` | An agent or maintainer has claimed the Issue and is working on it. |
| `blocked` | Work cannot continue until a dependency, decision, or external condition is resolved. |

Prefer one primary type label per Issue. Add status labels only while they reflect current work state.

## 9. Project state

`ai/PROJECT_STATE.md` stores the compact current project snapshot.

Recommended sections:

```md
## Current phase
## Architecture snapshot
## Main subsystems
## Implemented
## In progress
## Known risks
## Sensitive areas
## Current technical constraints
## Next likely milestones
```

It is a snapshot, not a historical journal.

## 10. Decisions

`ai/DECISIONS.md` stores durable architecture and product decisions.

Recommended decision format:

```md
## YYYY-MM-DD — Decision title

Status: accepted | superseded | rejected

### Context
### Decision
### Rejected alternatives
### Consequences
### Related
```

Only decisions important for future agents and maintainers should be recorded.

## 11. Handoff protocol

`ai/HANDOFF_PROTOCOL.md` defines the operating protocol for agents.

It should define:

- how work starts;
- how agent identity is chosen;
- how work is claimed in Issues and Pull Requests;
- how an Issue is selected;
- how a branch is created;
- when a Draft PR is opened;
- how progress updates are written;
- how handoff files are created;
- which checks and smoke tests must run;
- how parallel agents coordinate;
- how work is completed or transferred.

## 12. Refactoring workflow

`ai/REFACTORING.md` is the entry point for code cleanup, decomposition, renaming, dependency simplification, dead-code removal, and internal restructuring.

It is a protocol and prompt, not a backlog.

Concrete refactoring tasks should live in GitHub Issues with the `refactoring` label.

## 13. Handoff index

`ai/handoffs/INDEX.md` is the index of handoff files.

Recommended format:

```md
| Date | Updated | Run | Issue | PR | Branch | Status | Relevance | Summary | File | Supersedes |
|---|---|---|---|---|---|---|---|---|---|---|
```

Allowed `Status` values:

- `completed`
- `paused`
- `blocked`
- `failed`
- `superseded`

Allowed `Relevance` values:

- `active`
- `historical`
- `obsolete`

## 14. Handoff files

One handoff file represents one meaningful agent run.

Recommended filename:

```text
YYYY-MM-DD_issue-123_pr-45_run-abc123.md
```

If issue or PR is missing:

```text
YYYY-MM-DD_no-issue_no-pr_run-abc123.md
```

Recommended metadata includes:

```yaml
type: handoff
version: 1
date: YYYY-MM-DD
updated: YYYY-MM-DD
run: abc123
agent: agent-name
agent_id: agent-id
project: project-name
branch: branch-name
issue: 123
pr: 45
base_commit: abc123
final_commit: def456
status: completed
relevance: active
supersedes:
```

A handoff must be a short snapshot, not a full work diary.

## 15. GitHub workflow

Each meaningful work item should be connected to a GitHub Issue or Pull Request.

Recommended process:

1. Select or create a GitHub Issue.
2. Check existing work claims, linked PRs, active handoffs, and recent comments.
3. Choose agent identity.
4. Claim the work in the Issue.
5. Define work scope.
6. Create a branch.
7. Open a Draft PR early.
8. Write progress updates in Issue or PR comments when useful.
9. Commit changes.
10. Run checks and mandatory smoke tests.
11. Update PR description.
12. Leave a handoff when work is completed or interrupted.

PR description should contain:

- agent name, agent id, and run id when work was done by an AI agent;
- what changed;
- related issue;
- how it was tested;
- smoke-test result;
- known risks;
- remaining work;
- links to relevant handoff files if needed.

## 16. GitHub templates

Use GitHub Issue Forms for structured issues.

Recommended issue forms:

- bug;
- enhancement;
- refactoring;
- research;
- backlog;
- testing;
- docs.

Keep one default PR template at `.github/pull_request_template.md` unless the repository has clearly different PR workflows.

## 17. Parallel work and conflict protocol

Main rule:

```text
one agent = one Issue / PR / branch / work scope
```

Agents coordinate through GitHub Issues, Draft PRs, PR comments, labels, branches, and `ai/handoffs/`.

Before editing high-risk files, check:

- open PRs touching the same files;
- related Issues;
- recent Issue or PR work claim comments;
- recent commits on the base branch;
- `ai/handoffs/INDEX.md` for active work.

If overlap is found:

1. do not silently continue;
2. comment in the related Issue or PR;
3. narrow the scope;
4. create a follow-up Issue if needed;
5. leave a handoff if the current work is paused.

## 18. Completion protocol and Definition of Done

After completing or interrupting meaningful work, the agent must:

1. update or create the PR;
2. add a progress update in an Issue or PR comment when useful;
3. run mandatory smoke tests before marking work as ready;
4. create a short handoff file in `ai/handoffs/`;
5. update `ai/handoffs/INDEX.md`;
6. update `ai/PROJECT_STATE.md` if stable project state changed;
7. update `ai/DECISIONS.md` if a durable decision was made;
8. commit changes.

Definition of Done:

- related Issue or PR is linked;
- work claim comment exists for AI-agent work;
- agent id and run id are repeated in PR or handoff when relevant;
- changes are committed;
- smoke tests were run before completion, or not-run reason is documented;
- focused checks were run, or not-run reason is documented;
- PR description is updated;
- risks are listed;
- handoff file exists for meaningful work;
- `ai/handoffs/INDEX.md` is updated;
- `PROJECT_STATE.md` is updated only if stable state changed;
- `DECISIONS.md` is updated only if a durable decision was made.

## 19. Mandatory smoke tests

Smoke tests are mandatory before completing work, marking a PR ready for review, or writing a handoff as `completed`.

Each repository must define project-specific smoke tests in `ai/HANDOFF_PROTOCOL.md`.

Default smoke-test categories:

- repository opens and basic commands still work;
- dependency files are validated when changed;
- the application starts, imports, builds, or shows help, depending on project type;
- at least one focused check covers the changed area;
- documentation-only changes pass Markdown/YAML/link sanity checks where practical;
- GitHub Issue Forms and PR templates remain syntactically valid when changed.

## 20. When to update ai/

Update `ai/` only if:

- a durable decision was made;
- current project state changed;
- meaningful work completed or was interrupted;
- the agent workflow protocol changed;
- an important risk or constraint appeared;
- the next agent cannot continue safely without a new note.

Do not update `ai/` for cosmetic changes, minor refactors, formatting-only commits, or changes fully explained by the PR diff and commit messages.

## 21. Machine-readable metadata

Use YAML front matter for files that represent durable AI-readable state.

Required for:

- `ai/PROJECT_STATE.md`;
- `ai/DECISIONS.md`;
- `ai/HANDOFF_PROTOCOL.md`;
- `ai/AGENT_IDENTITY.md`;
- `ai/WORK_CLAIM_PROTOCOL.md`;
- `ai/REFACTORING.md`;
- `ai/handoffs/INDEX.md`;
- `ai/handoffs/*.md`;
- archive index files.

Required front matter fields:

```yaml
type: project_state | decisions | handoff_protocol | agent_identity_protocol | work_claim_protocol | refactoring_protocol | handoff_index | handoff | archive_index
version: 1
status: active
updated: YYYY-MM-DD
project: project-name
```

Handoff files should additionally include run, agent, agent_id, branch, issue, PR, base commit, final commit, status, relevance, and supersedes.

## 22. Portability

AI Handoff must be portable.

A new agent should recover state after `git clone` and access to GitHub.

Recovery must not require a local database of a previous agent, old local state, uncommitted local files, or hidden tool data.

## 23. Final rule

Code changes together with compact state for the next agent.

Large data stays in GitHub and Git.

`ai/` stores only what helps future agents continue development quickly and safely.
