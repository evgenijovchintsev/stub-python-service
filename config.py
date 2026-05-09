from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    db_url: str = "postgresql+asyncpg://user:password@localhost:5432/db"
    jwt_secret: str = "change-me"
    jwt_expire_minutes: int = 60
    debug: bool = False


settings = Settings()
