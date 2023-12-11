import asyncio
from typing import AsyncGenerator

import httpx
import pytest
import pytest_asyncio

from .auth.auth import current_user
from .auth.models import User
from .database import async_session_maker, get_async_session
from .main import app

user = User(
    email="temp@mail.com",
    hashed_password="temp",
    is_active=True,
    is_verified=False,
    is_superuser=False,
)


async def override_get_async_session() -> AsyncGenerator | None:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Force the pytest-asyncio loop to be the main one."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def user_client():
    app.dependency_overrides[current_user] = lambda: user
    async with httpx.AsyncClient(
            app=app, base_url="http://test"
    ) as test_client:
        yield test_client


@pytest.mark.asyncio
async def test_create_rating(user_client: httpx.AsyncClient):
    response = await user_client.post("/api/ratings", json={"comic_id": 100, "VALUE": 5})
    assert response.status_code == 200, response.text
    assert response.json() == {
        'VALUE': 5,
        'comic_id': 100,
        'user_id': None,
    }


@pytest.mark.asyncio
async def test_get_rating(user_client: httpx.AsyncClient):
    response = await user_client.get("/api/comics/100/rating")
    assert response.status_code == 200
    assert response.json() == 3.8, response.json()
