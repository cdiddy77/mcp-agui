import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "environment" in data


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@pytest.mark.asyncio
async def test_example_get(client: AsyncClient):
    response = await client.get("/api/v1/example/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello from FastAPI!"
    assert "data" in data


@pytest.mark.asyncio
async def test_example_post(client: AsyncClient):
    response = await client.post(
        "/api/v1/example/",
        json={"name": "Test User", "description": "Test Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "Test User" in data["message"]
    assert data["data"]["name"] == "Test User"
