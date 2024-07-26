import os
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import DirectoryPath


class Settings(BaseSettings):
    PG_HOST: str = os.getenv("POSTGRES_HOST")
    PG_PORT: str = os.getenv("POSTGRES_PORT")
    PG_DB: str = os.getenv("POSTGRES_DB")
    PG_USER: str = os.getenv("POSTGRES_USER")
    PG_PASS: str = os.getenv("POSTGRES_PASSWORD")
    PG_URL: str = (f'postgresql+asyncpg://{PG_USER}:{PG_PASS}'
                   f'@{PG_HOST}:{PG_PORT}/{PG_DB}')
    BASE_DIR: DirectoryPath = Path(os.path.dirname(__file__)).parents[0]


settings = Settings()
