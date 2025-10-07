from . import DEFAULT_API_URL, DEFAULT_OAUTH_URL, max_network_retries
from typing import ClassVar, TypedDict


class APIAddresses(TypedDict):
    api: str | None
    oauth: str | None


class RequestOptions(TypedDict):
    max_network_retries: int | None
    oauth_key: str | None
    client_id: str | None
    user_id: str | None
    webhook_url: str | None


class RequestorOptions:
    max_network_retries: ClassVar[int | None]
    api_addresses: ClassVar[APIAddresses]
    oauth_key: ClassVar[str | None]
    client_id: ClassVar[str | None]
    user_id: ClassVar[str | None]
    webhook_url: ClassVar[str | None]

    def __init__(self,
                 api_addresses: APIAddresses | None = None,
                 max_network_retries: int | None = None,
                 oauth_key: str | None = None,
                 client_id: str | None = None,
                 user_id: str | None = None,
                 webhook_url: str | None = None,
                 ):
        self.api_addresses = dict()
        self.max_network_retries = max_network_retries
        if api_addresses:
            if api := api_addresses.get('api'):
                self.api_addresses['api'] = api
            if oauth := api_addresses.get('oauth'):
                self.api_addresses['oauth'] = oauth
        self.oauth_key = oauth_key
        self.client_id = client_id
        self.user_id = user_id
        self.webhook_url = webhook_url

    def to_dict(self):
        return {
            'api_addresses': self.api_addresses,
            'max_network_retries': self.max_network_retries,
            'oauth_key': self.oauth_key,
            'client_id': self.client_id,
            'user_id': self.user_id,
            'webhook_url': self.webhook_url,
        }


class GlobalRequestorOptions(RequestorOptions):
    def __init__(self):
        pass

    @property
    def api_addresses(self):
        return {
            'api': DEFAULT_API_URL,
            'oauth': DEFAULT_OAUTH_URL,
        }

    @property
    def max_network_retries(self):
        return max_network_retries
