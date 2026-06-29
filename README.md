# AI Handoff

AI Handoff is a compact standard for passing development state between AI coding agents through GitHub, Git, and small repository-tracked memory files.

AI Handoff — компактный стандарт передачи состояния разработки между AI-агентами через GitHub, Git и небольшие файлы памяти внутри репозитория.

## Language / Язык

| Language | Start here |
|---|---|
| English | [Open English documentation](docs/en/README.md) |
| Русский | [Открыть русскую документацию](docs/ru/README.md) |

## Current standard / Текущий стандарт

Version / версия: **1.1**

| English | Русский |
|---|---|
| [AI Handoff Standard](AI_HANDOFF_STANDARD.md) | [Стандарт AI Handoff](docs/ru/AI_HANDOFF_STANDARD.md) |
| [Agent entrypoint](AGENTS.md) | [Инструкция для агентов](docs/ru/AGENTS.md) |
| [AI memory map](ai/README.md) | [Карта AI-памяти](docs/ru/README.md) |
| [Workflow protocol](ai/HANDOFF_PROTOCOL.md) | [Протокол работы](docs/ru/HANDOFF_PROTOCOL.md) |

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
handoffs/  = короткие снимки агентских сессий
```

Large data should stay in GitHub or Git, not in `ai/`.

Большие данные должны оставаться в GitHub или Git, а не в `ai/`.
