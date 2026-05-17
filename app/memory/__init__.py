"""Memory models and context packet helpers."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

MemoryScope = Literal["shared_team", "agent_scoped", "session"]
MemorySource = Literal["user_confirmed", "agent_proposed", "system"]


@dataclass(frozen=True)
class MemoryEntry:
    memory_id: str
    scope: MemoryScope
    content: str
    source: MemorySource
    confidence: float
    created_at: datetime
    tags: tuple[str, ...] = field(default_factory=tuple)
    agent_id: str | None = None
