#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'AGENTS.md',
    'AGENT_HANDOFF_STANDARD.md',
    'ISSUE_LABELS.md',
    'ISSUE_STATUS.md',
    'README.md',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'SECURITY.md',
    'FAQ.md',
    'CHANGELOG.md',
    'ai/README.md',
    'ai/PROJECT_STATE.md',
    'ai/DECISIONS.md',
    'ai/GITHUB_WORKFLOW.md',
    'ai/HANDOFF_PROTOCOL.md',
    'ai/AGENT_IDENTITY.md',
    'ai/WORK_CLAIM_PROTOCOL.md',
    'ai/REFACTORING.md',
    'ai/handoffs/INDEX.md',
    '.github/ISSUE_TEMPLATE',
    '.github/pull_request_template.md',
    'docs/en',
    'docs/ru',
    'examples/README.md',
    'assets/social-preview.svg',
]


def main():
    errors = []

    for item in REQUIRED:
        if not (ROOT / item).exists():
            errors.append(f'missing required path: {item}')

    for directory in [ROOT / '.github' / 'ISSUE_TEMPLATE', ROOT / '.github' / 'workflows']:
        if not directory.exists():
            continue
        for path in sorted(directory.glob('*.y*ml')):
            try:
                data = yaml.safe_load(path.read_text(encoding='utf-8'))
            except Exception as exc:
                errors.append(f'invalid YAML: {path.relative_to(ROOT)}: {exc}')
                continue
            if not isinstance(data, dict):
                errors.append(f'YAML root must be a map: {path.relative_to(ROOT)}')

    preview = ROOT / 'assets' / 'social-preview.svg'
    if preview.exists():
        text = preview.read_text(encoding='utf-8')
        if 'width="1280"' not in text or 'height="640"' not in text:
            errors.append('social preview must be 1280x640')
        if '>ai/</text>' in text:
            errors.append('social preview must not show ai slash label')

    if errors:
        print('Agent Handoff checks failed:')
        for error in errors:
            print('-', error)
        return 1

    print('Agent Handoff checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
