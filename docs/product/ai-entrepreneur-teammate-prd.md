# AI Entrepreneur Teammate PRD

## Product Summary

AI Entrepreneur Teammate is a Discord-native AI teammate for a small founder group. It watches the shared channel, remembers decisions and business context, summarizes discussion windows, and produces MBA-style research deliverables for products, markets, competitors, and business ideas.

The product should feel like a high-agency business analyst who participates when asked, keeps context over time, and turns messy chat into useful strategic assets.

## Target Users

- Founder/operator group of 3 people working in Discord
- Two engineers building and operating the system
- Future users: small startup teams that need research, synthesis, and operating-memory support

## Core Jobs To Be Done

1. When the team has discussed a topic in Discord, summarize the relevant chat so we can quickly recover decisions, ideas, risks, and next actions.
2. When the team is exploring a product, business, market, or competitor, research it like a trained business analyst and produce a polished document.
3. When the team keeps working over weeks, remember durable business context, open questions, decisions, and previous research so the bot gets more useful over time.
4. When output is valuable, publish it into the team's knowledge workspace, starting with Markdown/GitHub and later Notion or Google Workspace.

## MVP Goals

- Discord bot can join one configured server and monitor selected channels.
- Users can request summaries for a time window or the last unresolved session.
- Users can request a structured research brief for a topic, product, market, or business idea.
- Bot stores memory for decisions, facts, preferences, open tasks, and prior research outputs.
- Bot can generate Markdown documentation suitable for GitHub and later export.
- Multi-agent architecture exists internally, even if early agents are simple routed workflows.

## Non-Goals For MVP

- Fully autonomous posting without explicit user command.
- Complex Notion dashboard automation.
- Full Google Slides/Sheets generation.
- Multi-server SaaS onboarding.
- Payment, admin billing, or public marketplace release.
- Real-time voice meeting participation.

## Success Metrics

- A founder can ask for a summary of the last session and get a useful recap in under 60 seconds.
- A founder can ask for a research brief and receive a structured document with sources, analysis frameworks, risks, and recommendations.
- The bot can recall previous decisions and use them in later summaries or research.
- Engineers can add a new tool integration without rewriting the agent orchestration layer.

## MVP User Experience

### Discord Commands

- `/summarize`
  - Defaults to the latest message session in the current channel, using 6+ hours of inactivity as the session boundary.
  - MVP output is a concise Discord reply plus a saved Markdown summary artifact.
  - Discord reply format: Summary date/time, Recap, Action Items, and Open Questions.
  - If there are fewer than 5 human messages, it says there is not enough activity to summarize.
  - Optional arguments: `since`, `until`, `channel`, `topic`.

- `/research`
  - Takes a topic, product, company, market, or idea.
  - Optional arguments: `depth`, `format`, `publish_to`.

- `/remember`
  - Saves an explicit durable memory from the team.
  - Example: `/remember Our ICP is solo real estate investors in Texas.`

- `/recall`
  - Retrieves related memory and previous artifacts.

- `/tasks`
  - Shows open action items discovered from summaries.

## Research Brief Standard

Every research output should include:

- Executive summary
- Business question and assumptions
- Customer and ICP analysis
- Market sizing with cited assumptions
- Competitor landscape
- SWOT analysis
- Porter's Five Forces where relevant
- Business model options
- Go-to-market channels
- Pricing and unit economics assumptions
- Risks and unknowns
- Recommended next experiments
- Source list

## Memory Model

The memory system should separate short-term, episodic, and durable memory.

- Short-term memory: current command context and recent Discord messages.
- Episodic memory: summaries, research briefs, sessions, and decisions over time.
- Durable memory: stable facts about the team, business strategy, preferences, users, and constraints.

Memory entries should include:

- `id`
- `type`
- `content`
- `source`
- `confidence`
- `created_at`
- `updated_at`
- `tags`
- `expires_at` when applicable

## Multi-Agent Design

The orchestrator owns command routing, tool permissions, memory retrieval, and final response assembly.

Initial agents:

- Discord Intake Agent: reads commands and channel context.
- Summarizer Agent: turns chat windows into summaries, decisions, and tasks.
- Research Manager Agent: plans research and delegates sub-analyses.
- Market Analyst Agent: market size, ICP, competitors, trends.
- Strategy Analyst Agent: SWOT, Five Forces, business model, GTM.
- Document Writer Agent: turns analysis into a polished artifact.
- Memory Curator Agent: extracts durable memories and avoids storing noise.
- Publisher Agent: writes Markdown first, then Notion or Google artifacts later.

## Tooling

MVP tools:

- Discord API
- Web search/research provider
- LLM provider
- Vector store or relational database with embeddings
- Markdown artifact writer
- GitHub repository for docs, issues, and code

Post-MVP tools:

- Notion pages, databases, and dashboards
- Google Docs
- Google Sheets
- Google Slides
- Scheduled jobs for daily/weekly digests

## Guardrails

- Ask before storing sensitive durable memory.
- Do not automatically save session summaries into durable memory until that behavior is explicitly confirmed.
- Separate sourced facts from AI inferences.
- Cite sources in research outputs.
- Never fabricate source links.
- Keep channel-specific permissions strict.
- Log tool calls and generated artifacts.
- Allow users to delete memory entries.

## Open Product Questions

- Should summaries be command-only, scheduled, or both?
- Do we want the bot to actively ask follow-up questions in Discord?
- Which workspace is source of truth for polished docs: GitHub, Notion, or Google Drive?
- Which LLM provider and models should we use first?
- How much autonomy should research have before asking for clarification?
