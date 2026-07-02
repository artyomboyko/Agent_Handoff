---
type: architecture_record
version: 1
status: active
updated: 2026-07-02
project: Agent_Handoff
---

# Architecture Records

## 2026-06-29 — Adopt Agent Handoff Standard 1.1

Status: accepted

### Background

The initial standard needed stronger support for parallel agents, structured GitHub templates, smoke-test discipline, private value policy, and machine-readable metadata.

### Chosen approach

Adopt Agent Handoff Standard 1.1 with source priority order, handoff statuses, expanded index columns, conflict protocol, Definition of Done, mandatory smoke tests, larger size guidance, GitHub Issue Forms, default PR template, YAML front matter, and private value policy.

### Alternatives

Avoid bulky operational records in `ai/`; keep GitHub and Git as primary history.

### Consequences

Future repositories get a compact workflow scaffold.

### Related

- Issue: #1

## 2026-07-02 — Rename to Agent Handoff

Status: accepted

### Background

The project name should emphasize agent-to-agent development handoff.

### Chosen approach

Use Agent Handoff as the project and standard name.

### Related

- Standard file: `AGENT_HANDOFF_STANDARD.md`
