import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import RequestLog


def test_info_endpoint(client):
    response = client.post(
        "/info",
        json={"address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi"}
    )

    assert response.status_code == 200
    assert response.json()['address'] == 'TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi'


def test_logs_endpoint(client):
    response = client.get("/logs?skip=0&limit=1")

    assert response.status_code == 200
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_db_write(db: AsyncSession):
    log = RequestLog(address="TX...")
    db.add(log)
    await db.commit()

    result = await db.execute(select(RequestLog).filter_by(address="TX..."))
    fetched_log = result.scalars().first()

    assert fetched_log is not None, "Запись не появилась в базе данных"
    assert fetched_log.address == "TX...", "Адрес записи не совпадает с ожидаемым"
