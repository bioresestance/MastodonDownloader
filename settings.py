from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache

class Settings(BaseSettings):
    access_code: str = Field("", env="ACCESS_CODE")
    mastodon_url: str = Field("https://mastodon.social", env="MASTODON_URL")
    mastodon_user: str = Field("", env="MASTODON_USER")



    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')



@lru_cache()
def get_settings() -> Settings:
    return Settings()