from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class ConfigDict:
        env_file = '.env'

    TRON_API_URL: str = 'https://api.trongrid.io'
    TRON_API_KEY: str = 'fbdc3ad7-8b59-4c97-b053-ce804190c298'
    DATABASE_URL: str = 'sqlite+aiosqlite:///./test.db'
    BASE_URL: str = 'http://localhost:8000/api/v1'


@lru_cache()
def get_settings():
    return Settings()
