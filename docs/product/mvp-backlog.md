# MVP Backlog

## Epic 1: Discord Bot Foundation

### Story 1.1: Configure Discord Bot

As a founder, I want the bot to join our Discord server so that I can interact with it in the team channel.

Acceptance criteria:

- Bot can authenticate with Discord.
- Bot can be invited to one server.
- Bot can read configured channels.
- Bot can respond to slash commands.
- Secrets are loaded from environment variables.

### Story 1.2: Channel Ingestion

As the system, I want to ingest recent Discord messages so that summaries and memory can use channel context.

Acceptance criteria:

- Messages are fetched by channel and time window.
- Author, timestamp, message content, and attachments metadata are preserved.
- Bot messages can be excluded from summary input.
- Fetching respects Discord API limits.

### Story 1.3: Slash Command Framework

As an engineer, I want a reusable command framework so that new bot capabilities are easy to add.

Acceptance criteria:

- `/summarize`, `/research`, `/remember`, `/recall`, and `/tasks` are registered.
- Command handlers share logging and error handling.
- Long-running commands defer responses and post completion updates.

## Epic 2: Chat Summarization

### Story 2.1: Summarize Last Session

As a founder, I want `/summarize` to default to the latest message session so that I can summarize the most recent meaningful conversation even if the channel is currently quiet.

Acceptance criteria:

- A session is a continuous block of messages where no gap between included messages is 6 hours or longer.
- If there have been no messages for the last 6+ hours, `/summarize` summarizes the latest completed session before that inactivity gap.
- If messages are currently active, `/summarize` summarizes the current active session.
- Bot excludes its own messages from summary input.
- Output states the exact time window summarized.
- Output includes recap, decisions, action items, risks, and open questions.
- If there are too few messages to summarize, bot returns a helpful response.

### Story 2.2: Summarize Custom Time Window

As a founder, I want to summarize a specific time range so that I can review any prior discussion.

Acceptance criteria:

- Command accepts `since` and optional `until`.
- Natural-language time inputs are normalized.
- Output names the covered time range.
- Empty windows return a helpful message.

### Story 2.3: Extract Tasks From Summary

As a founder, I want action items extracted from discussions so that follow-through is not lost.

Acceptance criteria:

- Summary output includes tasks with owner when inferable.
- Low-confidence owners are marked as inferred.
- Open tasks are stored for `/tasks`.

## Epic 3: Research Briefs

### Story 3.1: Research Request Intake

As a founder, I want to request research on a topic or product so that the bot can create a useful business brief.

Acceptance criteria:

- `/research topic:<text>` starts a research workflow.
- Bot asks one clarification question only when required.
- Bot posts progress updates for longer jobs.

### Story 3.2: MBA-Style Research Framework

As a founder, I want research to use proven business frameworks so that output is strategically useful.

Acceptance criteria:

- Brief includes executive summary, ICP, market, competitors, SWOT, GTM, pricing, risks, and next experiments.
- Business assumptions are labeled.
- Research distinguishes sourced facts from model analysis.

### Story 3.3: Source Collection

As a founder, I want sources attached to research so that I can verify claims.

Acceptance criteria:

- Important claims include citations.
- Source list is included at the end.
- If sources are weak or unavailable, the brief says so.

### Story 3.4: Research Artifact Creation

As a founder, I want research saved as a durable artifact so that the team can return to it later.

Acceptance criteria:

- Research brief is saved as Markdown in a configured artifact directory.
- Artifact has a stable title, timestamp, and slug.
- Discord response links or references the generated artifact.

## Epic 4: Memory System

### Story 4.1: Durable Memory Store

As the bot, I want to store durable facts so that I can personalize future summaries and research.

Acceptance criteria:

- Memory entries support type, content, source, confidence, timestamps, and tags.
- Explicit `/remember` entries are stored with high confidence.
- Memory can be retrieved by semantic similarity and tags.

### Story 4.2: Memory Recall

As a founder, I want `/recall` to find relevant prior context so that we do not repeat ourselves.

Acceptance criteria:

- Recall accepts a query.
- Results include source and timestamp.
- Results are ranked by relevance.

### Story 4.3: Memory Curation

As the system, I want to extract durable memories from summaries so that useful context accumulates.

Acceptance criteria:

- Candidate memories are extracted after summaries.
- Sensitive or ambiguous memories require confirmation before durable storage.
- Duplicate or conflicting memories are detected.

## Epic 5: Agent Orchestration

### Story 5.1: Orchestrator Interface

As an engineer, I want a central orchestrator so that commands can call agents, memory, and tools consistently.

Acceptance criteria:

- Orchestrator accepts a structured task request.
- Orchestrator can call memory retrieval before LLM work.
- Orchestrator returns structured outputs and human-facing text.

### Story 5.2: Tool Registry

As an engineer, I want tools registered behind a common interface so that we can add Notion and Google later.

Acceptance criteria:

- Tools have name, description, input schema, and permission level.
- Tool calls are logged.
- Failed tool calls return recoverable errors.

### Story 5.3: Agent Roles

As an engineer, I want clearly defined agent roles so that research and summarization are modular.

Acceptance criteria:

- Summarizer, Research Manager, Analyst, Writer, Memory Curator, and Publisher roles exist.
- Each role has an input and output contract.
- Agents can be tested independently with fixture inputs.

## Epic 6: Publishing And Workspace Integrations

### Story 6.1: Markdown Publisher

As a founder, I want generated docs stored in the repo so that GitHub can be our first source of truth.

Acceptance criteria:

- Summaries and research briefs can be saved as Markdown.
- Files are organized by artifact type and date.
- File names are stable and readable.

### Story 6.2: Notion Publishing

As a founder, I want research briefs published to Notion so that the team can use Notion as an operating workspace.

Acceptance criteria:

- Notion integration is configured with token and target database/page.
- Bot can create a research page.
- Bot can create or update basic tables.
- Notion URL is returned in Discord.

### Story 6.3: Google Workspace Publishing

As a founder, I want the bot to create Google Docs, Sheets, and Slides so that research can become docs, dashboards, and presentations.

Acceptance criteria:

- Google auth is configured.
- Bot can create a Google Doc from a brief.
- Bot can create a basic Sheet table for competitor or market data.
- Bot can create a simple Slides outline from a brief.

## MVP Priority

P0:

- Discord bot foundation
- Slash commands
- Last-session summary
- Custom-window summary
- Markdown research brief
- Basic durable memory
- Orchestrator and tool registry

P1:

- Task extraction
- Memory curation from summaries
- Source-backed deeper research
- Markdown artifact publishing

P2:

- Notion publishing
- Google Docs/Sheets/Slides
- Dashboards
- Scheduled summaries
