# AI Handoff Issue Labels

This file defines the recommended universal Issue labels for AI Handoff repositories.

The labels are intentionally small and task-oriented. They describe the type of work, not every subsystem in a project.

## Core labels

| Label | Use for |
|---|---|
| `bug` | A confirmed or suspected problem in behavior, structure, documentation, templates, or the standard. |
| `enhancement` | A proposed improvement to the standard, workflow, templates, or repository structure. |
| `refactoring` | Code cleanup, file decomposition, renaming, dead-code removal, or internal restructuring without intended behavior change. |
| `research` | Investigation, comparison, feasibility analysis, or design exploration before implementation. |
| `backlog` | Future work that is useful to keep, but not ready or not scheduled for immediate implementation. |
| `testing` | Test coverage gaps, failing checks, flaky checks, smoke-test improvements, or validation tasks. |
| `docs` | Documentation fixes, missing docs, unclear docs, examples, guides, README updates, or translation updates. |

## Rules

- Prefer one primary type label per Issue.
- Add extra labels only when they clarify routing.
- Keep project-specific area labels optional and separate from these universal labels.
- Do not use `ai/` files as a long issue backlog; use GitHub Issues.
- Use `backlog` for deferred work and `research` for investigation work.
- Use `testing` when the main task is about checks, coverage, validation, or test reliability.
- Use `docs` when the main deliverable is documentation.

## Template mapping

| Label | Issue form |
|---|---|
| `bug` | `.github/ISSUE_TEMPLATE/bug_report.yml` |
| `enhancement` | `.github/ISSUE_TEMPLATE/standard_change.yml` |
| `refactoring` | `.github/ISSUE_TEMPLATE/refactoring.yml` |
| `research` | `.github/ISSUE_TEMPLATE/research.yml` |
| `backlog` | `.github/ISSUE_TEMPLATE/backlog.yml` |
| `testing` | `.github/ISSUE_TEMPLATE/testing.yml` |
| `docs` | `.github/ISSUE_TEMPLATE/doc.yml` |
