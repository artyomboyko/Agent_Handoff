# Протокол / Protocol

Эта страница соответствует `ai/HANDOFF_PROTOCOL.md` и кратко повторяет его по-русски.

## Старт

Перед работой агент читает:

1. `AGENTS.md`
2. `AGENT_HANDOFF_STANDARD.md`
3. `ai/README.md`
4. `ai/GITHUB_WORKFLOW.md`
5. `ai/AGENT_IDENTITY.md`
6. `ai/WORK_CLAIM_PROTOCOL.md`
7. `ai/PROJECT_STATE.md`
8. `ai/DECISIONS.md`
9. связанное Issue или PR
10. `ai/handoffs/INDEX.md`

## Claim работы

Перед изменениями агент оставляет Work Claim comment в Issue и повторяет identity в Draft PR.

## Scope

Одна значимая задача = одно Issue, одна branch, один PR и один ясный scope.

Branch должна иметь осмысленное имя без `/`, номеров Issue и случайных идентификаторов по умолчанию.

## Проверки

Перед завершением нужны smoke tests. Если проверки не запущены, нужно указать причину, риск и следующий шаг.

## Завершение

PR должен быть обновлён, риски описаны, handoff добавлен при необходимости, а `ai/handoffs/INDEX.md` обновлён.
