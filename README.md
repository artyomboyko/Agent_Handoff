# AI Handoff

AI Handoff is a compact standard for passing development state between AI coding agents through GitHub, Git, and small repository-tracked memory files.

A new agent should be able to clone the repository, open the related GitHub Issue or Pull Request, inspect Git state, read the compact `ai/` memory, and continue work without relying on earlier local state.

## Current standard

- Full standard: [`AI_HANDOFF_STANDARD.md`](AI_HANDOFF_STANDARD.md)
- Agent entrypoint: [`AGENTS.md`](AGENTS.md)
- AI memory map: [`ai/README.md`](ai/README.md)
- Workflow protocol: [`ai/HANDOFF_PROTOCOL.md`](ai/HANDOFF_PROTOCOL.md)

## Core model

```text
GitHub     = Issues, Pull Requests, reviews, CI, discussions
Git        = source code, branches, commits, diffs, tags, history
ai/        = compact durable project memory
handoffs/  = short snapshots of agent runs
```

Large diffs, bulky records, GitHub discussions, and CI data should stay in GitHub or Git, not in `ai/`.

Current standard version: **1.1**.
