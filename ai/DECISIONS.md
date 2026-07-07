---
type: architecture_record
version: 1
status: active
updated: 2026-07-07
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
