---
type: architecture_record
version: 1
status: active
updated: 2026-07-24
project: Agent_Handoff
---

# Architecture Records

## 2026-06-29 — Adopt Agent Handoff Standard 1.1

Status: accepted

### Background

The initial standard needed support for parallel agents, GitHub templates, smoke tests, and machine-readable metadata.

### Decision

Adopt Agent Handoff Standard 1.1 as a compact workflow scaffold.

### Related

- Issue: #1

## 2026-07-02 — Rename to Agent Handoff

Status: accepted

### Background

The project name should emphasize agent-to-agent development handoff.

### Decision

Use Agent Handoff as the project and standard name.

### Related

- Standard file: `AGENT_HANDOFF_STANDARD.md`

## 2026-07-07 — English-only canonical repository

Status: accepted

### Background

The public repository should be simpler to maintain and easier for an international audience to scan.

### Decision

Maintain this repository in English only. Downstream projects may adapt Agent Handoff to another repository language, but canonical files here stay English-only.

### Related

- `AGENT_HANDOFF_STANDARD.md`
- `docs/en/README.md`

## 2026-07-18 — User-controlled containerization layout

Status: accepted in Standard 1.3

### Background

Docker and Docker Compose files can be organized in several valid ways. Automatically applying one preferred structure during repository initialization or Agent Handoff adoption could create unnecessary migrations, break paths and commands, or override established project ownership boundaries.

### Decision

Document all supported containerization approaches in `ai/CONTAINERIZATION.md`.

During both new-repository initialization and adoption into an existing repository, require the agent to ask the user a separate, explicit question about whether containerization is used or planned, which layout should be used, whether an existing layout may be migrated, and whether production deployment belongs in the same repository.

Do not allow the agent to infer approval or automatically apply the recommended hybrid layout.

### Rejected alternatives

- Require one universal Docker layout for all repositories.
- Automatically migrate existing repositories to the hybrid layout.
- Treat the container layout as an implementation detail that the agent may decide silently.
- Create placeholder Docker infrastructure before a confirmed requirement exists.

### Consequences

- Container layout remains a human-controlled architecture decision.
- Existing repositories are preserved until migration is explicitly approved.
- New repositories do not receive speculative Docker infrastructure.
- Agents have a complete catalog of supported layouts and shared verification requirements.
- Initialization prompts and handoff procedures expose the decision gate explicitly.

### Related

- Issue: #12
- Pull Request: #13
- `AGENT_HANDOFF_STANDARD.md`
- `ai/CONTAINERIZATION.md`
- `ai/HANDOFF_PROTOCOL.md`
- `docs/en/README.md`

## 2026-07-18 — Stable GUI automation over position-dependent tests

Status: accepted in Standard 1.3

### Background

GUI tests that depend on absolute coordinates, screen positions, pixel offsets, or incidental layout order are fragile and frequently fail after harmless interface changes.

### Decision

Do not include position-dependent GUI checks in the routine automated test suite. Perform those checks manually or as supervised exploratory checks with Codex.

Automated GUI tests use stable semantic roles, accessible names, labels, documented component identifiers, or dedicated test IDs.

### Consequences

- Routine GUI automation is more resilient to layout changes.
- Visual and position-dependent behavior remains explicitly testable through manual or supervised exploratory checks.
- Handoffs and Pull Requests must state when such checks were performed manually.

### Related

- Issue: #12
- Pull Request: #13
- `AGENT_HANDOFF_STANDARD.md`

## 2026-07-24 — Proportionate security and evidence

Status: accepted in Standard 1.4

### Background

The standard required risks and checks to be recorded but did not require security and evidence work to be proportional to a risk in the current scope. Hypothetical threats could therefore create blocking gates, extra documents, or separate stages before a useful end-to-end scenario existed.

### Decision

Treat security and evidence work as blocking only when it is connected to a concrete and credible current-scope threat or failure scenario, affected asset or trust boundary, likely impact, minimum sufficient control, and verification.

Preserve the existing security baseline and prioritize concrete critical risks. Classify unsupported hardening as non-blocking follow-up, explicitly owner-accepted risk, or out of scope so MVPs, prototypes, and runtime spikes can run the smallest useful vertical slice early.

Use a 10–15% security-and-evidence share only as a non-binding planning heuristic.

### Rejected alternatives

- Require a formal threat model for every Pull Request.
- Enforce a fixed percentage of work for security and evidence.
- Add automated risk-severity scoring.
- Add approval stages or ADRs for theoretical risks.
- Weaken existing controls to accelerate delivery.

### Consequences

- Blocking security work has a reviewable current-scope justification.
- Evidence and process remain minimal unless acceptance criteria, verified requirements, or credible critical risks require more.
- Reviews and handoffs distinguish blocking risk, follow-up hardening, and owner-accepted risk.
- The structural checker confirms the PR checklist item but does not judge risk realism.

### Related

- Issue: #14
- Pull Request: pending
- `AGENT_HANDOFF_STANDARD.md`
- `ai/HANDOFF_PROTOCOL.md`
- `ai/TASK_REPORT_PROTOCOL.md`
