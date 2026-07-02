---
type: github_workflow
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Coordinated GitHub Flow / Координированный GitHub Flow

Agent Handoff uses Coordinated GitHub Flow for medium repositories.
Agent Handoff использует Coordinated GitHub Flow для средних репозиториев.

## Roles / Роли

- Maintainer or coordinator / Maintainer или coordinator
- Human contributor / Человек-контрибьютор
- Autonomous agent / Автономный агент
- Human-supervised agent / Агент под контролем человека
- Reviewer / Reviewer

## Work unit / Единица работы

One work item should have one Issue, one scope, one short-lived branch, one Pull Request, and one visible owner.
Одна задача должна иметь одно Issue, один scope, одну короткоживущую branch, один Pull Request и одного видимого owner.

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

Recommended formats / Рекомендуемые форматы:

```text
<type>-<topic>
<type>-<scope>-<topic>
```

Examples / Примеры:

```text
workflow-branch-naming
protocol-work-claim
docs-readme-quickstart
refactor-handoff-index
research-github-flow
fix-issue-template-yaml
```

The branch is not the source of truth for Issue linkage.
Branch не является источником правды для связи с Issue.

Link the Issue in the Work Claim comment, PR description, and handoff metadata.
Связывайте Issue через Work Claim comment, PR description и handoff metadata.

## Workflow / Процесс

1. Triage or create an Issue. / Провести triage или создать Issue.
2. Mark it `ready` when scope is clear. / Ставить `ready`, когда scope ясен.
3. Choose agent identity when an agent is involved. / Выбрать identity агента.
4. Claim work before editing. / Claim работы перед изменениями.
5. Create a short-lived branch. / Создать короткоживущую branch.
6. Open a Draft PR early. / Рано открыть Draft PR.
7. Link the PR to the Issue. / Связать PR с Issue.
8. Keep discussion in Issue or PR. / Вести обсуждение в Issue или PR.
9. Run checks and smoke tests. / Запустить checks и smoke tests.
10. Merge only after checks and review. / Merge только после checks и review.
11. Delete the branch after merge. / Удалить branch после merge.
12. Add a handoff when needed. / Добавить handoff при необходимости.

## Human coordination / Координация людьми

A human coordinator may reassign, pause, split, or supersede agent work.
Человек-координатор может переназначить, остановить, разделить или заменить работу агента.

If the work is human-supervised, the Work Claim should include:
Если работа идёт под контролем человека, Work Claim должен включать:

```text
Coordinator: @username
Supervision: autonomous | human-supervised | human-driven
```
