---
type: github_workflow
version: 1
status: active
updated: 2026-07-04
project: Agent_Handoff
---

# Coordinated GitHub Flow / Координированный GitHub Flow

Agent Handoff uses Coordinated GitHub Flow for medium repositories.
Agent Handoff использует Coordinated GitHub Flow для средних репозиториев.

## Work unit / Единица работы

One work item should have one Issue, one scope, one short-lived branch, one Pull Request, one visible owner, and required result reporting.
Одна задача должна иметь одно Issue, один scope, одну короткоживущую branch, один Pull Request, одного видимого owner и обязательный result report.

## Status labels / Статусные метки

- `needs-triage`
- `ready`
- `in-progress`
- `blocked`
- `in-review`
- `changes-requested`
- `ready-to-merge`

Closed Issue or merged PR is the normal `done` state.
Закрытое Issue или merged PR — обычное состояние `done`.

## Branch naming / Имена веток

Use meaningful branch names without `/`, Issue numbers, or random identifiers by default.
Используйте осмысленные имена веток без `/`, номеров Issue и случайных идентификаторов по умолчанию.

Issue linkage belongs in the Work Claim comment, PR description, GitHub links, and handoff metadata.
Связь с Issue фиксируется в Work Claim comment, PR description, GitHub links и handoff metadata.

## Result reports / Отчёты результата

Every meaningful Issue must have a result comment.
Каждое значимое Issue должно иметь result comment.

Large or multi-stage Issues use stage result comments after stable stages.
Большие или многоэтапные Issues используют stage result comments после стабильных stages.

Small Issues use one final result comment.
Небольшие Issues используют один final result comment.

Use `ai/TASK_REPORT_PROTOCOL.md`.
Используйте `ai/TASK_REPORT_PROTOCOL.md`.

## Workflow / Процесс

1. Triage or create an Issue. / Провести triage или создать Issue.
2. Mark it `ready` when scope is clear. / Ставить `ready`, когда scope ясен.
3. Choose agent identity when an agent is involved. / Выбрать identity агента.
4. Claim work before editing. / Claim работы перед изменениями.
5. Create a short-lived branch. / Создать короткоживущую branch.
6. Open a Draft PR early. / Рано открыть Draft PR.
7. Link the PR to the Issue. / Связать PR с Issue.
8. Keep discussion and result reports in Issue or PR. / Вести обсуждение и result reports в Issue или PR.
9. Run checks and smoke tests. / Запустить checks и smoke tests.
10. Finish only after checks, review, and result report. / Завершать только после checks, review и result report.
11. Add a handoff when needed. / Добавить handoff при необходимости.
