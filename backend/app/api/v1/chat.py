from fastapi import APIRouter
from pydantic_ai.ag_ui import handle_ag_ui_request
from starlette.requests import Request
from starlette.responses import Response

from app.services.chat_agent import get_chat_agent

router = APIRouter()


@router.post("/chat")
async def stream_chat(request: Request) -> Response:
    """Handle AG-UI streaming chat requests."""
    return await handle_ag_ui_request(get_chat_agent(), request)
