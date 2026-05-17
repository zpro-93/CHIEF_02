# Security Baseline

## Security Posture

CHIEF_02 should be built with an enterprise-grade security posture from the start.

The early system will handle:

- Discord messages from a private founder channel
- business research and strategy
- team preferences and decisions
- memory that may contain sensitive operating context
- integrations with Notion, Google Workspace, GitHub, and future tools

Security decisions should assume this data matters.

## Supply Chain Principles

Use the smallest reasonable trusted toolchain.

Initial baseline:

- Python runtime
- standard-library `venv`
- `pip`
- pinned requirements files

Avoid adding third-party package managers unless there is a clear feature or operational need.

When adding third-party dependencies:

- prefer mature packages with active maintenance
- pin versions
- review transitive dependencies
- scan for known vulnerabilities
- avoid install scripts that pipe remote code directly into a shell
- do not commit lock or requirements changes without review

## Dependency Scanning

Recommended development security tooling:

- `pip-audit` for Python dependency vulnerability checks
- GitHub Dependabot for dependency update visibility
- GitHub secret scanning where available

Story 0.1 should include dependency scanning with `pip-audit` unless there is a specific blocker.

`pip-audit` should run in CI. Local pre-commit hooks may run faster checks by default, but dependency audit should be available as an explicit local command too.

## Secrets Management

Rules:

- never commit real secrets
- keep `.env` ignored by Git
- commit `.env.example` with names only
- load secrets from environment variables
- keep production secrets in the deployment platform's secret manager
- scope API tokens to least privilege

Expected early secrets:

- `DISCORD_TOKEN`
- `DISCORD_CLIENT_ID`
- `DISCORD_GUILD_ID`
- `DISCORD_ALLOWED_CHANNEL_IDS`
- `OPENAI_API_KEY`
- `DATABASE_URL`
- `NOTION_TOKEN`
- `GOOGLE_APPLICATION_CREDENTIALS`
- `GITHUB_TOKEN`

## Tool Access Model

Specialist agents should not directly access external tools.

Expected flow:

```text
Specialist Agent
 -> Orchestrator
 -> MCP Tool Broker
 -> External Tool
```

The tool broker should eventually enforce:

- tool schemas
- permission levels
- allowed channels/workspaces
- audit logging
- recoverable error handling
- output normalization

## Memory Security

Memory is sensitive.

Rules:

- do not automatically store all chat content as durable memory
- distinguish shared team memory, agent-scoped memory, and session memory
- prefer explicit user confirmation for durable memory
- track source and confidence for every memory entry
- support future deletion or correction of memory entries
- prevent specialist agents from directly rummaging through raw memory

Expected flow:

```text
Specialist proposes memory
 -> Memory Curator reviews
 -> Memory Curator scopes, deduplicates, and saves
```

## Discord Permissions

The bot should use the minimum Discord permissions needed for MVP.

MVP needs:

- read selected channel messages
- respond to slash commands
- send messages in selected channels

The bot should not have broad admin permissions.

Allowed channel IDs should be configurable.

## Logging

Logs should help debug behavior without leaking sensitive content.

Early rules:

- log command type, channel id, and correlation id
- avoid logging full raw message content by default
- never log secrets
- log tool calls at metadata level first
- add redaction before logging sensitive payloads

## CI Baseline

Initial CI should run:

- dependency installation
- tests
- formatting checks with `black`
- lint checks with `pylint`
- dependency vulnerability audit with `pip-audit`

CI should not require production secrets.

## Future Security Work

Likely future tickets:

- threat model
- dependency vulnerability scanning
- secret scanning verification
- tool-call audit trail
- memory deletion/correction workflow
- integration permission review
- deployment hardening
