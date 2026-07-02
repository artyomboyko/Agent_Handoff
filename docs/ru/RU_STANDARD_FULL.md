# Стандарт Agent Handoff

Agent Handoff описывает, как передавать проектный контекст между людьми, AI-агентами и агентами под контролем человека через GitHub, Git и `ai/`.

## Модель

GitHub управляет задачами, Pull Request, ревью, проверками, метками, комментариями и текущим ownership.

Git хранит код, ветки, коммиты, diff, теги и историю.

`ai/` хранит компактную долговременную память проекта и агентские протоколы.

`ai/handoffs/` хранит короткие снимки сессий.

## Структура

- `AGENTS.md`
- `AGENT_HANDOFF_STANDARD.md`
- `ISSUE_LABELS.md`
- `ai/README.md`
- `ai/PROJECT_STATE.md`
- `ai/DECISIONS.md`
- `ai/GITHUB_WORKFLOW.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/AGENT_IDENTITY.md`
- `ai/WORK_CLAIM_PROTOCOL.md`
- `ai/REFACTORING.md`
- `ai/handoffs/INDEX.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `docs/en/`
- `docs/ru/`

## Coordinated GitHub Flow

Agent Handoff использует Coordinated GitHub Flow для средних репозиториев, где параллельно работают люди, автономные агенты и агенты под контролем человека.

Единица работы: одно GitHub Issue, один ясный scope, одна короткоживущая branch, один Pull Request и один видимый owner.

## Branch naming

Используйте осмысленные имена веток без `/`, без номеров Issue и без случайных идентификаторов по умолчанию.

Рекомендуемые форматы:

```text
<type>-<topic>
<type>-<scope>-<topic>
```

Примеры:

```text
workflow-branch-naming
protocol-work-claim
docs-readme-quickstart
refactor-handoff-index
research-github-flow
fix-issue-template-yaml
```

Связь с Issue фиксируется в Work Claim comment, PR description, GitHub links и handoff metadata, а не в имени ветки.

## Issue templates

Issue templates должны поддерживать выбор языка и двуязычные поля.

## Завершение

Перед завершением значимого изменения нужны smoke tests, обновлённый PR, короткий handoff и обновлённый index.

## Финальное правило

Код меняется вместе с компактным контекстом для следующего агента. Большие данные остаются в GitHub и Git.
