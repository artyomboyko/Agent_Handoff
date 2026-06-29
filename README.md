# AI Handoff

AI Handoff is a compact standard for passing project context between AI coding agents through GitHub, Git, and small repository-tracked memory files.

AI Handoff — компактный стандарт передачи проектного контекста между AI-агентами через GitHub, Git и небольшие файлы памяти внутри репозитория.

## Language / Язык

| Language | Start here |
|---|---|
| English | [Open English documentation](docs/en/README.md) |
| Русский | [Открыть русскую документацию](docs/ru/README.md) |

## Current standard / Текущий стандарт

Version / версия: **1.1**

| English | Русский |
|---|---|
| [AI Handoff Standard](AI_HANDOFF_STANDARD.md) | [Стандарт AI Handoff](docs/ru/RU_STANDARD_FULL.md) |
| [Agent entrypoint](AGENTS.md) | [Инструкция](docs/ru/RU_GUIDE.md) |
| [AI memory map](ai/README.md) | [Карта документов](docs/ru/README.md) |
| [Workflow protocol](ai/HANDOFF_PROTOCOL.md) | [Протокол](docs/ru/PROTOCOL_RU.md) |

## Core model / Основная модель

```text
GitHub     = Issues, Pull Requests, reviews, CI, discussions
Git        = source code, branches, commits, diffs, tags, history
ai/        = compact durable project memory
handoffs/  = short snapshots of agent runs
```

```text
GitHub     = задачи, Pull Request, ревью, CI, обсуждения
Git        = код, ветки, коммиты, diff, теги, история
ai/        = компактная долговременная память проекта
handoffs/  = короткие снимки сессий
```

Large data should stay in GitHub or Git, not in `ai/`.

Большие данные должны оставаться в GitHub или Git, а не в `ai/`.
