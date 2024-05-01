from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    token: SecretStr
    secret_token = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()