# English documentation

This page mirrors the Russian index `docs/ru/README.md`.

## Documents

- [Standard](../../AGENT_HANDOFF_STANDARD.md)
- [Issue labels](../../ISSUE_LABELS.md)
- [Issue status](../../ISSUE_STATUS.md)
- [Guide](../../AGENTS.md)
- [Memory map](../../ai/README.md)
- [GitHub workflow](../../ai/GITHUB_WORKFLOW.md)
- [Handoff protocol](../../ai/HANDOFF_PROTOCOL.md)
- [Agent identity](../../ai/AGENT_IDENTITY.md)
- [Work claim protocol](../../ai/WORK_CLAIM_PROTOCOL.md)
- [Project state](../../ai/PROJECT_STATE.md)
- [Decisions](../../ai/DECISIONS.md)
- [Refactoring workflow](../../ai/REFACTORING.md)
- [FAQ](FAQ_EN.md)
- [Examples](../../examples/README.md)
- [Promotion checklist](PROMOTION_CHECKLIST_EN.md)
- [Contributing](../../CONTRIBUTING.md)
- [Security](../../SECURITY.md)
- [Code of Conduct](../../CODE_OF_CONDUCT.md)
- [Changelog](../../CHANGELOG.md)
- [Promotion changelog appendix](../CHANGELOG_PROMOTION_APPENDIX.md)
- [Repository discovery settings](REPOSITORY_SETTINGS_EN.md)
- [Русский](../ru/README.md)

## Scenario 1: new repository

```text
Initialize this repository with Agent Handoff.
Use the latest standard from https://github.com/artyomboyko/Agent_Handoff.
Create the Agent Handoff files, GitHub issue templates, and pull request template.
Fill PROJECT_STATE.md with the initial project snapshot.
Configure HANDOFF_PROTOCOL.md with smoke tests for this project.
Create the first short handoff and update the handoff index.
```

## Scenario 2: existing repository

```text
Add Agent Handoff to this existing repository.
Use the latest standard from https://github.com/artyomboyko/Agent_Handoff.
Inspect the current repository first.
Do not overwrite existing important files blindly.
Merge similar files carefully.
Move outdated long notes to ai/archive when appropriate.
Compress current state into ai/PROJECT_STATE.md.
Put durable decisions into ai/DECISIONS.md.
Configure smoke tests in ai/HANDOFF_PROTOCOL.md.
Open a pull request and leave a short handoff.
```
