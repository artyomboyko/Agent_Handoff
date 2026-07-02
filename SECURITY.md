# Security Policy / Политика безопасности

Agent Handoff is a workflow and documentation standard. It may be used in repositories that contain private project context, agent outputs, or operational notes.
Agent Handoff — это workflow и documentation standard. Он может использоваться в репозиториях с приватным проектным контекстом, output агентов или operational notes.

## Do not commit / Не добавляйте в репозиторий

- API keys, tokens, passwords / API keys, tokens, passwords;
- SSH keys or private certificates / SSH keys или private certificates;
- private logs or full chat transcripts / private logs или полные chat transcripts;
- customer data or personal data / customer data или personal data;
- raw tool dumps with sensitive values / raw tool dumps с sensitive values.

## Safe repository memory / Безопасная память репозитория

The `ai/` folder should contain compact durable context, not secrets or bulky operational data.
Папка `ai/` должна хранить компактный устойчивый контекст, а не secrets или громоздкие operational data.

## Reporting a vulnerability / Сообщить об уязвимости

If you find a security issue in this repository, contact the maintainer privately before opening a public Issue.
Если вы нашли security issue в этом репозитории, сначала свяжитесь с maintainer privately, прежде чем открывать публичное Issue.

## Public release checklist / Checklist перед публикацией

Before making a repository public:
Перед переводом репозитория в public:

- review Git history / проверьте Git history;
- review Issues and Pull Requests / проверьте Issues и Pull Requests;
- review GitHub Actions logs / проверьте GitHub Actions logs;
- review generated files and attachments / проверьте generated files и attachments;
- remove or rotate exposed secrets / удалите или перевыпустите exposed secrets.
