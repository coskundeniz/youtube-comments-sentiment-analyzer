import os

# client_secret files
CLIENT_SECRETS_FILE = "credentials.json"
CLIENT_SECRETS_FILE_CONSOLE = os.path.join(os.path.expanduser("~"), "client_secret_for_oauth.json")

API_KEY = os.environ.get("YOUTUBE_DATA_API_KEY")

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
