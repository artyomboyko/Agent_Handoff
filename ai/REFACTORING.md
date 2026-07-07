---
type: refactoring_protocol
version: 1
status: active
updated: 2026-07-04
project: Agent_Handoff
---

# Refactoring Workflow / Workflow рефакторинга

This file is a compact entry point for cleanup, decomposition, renaming, optimization, and internal restructuring.
Этот файл — компактная точка входа для cleanup, decomposition, renaming, optimization и внутренней перестройки.

Track concrete refactoring work in GitHub Issues.
Конкретные задачи рефакторинга ведите в GitHub Issues.

Keep this file as protocol, not as a long backlog.
Держите этот файл как протокол, а не длинный backlog.

## Use for / Использовать для

- splitting large files / разделение больших файлов;
- removing confirmed unused code / удаление подтверждённого неиспользуемого кода;
- simplifying duplicated logic / упрощение дублирующейся логики;
- optimizing existing functions / оптимизация существующих функций;
- reducing module or layer coupling / снижение связанности модулей или слоёв;
- clarifying ownership and source of truth / уточнение ownership и source of truth;
- renaming confusing internal names / переименование непонятных внутренних имён;
- moving responsibilities to clearer modules / перенос ответственности в понятные модули.

## Do not use for / Не использовать для

- product features / продуктовые функции;
- UX or visual redesign unless the Issue explicitly says so / UX или visual redesign, если Issue явно этого не требует;
- broad rewrites without an audit / широкий rewrite без audit;
- research notes / заметки исследования;
- ordinary bug reports / обычные bug reports;
- long logs / длинные логи;
- full diffs / полные diff.

## Issue fields / Поля Issue

A refactoring Issue should include / Refactoring Issue должен включать:

- code area / область кода;
- current problem / текущая проблема;
- target state / целевое состояние;
- non-goals / что не входит в задачу;
- invariants / что должно остаться неизменным;
- compatibility boundaries / compatibility boundaries;
- risk / риск;
- required checks / обязательные проверки;
- related files or PRs / связанные файлы или PR.

## Core rule / Основное правило

Refactoring is audit-first and layer-by-layer.
Рефакторинг выполняется audit-first и по слоям.

Do not start with a mass rewrite.
Не начинайте с массового rewrite.

For every meaningful refactoring task, first define what must not change.
Для каждой значимой задачи рефакторинга сначала определите, что не должно измениться.

Keep external behavior unchanged unless the Issue explicitly allows behavior changes.
Не меняйте внешнее поведение, если Issue явно этого не разрешает.

## Large refactoring / Большой рефакторинг

For large or multi-stage refactoring, create stages and follow `ai/TASK_REPORT_PROTOCOL.md`.
Для большого или многоэтапного рефакторинга создайте stages и следуйте `ai/TASK_REPORT_PROTOCOL.md`.

Each stage must / Каждый stage должен:

1. record findings / зафиксировать findings;
2. make a small focused change / сделать маленькое сфокусированное изменение;
3. run targeted tests or explain why they were not run / запустить targeted tests или объяснить, почему они не запускались;
4. update AI or project docs when relevant / обновить AI или project docs, когда это релевантно;
5. make a bilingual commit when the repository is bilingual / сделать bilingual commit, если репозиторий двуязычный;
6. continue only after the layer is stable / продолжать только после стабильного слоя;
7. leave a stage result comment / оставить stage result comment.

## Baseline audit / Baseline audit

For large refactoring, capture a baseline before changing runtime code.
Для большого рефакторинга зафиксируйте baseline до изменения runtime-кода.

Useful baseline items / Полезные baseline items:

- size of the code area / размер области кода;
- largest files, functions, or classes / крупнейшие файлы, функции или классы;
- dependency count or heavy dependencies / количество зависимостей или тяжёлые зависимости;
- current test count and runtime / текущее число тестов и runtime;
- migration or schema state when relevant / состояние migrations или schema, когда релевантно;
- direct cross-layer call sites / прямые cross-layer call sites;
- compatibility layers / compatibility layers;
- known risk zones / известные risk zones;
- dead code candidates / кандидаты на dead code.

## Finding classification / Классификация findings

Classify findings before editing / Классифицируйте findings перед изменениями:

```text
delete now
refactor now
optimize now
keep as explicit compatibility boundary
move to separate issue
do not touch yet
```

If the work is larger than the current Issue scope, move it to a separate Issue.
Если работа больше scope текущей Issue, вынесите её в отдельную Issue.

## Safety rules / Правила безопасности

- Delete only confirmed dead code. / Удаляйте только подтверждённый dead code.
- Do not remove compatibility layers without call-site audit and tests. / Не удаляйте compatibility layers без call-site audit и tests.
- Do not change schema or storage format without migration and rollback notes. / Не меняйте schema или storage format без migration и rollback notes.
- Do not mix unrelated refactoring types in one stage. / Не смешивайте несвязанные виды рефакторинга в одном stage.
- Do not hide product behavior changes inside refactoring. / Не прячьте изменения product behavior внутри рефакторинга.
- Preserve public APIs, routes, files, and data formats unless the Issue allows changes. / Сохраняйте public APIs, routes, files и data formats, если Issue не разрешает изменения.

## Architecture boundaries / Архитектурные границы

When refactoring boundaries, define the intended direction of dependencies.
При рефакторинге границ определите ожидаемое направление зависимостей.

Add or update lightweight architecture checks when practical.
Добавьте или обновите lightweight architecture checks, когда это практично.

Examples / Примеры:

- UI should not import storage internals directly. / UI не должен напрямую импортировать storage internals.
- Repositories should not import UI. / Repositories не должны импортировать UI.
- Transport or provider calls should stay in approved adapters. / Transport или provider calls должны оставаться в approved adapters.
- Export or reporting code should not depend on interactive UI. / Export или reporting code не должен зависеть от interactive UI.

## Function-level optimization / Оптимизация функций

When optimizing existing functions, check for / При оптимизации существующих функций проверяйте:

- very long functions / слишком длинные функции;
- deep nested branching / глубокие вложенные ветвления;
- mixed responsibilities / смешанные ответственности;
- repeated calls or conversions / повторяющиеся calls или conversions;
- database or network calls inside loops / database или network calls внутри циклов;
- blocking work in async or UI paths / blocking work в async или UI paths;
- unclear error handling / неясную обработку ошибок;
- obsolete fallback branches / устаревшие fallback branches.

For each optimization, document / Для каждой оптимизации документируйте:

```text
Function or area:
Old problem:
Change:
Behavior changed: yes/no
Expected or measured benefit:
Tests:
```

## Agent instruction / Инструкция агенту

Perform the refactoring task described in the related GitHub Issue.
Выполните задачу рефакторинга, описанную в связанном GitHub Issue.

Before editing, read the required Agent Handoff files, related Issue or PR, current branch, recent commits, and active handoffs.
Перед изменениями прочитайте обязательные файлы Agent Handoff, связанное Issue или PR, текущую branch, последние commits и активные handoffs.

Before finishing, run checks, describe what changed and what was tested, list risks, and leave the required stage or final result comment.
Перед завершением запустите проверки, опишите изменения и проверки, укажите риски и оставьте обязательный stage или final result comment.
