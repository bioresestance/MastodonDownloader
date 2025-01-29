from mastodon import Mastodon
from settings import get_settings
from peewee import Model, CharField, SqliteDatabase, MySQLDatabase
import requests
import os


settings = get_settings()

if settings.sql_url:
    db = MySQLDatabase( settings.sql_db, user=settings.sql_user, password=settings.sql_password,
                       host=settings.sql_url, port=3306)
else:
    db = SqliteDatabase('database.db')

class Media(Model):
    mastodon_id = CharField(primary_key=True, unique=True)
    mastodon_url = CharField()

    class Meta:
        database = db


def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def main():

    if not os.path.exists('./Files'):
        os.makedirs('./Files')


    mastodon = Mastodon(access_token = settings.access_code, api_base_url = settings.mastodon_url)
    user = mastodon.account_lookup(settings.mastodon_user)
    posts = mastodon.account_statuses(user['id'])

    max_downloads = settings.download_limit

    current_downloads = 0

    while True:
        for post in posts:
            for media in post['reblog']['media_attachments']:

                if max_downloads > 0 and current_downloads >= max_downloads:
                    print(f"Download limit reached, stopping...")
                    break
                try:
                    url = media['url']
                    filename = url.split("/")[-1]

                    if filename == "original":
                        continue

                    file_id = filename.split(".")[0]

                    if Media.select().where(Media.mastodon_id == file_id).exists():
                        print(f"Already downloaded {filename}, skipping...")
                        continue

                    Media.create(mastodon_id=file_id, mastodon_url=url)

                    download_file(url, "./Files/" + filename)
                    print(f"Downloaded {filename}")
                    current_downloads += 1
                except Exception as e:
                    print(f"Error downloading {filename}: {e}")
                    continue
    
        if max_downloads > 0 and current_downloads >= max_downloads:
            break
        posts = mastodon.fetch_next(posts)
        if not posts or posts == None:
            break



if __name__ == "__main__":
    db.connect()

    if not Media.table_exists():
        db.create_tables([Media])

    main()
    db.close()
