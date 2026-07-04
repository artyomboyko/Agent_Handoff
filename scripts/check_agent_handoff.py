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
    'CITATION.cff',
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
    '.github/workflows/standard-check.yml',
    'docs/en',
    'docs/ru',
    'docs/index.html',
    'docs/404.html',
    'docs/robots.txt',
    'docs/sitemap.xml',
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
                continue
            if directory.name == 'ISSUE_TEMPLATE' and path.name != 'config.yml':
                body = data.get('body')
                if not isinstance(body, list):
                    errors.append(f'Issue Form body must be a list: {path.relative_to(ROOT)}')
                    continue
                found_language = False
                for item in body:
                    if not isinstance(item, dict):
                        continue
                    attrs = item.get('attributes') or {}
                    label = str(attrs.get('label', ''))
                    description = str(attrs.get('description', ''))
                    if item.get('id') == 'language' and 'Issue language' in label and 'Язык заполнения Issue' in label:
                        if 'bilingual' in description or 'двуязычными' in description:
                            found_language = True
                if not found_language:
                    errors.append(f'Issue Form language selector is unclear: {path.relative_to(ROOT)}')

    pr_template = ROOT / '.github' / 'pull_request_template.md'
    if pr_template.exists():
        text = pr_template.read_text(encoding='utf-8')
        for required_text in ['Related Issue or PR is linked.', 'Required files exist.', 'Links work.', 'Forms are valid when changed.', 'Smoke tests were run or reason is documented.']:
            if required_text not in text:
                errors.append(f'PR template missing checklist item: {required_text}')

    en_index = ROOT / 'docs' / 'en' / 'README.md'
    ru_index = ROOT / 'docs' / 'ru' / 'README.md'
    if en_index.exists() and ru_index.exists():
        en_count = sum(1 for line in en_index.read_text(encoding='utf-8').splitlines() if line.startswith('- ['))
        ru_count = sum(1 for line in ru_index.read_text(encoding='utf-8').splitlines() if line.startswith('- ['))
        if en_count != ru_count:
            errors.append(f'docs index item count mismatch: en={en_count} ru={ru_count}')

    preview = ROOT / 'assets' / 'social-preview.svg'
    if preview.exists():
        text = preview.read_text(encoding='utf-8')
        if 'width="1280"' not in text or 'height="640"' not in text or 'viewBox="0 0 1280 640"' not in text:
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
