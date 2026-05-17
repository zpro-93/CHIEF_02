# GitHub Issue Architecture Audit

Audit date: 2026-05-17

This audit compares the current GitHub issues against the architecture documented in `README.md`.

## Summary

The current issue set covers the original MVP foundation well:

- Discord bot setup
- Discord message ingestion
- summarization
- custom time-window summarization
- research brief generation
- basic memory storage
- orchestrator interfaces
- Markdown publishing
- Notion and Google publishing

However, the architecture has evolved. The issue set does not yet fully cover:

- MCP as the standard tool protocol
- MCP Tool Broker implementation
- Memory Curator / Context Engineer agent
- agent-scoped memory
- context packet generation
- Planner Agent
- slash command framework for all commands
- explicit specialist-agent behavior profiles
- calendar and scheduling workflows
- architecture consistency around latest-session chunking rules

## Coverage Matrix

| Architecture component | Current coverage | Status |
| --- | --- | --- |
| Discord UI | Story 1.1, Story 1.2 | Covered |
| Slash commands | Story 1.1 partially | Needs dedicated ticket |
| Message ingestion | Story 1.2 | Covered |
| Orchestrator / Router | Story 5.1 | Partially covered |
| Intent classification | Story 5.1 partially | Needs more detail |
| Summarizer Agent | Story 2.1, Story 2.2 | Covered, but rule conflict needs resolution |
| Researcher + Documenter Agent | Story 3.1, Story 3.3 | Partially covered |
| MBA framework behavior | Story 3.1 partially | Needs dedicated detail |
| Planner Agent | No current issue | Missing |
| Memory store | Story 4.1 | Covered for basic memory |
| Memory Curator / Context Engineer | No current issue | Missing |
| Shared team memory | Story 4.1 partially | Needs scoped schema detail |
| Agent-scoped memory | No current issue | Missing |
| Session memory | Story 2.1/1.2 partially | Needs explicit design |
| Context packets | No current issue | Missing |
| MCP Tool Broker | Story 5.1 has generic tool registry | Missing MCP-specific ticket |
| MCP adapters/tools | Stories 3.3, 6.2, 6.3 partially | Needs MCP-specific adapter tickets |
| Markdown publishing | Story 6.1 | Covered |
| Notion publishing | Story 6.2 | Covered as publisher, not MCP adapter |
| Google Workspace publishing | Story 6.3 | Covered as publisher, not MCP adapter |
| Google Calendar / meeting scheduling | No current issue | Missing |
| GitHub integration | Current repo setup only | Missing as runtime tool if needed |
| Logging, permissioning, audit trail | Story 5.1 partially | Needs more detail |
| Tests/evals for agents | Individual issues partially | Needs broader eval ticket later |

## Important Inconsistency To Resolve

The README currently says the Summarizer Agent uses this fallback behavior:

> If no timeframe is mentioned, summarize the latest meaningful message chunk where the max gap between messages is 5 minutes.

But approved Story 2.1 says:

> `/summarize` finds the latest session using a 6+ hour inactivity boundary.

These are different algorithms.

Recommendation:

- Keep approved Story 2.1 as the MVP behavior: latest session in current channel, 6+ hour inactivity boundary.
- Treat the 5-minute chunking idea as a future or alternate summarization mode only if we explicitly want it.
- Update README to remove or clarify the 5-minute rule.

## Recommended New GitHub Issues

### Story 1.3: Build Slash Command Framework

Purpose:

Create a reusable command framework for `/summarize`, `/research`, `/remember`, `/recall`, `/tasks`, and future commands.

Why needed:

Story 1.1 proves `/ping`, but the architecture needs a real command layer.

### Story 3.2: Define MBA Research Framework

Purpose:

Define the exact structure, prompts, output schema, and evaluation criteria for MBA-style business research.

Why needed:

Story 3.1 builds research workflow, but the specialist behavior should be explicit and testable.

### Story 3.4: Build Planner Agent

Purpose:

Implement the Planner Agent for project plans, clarifying questions, action trackers, dashboards, dependencies, and meeting planning.

Why needed:

Planner Agent is in the architecture but has no issue.

### Story 4.2: Add Agent-Scoped And Session Memory

Purpose:

Extend memory schema to support shared team memory, agent-scoped memory, and session memory.

Why needed:

Story 4.1 only covers basic durable memory.

### Story 4.3: Build Memory Curator / Context Engineer Agent

Purpose:

Build the agent that manages memory writes, deduplication, conflicts, behavior rules, and context packets for specialists.

Why needed:

The architecture depends on the Memory Curator, but no issue currently builds it.

### Story 4.4: Implement Context Packet Retrieval

Purpose:

Create the query and packaging layer that returns task-relevant context to the Orchestrator and specialist agents.

Why needed:

Specialists need clean context packets, not raw database access.

### Story 5.2: Build MCP Tool Broker

Purpose:

Implement MCP as the standard protocol for tool access, including permission checks, schemas, logs, error handling, and normalized results.

Why needed:

Current Story 5.1 mentions a generic tool registry, but the architecture specifically chooses MCP.

### Story 5.3: Add MCP Tool Adapters

Purpose:

Create MCP adapters for Discord, web research, Notion, Google Workspace, Google Calendar, GitHub, and database/vector search.

Why needed:

The architecture says tools are accessed through MCP, but integration tickets do not yet enforce that pattern.

### Story 5.4: Add Tool Permission And Audit Logging

Purpose:

Log tool calls, enforce permissions, and make specialist tool access reviewable.

Why needed:

This is important for safety, debugging, and future autonomy.

### Story 6.4: Add Calendar And Scheduling Publisher

Purpose:

Support meeting schedule generation and Google Calendar integration.

Why needed:

Planner Agent includes meeting schedules, but there is no ticket for calendar output.

## Recommendation

Before implementation begins, add the missing issues above and resolve the summarizer chunking-rule inconsistency.

After that, the issue set will match the architecture closely enough for two engineers to start building in parallel.
