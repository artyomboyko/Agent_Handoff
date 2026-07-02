# Русский

- [Стандарт](RU_STANDARD_FULL.md)
- [Инструкция](RU_GUIDE.md)
- [Протокол](PROTOCOL_RU.md)
- [Проект](PROJECT_RU.md)

## Сценарий 1: новый репозиторий

Попросите coding agent сразу создать проект со структурой Agent Handoff.

```text
Инициализируй этот репозиторий с Agent Handoff.
Используй последнюю версию стандарта из https://github.com/artyomboyko/Agent_Handoff.
Создай файлы Agent Handoff, GitHub issue templates и pull request template.
Заполни PROJECT_STATE.md начальным snapshot проекта.
Настрой HANDOFF_PROTOCOL.md со smoke tests для этого проекта.
Создай первый короткий handoff и обнови handoff index.
```

## Сценарий 2: существующий репозиторий

Попросите coding agent выполнить аккуратную миграцию.

```text
Внедри Agent Handoff в этот существующий репозиторий.
Используй последнюю версию стандарта из https://github.com/artyomboyko/Agent_Handoff.
Сначала изучи текущую структуру репозитория.
Не перезаписывай важные существующие файлы без анализа.
Аккуратно объедини похожие файлы.
Устаревшие длинные заметки при необходимости перенеси в ai/archive.
Актуальное состояние сожми в ai/PROJECT_STATE.md.
Устойчивые решения перенеси в ai/DECISIONS.md.
Настрой smoke tests в ai/HANDOFF_PROTOCOL.md.
Открой pull request и оставь короткий handoff.
```

English: [docs/en/README.md](../en/README.md)
