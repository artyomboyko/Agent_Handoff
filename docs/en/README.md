# English

- [Standard](../../AI_HANDOFF_STANDARD.md)
- [Guide](../../AGENTS.md)
- [Memory map](../../ai/README.md)
- [Protocol](../../ai/HANDOFF_PROTOCOL.md)

## Scenario 1: new repository

Ask the coding agent to initialize AI Handoff from the start.

```text
Initialize this repository with AI Handoff.
Use the latest standard from https://github.com/artyomboyko/AI_Handoff.
Create the AI Handoff files, GitHub issue templates, and pull request template.
Fill PROJECT_STATE.md with the initial project snapshot.
Configure HANDOFF_PROTOCOL.md with smoke tests for this project.
Create the first short handoff and update the handoff index.
```

## Scenario 2: existing repository

Ask the coding agent to migrate carefully.

```text
Add AI Handoff to this existing repository.
Use the latest standard from https://github.com/artyomboyko/AI_Handoff.
Inspect the current repository first.
Do not overwrite existing important files blindly.
Merge similar files carefully.
Move outdated long notes to ai/archive when appropriate.
Compress current state into ai/PROJECT_STATE.md.
Put durable decisions into ai/DECISIONS.md.
Configure smoke tests in ai/HANDOFF_PROTOCOL.md.
Open a pull request and leave a short handoff.
```

Russian: [docs/ru/README.md](../ru/README.md)
