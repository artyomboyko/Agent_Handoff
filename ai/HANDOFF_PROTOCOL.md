---
type: handoff_protocol
version: 1
status: active
updated: 2026-07-04
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
7. `ai/TASK_REPORT_PROTOCOL.md`
8. `ai/PROJECT_STATE.md`
9. `ai/DECISIONS.md`
10. Related Issue or PR / Связанное Issue или PR
11. Current branch and recent commits / Текущая branch и последние commits
12. `ai/handoffs/INDEX.md`

Choose `agent_name`, `agent_id`, and `run_id` before taking work.
Перед работой выберите `agent_name`, `agent_id` и `run_id`.

## Work claim / Claim работы

Before editing, leave a work claim comment using `ai/WORK_CLAIM_PROTOCOL.md`.
Перед изменениями оставьте work claim comment по `ai/WORK_CLAIM_PROTOCOL.md`.

## Task reports / Отчёты по задачам

Result comments are required for meaningful Issues.
Result comments обязательны для значимых Issues.

Large or multi-stage Issues use stage result comments after stable stages.
Большие или многоэтапные Issues используют stage result comments после стабильных stages.

Small Issues use one final result comment before completion.
Небольшие Issues используют один final result comment перед завершением.

Use `ai/TASK_REPORT_PROTOCOL.md`.
Используйте `ai/TASK_REPORT_PROTOCOL.md`.

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

Current automated repository checks / Текущие автоматические проверки репозитория:

1. Required files exist. / Обязательные файлы существуют.
2. Issue Forms and workflows are valid YAML. / Issue Forms и workflows являются валидным YAML.
3. Issue Forms include a clear Issue language selector. / Issue Forms содержат понятный selector языка заполнения Issue.
4. PR template includes the required checklist. / PR template содержит обязательный checklist.
5. English and Russian documentation indexes have matching item counts. / Английский и русский индексы документации имеют одинаковое число пунктов.
6. Social preview asset uses the expected 1280x640 size and no ambiguous `ai/` label. / Social preview asset использует ожидаемый размер 1280x640 и не содержит неоднозначный label `ai/`.

## Done checklist / Checklist завершения

- [ ] Related Issue or PR is linked. / Связанное Issue или PR указано.
- [ ] Work claim comment exists. / Work claim comment существует.
- [ ] Required stage or final result comment exists. / Обязательный stage или final result comment существует.
- [ ] Branch contains only intended changes. / Branch содержит только ожидаемые изменения.
- [ ] Smoke tests were run or reason is documented. / Smoke tests выполнены или причина описана.
- [ ] PR description is updated. / PR description обновлён.
- [ ] Risks are listed. / Риски указаны.
- [ ] Handoff file is created when needed. / Handoff-файл создан при необходимости.
- [ ] `ai/handoffs/INDEX.md` is updated when needed. / `ai/handoffs/INDEX.md` обновлён при необходимости.
