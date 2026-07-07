---
type: work_claim_protocol
version: 1
status: active
updated: 2026-07-04
project: Agent_Handoff
---

# Work Claim Protocol / Протокол claim работы

This file defines current work ownership in GitHub Issues and Pull Requests.
Этот файл описывает текущий ownership работы в GitHub Issues и Pull Requests.

## Before starting work / Перед началом работы

1. Read the Issue. / Прочитать Issue.
2. Check linked Pull Requests. / Проверить связанные Pull Requests.
3. Check active handoffs. / Проверить активные handoffs.
4. Choose `agent_name`, `agent_id`, and `run_id`. / Выбрать `agent_name`, `agent_id` и `run_id`.
5. Leave a work claim comment. / Оставить work claim comment.
6. Plan stage or final result reports using `ai/TASK_REPORT_PROTOCOL.md`. / Запланировать stage или final result reports по `ai/TASK_REPORT_PROTOCOL.md`.
7. Create a branch and Draft PR early. / Рано создать branch и Draft PR.

## Claim comment / Claim comment

```md
## Agent Handoff Work Claim

Agent: <agent_name>
Agent ID: <agent_id>
Run ID: <run_id>
Coordinator: <coordinator>
Supervision: autonomous | human-supervised | human-driven
Started: YYYY-MM-DD HH:MM UTC
Issue: #<issue-number>
Branch: <branch-name>
Draft PR: #<pr-number or TBD>
Scope: <short scope>
Status: in-progress
Next update: <time or condition>
```

## Update comment / Update comment

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

## Result comments / Comments результата

Every meaningful Issue must have result comments.
Каждое значимое Issue должно иметь result comments.

Large or multi-stage Issues use stage result comments after each stable stage.
Большие или многоэтапные Issues используют stage result comments после каждого стабильного stage.

Small Issues use one final result comment before completion.
Небольшие Issues используют один final result comment перед завершением.

Use `ai/TASK_REPORT_PROTOCOL.md` for templates.
Используйте `ai/TASK_REPORT_PROTOCOL.md` для templates.

## Done / Завершение

When work is finished, write what changed, what was tested, remaining risks, related PR or handoff, and the required result comment.
После завершения укажите изменения, проверки, оставшиеся риски, связанный PR или handoff и обязательный result comment.

If an Issue or PR already has a recent work claim, coordinate before continuing.
Если в Issue или PR уже есть свежий work claim, согласуйте действия перед продолжением.
