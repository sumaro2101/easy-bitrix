import os

DEFAULT_API_URL = 'https://{}.bitrix24.{}/rest/{}.json'
DEFAULT_OAUTH_URL = 'https://oauth.bitrix.info/oauth/token/'
CLIENT_ID = os.getenv('CLIENT_ID')
log = 'debug'
max_network_retries: int = 5
