"""MCP-oriented tool interfaces and adapters."""

from dataclasses import dataclass
from typing import Literal

ToolPermission = Literal["read", "write", "admin"]


@dataclass(frozen=True)
class ToolRequest:
    tool_name: str
    permission: ToolPermission
    payload: dict[str, object]
