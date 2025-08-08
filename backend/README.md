# MCP AGUI Backend

FastAPI backend for the MCP Agent UI.

## Quick Start

```bash
# Install dependencies
uv sync

# Run development server
uv run uvicorn app.main:app --reload

# Run tests
uv run pytest
```

## AG-UI Chat Setup

This backend includes an AG-UI streaming chat endpoint that works with pydanticAI.

### Configuration

1. Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Add your OpenAI API key to `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Testing the Chat Endpoint

Test the AG-UI chat endpoint:

```bash
# Run the test script
uv run python test_chat.py
```

Or test with curl:

```bash
curl -X POST "http://localhost:8001/api/v1/chat" \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Hello! How are you?"
      }
    ],
    "state": {},
    "frontend_url": "http://localhost:3000"
  }'
```

## API Documentation

When running in development mode, visit:

- http://localhost:8001/api/docs - Interactive Swagger UI
- http://localhost:8001/api/redoc - ReDoc documentation
