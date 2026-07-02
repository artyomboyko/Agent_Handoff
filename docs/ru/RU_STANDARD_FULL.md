# Стандарт Agent Handoff

Agent Handoff описывает, как хранить и передавать проектный контекст между AI-агентами через GitHub, Git и `ai/`.

## Модель

GitHub управляет задачами, Pull Request, ревью, CI и обсуждениями.

Git хранит код, ветки, коммиты, diff и историю.

`ai/` хранит компактную долговременную память проекта.

`ai/handoffs/` хранит короткие снимки сессий.

## Приоритет

1. Текущая branch и Git state.
2. GitHub Pull Request.
3. GitHub Issue.
4. Work claim comments в Issue или PR.
5. `ai/PROJECT_STATE.md`.
6. `ai/DECISIONS.md`.
7. Handoff-файлы.

## Структура

- `AGENTS.md`
- `AGENT_HANDOFF_STANDARD.md`
- `ISSUE_LABELS.md`
- `ai/README.md`
- `ai/PROJECT_STATE.md`
- `ai/DECISIONS.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/AGENT_IDENTITY.md`
- `ai/WORK_CLAIM_PROTOCOL.md`
- `ai/REFACTORING.md`
- `ai/handoffs/INDEX.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `docs/en/`
- `docs/ru/`

## Метки Issue

Базовые универсальные метки:

- `bug` — ошибка или проблема.
- `enhancement` — улучшение стандарта, workflow или шаблонов.
- `refactoring` — cleanup, decomposition, renaming или внутреннее упрощение без намеренного изменения поведения.
- `research` — исследование, сравнение подходов или подготовка решения.
- `backlog` — отложенная полезная работа.
- `testing` — тесты, smoke checks, validation или нестабильные проверки.
- `docs` — документация, README, примеры, guides или переводы.

Статусные метки:

- `in-progress` — работа взята агентом или maintainer'ом.
- `blocked` — работа временно заблокирована.

Подробная таблица: `ISSUE_LABELS.md`.

## Завершение

Перед завершением значимого изменения нужны smoke tests, обновлённый PR, короткий handoff и обновлённый index.

## Размеры

`ai/` должен быть компактным. Большие diff, длинные выводы команд, полные обсуждения и артефакты остаются в GitHub, Git или другом подходящем месте.

## Финальное правило

Код меняется вместе с компактным контекстом для следующего агента.
