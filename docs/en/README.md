# English documentation

This page is the documentation index for Agent Handoff Standard 1.4.

## Documents

- [Standard](../../AGENT_HANDOFF_STANDARD.md)
- [Release notes 1.4](../releases/v1.4.md)
- [Issue labels](../../ISSUE_LABELS.md)
- [Issue status](../../ISSUE_STATUS.md)
- [Guide](../../AGENTS.md)
- [Memory map](../../ai/README.md)
- [GitHub workflow](../../ai/GITHUB_WORKFLOW.md)
- [Handoff protocol](../../ai/HANDOFF_PROTOCOL.md)
- [Agent identity](../../ai/AGENT_IDENTITY.md)
- [Work claim protocol](../../ai/WORK_CLAIM_PROTOCOL.md)
- [Task report protocol](../../ai/TASK_REPORT_PROTOCOL.md)
- [Project state](../../ai/PROJECT_STATE.md)
- [Decisions](../../ai/DECISIONS.md)
- [Refactoring workflow](../../ai/REFACTORING.md)
- [Containerization protocol](../../ai/CONTAINERIZATION.md)
- [FAQ](FAQ_EN.md)
- [Examples](../../examples/README.md)
- [Promotion checklist](PROMOTION_CHECKLIST_EN.md)
- [Community files](../COMMUNITY_FILES.md)
- [Contributing](../../CONTRIBUTING.md)
- [Security](../../SECURITY.md)
- [Code of Conduct](../../CODE_OF_CONDUCT.md)
- [Changelog](../../CHANGELOG.md)
- [Promotion changelog appendix](../CHANGELOG_PROMOTION_APPENDIX.md)
- [Repository discovery settings](REPOSITORY_SETTINGS_EN.md)

## Proportionate security and evidence

Security and evidence work must not block acceptance or expand scope unless a current-scope risk is verified as High or Critical with reproducible evidence or a directly applicable authoritative source. A suspected High or Critical risk permits only a short, time-boxed investigation until confirmed.

Low, Medium, unrated, and unverified risks remain non-blocking. The agent preserves the existing security baseline and runs the smallest useful end-to-end scenario early. An exact acceptance criterion or verified mandatory requirement may independently block acceptance only when cited.

The 10–15% security-and-evidence share is only an optional planning heuristic. Substantially exceeding it requires a verified High or Critical risk or an exactly cited mandatory requirement.

## Mandatory containerization question

For both a new repository and an existing repository, the coding agent must ask a separate, explicit question about Docker and Docker Compose organization before changing any container files or paths.

The agent must not choose the recommended layout automatically. Read `ai/CONTAINERIZATION.md` for the supported choices and decision rules.

## Scenario 1: new repository

```text
Initialize this repository with Agent Handoff.
Use the latest standard from https://github.com/artyomboyko/Agent_Handoff.
Create the Agent Handoff files, GitHub issue templates, and pull request template.
Fill PROJECT_STATE.md with the initial project snapshot.
Configure HANDOFF_PROTOCOL.md with smoke tests for this project.

Before creating any Docker or Docker Compose files, ask me a separate explicit question about containerization.
Ask whether Docker or Compose is needed, which supported layout I want, and whether production deployment configuration belongs in this repository or a separate deployment repository.
Do not infer the answer or create container infrastructure until I answer.

Do not let security or evidence work block acceptance or expand scope without a verified High or Critical current-scope risk or an exactly cited mandatory requirement.
Keep Low, Medium, unrated, and unverified risks non-blocking, preserve the existing security baseline, and prioritize the smallest useful end-to-end scenario.

Create the first short handoff and update the handoff index.
```

## Scenario 2: existing repository

```text
Add Agent Handoff to this existing repository.
Use the latest standard from https://github.com/artyomboyko/Agent_Handoff.
Inspect the current repository first.
Merge similar Agent Handoff files carefully.
Compress current state into ai/PROJECT_STATE.md.
Put durable decisions into ai/DECISIONS.md.
Configure smoke tests in ai/HANDOFF_PROTOCOL.md.

Inspect existing Dockerfiles, Compose files, scripts, build contexts, ignore files, environment references, and documented commands.
Then ask me a separate explicit question whether the existing container layout must be preserved or may be migrated, which supported target layout I want, and whether production deployment configuration belongs here or in a separate repository.
Do not move, rename, delete, consolidate, or create container infrastructure until I answer.

Do not let security or evidence work block acceptance or expand scope without a verified High or Critical current-scope risk or an exactly cited mandatory requirement.
Keep Low, Medium, unrated, and unverified risks non-blocking, preserve the existing security baseline, and prioritize the smallest useful end-to-end scenario.

Open a pull request and leave a short handoff.
```
