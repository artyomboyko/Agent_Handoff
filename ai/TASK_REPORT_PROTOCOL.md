---
type: task_report_protocol
version: 1
status: active
updated: 2026-07-04
project: Agent_Handoff
---

# Task Report Protocol / Протокол отчётов по задачам

This file defines mandatory result comments for GitHub Issues and Pull Requests.
Этот файл описывает обязательные result comments для GitHub Issues и Pull Requests.

Task reports are written in the related Issue or PR so humans and agents can follow progress without reading chat history.
Task reports пишутся в связанном Issue или PR, чтобы люди и агенты могли отслеживать прогресс без чтения истории чата.

## Rule / Правило

Every meaningful Issue must have a result comment.
Каждое значимое Issue должно иметь result comment.

Large or multi-stage Issues must have one result comment after each stable stage.
Большие или многоэтапные Issues должны иметь result comment после каждого стабильного stage.

Small Issues may have one final result comment.
Небольшие Issues могут иметь один итоговый result comment.

## Large or multi-stage tasks / Большие или многоэтапные задачи

For each stage, an agent must / Для каждого stage агент должен:

1. record findings / зафиксировать, что найдено;
2. make a small focused change / сделать маленькое сфокусированное изменение;
3. run targeted tests or document why they were not run / запустить targeted tests или объяснить, почему они не запускались;
4. update AI or project docs when relevant / обновить AI или project docs, когда это релевантно;
5. make a bilingual commit when the repository is bilingual / сделать bilingual commit, если репозиторий двуязычный;
6. continue only after the layer is stable / продолжать только после стабильного слоя;
7. leave a stage result comment / оставить stage result comment.

## Small tasks / Небольшие задачи

For a small single-stage Issue, an agent must leave one final result comment before marking the work done.
Для небольшой одноэтапной Issue агент должен оставить один итоговый result comment перед завершением работы.

## Stage result comment / Comment результата stage

```md
## Agent Handoff Stage Result

Stage: <number or name>
Agent ID: <agent_id>
Run ID: <run_id>
Status: completed | blocked | partial

Findings:
- <what was found>

Changed:
- <small focused change>

Not changed:
- <explicit non-changes or preserved behavior>

Tests:
- <targeted tests and result, or reason not run>

Docs:
- <docs updated or not needed>

Commit:
- <commit sha or not committed yet>

Risks:
- <remaining risks>

Next:
- <next stage or handoff target>
```

## Final result comment / Итоговый comment результата

```md
## Agent Handoff Final Result

Agent ID: <agent_id>
Run ID: <run_id>
Status: completed | blocked | partial

Summary:
- <what was done>

Changed:
- <files, modules, docs, or behavior changed>

Not changed:
- <explicit non-changes or preserved behavior>

Tests:
- <checks and smoke tests, or reason not run>

Docs:
- <docs updated or not needed>

Commits:
- <commit shas>

Risks:
- <remaining risks>

Follow-up:
- <next work, if any>
```

## Stability gate / Gate стабильности

A multi-stage Issue must not move to the next stage until the current stage has a result comment and the checks for that stage are stable or the blocker is documented.
Многоэтапная Issue не должна переходить к следующему stage, пока текущий stage не имеет result comment, а проверки этого stage не стабильны или blocker не описан.
