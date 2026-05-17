"""Shared schemas for normalized application data."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class DiscordMessage:
    message_id: str
    channel_id: str
    author_id: str
    author_display_name: str
    timestamp: datetime
    content: str
    is_bot: bool
    attachment_urls: tuple[str, ...] = field(default_factory=tuple)
