---
type: project_state
version: 1
status: active
updated: 2026-07-04
project: Agent_Handoff
---

# Project State / Состояние проекта

## Current phase / Текущая фаза

Agent Handoff Standard 1.2 is implemented, public, and in final pre-release consistency review.
Agent Handoff Standard 1.2 реализован, публичен и находится на финальной проверке согласованности перед release.

The repository has a landing README, bilingual documentation indexes, bilingual Issue Forms, bilingual PR template, Coordinated GitHub Flow, agent identity, work claim, refactoring workflow, FAQ, examples, contributing guide, security policy, code of conduct, changelog, promotion checklist, social preview asset, GitHub Actions checks, GitHub Pages site, and citation metadata.
В репозитории есть landing README, двуязычные индексы документации, двуязычные Issue Forms, двуязычный PR template, Coordinated GitHub Flow, agent identity, work claim, refactoring workflow, FAQ, examples, contributing guide, security policy, code of conduct, changelog, promotion checklist, social preview asset, GitHub Actions checks, GitHub Pages site и citation metadata.

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
- Automated checks / Автоматические проверки: `.github/workflows/standard-check.yml`, `scripts/check_agent_handoff.py`
- Public site / Публичный сайт: `docs/index.html`, `docs/404.html`, `docs/robots.txt`, `docs/sitemap.xml`
- Community files / Community files: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `docs/COMMUNITY_FILES.md`
- Discovery files / Файлы продвижения: `README.md`, `FAQ.md`, `CITATION.cff`, `docs/en/FAQ_EN.md`, `docs/ru/FAQ_RU.md`, `examples/`, `assets/social-preview.svg`, `.github/REPOSITORY_SETTINGS.md`, `docs/en/REPOSITORY_SETTINGS_EN.md`, `docs/ru/REPOSITORY_SETTINGS_RU.md`, `docs/en/PROMOTION_CHECKLIST_EN.md`, `docs/ru/PROMOTION_CHECKLIST_RU.md`
- Language docs / Языковая документация: `docs/en/`, `docs/ru/`

## Implemented / Реализовано

- Agent Handoff Standard 1.2.
- Public GitHub repository.
- Landing README with problem, solution, diagram, quick start, principles, comparison, search terms, humans/agents sections.
- English and Russian standard documents are intended to stay synchronized in structure and meaning.
- Coordinated GitHub Flow.
- Meaningful branch naming without `/`, Issue numbers, or random identifiers by default.
- Extended status labels: `needs-triage`, `ready`, `in-progress`, `blocked`, `in-review`, `changes-requested`, `ready-to-merge`.
- Agent identity and run IDs.
- Work claim protocol with coordinator and supervision fields.
- Issue labels and bilingual Issue Forms with explicit Issue language selector.
- Bilingual Pull Request template aligned with Done checklist.
- Bilingual documentation indexes.
- FAQ with English and Russian mirrors.
- Promotion checklist and repository settings with English and Russian mirrors.
- Examples, contributing guide, security policy, code of conduct, changelog.
- Community files index.
- Social preview SVG asset and GitHub social preview upload.
- Repository discovery settings guide with About description, Website, and topics.
- GitHub Pages site published from `/docs`.
- GitHub Actions checks workflow.
- Citation metadata through `CITATION.cff`.

## Known risks / Известные риски

- GitHub Issue Forms must remain valid YAML.
- GitHub Issue Forms должны оставаться валидным YAML.
- Repository documentation should remain synchronized after final pre-release consistency fixes.
- Документация репозитория должна оставаться синхронизированной после финальных pre-release исправлений.

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
- `scripts/check_agent_handoff.py`
- `docs/index.html`
- `CITATION.cff`

## Next likely milestones / Следующие шаги

1. Complete final consistency fixes. / Завершить финальные исправления согласованности.
2. Confirm GitHub Actions checks and Pages deployment are green. / Проверить, что GitHub Actions checks и Pages deployment зелёные.
3. Prepare public release `v1.2`. / Подготовить public release `v1.2`.
