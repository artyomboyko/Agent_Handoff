---
standard: Agent Handoff
version: "1.5"
status: active
updated: 2026-07-26
---

# Agent Handoff Standard

Agent Handoff is a compact standard for passing development state between humans, AI agents, and human-supervised agents through GitHub, Git, and small repository-tracked memory files.

This repository is maintained in English. Downstream projects may adapt the standard to another project language, but the canonical files in this repository stay English-only.

## Core model

```text
GitHub manages work: Issues, Pull Requests, reviews, checks, labels, comments, and current ownership.
Git stores code: branches, commits, diffs, tags, and history.
ai/ stores compact durable memory and agent protocols.
ai/handoffs/ stores short snapshots of agent runs.
```

## Required files

```text
AGENTS.md
AGENT_HANDOFF_STANDARD.md
ISSUE_LABELS.md
ISSUE_STATUS.md
ai/README.md
ai/PROJECT_STATE.md
ai/DECISIONS.md
ai/GITHUB_WORKFLOW.md
ai/HANDOFF_PROTOCOL.md
ai/AGENT_IDENTITY.md
ai/WORK_CLAIM_PROTOCOL.md
ai/TASK_REPORT_PROTOCOL.md
ai/REFACTORING.md
ai/handoffs/INDEX.md
.github/ISSUE_TEMPLATE/
.github/pull_request_template.md
docs/en/
```

For projects that use or plan Docker or Docker Compose, `ai/CONTAINERIZATION.md` is also required.

## Start order

Before meaningful work, read:

1. `AGENTS.md`
2. `AGENT_HANDOFF_STANDARD.md`
3. `ai/README.md`
4. `ai/GITHUB_WORKFLOW.md`
5. `ai/HANDOFF_PROTOCOL.md`
6. `ai/AGENT_IDENTITY.md`
7. `ai/WORK_CLAIM_PROTOCOL.md`
8. `ai/TASK_REPORT_PROTOCOL.md`
9. `ai/PROJECT_STATE.md`
10. `ai/DECISIONS.md`
11. `ai/CONTAINERIZATION.md` when Docker or Compose is used, planned, or being discussed
12. related GitHub Issue or Pull Request
13. relevant handoffs through `ai/handoffs/INDEX.md`

## Task result reports

Task result comments are mandatory for meaningful Issues.

Large or multi-stage Issues must have a stage result comment after each legitimate outcome stage.

Small single-stage Issues must have one final result comment before the work is marked done.

Use `ai/TASK_REPORT_PROTOCOL.md` for the required comment templates.

## Workflow

1. Select or create a GitHub Issue.
2. Check existing work claims, linked PRs, active handoffs, and recent comments.
3. Choose agent identity.
4. Claim the work.
5. Define the primary outcome, smallest acceptance proof, execution envelope, and stages when the task is large.
6. Create a meaningful short-lived branch.
7. Open a Draft PR early.
8. Write required stage or final result comments in the Issue or PR.
9. Commit changes.
10. Run checks and smoke tests.
11. Update PR description.
12. Leave a handoff when work is completed or interrupted.

## Repository initialization and adoption decision gate

When Agent Handoff is initialized in a new repository or added to an existing repository, the agent MUST inspect the repository and ask the user a separate, explicit question about containerization before changing any Docker or Compose structure.

The question must confirm:

- whether Docker or Docker Compose is used now or planned;
- which container file layout the user wants;
- for an existing repository, whether the current layout must be preserved or may be migrated;
- whether production deployment configuration belongs in the same repository or a separate deployment repository.

The agent MUST NOT infer this decision from existing files, an empty repository, general best practices, or the recommended default.

Until the user answers, the agent must not create, move, rename, delete, or consolidate Dockerfiles, Compose files, build contexts, ignore files, container scripts, environment-file references, or container configuration.

For an unanswered new-repository decision, create no container infrastructure. For an unanswered existing-repository decision, preserve the current layout.

## Containerized project organization

Agent Handoff supports these approaches:

1. no repository-managed containerization;
2. Dockerfiles colocated with service code and primary Compose files at the root;
3. centralized Docker and Compose infrastructure under `docker/`;
4. a hybrid layout with root Compose files, service-local Dockerfiles, and shared infrastructure under `docker/`;
5. a modular monorepo layout with service-level container modules and explicit top-level orchestration;
6. a separate deployment repository for production orchestration;
7. preservation of an established or custom layout.

The hybrid layout is the recommended option to present for many small and medium multi-service repositories, but it must never be selected without explicit user confirmation.

The selected approach, canonical commands, build contexts, Compose file order, environment handling, and migration decision must be documented. Use `ai/CONTAINERIZATION.md` for the complete decision gate, layouts, migration rules, and verification requirements.

## GUI testing

Do not create brittle automated GUI tests that locate, interact with, or validate interface elements through absolute coordinates, screen position, pixel offsets, or incidental layout order.

Position-dependent GUI checks must be performed manually or as supervised exploratory checks with Codex. They must not be committed as part of the routine automated test suite.

Automated GUI tests should use stable semantic selectors such as roles, accessible names, labels, documented component identifiers, or dedicated test IDs.

## Outcome-oriented execution and bounded supporting work

Before implementation starts, every meaningful work item MUST identify:

- the primary outcome: the observable behavior, artifact, decision, or capability that the work must deliver;
- the smallest acceptance proof: the minimum demonstration, check, or evidence that establishes the outcome;
- the execution envelope: permitted in-scope changes, verification runs, resource limits, external effects, and actions that require separate owner approval.

The primary outcome may itself be application behavior, infrastructure, test tooling, documentation, research, security, release preparation, or another deliverable when the related Issue explicitly defines it as such.

Work that only enables, checks, documents, or proves the primary outcome is supporting work. Examples include test harnesses, smoke wrappers, evidence collection, CI scaffolding, review preparation, release mechanics, optional hardening, benchmarks, and incidental refactoring.

### Outcome progress

Work counts as outcome progress only when it:

1. implements or improves the primary outcome;
2. produces the stated smallest acceptance proof; or
3. removes a verified blocker on the shortest path to the primary outcome.

Supporting work MUST remain minimum sufficient. It MUST NOT become a separate stage, handoff, approval gate, or completion target merely because it failed or required repair.

A localized, reversible, in-scope defect in supporting work MUST normally be fixed and verified within the current work item, work claim, and execution envelope.

A repeated failed action and post-fix verification are different:

- repeating the same failed action without a relevant change is a retry and SHOULD NOT be performed without a documented reason;
- rerunning the affected check after an evidence-based fix is verification and remains part of the current work item.

Unless the execution envelope sets a stricter run or resource limit, one bounded verification rerun after each relevant fix is permitted.

The fix-and-verification cycle MUST stop when the execution envelope would be exceeded, the same failure recurs without a new evidence-based fix, or the progress-stall rule is triggered.

### Authorization and approval boundary

The original work authorization covers reversible implementation, localized blocker fixes, focused tests, and bounded verification reruns that remain inside the declared scope and execution envelope.

A new owner decision is required only when the proposed action:

- changes the primary outcome or acceptance criteria;
- expands the Issue scope, architecture, or accepted baseline;
- is destructive, irreversible, or has an external side effect outside the declared envelope;
- materially exceeds the declared cost, resource, data, security, or time boundary;
- weakens an existing security control;
- conflicts with a project-specific or platform-enforced permission gate.

A supporting-tool failure alone MUST NOT create a new approval requirement.

### Stage and handoff boundary

A supporting-tool failure or its localized repair is not by itself a legitimate outcome stage.

A stage result or handoff is appropriate only when:

- the primary outcome materially advanced;
- the smallest acceptance proof was completed;
- a verified blocker remains outside the current execution envelope; or
- work is genuinely interrupted or transferred to another actor.

Routine supporting fixes and their verification SHOULD be summarized in the next legitimate stage or final report instead of creating additional handoff cycles.

### Progress-stall rule

If two consecutive work updates, proposed stages, or handoffs report no outcome progress and advance only supporting work, the agent MUST mark the work `progress-stalled`.

The agent must then:

1. stop adding optional supporting work;
2. restate the primary outcome and smallest acceptance proof;
3. identify the shortest remaining path;
4. move non-blocking work to follow-up or backlog;
5. continue inside the execution envelope, or request one owner decision when an approval boundary has actually been crossed.

A separate Issue for supporting work is justified only when that work has an independent primary outcome, cannot safely fit the current execution envelope, or is a verified blocker that cannot be resolved within the current scope.

Agent Handoff does not override tool, platform, repository, or organization permission systems.

## Proportionate security and evidence

Security and evidence work MUST NOT block acceptance or expand the current scope unless it addresses a verified High or Critical risk introduced, changed, or exposed by the current scope. A risk is verified only when it is supported by reproducible evidence from the current implementation or environment, or by a directly applicable authoritative source. A possible or merely credible scenario is not sufficient.

Before declaring security or evidence work blocking, the agent must state:

- the concrete threat or failure scenario and its supporting evidence;
- the affected asset or trust boundary;
- why the risk applies to the current change;
- the High or Critical severity, using the project's adopted method or, when none exists, an explicit likelihood-and-impact rationale showing equivalent severity;
- the minimum sufficient control;
- the smallest verification that demonstrates the control works.

A credible suspicion of a High or Critical risk may justify only a short, time-boxed investigation to confirm or refute it. Before confirmation, it MUST NOT justify hardening, architecture changes, gates, architecture decision records, checkers, mandatory evidence steps, or a separate stage. If the investigation does not confirm the risk, classify the proposal as non-blocking follow-up, owner-accepted risk when explicit acceptance exists, or out of scope.

Low, Medium, unrated, and unverified risks MUST NOT block an MVP or working vertical slice, expand the current Issue, or add mandatory work. Record them as a warning, documentation note, or backlog item. An opportunistic fix is allowed only when it already fits the current scope and does not delay acceptance.

An MVP, prototype, or runtime spike must preserve the existing security baseline, address verified High or Critical risks, and run the smallest useful end-to-end scenario as early as practical. Optional hardening, exhaustive compatibility checks, and defense in depth follow a working vertical slice. An exact acceptance criterion or a verified legal or project requirement may independently block acceptance, but the agent must cite the exact requirement and must not invent one.

For a local, owner-only, and easily recoverable risk, a warning or documentation is normally sufficient. Secrets, untrusted input, external network access, privilege boundaries, irreversible or destructive actions, sensitive data, and supply-chain exposure justify checking applicability; their presence alone does not prove High or Critical severity.

The existing security baseline MUST NOT be weakened without an explicit owner decision. Agents must not invent policies or regulatory requirements; unresolved requirements are questions for the owner.

A 10–15% share of stage work for security and evidence may be used as a non-binding planning heuristic, never as an acceptance metric or hard cap. Substantially exceeding it requires a verified High or Critical risk or an exactly cited mandatory requirement.

Reviews, task reports, and handoffs must distinguish verified blocking High or Critical risks, time-boxed investigations of suspected High or Critical risks, follow-up hardening, and owner-accepted risks.

## Definition of Done

- related Issue or PR is linked;
- work claim comment exists for agent work;
- agent id and run id are repeated in PR or handoff when relevant;
- required stage or final result comment exists;
- primary outcome, smallest acceptance proof, and execution envelope are recorded;
- supporting work remained subordinate or a justified independent outcome is documented;
- stage and handoff boundaries reflect outcome progress, completed acceptance proof, an out-of-envelope blocker, or genuine interruption or transfer;
- `progress-stalled` was handled when two consecutive updates advanced only supporting work;
- changes are committed;
- smoke tests were run or reason is documented;
- PR description is updated;
- verified blocking High or Critical risks, time-boxed investigations, follow-up hardening, and owner-accepted risks are distinguished;
- security and evidence work did not block acceptance or expand scope without a verified High or Critical current-scope risk or an exactly cited mandatory requirement;
- handoff exists for meaningful work;
- `ai/handoffs/INDEX.md` is updated when needed;
- mandatory initialization or adoption questions were answered when relevant;
- container layout and canonical commands are recorded when Docker or Compose is used;
- changed Compose configuration was rendered and checked, or the reason and risk are documented.

## Final rule

Code changes together with compact state for the next agent.

Large data stays in GitHub and Git.

`ai/` stores only what helps future agents continue development quickly and safely.
