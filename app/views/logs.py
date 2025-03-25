from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db_session
from app.models import RequestLog

router = APIRouter()


@router.get("/logs")
async def get_logs(
    db: AsyncSession = Depends(get_db_session),
    skip: int = 0,
    limit: int = 10
):
    result = await db.execute(
        select(RequestLog)
        .offset(skip)
        .limit(limit)
        .order_by(RequestLog.timestamp.desc())
    )
    return result.scalars().all()
