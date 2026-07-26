# FAQ

Agent Handoff FAQ.

## Why should supporting-tool failures stay inside the current work item?

Test harnesses, smoke wrappers, evidence collectors, CI scaffolding, and similar tools usually exist to enable or prove another outcome. Turning every localized failure into a separate stage, handoff, or approval cycle can advance the process without advancing that outcome.

Agent Handoff therefore keeps reversible in-scope repairs and bounded post-fix verification inside the original execution envelope. A new owner decision is still required when the outcome, scope, architecture, accepted baseline, external effects, resource or risk boundary, security baseline, or enforced permission gate changes.
