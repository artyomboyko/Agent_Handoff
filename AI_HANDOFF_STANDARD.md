---
standard: AI Handoff
version: "1.1"
status: active
updated: 2026-06-29
---

# AI Handoff Standard

## 1. Purpose

AI Handoff is a standard for passing development state between AI coding agents through GitHub, Git, and compact files stored inside the repository.

The standard exists so that a new agent can recover project state, understand current architecture, find accepted decisions, continue work after another agent, coordinate parallel work, and avoid dependence on earlier local state.

Core formula:

```text
GitHub manages the work.
Git stores code and history.
ai/ stores compact durable project memory.
handoffs/ stores short snapshots of AI agent runs.
```

## 2. Sources of truth

### GitHub

GitHub is the primary workflow system.

GitHub stores Issues, Pull Requests, PR comments, labels, reviews, GitHub Actions, CI status, task discussions, and links between tasks, branches, and PRs.

GitHub Issues are used for tasks, bugs, features, refactoring, research, and future queue.

Pull Requests are used for implementation, review, checks, and operational state.

### Git

Git stores source code, commits, branches, diffs, tags, and history.

Full diffs and history must not be duplicated in `ai/`.

### ai/

The `ai/` folder stores compact project memory that is versioned with the repository.

`ai/` does not replace GitHub Issues, Pull Requests, Actions data, or Git history.

## 3. Source priority

If information conflicts:

1. Git working tree and current branch are the source for actual code state.
2. GitHub Pull Request is the source for current implementation status.
3. GitHub Issue is the source for task intent and acceptance criteria.
4. `ai/PROJECT_STATE.md` is the compact current project snapshot.
5. `ai/DECISIONS.md` is the source for durable architecture and product decisions.
6. `ai/handoffs/*.md` are run snapshots, not authoritative history.

A handoff can be stale. Code, PR state, and current GitHub discussion have higher priority.

## 4. Repository structure

Required structure:

```text
AGENTS.md
ai/
  README.md
  PROJECT_STATE.md
  DECISIONS.md
  HANDOFF_PROTOCOL.md
  handoffs/
    INDEX.md
    YYYY-MM-DD_issue-123_pr-45_run-abc123.md
  archive/
    README.md
.github/
  ISSUE_TEMPLATE/
    bug_report.yml
    standard_change.yml
    config.yml
  pull_request_template.md
```

A standalone standard repository may also keep `AI_HANDOFF_STANDARD.md` at the root.

## 5. AGENTS.md

`AGENTS.md` is the short root entrypoint.

It should direct the agent to:

1. `ai/README.md`;
2. `ai/HANDOFF_PROTOCOL.md`;
3. `ai/PROJECT_STATE.md`;
4. `ai/DECISIONS.md`;
5. the related GitHub Issue or Pull Request;
6. current Git status and branch.

`AGENTS.md` must stay small.

## 6. ai/README.md

`ai/README.md` is the map of AI documentation.

Recommended reading order:

1. `AGENTS.md`
2. `ai/README.md`
3. `ai/HANDOFF_PROTOCOL.md`
4. `ai/PROJECT_STATE.md`
5. `ai/DECISIONS.md`
6. related GitHub Issue or Pull Request
7. `ai/handoffs/INDEX.md`
8. relevant handoff files only

The agent must not read every handoff file blindly.

## 7. ai/PROJECT_STATE.md

`ai/PROJECT_STATE.md` stores the compact current project snapshot.

Recommended structure:

```md
---
type: project_state
version: 1
status: active
updated: YYYY-MM-DD
project: project-name
---

# Project State

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

It is a snapshot, not a historical journal. Stale material should be compressed or moved to `ai/archive/`.

## 8. ai/DECISIONS.md

`ai/DECISIONS.md` stores durable architecture and product decisions.

Recommended file metadata:

```md
---
type: decisions
version: 1
status: active
updated: YYYY-MM-DD
project: project-name
---
```

Recommended decision format:

```md
## YYYY-MM-DD — Decision title

Status: accepted | superseded | rejected

### Context
Why the decision was needed.

### Decision
What was chosen.

### Rejected alternatives
What was rejected.

### Consequences
What follows from the decision.

### Related
GitHub Issue / PR / commit links.
```

Only decisions important for future agents and maintainers should be recorded.

If decisions grow too much, keep `ai/DECISIONS.md` as an index and move full ADRs to `ai/decisions/ADR-YYYY-MM-DD-title.md`.

## 9. ai/HANDOFF_PROTOCOL.md

`ai/HANDOFF_PROTOCOL.md` defines the operating protocol for agents.

It should define:

- how work starts;
- how an Issue is selected;
- how a branch is created;
- when a Draft PR is opened;
- how progress updates are written;
- how handoff files are created;
- which checks and smoke tests must run;
- how Docker or Compose is handled when relevant;
- how parallel agents coordinate;
- how work is completed or transferred;
- which actions need extra care.

## 10. ai/handoffs/INDEX.md

`ai/handoffs/INDEX.md` is the index of handoff files.

Recommended format:

```md
---
type: handoff_index
version: 1
status: active
updated: YYYY-MM-DD
project: project-name
---

# Handoff Index

| Date | Updated | Run | Issue | PR | Branch | Status | Relevance | Summary | File | Supersedes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-29 | 2026-06-29 | abc123 | #123 | #45 | work/issue-123-compose | completed | historical | Fixed Compose startup | 2026-06-29_issue-123_pr-45_run-abc123.md | |
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

If a handoff is superseded by a newer run, mark the old entry as `obsolete`.

## 11. ai/handoffs/*.md

One handoff file represents one meaningful agent run.

Recommended filename:

```text
YYYY-MM-DD_issue-123_pr-45_run-abc123.md
```

If issue or PR is missing:

```text
YYYY-MM-DD_no-issue_no-pr_run-abc123.md
```

Recommended metadata:

```md
---
type: handoff
version: 1
date: YYYY-MM-DD
updated: YYYY-MM-DD
run: abc123
agent: agent-name
project: project-name
branch: branch-name
issue: 123
pr: 45
base_commit: abc123
final_commit: def456
status: completed
relevance: active
supersedes:
---
```

Recommended body:

```md
# Handoff: abc123

## Task
Short task description.

## What changed
Short description of completed changes.

## Files changed
Changed files with short explanations.

## Smoke tests
Mandatory smoke tests and results.

## What was tested
Other checks and results.

## What failed / risks
Failures, risks, or attention points.

## Next recommended step
What the next agent or human should do.

## Links
- Issue:
- PR:
- Commits:
- Actions:
```

A handoff must be a short snapshot, not a full work diary.

## 12. ai/archive/

`ai/archive/` stores stale project memory that is not needed now in the active state.

`ai/archive/README.md` should explain what is stored there and when to archive it.

## 13. Size limits

Recommended soft limits:

- `AGENTS.md`: up to 120 lines;
- `ai/README.md`: up to 250 lines;
- `ai/PROJECT_STATE.md`: up to 600 lines;
- `ai/DECISIONS.md`: up to 1,000 lines total;
- one decision entry: up to 120 lines;
- `ai/HANDOFF_PROTOCOL.md`: up to 700 lines;
- one handoff file: up to 250 lines;
- active `ai/` memory, excluding archive: preferably under 150 KB.

These are soft limits. If state becomes hard to load, compress or archive.

Do not place in `ai/`:

- large diffs;
- bulky command records;
- full work diaries;
- large stack traces;
- full GitHub discussions;
- full GitHub Actions data;
- private access values;
- large tool data;
- generated artifacts that fit elsewhere.

Use links to GitHub, commits, PRs, Actions, or repository files for large data.

## 14. GitHub workflow

Each meaningful work item should be connected to a GitHub Issue or Pull Request.

Recommended process:

1. Select or create a GitHub Issue.
2. Define work scope.
3. Create a branch.
4. Open a Draft PR early.
5. Write progress updates in PR comments.
6. Commit changes.
7. Run checks and mandatory smoke tests.
8. Update PR description.
9. Leave a handoff when work is completed or interrupted.

PR description should contain:

- what changed;
- related issue;
- how it was tested;
- smoke-test result;
- known risks;
- remaining work;
- links to relevant handoff files if needed.

## 15. GitHub templates

Recommended default:

- use GitHub Issue Forms for structured issues;
- provide at least two issue templates:
  - Bug report;
  - Standard change / enhancement;
- keep one default PR template at `.github/pull_request_template.md`.

Multiple PR templates may be added later in `.github/PULL_REQUEST_TEMPLATE/`, but the default single template is preferred unless the repository has clearly different PR workflows.

Issue forms should collect structured data, required fields, affected section, expected behavior, risks, and acceptance criteria.

PR templates should require summary, related issue, change type, smoke tests, state updates, risks, and next steps.

## 16. Parallel work and conflict protocol

Main rule:

```text
one agent = one Issue / PR / branch / work scope
```

Agents coordinate through GitHub Issues, Draft PRs, PR comments, labels, branches, and `ai/handoffs/`.

Before editing high-risk files, check:

- open PRs touching the same files;
- related Issues;
- recent commits on the base branch;
- `ai/handoffs/INDEX.md` for active work.

High-risk files include dependency manifests, Dockerfiles, Compose files, CI workflows, migrations, auth code, shared configuration, public API contracts, core architecture files, and active `ai/` memory files.

If overlap is found:

1. do not silently continue;
2. comment in the related Issue or PR;
3. narrow the scope;
4. create a follow-up Issue if needed;
5. leave a handoff if the current work is paused.

## 17. Start protocol

Before changing code, the agent must:

1. read `AGENTS.md`;
2. read `ai/README.md`;
3. read `ai/HANDOFF_PROTOCOL.md`;
4. read `ai/PROJECT_STATE.md`;
5. read `ai/DECISIONS.md`;
6. find the related GitHub Issue or PR;
7. check `git status`;
8. check current branch;
9. check recent commits;
10. check relevant handoffs through `ai/handoffs/INDEX.md`.

Only after that may the agent propose or make changes.

## 18. Completion protocol and Definition of Done

After completing or interrupting meaningful work, the agent must:

1. update or create the PR;
2. add a progress update in a PR comment when useful;
3. run mandatory smoke tests before marking work as ready;
4. create a short handoff file in `ai/handoffs/`;
5. update `ai/handoffs/INDEX.md`;
6. update `ai/PROJECT_STATE.md` if stable project state changed;
7. update `ai/DECISIONS.md` if a durable decision was made;
8. commit changes.

Definition of Done:

- related Issue or PR is linked;
- changes are committed;
- smoke tests were run before completion, or not-run reason is documented;
- focused checks were run, or not-run reason is documented;
- PR description is updated;
- risks are listed;
- handoff file exists for meaningful work;
- `ai/handoffs/INDEX.md` is updated;
- `PROJECT_STATE.md` is updated only if stable state changed;
- `DECISIONS.md` is updated only if a durable decision was made;
- private access values were not added.

## 19. Mandatory smoke tests

Smoke tests are mandatory before completing work, marking a PR ready for review, or writing a handoff as `completed`.

Each repository must define project-specific smoke tests in `ai/HANDOFF_PROTOCOL.md`.

Default smoke-test categories:

- repository opens and basic commands still work;
- dependency files are validated when changed;
- the application starts, imports, builds, or shows help, depending on project type;
- at least one focused check covers the changed area;
- documentation-only changes pass Markdown/YAML/link sanity checks where practical;
- GitHub Issue Forms and PR templates remain syntactically valid when changed;
- private access values are not present in changed files.

If smoke tests cannot be run, write:

```text
Smoke tests: not run
Reason:
Risk:
Next step:
```

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
- `ai/handoffs/INDEX.md`;
- `ai/handoffs/*.md`;
- archive index files.

Optional for:

- `AI_HANDOFF_STANDARD.md`;
- large standalone ADR files if decisions are split.

Not required for:

- `AGENTS.md`;
- `.github` issue templates;
- `.github/pull_request_template.md`.

Required front matter fields:

```yaml
type: project_state | decisions | handoff_protocol | handoff_index | handoff | archive_index
version: 1
status: active
updated: YYYY-MM-DD
project: project-name
```

Handoff files should additionally include run, branch, issue, PR, base commit, final commit, status, relevance, and supersedes.

The goal is to keep files human-readable while making indexing and automation easier.

## 22. Security and private access values

Private access values must stay outside `ai/` and outside handoff files.

Do not place in repository memory:

- API keys;
- auth values;
- sign-in values;
- local key material;
- production access values;
- personal data;
- full local environment files;
- private customer data;
- sensitive internal incident data.

If a private access value was exposed:

1. stop normal work;
2. notify the owner or maintainer;
3. rotate the value;
4. repair Git history if needed;
5. document only the remediation, never the value itself.

## 23. Portability

AI Handoff must be portable.

A new agent should recover state after `git clone` and access to GitHub.

Recovery must not require a local database of a previous agent, old local state, uncommitted local files, or hidden tool data.

## 24. Final rule

Code changes together with compact state for the next agent.

Large data stays in GitHub and Git.

`ai/` stores only what helps future agents continue development quickly and safely.
