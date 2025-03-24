from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer

from app.database import Base


class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True)
    address = Column(String(42), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
