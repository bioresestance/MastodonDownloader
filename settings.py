from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache
import argparse

class Settings(BaseSettings):
    access_code: str = Field("", env="ACCESS_CODE")
    mastodon_url: str = Field("https://mastodon.social", env="MASTODON_URL")
    mastodon_user: str = Field("", env="MASTODON_USER")
    download_limit: int = Field(0, env="DOWNLOAD_LIMIT")
    sql_url: str = Field("", env="SQL_URL")
    sql_user: str = Field("", env="SQL_USER")
    sql_password: str = Field("", env="SQL_PASSWORD")
    sql_db: str = Field("", env="SQL_DB")

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    parser = argparse.ArgumentParser(description="Mastodon Downloader Settings")
    parser.add_argument("--access_code", type=str, help="Access code for Mastodon API")
    parser.add_argument("--mastodon_url", type=str, help="Mastodon instance URL")
    parser.add_argument("--mastodon_user", type=str, help="Mastodon username")
    parser.add_argument("--download_limit", type=int, help="Limit the number of files to download")
    parser.add_argument("--sql-url", type=str, help="URL for an external SQL database")
    parser.add_argument("--sql-user", type=str, help="Username for an external SQL database")
    parser.add_argument("--sql-password", type=str, help="Password for an external SQL database")
    parser.add_argument("--sql-db", type=str, help="Database name for an external SQL database", default="Mastodon")

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
    if args.sql_url:
        settings.sql_url = args.sql_url
    if args.sql_user:
        settings.sql_user = args.sql_user
    if args.sql_password:
        settings.sql_password = args.sql_password
    if args.sql_db:
        settings.sql_db = args.sql_db

    return settings