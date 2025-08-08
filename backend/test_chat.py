#!/usr/bin/env python3
"""
Simple test script to verify the AG-UI chat endpoint works.
This simulates what an AG-UI frontend would send.
"""

import asyncio
import uuid

import httpx
from ag_ui.core import RunAgentInput
from ag_ui.core.types import UserMessage


async def test_chat_endpoint():
    """Test the chat endpoint with a proper AG-UI message structure."""

    # Create a proper AG-UI user message
    user_message = UserMessage(
        id=str(uuid.uuid4()), content="Hello! Can you help me with a simple question?"
    )

    # Create the AG-UI run input with all required fields
    run_input = RunAgentInput(
        thread_id=str(uuid.uuid4()),
        run_id=str(uuid.uuid4()),
        messages=[user_message],
        state={},
        tools=[],
        context=[],
        forwarded_props={},
    )

    # Send request to the chat endpoint
    url = "http://localhost:8001/api/v1/chat"

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                url,
                json=run_input.model_dump(),
                headers={
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
            )

            print(f"Status: {response.status_code}")
            print(f"Content-Type: {response.headers.get('content-type')}")
            print("\nResponse:")
            if response.status_code == 200:
                print("✅ Success! AG-UI Stream response:")
                # Show first 8000 characters of streaming response
                response_text = response.text
                if len(response_text) > 8000:
                    print(response_text[:8000] + "\n... (truncated)")
                else:
                    print(response_text)
            else:
                print("❌ Error response:")
                print(response.text)

        except Exception as e:
            print(f"❌ Request failed: {e}")


if __name__ == "__main__":
    asyncio.run(test_chat_endpoint())
