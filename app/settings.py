import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    TG_BOT_TOKEN: str
    NEWS_API_URL: str
    NEWS_API_KEY: str
    REDIS_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
