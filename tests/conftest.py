import pytest

from fastapi.testclient import TestClient

from app.database import engine, Base
from app.main import app


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def async_client():
    async with TestClient(app, base_url="http://test") as ac:
        yield ac
