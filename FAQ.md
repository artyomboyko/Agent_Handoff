# FAQ

## What is Agent Handoff?

Agent Handoff is a GitHub-native standard for passing project context between AI coding agents, human maintainers, and human-supervised agents.

## Why not just use chat memory?

Chat memory is usually tied to one tool, session, or provider. Agent Handoff stores compact durable context in the repository, next to Issues, Pull Requests, and code history.

## Is this a replacement for README?

No. README explains the project to people. Agent Handoff adds workflow, ownership, compact memory, and handoff rules for agents and maintainers.

## Is this a replacement for GitHub Issues?

No. GitHub Issues and Pull Requests remain the source of work truth. Agent Handoff uses them as the coordination layer.

## What is stored in `ai/`?

Compact durable project state, decisions, protocols, and handoff indexes.

## Which language should this repository use?

This repository is maintained in English.

## Do branch names include Issue numbers?

No by default. Use meaningful branch names and link Issues through Work Claim comments, PR descriptions, GitHub links, and handoff metadata.
