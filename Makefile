.PHONY: install install-backend install-frontend dev dev-backend dev-frontend test test-backend test-frontend lint lint-backend lint-frontend format format-backend format-frontend clean

# Install everything
install: install-backend install-frontend
	@echo "✅ All dependencies installed"

install-backend:
	@echo "📦 Installing backend dependencies..."
	@cd backend && uv sync

install-frontend:
	@echo "📦 Installing frontend dependencies..."
	@cd frontend && yarn install

# Development
dev:
	@echo "🚀 Starting development servers..."
	@make -j2 dev-backend dev-frontend

dev-backend:
	@echo "🔧 Starting FastAPI backend..."
	@cd backend && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8001

dev-frontend:
	@echo "🔧 Starting Next.js frontend..."
	@cd frontend && yarn dev --port 3001

# Testing
test: test-backend test-frontend
	@echo "✅ All tests passed"

test-backend:
	@echo "🧪 Running backend tests..."
	@cd backend && uv run pytest

test-frontend:
	@echo "🧪 Running frontend tests..."
	@cd frontend && yarn test

# Linting
lint: lint-backend lint-frontend
	@echo "✅ All linting passed"

lint-backend:
	@echo "🔍 Linting backend..."
	@cd backend && uv run ruff check .

lint-frontend:
	@echo "🔍 Linting frontend..."
	@cd frontend && yarn lint

# Formatting
format: format-backend format-frontend
	@echo "✅ All code formatted"

format-backend:
	@echo "✨ Formatting backend..."
	@cd backend && uv run ruff format .

format-frontend:
	@echo "✨ Formatting frontend..."
	@cd frontend && yarn format

# Clean
clean:
	@echo "🧹 Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".next" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleanup complete"