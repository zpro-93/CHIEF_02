# CHIEF_02 Project Handoff

Last updated: 2026-05-17

Use this file when continuing CHIEF_02 in a new Codex chat.

## New Chat Startup Prompt

Paste this into the next chat:

```text
We are continuing CHIEF_02.

Read these first:
- README.md
- docs/project-handoff.md
- docs/architecture/engineering-standards.md
- docs/architecture/security-baseline.md
- docs/product/technical-story-breakdown.md
- GitHub issue #1: Story 0.1

Project rules:
- Enterprise-grade decisions by default.
- Ask before making architecture/tooling choices.
- Use Python as the main runtime.
- Use venv + pip, not uv, Poetry, or TypeScript.
- Use pytest, black, pylint, and pip-audit.
- Use repo-managed Git hooks first, not the third-party pre-commit framework unless explicitly approved.
- MCP is the go-to tool protocol, but MCP Tool Broker implementation belongs in a separate story.

Continue with Story 0.1 implementation only after confirming the current working tree is clean.
```

## Current Project State

The repo is currently in planning/bootstrap stage.

Completed:

- Product PRD
- MVP backlog
- technical story breakdown
- architecture diagrams
- workflow swimlane diagram
- GitHub issues #1-#12
- enterprise engineering standards
- security baseline

Current active story:

- GitHub issue #1: `Story 0.1: Initialize Project Repository`

Story 0.1 is approved for implementation with:

- Python runtime
- `venv` + `pip`
- `requirements.txt`
- `requirements-dev.txt`
- `pytest`
- `black`
- `pylint`
- `pip-audit`
- repo-managed hooks under `.githooks/`
- CI for install, format check, lint, tests, and dependency audit

## Do Not Do

- Do not use TypeScript.
- Do not use `uv`.
- Do not use Poetry.
- Do not add the third-party `pre-commit` framework unless explicitly approved.
- Do not implement MCP Tool Broker inside Story 0.1.
- Do not start Discord bot implementation beyond safe placeholders in Story 0.1.
- Do not commit secrets.

## Next Implementation Plan

For Story 0.1, create:

```text
.env.example
.gitignore
.githooks/
  pre-commit
.github/
  workflows/
    ci.yml
requirements.txt
requirements-dev.txt
pyproject.toml
pylintrc
pytest.ini
app/
  __init__.py
  discord_bot/
    __init__.py
  agents/
    __init__.py
  memory/
    __init__.py
  tools/
    __init__.py
  schemas/
    __init__.py
  publishers/
    __init__.py
tests/
  test_smoke.py
```

Update `README.md` with local setup commands:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest
python -m black --check .
python -m pylint app tests
python -m pip_audit
git config core.hooksPath .githooks
```

On macOS/Linux, activation is:

```bash
source .venv/bin/activate
```

## Verification Before Final Response

Before ending the implementation turn:

1. Run `git status --short`.
2. Run tests and quality checks.
3. Commit changes.
4. Push to GitHub.
5. Update GitHub issue #1 with what was completed.
6. If Story 0.1 acceptance criteria are all met, ask before closing the issue.

## Key Repo Links

- README: `README.md`
- Engineering standards: `docs/architecture/engineering-standards.md`
- Security baseline: `docs/architecture/security-baseline.md`
- Technical story breakdown: `docs/product/technical-story-breakdown.md`
- Architecture audit: `docs/product/github-issue-architecture-audit.md`

## Current Architecture Principles

- Discord is the primary UI.
- Orchestrator routes requests to specialist agents.
- Specialist agents request tools indirectly.
- MCP Tool Broker will mediate external tool access.
- Memory Curator manages shared, agent-scoped, and session memory.
- Memory should be scoped, deduplicated, and auditable.
- Enterprise-grade posture is the default.
