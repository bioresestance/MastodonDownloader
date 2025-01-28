from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache
import argparse

class Settings(BaseSettings):
    access_code: str = Field("", env="ACCESS_CODE")
    mastodon_url: str = Field("https://mastodon.social", env="MASTODON_URL")
    mastodon_user: str = Field("", env="MASTODON_USER")
    download_limit: int = Field(0, env="DOWNLOAD_LIMIT")

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    parser = argparse.ArgumentParser(description="Mastodon Downloader Settings")
    parser.add_argument("--access_code", type=str, help="Access code for Mastodon API")
    parser.add_argument("--mastodon_url", type=str, help="Mastodon instance URL")
    parser.add_argument("--mastodon_user", type=str, help="Mastodon username")
    parser.add_argument("--download_limit", type=int, help="Limit the number of files to download")

    args = parser.parse_args()

    settings = Settings()

    if args.access_code:
        settings.access_code = args.access_code
    if args.mastodon_url:
        settings.mastodon_url = args.mastodon_url
    if args.mastodon_user:
        settings.mastodon_user = args.mastodon_user
    if args.download_limit is not None:
        settings.download_limit = args.download_limit

    return settings