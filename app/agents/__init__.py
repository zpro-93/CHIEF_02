"""Agent role definitions and orchestration helpers."""

from dataclasses import dataclass
from typing import Literal

AgentId = Literal["orchestrator", "summarizer", "researcher", "planner", "memory_curator"]


@dataclass(frozen=True)
class AgentRole:
    """Descriptive role metadata, not a permissions or authorization model."""

    agent_id: AgentId
    purpose: str


INITIAL_AGENT_ROLES: tuple[AgentRole, ...] = (
    AgentRole(
        agent_id="orchestrator",
        purpose="Classify requests, select specialist agents, and coordinate tools and memory.",
    ),
    AgentRole(
        agent_id="summarizer",
        purpose="Summarize Discord message chunks and extract action items and open questions.",
    ),
    AgentRole(
        agent_id="researcher",
        purpose="Create MBA-style business research briefs with sourced facts and analysis.",
    ),
    AgentRole(
        agent_id="planner",
        purpose="Create execution plans, trackers, dashboards, and scheduling recommendations.",
    ),
    AgentRole(
        agent_id="memory_curator",
        purpose="Manage shared, agent-scoped, and session memory as context packets.",
    ),
)
