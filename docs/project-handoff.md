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

First run `git status --short`, then continue with the next open GitHub issue/story after confirming Story 0.1 status.
```

## Current Project State

The repo is currently in Story 0.1 implementation review.

Completed:

- Product PRD
- MVP backlog
- technical story breakdown
- architecture diagrams
- workflow swimlane diagram
- GitHub issues #1-#12
- enterprise engineering standards
- security baseline
- reusable local Codex skill: `project-handoff`
- reusable local Codex skill: `project-resume`

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

Current implementation status:

- Story 0.1 bootstrap files have been generated and are ready to commit/push.
- Verification has passed locally:
  - `black --check app tests`
  - `pylint app tests` with `10.00/10`
  - `pytest` with 2 passing tests
  - `pip-audit` with no known vulnerabilities
- `pip-audit` initially found vulnerable pins for `python-dotenv`, `black`, and `pytest`; those pins were updated to fixed versions.
- `AgentRole.purpose` is documented as descriptive metadata only, not authorization.
- Pytest config lives in `pyproject.toml`; the duplicate `pytest.ini` file was removed.

Story 0.1 files:

```text
.env.example
.gitignore
.githooks/pre-commit
.github/workflows/ci.yml
requirements.txt
requirements-dev.txt
pyproject.toml
pylintrc
app/
tests/
```

Recent review questions discussed:

- `pyproject.toml` is used for project/tool configuration only, not as Poetry/uv.
- `.github/workflows/ci.yml` is for GitHub Actions quality checks, not deployment.
- GitHub-hosted runners run on GitHub temporary infrastructure, not locally.
- CI is useful as a neutral quality gate before merge.
- `.gitignore` was derived from Python generated files, tool caches, virtualenvs, secrets, build outputs, logs, and OS files.
- `app/__init__.py` only marks `app/` as a Python package.
- `app/agents/__init__.py` contains minimal architecture-aligned role metadata for smoke tests.
- `AgentRole.purpose` is descriptive metadata only and must not be used for authorization.
- `project-resume` skill exists at `C:\Users\zpro\.codex\skills\project-resume`.

## Do Not Do

- Do not use TypeScript.
- Do not use `uv`.
- Do not use Poetry.
- Do not add the third-party `pre-commit` framework unless explicitly approved.
- Do not implement MCP Tool Broker inside Story 0.1.
- Do not start Discord bot implementation beyond safe placeholders in Story 0.1.
- Do not commit secrets.
- Do not treat `AgentRole.purpose` as a permission or authorization model.

## Next Implementation Plan

For Story 0.1, generated files are:

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

README now includes local setup commands.

Recommended follow-up after Story 0.1:

1. Confirm whether to close GitHub issue #1 after reviewing the commit.
2. Pick the next story from the technical story breakdown.
3. Continue implementing in small reviewed increments.

Current local setup commands:

```bash
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m black --check app tests
python -m pylint app tests
python -m pytest
New-Item -ItemType Directory -Force .cache\tmp, .cache\pip-audit | Out-Null
$env:TMPDIR = "$PWD\.cache\tmp"
python -m pip_audit --cache-dir .cache\pip-audit -r requirements.txt -r requirements-dev.txt
git config core.hooksPath .githooks
```

On macOS/Linux, activation is:

```bash
source .venv/bin/activate
```

## Verification Before Final Response

Before ending an implementation turn:

1. Run `git status --short`.
2. Run tests and quality checks.
3. Show the user the final changed files for review when requested.
4. Commit/push only after approval.
5. Update the active GitHub issue with what was completed when useful.
6. Ask before closing issues unless the user explicitly says to close them.

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
