# Agent Handoff

Agent Handoff is a compact standard for passing project context between AI coding agents through GitHub, Git, and small repository-tracked memory files.

## Language / Язык

| Language | Start here |
|---|---|
| English | [Open English documentation](docs/en/README.md) |
| Русский | [Открыть русскую документацию](docs/ru/README.md) |

## Quick start / Быстрый старт

Use the language links above. Each language page includes two short examples:

- starting a new repository with Agent Handoff;
- adding Agent Handoff to an existing repository.

## Current standard / Текущий стандарт

Version / версия: **1.2**

| English | Русский |
|---|---|
| [Agent Handoff Standard](AGENT_HANDOFF_STANDARD.md) | [Стандарт Agent Handoff](docs/ru/RU_STANDARD_FULL.md) |
| [Issue labels](ISSUE_LABELS.md) | [Метки Issue](ISSUE_LABELS.md) |
| [Agent entrypoint](AGENTS.md) | [Инструкция](docs/ru/RU_GUIDE.md) |
| [Agent memory map](ai/README.md) | [Карта документов](docs/ru/README.md) |
| [Workflow protocol](ai/HANDOFF_PROTOCOL.md) | [Протокол](docs/ru/PROTOCOL_RU.md) |
| [Agent identity](ai/AGENT_IDENTITY.md) | [Agent identity](ai/AGENT_IDENTITY.md) |
| [Work claim protocol](ai/WORK_CLAIM_PROTOCOL.md) | [Work claim protocol](ai/WORK_CLAIM_PROTOCOL.md) |

## Core model / Основная модель

```text
GitHub     = Issues, Pull Requests, reviews, CI, discussions
Git        = source code, branches, commits, diffs, tags, history
ai/        = compact durable project memory
handoffs/  = short snapshots of agent runs
```

Large data should stay in GitHub or Git, not in `ai/`.
