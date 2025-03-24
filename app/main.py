from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from app.database import create_tables, engine, get_db_session
from app.routers import info, logs


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Асинхронный менеджер жизненного цикла приложения"""
    # Инициализация при старте
    print("Starting service...")
    await create_tables()

    # Тестовое подключение к Tron
    from tronpy import AsyncTron
    async with AsyncTron(network="shasta") as client:
        print(f"Connected to Tron {client} network")

    yield  # Здесь приложение работает

    # Очистка при завершении
    print("Shutting down...")
    await engine.dispose()

app = FastAPI(
    title="Tron Address Analyzer",
    lifespan=lifespan,
    dependencies=[Depends(get_db_session)]
)

# Подключение роутеров
app.include_router(info.router, prefix="/api/v1")
app.include_router(logs.router, prefix="/api/v1")
