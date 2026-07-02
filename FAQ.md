# FAQ / Частые вопросы

## What is Agent Handoff? / Что такое Agent Handoff?

Agent Handoff is a GitHub-native standard for passing project context between AI coding agents, human maintainers, and human-supervised agents.

Agent Handoff — GitHub-native стандарт передачи проектного контекста между AI-агентами, людьми-maintainers и агентами под контролем человека.

## Why not just use chat memory? / Почему не достаточно chat memory?

Chat memory is usually tied to one tool, session, or provider. Agent Handoff stores compact durable context in the repository, next to Issues, Pull Requests, and code history.

Chat memory обычно привязана к одному инструменту, сессии или provider. Agent Handoff хранит компактный устойчивый контекст в репозитории рядом с Issues, Pull Requests и историей кода.

## Is this a replacement for README? / Это замена README?

No. README explains the project to people. Agent Handoff adds workflow, ownership, compact memory, and handoff rules for agents and maintainers.

Нет. README объясняет проект людям. Agent Handoff добавляет workflow, ownership, компактную память и правила handoff для агентов и maintainers.

## Is this a replacement for GitHub Issues? / Это замена GitHub Issues?

No. GitHub Issues and Pull Requests remain the source of work truth. Agent Handoff uses them as the coordination layer.

Нет. GitHub Issues и Pull Requests остаются источником правды по работе. Agent Handoff использует их как слой координации.

## What is stored in `ai/`? / Что хранится в `ai/`?

Compact durable project state, decisions, protocols, and handoff indexes. Do not store secrets, full logs, full chats, or large generated data.

Компактное устойчивое состояние проекта, решения, протоколы и handoff indexes. Не храните secrets, полные logs, полные chats или большие generated data.

## Can I use it with Codex, ChatGPT, Cursor, Claude Code, or local agents? / Можно ли использовать с Codex, ChatGPT, Cursor, Claude Code или локальными агентами?

Yes. Agent Handoff is tool-agnostic. It is designed for GitHub-based workflows and can be used by humans and different coding agents.

Да. Agent Handoff не привязан к конкретному инструменту. Он рассчитан на GitHub-based workflows и может использоваться людьми и разными coding agents.

## Which language should a repository use? / На каком языке работать в репозитории?

Use English for English repositories and Russian for Russian repositories. Bilingual standard documents should keep matching meaning.

Используйте английский для английских репозиториев и русский для русских репозиториев. Двуязычные документы стандарта должны сохранять соответствие смысла.

## Do branch names include Issue numbers? / Нужны ли номера Issue в именах веток?

No by default. Use meaningful branch names such as `workflow-branch-naming` or `docs-readme-quickstart`. Link Issues through Work Claim comments, PR descriptions, GitHub links, and handoff metadata.

По умолчанию нет. Используйте осмысленные имена веток, например `workflow-branch-naming` или `docs-readme-quickstart`. Связывайте Issues через Work Claim comments, PR descriptions, GitHub links и handoff metadata.

## Is Agent Handoff only for large teams? / Agent Handoff только для больших команд?

No. It is most useful for medium repositories and mixed human-agent work, but the minimal version can also help solo developers.

Нет. Он наиболее полезен для средних репозиториев и mixed human-agent work, но минимальная версия полезна и solo developers.
