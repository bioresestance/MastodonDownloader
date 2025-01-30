# MastodonDownloader
Tool to automate downloading media from a Mastodon user. This tool will go to a Mastodon users profile, get all of their posts, Likes and reposts and download all attached media off of them. This will include photos and videos.


# Requirements
- python 3.12 (or greater)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bioresestance/MastodonDownloader
    cd MastodonDownloader
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

You may either use environment variables or command line arguments to configure the script.

### Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```

ACCESS_CODE=<your_mastodon_access_code> 

MASTODON_URL=https://mastodon.social 

MASTODON_USER=<your_mastodon_username> 

# Set to 0 for no limit 
DOWNLOAD_LIMIT=0 

# Optional to use an external mySQL database instead of a sqlite DB.
SQL_URL=<your_sql_url> 
SQL_PASSWORD=<your_sql_password> 
SQL_DB=<your_sql_database_name>

```

### Command Line Arguments
``` sh
python main.py --access_code <your_mastodon_access_code> --mastodon_url <mastodon_instance_url> --mastodon_user <mastodon_username> --download_limit <limit> --sql-url <sql_url> --sql-user <sql_user> --sql-password <sql_password> --sql-db <sql_database_name>
```

### Access Code
In order to get an access code for the script, you must register the app with your Mastodon instance.

In your logged in Mastodon instance, go to `settings` -> `Development` -> `New Application`. Follow the steps and give the app appropriate permissions. Save the access code for usage with the above.
