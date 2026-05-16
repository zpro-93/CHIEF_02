# Technical Story Breakdown

This document translates the current product stories into implementation steps. Product requirements define what the bot should do; these steps define how engineers can build each ticket.

## Setup 0.1: Initialize Project Repository

Goal: create a clean engineering workspace both engineers can run locally.

Technical steps:

1. Choose runtime and framework stack.
2. Create base repo structure for bot, agents, memory, tools, schemas, docs, and tests.
3. Add package/dependency management.
4. Add formatter and linter.
5. Add test runner with one passing smoke test.
6. Add `.env.example` with required variables and no secrets.
7. Add local development instructions to `README.md`.
8. Add basic CI workflow for lint/test once stack is selected.

Engineering notes:

- Recommended MVP stack: TypeScript, `discord.js`, Postgres, and `pgvector`.
- Keep the first repo structure boring and obvious; avoid premature framework sprawl.

## Story 1.1: Create Discord Bot Skeleton

Goal: prove the bot can exist in Discord and respond to commands.

Technical steps:

1. Create Discord application and bot in Discord Developer Portal.
2. Configure bot token, client id, guild id, and allowed channel ids through environment variables.
3. Create minimal bot process.
4. Register `/ping` slash command for the development guild.
5. Implement `/ping` handler returning a short success response.
6. Add startup logging with bot identity and configured environment.
7. Add command error handling so failures return a safe Discord response.
8. Document local run command and Discord invite steps.

Acceptance support:

- This story does not implement summarization.
- This story proves authentication, command registration, permissions, and response flow.

## Story 1.2: Implement Message Window Fetching

Goal: fetch Discord messages from the current channel for later summarization.

Technical steps:

1. Define internal message schema: id, channel id, author id, author display name, timestamp, content, attachments metadata, and bot flag.
2. Implement Discord message fetcher for a channel and time window.
3. Handle Discord pagination when more than one page is needed.
4. Exclude bot messages by default.
5. Normalize timestamps to UTC internally.
6. Preserve display timezone for user-facing output.
7. Add rate-limit handling and retry behavior.
8. Add fixtures or mocks for testing message windows.
9. Add tests for empty channel, bot-only messages, mixed authors, and paginated windows.

Engineering notes:

- This should be a reusable service, not embedded directly inside `/summarize`.
- The summarizer should receive normalized messages, not raw Discord API objects.

## Story 2.1: Implement `/summarize` Last Session

Goal: summarize the latest meaningful conversation session in the current channel.

Product status: Approved.

Technical steps:

1. Add `/summarize` command with no required arguments.
2. Fetch recent messages from the current Discord channel.
3. Identify the latest session by scanning backward until a 6+ hour inactivity gap.
4. If the latest session contains fewer than 5 human messages, return a not-enough-activity response.
5. Exclude bot messages before summarization.
6. Build summarizer input with channel name, time window, participants, and message list.
7. Generate concise Discord response with only Summary date/time, Recap, Action Items, and Open Questions.
8. Infer action item owners only when clear; otherwise use `Unassigned`.
9. Generate full Markdown artifact with richer detail: decisions, blockers, participants, and potential memory candidates.
10. Save Markdown artifact under `docs/artifacts/summaries/YYYY-MM-DD-channel-name-summary.md`.
11. Return Discord response and include the artifact path.
12. Add tests for active session, completed session after 6+ hours, too few messages, bot messages, and unclear action item owners.

Engineering notes:

- Memory candidates may be listed in the Markdown artifact, but do not save them to durable memory yet.
- The command reads the current channel only.

## Story 2.2: Implement `/summarize` Custom Time Range

Goal: let users summarize a specific time range in the current channel.

Technical steps:

1. Add optional `/summarize since:<text> until:<text>` arguments.
2. Parse common time inputs such as `yesterday`, `today 9am`, `last Friday`, and ISO timestamps.
3. Resolve parsed times in the server/user timezone, then normalize to UTC.
4. Validate that `since` is before `until`.
5. Fetch messages from the current channel in that explicit window.
6. Use the same summary formatter as Story 2.1.
7. Save Markdown artifact with a filename that includes date and channel slug.
8. Return helpful errors for unparseable time input or empty windows.
9. Add tests for natural language parsing, explicit timestamps, invalid ranges, and empty results.

Engineering notes:

- Custom time range should not use the 6-hour session heuristic.
- It should still exclude bot messages and require at least 5 human messages.

## Story 3.1: Build Research Brief Workflow

Goal: generate an MBA-style research brief from a Discord command.

Technical steps:

1. Add `/research topic:<text>` command.
2. Create research request schema with topic, requester, channel id, requested depth, and output format.
3. Add research planner that converts the topic into research questions.
4. Retrieve relevant memory when memory MVP exists; skip gracefully before then.
5. Call web research tool when available; before then, support a no-sources draft mode only if clearly labeled.
6. Generate structured brief with executive summary, ICP, market, competitors, SWOT, GTM, pricing, risks, and next experiments.
7. Separate sourced facts from AI analysis.
8. Save Markdown artifact under `docs/artifacts/research/YYYY-MM-DD-topic-slug.md`.
9. Return concise Discord completion response with artifact path.
10. Add tests using fixed research fixtures.

Engineering notes:

- Long-running research should defer the Discord response and post progress updates.
- Final output should be useful even before Notion or Google publishing exists.

## Story 3.3: Add Web Research Tool

Goal: give research briefs verifiable source material.

Technical steps:

1. Define web research tool interface with query input and normalized source output.
2. Return source title, URL, snippet, publisher/domain, retrieved date, and confidence notes.
3. Add query planner that generates multiple searches from a research topic.
4. Deduplicate sources by normalized URL/domain.
5. Rank sources by relevance and credibility.
6. Pass source summaries into the research workflow.
7. Add citation format for Markdown briefs.
8. Add failure mode when sources are weak or unavailable.
9. Add tests with mocked search responses.

Engineering notes:

- Never fabricate source links.
- Clearly distinguish sourced facts from analysis.

## Story 4.1: Build Memory Store MVP

Goal: store and retrieve durable team memory.

Technical steps:

1. Define memory entry schema with id, type, content, source, confidence, timestamps, tags, and optional expiration.
2. Create persistence layer for memory entries.
3. Add embedding generation for semantic retrieval.
4. Add `/remember content:<text>` command for explicit memory writes.
5. Add `/recall query:<text>` command for memory search.
6. Return source, timestamp, confidence, and content in recall results.
7. Add duplicate detection for near-identical memories.
8. Add conflict marker for memories that contradict previous durable facts.
9. Add tests for write, recall, duplicate, and conflict cases.

Engineering notes:

- Automatic memory extraction is not part of this story.
- Explicit user memory writes should be high confidence.

## Story 5.1: Define Agent Orchestrator Interfaces

Goal: create the internal contracts that let commands call agents and tools consistently.

Technical steps:

1. Define `TaskRequest` schema for command-originated work.
2. Define `AgentResult` schema with human response, artifact references, structured data, and errors.
3. Define agent role interface with name, purpose, input schema, and output schema.
4. Define tool registry interface with tool name, description, input schema, permission level, and executor.
5. Add orchestration flow for command handler to memory retrieval, agent execution, tool calls, and publisher.
6. Add tool-call logging.
7. Add recoverable error handling for failed tools.
8. Add tests for a fake command invoking a fake agent and fake tool.

Engineering notes:

- Avoid hard-coding Discord or Notion into agent logic.
- Keep orchestration simple until there is real complexity.

## Story 6.1: Add Markdown Publisher

Goal: save generated summaries and research briefs as Markdown artifacts.

Technical steps:

1. Define artifact metadata schema: type, title, slug, created at, source channel, and path.
2. Create Markdown renderer for summaries.
3. Create Markdown renderer for research briefs.
4. Implement safe slug generation for channel names and topics.
5. Write artifacts under `docs/artifacts/summaries` and `docs/artifacts/research`.
6. Prevent accidental overwrite by appending a sequence or timestamp when needed.
7. Return artifact path to caller.
8. Add tests for path generation, slugging, and Markdown rendering.

Engineering notes:

- This is the MVP publisher.
- Notion and Google publishers should later consume the same artifact data.

## Story 6.2: Add Notion Publisher

Goal: publish selected generated artifacts into Notion.

Technical steps:

1. Configure Notion token and target parent page/database through environment variables.
2. Define Notion publisher interface matching the generic publisher contract.
3. Convert Markdown sections into Notion blocks.
4. Create Notion page for summary or research artifact.
5. Support simple tables for competitors, risks, or action items.
6. Store returned Notion page URL in artifact metadata.
7. Return Notion URL in Discord response.
8. Add mocked tests for Notion payload generation.

Engineering notes:

- This is post-MVP unless product priorities change.
- Notion publishing should be optional per command or config.

## Story 6.3: Add Google Workspace Publisher

Goal: publish selected artifacts into Google Docs, Sheets, or Slides.

Technical steps:

1. Configure Google authentication.
2. Define Google publisher interface matching the generic publisher contract.
3. Create Google Doc from summary or research Markdown.
4. Create Google Sheet from structured tables such as competitor matrix or market assumptions.
5. Create Google Slides outline from research brief sections.
6. Store returned file URLs in artifact metadata.
7. Return created file URLs in Discord response.
8. Add mocked tests for Docs, Sheets, and Slides payload generation.

Engineering notes:

- This is post-MVP unless product priorities change.
- Google publishers should reuse structured artifact data instead of reparsing Discord text.
