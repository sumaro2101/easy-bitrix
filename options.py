from . import DEFAULT_API_URL, DEFAULT_OAUTH_URL, max_network_retries
from typing import ClassVar, TypedDict, Literal


class APIAddresses(TypedDict):
    api: str | None
    oauth: str | None


class RequestOptions(TypedDict):
    max_network_retries: int | None
    oauth_token: str | None
    client_id: str | None
    user_id: str | None
    webhook_url: str | None
    high_level_domain: Literal['ru', 'com', 'de'] | None


class RequestorOptions:
    max_network_retries: ClassVar[int | None]
    api_addresses: ClassVar[APIAddresses]
    oauth_token: ClassVar[str | None]
    client_id: ClassVar[str | None]
    user_id: ClassVar[str | None]
    webhook_url: ClassVar[str | None]
    high_level_domain: ClassVar[Literal['ru', 'com', 'de'] | None]

    def __init__(self,
                 api_addresses: APIAddresses | None = None,
                 max_network_retries: int | None = None,
                 oauth_token: str | None = None,
                 client_id: str | None = None,
                 user_id: str | None = None,
                 webhook_url: str | None = None,
                 high_level_domain: Literal['ru', 'com', 'de'] | None = None,
                 ):
        self.api_addresses = dict()
        self.max_network_retries = max_network_retries
        if api_addresses:
            if api := api_addresses.get('api'):
                self.api_addresses['api'] = api
            if oauth := api_addresses.get('oauth'):
                self.api_addresses['oauth'] = oauth
        self.oauth_token = oauth_token
        self.client_id = client_id
        self.user_id = user_id
        self.webhook_url = webhook_url
        self.high_level_domain = high_level_domain

    def to_dict(self):
        return {
            'api_addresses': self.api_addresses,
            'max_network_retries': self.max_network_retries,
            'oauth_token': self.oauth_token,
            'client_id': self.client_id,
            'user_id': self.user_id,
            'webhook_url': self.webhook_url,
            'high_level_domain': self.high_level_domain,
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


def merge_options(
    requestor: RequestorOptions,
    request: RequestOptions | None,
) -> RequestOptions:
    if request is None:
        return {
            'max_network_retries': requestor.max_network_retries,
            'api_addresses': requestor.api_addresses,
            'oauth_token': None,
            'client_id': None,
            'user_id': None,
            'webhook_url': None,
            'high_level_domain': None,
        }

    return {
        'max_network_retries': request.get('max_network_retries')
        if request.get('max_network_retries') is not None
        else requestor.max_network_retries,
        'api_addresses': requestor.api_addresses,
        'oauth_token': request.get('oauth_token'),
        'client_id': request.get('client_id'),
        'user_id': request.get('user_id'),
        'webhook_url': request.get('webhook_url'),
        'high_level_domain': request.get('high_level_domain'),
    }
