#!/usr/bin/env python3
"""
Simple test using raw HTTP request to test the AG-UI endpoint
"""

import asyncio
import uuid

import httpx


async def test_simple():
    """Test with minimal AG-UI payload"""

    payload = {
        "threadId": str(uuid.uuid4()),
        "runId": str(uuid.uuid4()),
        "messages": [
            {"role": "user", "id": str(uuid.uuid4()), "content": "Hello! How are you?"}
        ],
        "state": {},
        "tools": [],
        "context": [],
        "forwardedProps": {},
    }

    url = "http://localhost:8001/api/v1/chat"

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                url,
                json=payload,
                headers={
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
            )

            print(f"Status: {response.status_code}")
            print(f"Content-Type: {response.headers.get('content-type')}")
            print("\nResponse:")
            if response.status_code == 200:
                print("✅ Success! Stream response:")
                print(
                    response.text[:500] + "..."
                    if len(response.text) > 500
                    else response.text
                )
            else:
                print("❌ Error response:")
                print(response.text)

        except Exception as e:
            print(f"❌ Request failed: {e}")


if __name__ == "__main__":
    asyncio.run(test_simple())
