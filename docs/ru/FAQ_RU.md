# FAQ / Частые вопросы

Эта страница соответствует `FAQ.md` и предназначена для быстрого чтения на русском.

## Что такое Agent Handoff?

Agent Handoff — GitHub-native стандарт передачи проектного контекста между AI-агентами, людьми-maintainers и агентами под контролем человека.

## Почему не достаточно chat memory?

Chat memory обычно привязана к одному инструменту, сессии или provider. Agent Handoff хранит компактный устойчивый контекст в репозитории рядом с Issues, Pull Requests и историей кода.

## Это замена README?

Нет. README объясняет проект людям. Agent Handoff добавляет workflow, ownership, компактную память и правила handoff для агентов и maintainers.

## Это замена GitHub Issues?

Нет. GitHub Issues и Pull Requests остаются источником правды по работе. Agent Handoff использует их как слой координации.

## Что хранится в `ai/`?

Компактное устойчивое состояние проекта, решения, протоколы и handoff indexes. Не храните secrets, полные logs, полные chats или большие generated data.

## Можно ли использовать с Codex, ChatGPT, Cursor, Claude Code или локальными агентами?

Да. Agent Handoff не привязан к конкретному инструменту. Он рассчитан на GitHub-based workflows и может использоваться людьми и разными coding agents.
