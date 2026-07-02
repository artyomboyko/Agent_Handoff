---
type: work_claim_protocol
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Work Claim Protocol / Протокол claim работы

This file defines work ownership in GitHub Issues and Pull Requests.
Этот файл описывает ownership работы в GitHub Issues и Pull Requests.

Current ownership is written in GitHub.
Текущий ownership записывается в GitHub.

## Before starting work / Перед началом работы

1. Read the Issue. / Прочитать Issue.
2. Check linked Pull Requests. / Проверить связанные Pull Requests.
3. Check active handoffs. / Проверить активные handoffs.
4. Choose `agent_name`, `agent_id`, and `run_id`. / Выбрать `agent_name`, `agent_id` и `run_id`.
5. Leave a work claim comment. / Оставить work claim comment.
6. Add coordinator and supervision fields. / Добавить поля coordinator и supervision.
7. Create a branch and Draft PR early. / Рано создать branch и Draft PR.

## Claim comment / Claim comment

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

## Done / Завершение

When work is finished, write what changed, what was tested, remaining risks, and related PR or handoff.
После завершения укажите изменения, проверки, оставшиеся риски и связанный PR или handoff.

If an Issue or PR already has a recent work claim, coordinate before continuing.
Если в Issue или PR уже есть свежий work claim, согласуйте действия перед продолжением.
