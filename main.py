from mastodon import Mastodon
from settings import get_settings
import requests
import os


settings = get_settings()


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

    while True:
        for post in posts:
            for media in post['reblog']['media_attachments']:
                url = media['url']
                filename = url.split("/")[-1]
                download_file(url, "./Files/" + filename)
                print(f"Downloaded {filename}")
    
        posts = mastodon.fetch_next(posts)
        if not posts or posts == None:
            break



if __name__ == "__main__":
    main()
