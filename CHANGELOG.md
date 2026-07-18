# Changelog

All notable changes to Agent Handoff are documented here.

## 1.3 - 2026-07-18

### Added

- GUI testing rule that prohibits brittle automated tests based on absolute coordinates, screen position, pixel offsets, or incidental layout order.
- `ai/CONTAINERIZATION.md` with supported Docker and Docker Compose organization approaches.
- Supported containerization choices for no repository-managed containers, colocated files, centralized `docker/`, hybrid layout, modular monorepos, separate deployment repositories, and established custom layouts.
- Container layout migration inventory, verification, project-memory, and handoff requirements.
- Release notes in `docs/releases/v1.3.md`.

### Changed

- New-repository initialization and existing-repository adoption now require a separate, explicit user decision about containerization and file layout.
- Agents may not infer, create, relocate, consolidate, or migrate container infrastructure before the user answers the mandatory question.
- The hybrid layout is a recommended option to present, not an automatic default.
- Repository checks and the Pull Request checklist now cover the containerization protocol and decision gate.

## 1.2 - 2026-07-07

### Added

- Coordinated GitHub Flow for humans, autonomous agents, and human-supervised agents.
- Meaningful branch naming without `/`, Issue numbers, or random identifiers by default.
- Agent identity protocol with `agent_name`, `agent_id`, and `run_id`.
- Work Claim protocol with `Coordinator` and `Supervision` fields.
- Mandatory task result reports for large multi-stage Issues and small Issues.
- Refactoring workflow and matching Issue form fields.
- Landing README with problem, solution, use cases, comparison, and search terms.
- GitHub Pages landing site from `/docs`.
- GitHub Actions checks workflow for repository structure and YAML validation.
- `CITATION.cff` metadata.
- Repository discovery settings for About, Website, topics, and social preview.

### Changed

- Repository documentation and templates simplified to English-only canonical files.
- Repository license note finalized as GPL-3.0.
- Repository Website moved from the repository URL to the GitHub Pages site.
- Repository topics aligned with the current public About sidebar.
- Social preview asset updated to use `AI memory` instead of ambiguous `ai/`.

## 1.1 - 2026-06-29

### Added

- Initial Agent Handoff standard structure.
- `ai/` memory map.
- Handoff index.
- Basic Issue and Pull Request templates.
