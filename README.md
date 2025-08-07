# MCP AGUI

A monorepo containing a Python FastAPI backend and Next.js frontend for MCP Agent UI.

## Tech Stack

- **Backend**: Python 3.12, FastAPI, uv for package management
- **Frontend**: Next.js 15+, TypeScript, Tailwind CSS, Yarn 2 (Berry)

## Project Structure

```
mcp-agui/
├── backend/          # FastAPI backend
├── frontend/         # Next.js frontend
├── Makefile         # Common commands
└── docker-compose.yml # Local services
```

## Prerequisites

- Python 3.12+
- Node.js 20+
- [uv](https://github.com/astral-sh/uv) for Python package management
- Yarn 2+ for frontend package management

## Getting Started

### Install uv (Python package manager)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install dependencies
```bash
make install
```

### Run development servers
```bash
make dev
```

This will start:
- Backend at http://localhost:8001
- Frontend at http://localhost:3001

## Available Commands

```bash
make install         # Install all dependencies
make dev            # Run both servers
make dev-backend    # Run backend only
make dev-frontend   # Run frontend only
make test           # Run all tests
make lint           # Lint all code
make format         # Format all code
```

## Development

### Backend Development
The FastAPI backend includes:
- Auto-reload in development
- Interactive API docs at http://localhost:8001/api/docs
- Example endpoints and project structure

### Frontend Development
The Next.js frontend includes:
- Fast refresh with webpack
- TypeScript strict mode
- Tailwind CSS for styling
- API proxy configuration for backend

## Testing

```bash
# Run all tests
make test

# Backend tests only
cd backend && uv run pytest

# Frontend tests (when added)
cd frontend && yarn test
```
