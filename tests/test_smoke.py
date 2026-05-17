from datetime import UTC, datetime

from app.agents import INITIAL_AGENT_ROLES
from app.schemas import DiscordMessage


def test_initial_agent_roles_are_defined() -> None:
    assert [role.agent_id for role in INITIAL_AGENT_ROLES] == [
        "orchestrator",
        "summarizer",
        "researcher",
        "planner",
        "memory_curator",
    ]


def test_discord_message_schema_smoke() -> None:
    message = DiscordMessage(
        message_id="message-1",
        channel_id="channel-1",
        author_id="user-1",
        author_display_name="Founder",
        timestamp=datetime(2026, 5, 17, 12, 0, tzinfo=UTC),
        content="Summarize the latest chunk.",
        is_bot=False,
    )

    assert message.content == "Summarize the latest chunk."
    assert not message.is_bot
