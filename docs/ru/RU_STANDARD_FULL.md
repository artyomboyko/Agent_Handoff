# Стандарт AI Handoff

AI Handoff описывает, как хранить и передавать проектный контекст через GitHub, Git и `ai/`.

## Модель

GitHub управляет задачами, Pull Request, ревью, CI и обсуждениями.

Git хранит код, ветки, коммиты, diff и историю.

`ai/` хранит компактную долговременную память проекта.

`ai/handoffs/` хранит короткие снимки сессий.

## Приоритет

1. Текущая branch и Git state.
2. GitHub Pull Request.
3. GitHub Issue.
4. `ai/PROJECT_STATE.md`.
5. `ai/DECISIONS.md`.
6. Handoff-файлы.

## Структура

- `AGENTS.md`
- `AI_HANDOFF_STANDARD.md`
- `ai/README.md`
- `ai/PROJECT_STATE.md`
- `ai/DECISIONS.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/handoffs/INDEX.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `docs/en/`
- `docs/ru/`

## Завершение

Перед завершением значимого изменения нужны smoke tests, обновлённый PR, короткий handoff и обновлённый index.

## Размеры

`ai/` должен быть компактным. Большие diff, длинные выводы команд, полные обсуждения и артефакты остаются в GitHub, Git или другом подходящем месте.

## Финальное правило

Код меняется вместе с компактным контекстом для следующего агента.
