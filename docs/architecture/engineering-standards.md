# Engineering Standards

## Decision Posture

CHIEF_02 should be designed as an enterprise-grade system by default.

When choosing tools, libraries, architecture patterns, and implementation approaches, prefer:

- security and auditability over novelty
- boring, well-understood tooling over fashionable tooling
- least-privilege access
- pinned dependencies
- explicit configuration
- clear operational runbooks
- testable modules
- documented tradeoffs before adopting third-party infrastructure

Velocity still matters, but not at the cost of avoidable supply-chain, operational, or maintainability risk.

## Runtime Decision

Primary runtime: Python.

Rationale:

- strong fit for AI/agent workflows
- mature ecosystem for APIs, data processing, testing, and automation
- straightforward deployment path for a Discord bot and worker-style backend
- familiar to many AI/backend engineers

## Dependency And Environment Decision

Initial project setup will use:

- `venv` for local virtual environments
- `pip` for package installation
- `requirements.txt` for runtime dependencies
- `requirements-dev.txt` for development and test dependencies

We are intentionally not starting with `uv` or Poetry.

Rationale:

- `venv` is part of the Python standard library
- `pip` is the standard Python package installer
- this keeps the trusted tooling path smaller
- this is easier for enterprise security review
- `uv` and Poetry can be reconsidered later if the workflow pain justifies the additional third-party tool

## Dependency Policy

Dependencies should be added deliberately.

Rules:

- Pin direct dependencies in requirements files.
- Separate runtime dependencies from development dependencies.
- Keep dependency count small.
- Prefer mature, widely used packages.
- Avoid adding convenience libraries unless they remove meaningful complexity.
- Review dependency changes in pull requests.
- Add vulnerability scanning before the project has meaningful runtime dependencies.

## Initial Tooling Recommendation

For Story 0.1, use conservative Python tooling:

- testing: `pytest`
- formatting: `black`
- linting: `flake8`
- dependency vulnerability check: `pip-audit`

These are third-party tools, so they should be documented as development tooling. They are not replacing the environment manager or package installer.

If we want even fewer third-party development dependencies at first, we can defer `black`, `flake8`, or `pip-audit`, but the recommended enterprise baseline includes them.

## Discord Framework Decision

Recommended framework: `discord.py`.

Rationale:

- mature Discord bot library
- broad community usage
- supports slash commands through app commands
- sufficient for Discord login, guild/channel access, message fetching, and command handling
- lower ecosystem fragmentation risk than choosing a fork without a specific need

Pycord remains a possible alternative if `discord.py` lacks a required feature, but there is no known MVP requirement that justifies choosing Pycord first.

## Project Shape

Use a modular monolith.

Planned structure:

```text
app/
  __init__.py
  discord_bot/
  agents/
  memory/
  tools/
  schemas/
  publishers/
tests/
docs/
```

Rationale:

- simple enough for two engineers
- avoids premature microservices
- keeps architecture boundaries visible
- allows later extraction of agents, tools, or memory into services if needed

## MCP Decision

MCP is the go-to protocol for tool access in the architecture.

For Story 0.1:

- document MCP as an architectural direction
- create a placeholder module/package only if useful
- do not implement the MCP Tool Broker yet

Full MCP implementation belongs in a dedicated story:

```text
Story 5.2: Build MCP Tool Broker
```

## Definition Of Done For Story 0.1

Story 0.1 is complete when:

- Python runtime decision is documented.
- `venv` + `pip` setup is documented.
- repo structure is created.
- requirements files exist.
- `.env.example` exists and contains no secrets.
- test runner is configured.
- formatter/linter decision is implemented or explicitly deferred.
- CI runs install, lint, and tests.
- README has local setup instructions.
- one smoke test passes.
