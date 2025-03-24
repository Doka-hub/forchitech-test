import pytest

from app.models import RequestLog


@pytest.mark.asyncio
async def test_info_endpoint(async_client):
    response = await async_client.post(
        "/info",
        json={"address": "TX0000000000000000000000000000000000"}
    )
    assert response.status_code == 200
    assert all(key in response.json() for key in ["balance", "bandwidth"])


@pytest.mark.asyncio
async def test_logs_endpoint(async_client, db_session):
    # Создаем тестовую запись
    log = RequestLog(address="TXtestaddress")
    db_session.add(log)
    await db_session.commit()

    response = await async_client.get("/logs?skip=0&limit=1")
    assert response.status_code == 200
    assert len(response.json()) == 1
