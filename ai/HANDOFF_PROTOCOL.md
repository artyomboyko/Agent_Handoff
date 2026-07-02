---
type: handoff_protocol
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Handoff Protocol / Протокол handoff

## Start / Старт

Read the required files before work.
Перед работой прочитайте обязательные файлы.

1. `AGENTS.md`
2. `AGENT_HANDOFF_STANDARD.md`
3. `ai/README.md`
4. `ai/GITHUB_WORKFLOW.md`
5. `ai/AGENT_IDENTITY.md`
6. `ai/WORK_CLAIM_PROTOCOL.md`
7. `ai/PROJECT_STATE.md`
8. `ai/DECISIONS.md`
9. Related Issue or PR / Связанное Issue или PR
10. Current branch and recent commits / Текущая branch и последние commits
11. `ai/handoffs/INDEX.md`

Choose `agent_name`, `agent_id`, and `run_id` before taking work.
Перед работой выберите `agent_name`, `agent_id` и `run_id`.

## Work claim / Claim работы

Before editing, leave a work claim comment using `ai/WORK_CLAIM_PROTOCOL.md`.
Перед изменениями оставьте work claim comment по `ai/WORK_CLAIM_PROTOCOL.md`.

## Scope / Scope

One meaningful work item should have one Issue, one branch, one PR, and one clear scope.
Одна значимая задача должна иметь одно Issue, одну branch, один PR и один ясный scope.

Use meaningful branch names without `/`, Issue numbers, or random identifiers by default.
Используйте осмысленные имена branch без `/`, номеров Issue и случайных идентификаторов по умолчанию.

Open a Draft PR early.
Открывайте Draft PR рано.

## Smoke tests / Smoke-проверки

Smoke tests are mandatory before marking work ready or setting a handoff to `completed`.
Smoke-проверки обязательны перед готовностью работы или статусом handoff `completed`.

Repository checks / Проверки репозитория:

1. Required files exist. / Обязательные файлы существуют.
2. Markdown links work. / Markdown-ссылки работают.
3. Issue Forms are valid YAML. / Issue Forms являются валидным YAML.
4. PR template includes the checklist. / PR template содержит checklist.
5. Handoff index is updated when needed. / Handoff index обновлён при необходимости.

## Done checklist / Checklist завершения

- [ ] Related Issue or PR is linked. / Связанное Issue или PR указано.
- [ ] Work claim comment exists. / Work claim comment существует.
- [ ] Branch contains only intended changes. / Branch содержит только ожидаемые изменения.
- [ ] Smoke tests were run or reason is documented. / Smoke tests выполнены или причина описана.
- [ ] PR description is updated. / PR description обновлён.
- [ ] Risks are listed. / Риски указаны.
- [ ] Handoff file is created when needed. / Handoff-файл создан при необходимости.
- [ ] `ai/handoffs/INDEX.md` is updated when needed. / `ai/handoffs/INDEX.md` обновлён при необходимости.

## Parallel work / Параллельная работа

Before editing shared files, check open PRs, related Issues, recent commits, active handoffs, and recent work claim comments.
Перед изменением общих файлов проверьте открытые PR, связанные Issues, последние commits, активные handoff и последние work claim comments.
