---
type: project_state
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Project State / Состояние проекта

## Current phase / Текущая фаза

Agent Handoff Standard 1.2 is implemented and prepared for public presentation.
Agent Handoff Standard 1.2 реализован и подготовлен к публичному оформлению.

The repository has a landing README, bilingual documentation indexes, bilingual Issue Forms, bilingual PR template, Coordinated GitHub Flow, agent identity, work claim, refactoring workflow, FAQ, examples, contributing guide, security policy, code of conduct, changelog, promotion checklist, and social preview asset.
В репозитории есть landing README, двуязычные индексы документации, двуязычные Issue Forms, двуязычный PR template, Coordinated GitHub Flow, agent identity, work claim, refactoring workflow, FAQ, examples, contributing guide, security policy, code of conduct, changelog, promotion checklist и social preview asset.

## Main subsystems / Основные подсистемы

- Standard / Стандарт: `AGENT_HANDOFF_STANDARD.md`, `docs/ru/RU_STANDARD_FULL.md`
- Agent entrypoint / Точка входа агента: `AGENTS.md`
- Project memory / Память проекта: `ai/`
- GitHub workflow / GitHub workflow: `ai/GITHUB_WORKFLOW.md`
- Agent identity / Идентификация агента: `ai/AGENT_IDENTITY.md`
- Work claim / Claim работы: `ai/WORK_CLAIM_PROTOCOL.md`
- Refactoring / Рефакторинг: `ai/REFACTORING.md`
- Handoffs / Handoffs: `ai/handoffs/`
- GitHub templates / GitHub templates: `.github/`
- Community files / Community files: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`
- Discovery files / Файлы продвижения: `README.md`, `FAQ.md`, `docs/en/FAQ_EN.md`, `docs/ru/FAQ_RU.md`, `examples/`, `assets/social-preview.svg`, `.github/REPOSITORY_SETTINGS.md`
- Language docs / Языковая документация: `docs/en/`, `docs/ru/`

## Implemented / Реализовано

- Agent Handoff Standard 1.2.
- Landing README with problem, solution, diagram, quick start, principles, comparison, search terms, humans/agents sections.
- English and Russian standard documents are synchronized in structure and meaning.
- Coordinated GitHub Flow.
- Meaningful branch naming without `/`, Issue numbers, or random identifiers by default.
- Extended status labels: `needs-triage`, `ready`, `in-progress`, `blocked`, `in-review`, `changes-requested`, `ready-to-merge`.
- Agent identity and run IDs.
- Work claim protocol with coordinator and supervision fields.
- Issue labels and bilingual Issue Forms.
- Bilingual Pull Request template aligned with Done checklist.
- Bilingual documentation indexes.
- FAQ with English and Russian mirrors.
- Examples, contributing guide, security policy, code of conduct, changelog.
- Social preview SVG asset.
- Repository discovery settings guide with About description and topics.

## Known risks / Известные риски

- Repository is still private; Google and GitHub public discovery require public visibility.
- Репозиторий всё ещё private; для Google и GitHub public discovery нужна public visibility.
- GitHub About description, topics, and social preview must be set manually in GitHub UI.
- GitHub About description, topics и social preview нужно установить вручную в GitHub UI.
- GitHub Issue Forms must remain valid YAML.
- GitHub Issue Forms должны оставаться валидным YAML.

## Sensitive areas / Чувствительные области

- `README.md`
- `AGENT_HANDOFF_STANDARD.md`
- `docs/ru/RU_STANDARD_FULL.md`
- `AGENTS.md`
- `ai/GITHUB_WORKFLOW.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/AGENT_IDENTITY.md`
- `ai/WORK_CLAIM_PROTOCOL.md`
- `ai/REFACTORING.md`
- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/pull_request_template.md`
- `.github/REPOSITORY_SETTINGS.md`

## Next likely milestones / Следующие шаги

1. Review all Issue Forms in GitHub UI. / Проверить все Issue Forms в GitHub UI.
2. Apply About description, topics, and social preview in GitHub settings. / Применить About description, topics и social preview в GitHub settings.
3. Add automated Markdown/YAML checks. / Добавить автоматические проверки Markdown/YAML.
4. Prepare public release `v1.2`. / Подготовить public release `v1.2`.
