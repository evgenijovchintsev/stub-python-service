"""Application configuration loaded from environment variables."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Service settings resolved from .env or environment variables."""

    model_config = SettingsConfigDict()  # No env_file to avoid missing file errors.

    db_url: str = Field("postgresql+asyncpg://user:password@localhost:5432/db", env="DB_URL")
    jwt_secret: str = Field("change-me", env="JWT_SECRET")
    jwt_expire_minutes: int = Field(60, env="JWT_EXPIRE_MINUTES")
    debug: bool = Field(False, env="DEBUG")


settings = Settings()
