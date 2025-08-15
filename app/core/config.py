from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field



class Settings(BaseSettings):
    JWT_SECRET: str = "change_me"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    DATABASE_URL: str = Field(default=..., validation_alias="DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
