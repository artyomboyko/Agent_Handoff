# Стандарт Agent Handoff

Agent Handoff — компактный стандарт передачи состояния разработки между людьми, AI-агентами и агентами под контролем человека через GitHub, Git и небольшие файлы памяти в репозитории.

## Модель

GitHub управляет работой: Issues, Pull Requests, reviews, checks, labels, comments и текущим ownership.

Git хранит код, branches, commits, diffs, tags и history.

`ai/` хранит компактную долговременную память и протоколы агентов.

`ai/handoffs/` хранит короткие снимки agent runs.

## Языковая модель

Стандарт применим к английским и русским репозиториям.

В английском репозитории агент работает на английском.

В русском репозитории агент работает на русском.

Английская и русская документация должны сохранять одинаковую структуру и смысл.

Issue Forms и Pull Request templates должны поддерживать выбор языка или двуязычные поля.

## Структура

- `AGENTS.md`
- `AGENT_HANDOFF_STANDARD.md`
- `ISSUE_LABELS.md`
- `ISSUE_STATUS.md`
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

## Work Claim

Перед значимыми изменениями работа фиксируется в GitHub Issue.

Шаблон должен включать:

```text
Agent
Agent ID
Run ID
Coordinator
Supervision
Started
Issue
Branch
Draft PR
Scope
Status
Next update
```

## Coordinated GitHub Flow

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

## Labels

Type labels: `bug`, `enhancement`, `refactoring`, `research`, `backlog`, `testing`, `docs`.

Status labels: `needs-triage`, `ready`, `in-progress`, `blocked`, `in-review`, `changes-requested`, `ready-to-merge`.

## Завершение

Перед завершением значимого изменения нужны smoke tests, обновлённый PR, описание рисков, короткий handoff при необходимости и обновлённый index.

## Финальное правило

Код меняется вместе с компактным контекстом для следующего агента.

Большие данные остаются в GitHub и Git.
