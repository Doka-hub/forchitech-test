from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import TronAddress, TronInfoResponse
from app.services import get_tron_info
from app.models import RequestLog
from app.database import get_db_session

router = APIRouter()


@router.post("/info", response_model=TronInfoResponse)
async def get_info(
    address: TronAddress,
    db: AsyncSession = Depends(get_db_session),
):
    tron_info = await get_tron_info(address.address)

    instance = RequestLog(address=address.address)
    db.add(instance)

    await db.commit()

    return tron_info
