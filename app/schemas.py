from datetime import datetime

from pydantic import BaseModel


class TronAddress(BaseModel):
    address: str


class TronInfoResponse(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance: float


class LogResponse(BaseModel):
    address: str
    timestamp: datetime
