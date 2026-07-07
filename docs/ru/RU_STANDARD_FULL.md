---
standard: Agent Handoff
version: "1.2"
status: active
updated: 2026-07-04
---

# Стандарт Agent Handoff

Agent Handoff — компактный стандарт передачи состояния разработки между людьми, AI-агентами и агентами под контролем человека через GitHub, Git и небольшие файлы памяти в репозитории.

## Core model / Базовая модель

```text
GitHub manages work: Issues, Pull Requests, reviews, checks, labels, comments, and current ownership.
Git stores code: branches, commits, diffs, tags, and history.
ai/ stores compact durable memory and agent protocols.
ai/handoffs/ stores short snapshots of agent runs.
```

GitHub управляет работой: Issues, Pull Requests, reviews, checks, labels, comments и текущим ownership.

Git хранит код: branches, commits, diffs, tags и history.

`ai/` хранит компактную долговременную память и протоколы агентов.

`ai/handoffs/` хранит короткие snapshots agent runs.

## Language model / Языковая модель

Стандарт применим к английским и русским репозиториям.

В английском репозитории агенты должны работать на английском.

В русском репозитории агенты должны работать на русском.

Английская и русская документация должны сохранять одинаковую структуру и смысл.

Issue Forms и Pull Request templates должны поддерживать выбор языка или двуязычные названия полей.

## Required files / Обязательные файлы

```text
AGENTS.md
AGENT_HANDOFF_STANDARD.md
ISSUE_LABELS.md
ISSUE_STATUS.md
ai/README.md
ai/PROJECT_STATE.md
ai/DECISIONS.md
ai/GITHUB_WORKFLOW.md
ai/HANDOFF_PROTOCOL.md
ai/AGENT_IDENTITY.md
ai/WORK_CLAIM_PROTOCOL.md
ai/TASK_REPORT_PROTOCOL.md
ai/REFACTORING.md
ai/handoffs/INDEX.md
.github/ISSUE_TEMPLATE/
.github/pull_request_template.md
docs/en/
docs/ru/
```

## Start order / Порядок старта

Перед значимой работой прочитайте:

1. `AGENTS.md`
2. `AGENT_HANDOFF_STANDARD.md`
3. `ai/README.md`
4. `ai/GITHUB_WORKFLOW.md`
5. `ai/HANDOFF_PROTOCOL.md`
6. `ai/AGENT_IDENTITY.md`
7. `ai/WORK_CLAIM_PROTOCOL.md`
8. `ai/TASK_REPORT_PROTOCOL.md`
9. `ai/PROJECT_STATE.md`
10. `ai/DECISIONS.md`
11. связанный GitHub Issue или Pull Request
12. релевантные handoffs через `ai/handoffs/INDEX.md`

## Agent identity / Идентификация агента

Каждый agent run должен использовать `agent_name`, `agent_id` и `run_id`.

Рекомендуемые форматы:

```text
agent_id: <two-words-slug>-<4-hex>
run_id: YYYYMMDD-issue-<number>-<4-hex>
```

## Work claim / Claim работы

Перед изменением code или docs для значимой задачи нужно зафиксировать claim работы в GitHub.

Используйте такой comment в связанном Issue и повторяйте identity values в Draft PR:

```md
## Agent Handoff Work Claim

Agent: <agent_name>
Agent ID: <agent_id>
Run ID: <run_id>
Coordinator: <username or none>
Supervision: autonomous | human-supervised | human-driven
Started: YYYY-MM-DD HH:MM UTC
Issue: #<issue-number>
Branch: <branch-name>
Draft PR: #<pr-number or TBD>
Scope: <short scope>
Status: in-progress
Next update: <time or condition>
```

Для updates:

```md
## Agent Handoff Work Update

Agent ID: <agent_id>
Run ID: <run_id>
Status: in-progress | blocked | completed
Changed:
Tested:
Risk:
Next:
```

Если в Issue или PR уже есть свежий work claim, нужно согласовать продолжение в связанном Issue или PR.

## Task result reports / Отчёты результата задачи

Task result comments обязательны для значимых Issues.

Большие или многоэтапные Issues должны иметь stage result comment после каждого стабильного stage.

Небольшие одноэтапные Issues должны иметь один final result comment перед завершением работы.

Для каждого stage большой задачи агент должен зафиксировать findings, сделать маленькое сфокусированное изменение, запустить targeted tests или объяснить, почему они не запускались, обновить AI или project docs, когда это релевантно, сделать bilingual commit, если репозиторий двуязычный, и продолжать только после стабильного слоя.

Используйте `ai/TASK_REPORT_PROTOCOL.md` для обязательных comment templates.

## Branch naming / Имена веток

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

## Labels / Метки

Type labels: `bug`, `enhancement`, `refactoring`, `research`, `backlog`, `testing`, `docs`.

Status labels: `needs-triage`, `ready`, `in-progress`, `blocked`, `in-review`, `changes-requested`, `ready-to-merge`.

## Workflow / Процесс

1. Выберите или создайте GitHub Issue.
2. Проверьте существующие work claims, linked PRs, active handoffs и recent comments.
3. Выберите agent identity.
4. Зафиксируйте claim работы.
5. Определите scope и stages, если задача большая.
6. Создайте осмысленную short-lived branch.
7. Рано откройте Draft PR.
8. Оставляйте обязательные stage или final result comments в Issue или PR.
9. Commit changes.
10. Run checks and smoke tests.
11. Обновите PR description.
12. Оставьте handoff, если работа завершена или прервана.

## Definition of Done / Критерии готовности

- related Issue или PR связан;
- work claim comment существует для agent work;
- agent id и run id повторены в PR или handoff, когда это релевантно;
- обязательный stage или final result comment существует;
- changes committed;
- smoke tests выполнены или причина описана;
- PR description обновлён;
- risks listed;
- handoff существует для значимой работы;
- `ai/handoffs/INDEX.md` обновлён, когда это нужно.

## Final rule / Финальное правило

Код меняется вместе с компактным состоянием для следующего агента.

Большие данные остаются в GitHub и Git.

`ai/` хранит только то, что помогает будущим агентам быстро и безопасно продолжить разработку.
