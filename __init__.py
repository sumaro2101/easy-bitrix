import os

DEFAULT_API_URL = 'https://{}.bitrix24.{}/rest/{}.json'
DEFAULT_OAUTH_URL = 'https://oauth.bitrix24.tech/oauth/token/'
CLIENT_ID = os.getenv('CLIENT_ID')
log = 'debug'
max_network_retries: int = 5

from easy_bitrix import error
from easy_bitrix import parameters
from easy_bitrix import operations
from easy_bitrix.options import RequestOptions
from easy_bitrix.bitrix_objects import Deal, Contact
from easy_bitrix.bitrix import Bitrix24
