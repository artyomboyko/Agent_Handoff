---
type: agent_identity_protocol
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Agent Identity Protocol / Протокол идентификации агента

This file defines how AI agents name themselves during parallel work.
Этот файл описывает, как AI-агенты называют себя при параллельной работе.

Current work ownership lives in GitHub Issues, Pull Requests, labels, branches, and handoffs.
Текущий ownership работы хранится в GitHub Issues, Pull Requests, labels, branches и handoffs.

Each agent run should use / Каждый запуск агента должен использовать:

- `agent_name` — human-readable name / понятное человеку имя.
- `agent_id` — short slug for this repository / короткий slug для репозитория.
- `run_id` — unique id for the current session / уникальный id текущей сессии.

Example / Пример:

```text
Agent: North Fox
Agent ID: north-fox-7c2a
Run ID: 20260702-issue-14-a91f
```

Recommended agent id format / Формат agent id:

```text
<two-words-slug>-<4-hex>
```

Recommended run id format / Формат run id:

```text
YYYYMMDD-issue-<number>-<4-hex>
```

Repeat `agent_name`, `agent_id`, and `run_id` in work claim, Draft PR, handoff metadata, and handoff index when relevant.
Повторяйте `agent_name`, `agent_id` и `run_id` в work claim, Draft PR, metadata handoff и handoff index при необходимости.

Do not keep an active agent registry in `ai/`.
Не храните активный registry агентов в `ai/`.
