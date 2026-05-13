# GitHub Issues Seed

Use this file to create initial GitHub issues manually or through automation.

## Issue 1: Story 0.1: Initialize Project Repository

Labels: `type:feature`, `priority:p0`

Description:

Set up the base repo structure, development tooling, and environment configuration.

Acceptance criteria:

- Runtime selected: TypeScript or Python.
- Formatter, linter, and test runner are configured.
- Example `.env` is documented.
- Product docs are committed under `docs/product`.

## Issue 2: Story 1.1: Create Discord Bot Skeleton

Labels: `type:feature`, `area:discord`, `priority:p0`

Description:

Create the Discord bot app with slash command registration and a basic health command.

Acceptance criteria:

- Bot authenticates using environment variables.
- Bot can register slash commands.
- `/ping` responds successfully.
- Logging exists for command invocation and errors.

## Issue 3: Story 1.2: Implement Message Window Fetching

Labels: `type:feature`, `area:discord`, `priority:p0`

Description:

Fetch Discord messages from a configured channel by time window.

Acceptance criteria:

- Fetch supports `since` and `until`.
- Message author, timestamp, content, and attachment metadata are captured.
- Bot messages can be excluded.
- API rate limits are handled gracefully.

## Issue 4: Story 2.1: Implement `/summarize` Last Session

Labels: `type:feature`, `area:agents`, `area:discord`, `priority:p0`

Description:

Create the first useful summary workflow for the latest Discord message session.

Product status: Approved.

Acceptance criteria:

- `/summarize` without arguments finds the latest message session in the current channel only.
- A session is a continuous block of messages where no gap between included messages is 6 hours or longer.
- If there have been no messages for the last 6+ hours, `/summarize` summarizes the latest completed session before that inactivity gap.
- If messages are currently active, `/summarize` summarizes the current active session.
- Bot excludes its own messages from the summary.
- Discord reply includes Summary date/time, Recap, Action Items, and Open Questions.
- Markdown artifact can include richer detail such as decisions, risks/blockers, participants, and potential memory candidates.
- Bot states the time window it summarized.
- If there are fewer than 5 human messages, bot says there is not enough activity to summarize.
- MVP output is a concise Discord reply plus a saved Markdown summary artifact.
- Markdown summaries are saved under `docs/artifacts/summaries/YYYY-MM-DD-channel-name-summary.md`.
- Bot may infer action item owners from chat, but uncertain owners must be marked `Unassigned`.
- The session summary can later become memory input, but memory saving is not automatic unless confirmed.

## Issue 5: Story 2.2: Implement `/summarize` Custom Time Range

Labels: `type:feature`, `area:discord`, `area:agents`, `priority:p0`

Description:

Allow users to summarize an explicit time range.

Acceptance criteria:

- Slash command accepts `since` and `until`.
- Time parsing supports common natural language inputs.
- Output states the exact covered time range.
- Empty result windows return a helpful response.

## Issue 6: Story 5.1: Define Agent Orchestrator Interfaces

Labels: `type:feature`, `area:agents`, `priority:p0`

Description:

Create the central interfaces for task routing, agent execution, memory lookup, and tool use.

Acceptance criteria:

- Orchestrator accepts structured task requests.
- Agent input and output contracts are defined.
- Tool calls pass through a registry.
- Workflows are testable without Discord.

## Issue 7: Story 4.1: Build Memory Store MVP

Labels: `type:feature`, `area:memory`, `priority:p0`

Description:

Implement durable memory storage and retrieval.

Acceptance criteria:

- Memory schema includes content, type, source, confidence, timestamps, and tags.
- `/remember` stores explicit memories.
- `/recall` retrieves relevant memories.
- Memory retrieval can be injected into summary and research workflows.

## Issue 8: Story 3.1: Build Research Brief Workflow

Labels: `type:feature`, `area:research`, `area:agents`, `priority:p0`

Description:

Implement `/research` to generate an MBA-style Markdown brief.

Acceptance criteria:

- Command accepts a topic or business idea.
- Brief includes executive summary, ICP, market, competitors, SWOT, GTM, pricing, risks, and next experiments.
- Claims are separated into sourced facts and analysis.
- Output is saved as Markdown.

## Issue 9: Story 3.3: Add Web Research Tool

Labels: `type:feature`, `area:research`, `priority:p1`

Description:

Add a web research tool that can collect sources for research briefs.

Acceptance criteria:

- Tool returns title, URL, snippet, and retrieved date.
- Research workflow cites sources.
- Weak source coverage is explicitly flagged.

## Issue 10: Story 6.1: Add Markdown Publisher

Labels: `type:feature`, `area:publishing`, `priority:p1`

Description:

Create a publisher that writes generated artifacts to the repo.

Acceptance criteria:

- Summaries and research briefs are saved under `docs/artifacts`.
- Filenames include date and slug.
- Discord response includes artifact path.

## Issue 11: Story 6.2: Add Notion Publisher

Labels: `type:feature`, `area:publishing`, `priority:p2`

Description:

Publish research briefs and summaries to Notion.

Acceptance criteria:

- Notion auth is documented.
- Bot can create a Notion page from a Markdown artifact.
- Bot can create simple tables for competitor or market data.
- Discord response includes Notion page URL.

## Issue 12: Story 6.3: Add Google Workspace Publisher

Labels: `type:feature`, `area:publishing`, `priority:p2`

Description:

Publish generated artifacts into Google Docs, Sheets, and Slides.

Acceptance criteria:

- Google auth is documented.
- Bot can create a Google Doc from a research brief.
- Bot can create a Google Sheet for structured tables.
- Bot can create a Slides outline from a brief.
