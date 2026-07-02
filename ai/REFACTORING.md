---
type: refactoring_protocol
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Refactoring Workflow / Workflow рефакторинга

This file is a compact entry point for cleanup, decomposition, renaming, and internal restructuring.
Этот файл — компактная точка входа для cleanup, decomposition, renaming и внутренней перестройки.

Track concrete tasks in GitHub Issues.
Конкретные задачи ведите в GitHub Issues.

Keep this file as protocol, not as a long backlog.
Держите этот файл как протокол, а не длинный backlog.

## Use for / Использовать для

- splitting large files / разделение больших файлов;
- removing unused code / удаление неиспользуемого кода;
- simplifying duplicated logic / упрощение дублирующейся логики;
- renaming confusing internal names / переименование непонятных внутренних имён;
- moving responsibilities to clearer modules / перенос ответственности в понятные модули.

## Do not use for / Не использовать для

- product features / продуктовые функции;
- research notes / заметки исследования;
- ordinary bug reports / обычные bug reports;
- long logs / длинные логи;
- full diffs / полные diff.

## Issue fields / Поля Issue

A cleanup Issue should include / Cleanup Issue должен включать:

- code area / область кода;
- current problem / текущая проблема;
- target state / целевое состояние;
- non-goals / что не входит в задачу;
- risk / риск;
- required checks / обязательные проверки;
- related files or PRs / связанные файлы или PR.

## Agent instruction / Инструкция агенту

Perform the cleanup task described in the related GitHub Issue.
Выполните cleanup-задачу, описанную в связанном GitHub Issue.

Before editing, read the required Agent Handoff files, related Issue or PR, current branch, recent commits, and active handoffs.
Перед изменениями прочитайте обязательные файлы Agent Handoff, связанное Issue или PR, текущую branch, последние commits и активные handoffs.

Keep external behavior unchanged unless the Issue explicitly allows it.
Не меняйте внешнее поведение, если Issue явно этого не разрешает.

Before finishing, run checks, describe what changed and what was tested, list risks, and add a short handoff when useful.
Перед завершением запустите проверки, опишите изменения и проверки, укажите риски и добавьте короткий handoff при необходимости.
