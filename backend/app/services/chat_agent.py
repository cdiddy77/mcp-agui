import os

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.ag_ui import StateDeps

from app.core.config import settings


class ChatState(BaseModel):
    """State for the chat conversation."""

    conversation_history: list[str] = []
    user_name: str = "User"


_chat_agent: Agent | None = None


def get_chat_agent() -> Agent:
    """Get or create the chat agent instance."""
    global _chat_agent

    if _chat_agent is None:
        # Set OpenAI API key from settings if available
        if settings.OPENAI_API_KEY:
            os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

        # Create the chat agent with OpenAI GPT-4
        _chat_agent = Agent(
            "openai:gpt-4",
            instructions="""You are a helpful AI assistant in a streaming chat interface.
            Be conversational, helpful, and engaging. Keep responses concise but informative.
            You can see the conversation history in the state.""",
            deps_type=StateDeps[ChatState],
        )

        @_chat_agent.tool
        async def get_conversation_history(ctx) -> str:
            """Get the current conversation history."""
            history = ctx.deps.state.conversation_history
            if not history:
                return "No previous conversation history."

            return "Previous conversation:\n" + "\n".join(history)

        @_chat_agent.tool
        async def update_conversation(ctx, message: str) -> str:
            """Add a message to the conversation history."""
            ctx.deps.state.conversation_history.append(message)
            return f"Added message to conversation history: {message}"

    return _chat_agent
