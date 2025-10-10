from json import loads
from logging import info
from requests import post

from .options import RequestOptions
from .error import CreateDefaultOptionsError
from .common import LogicErrors
from .api_requestor import APIRequestor
from .dto import SelectData
from . import CLIENT_ID


class Bitrix24:
    """Class for working with Bitrix24 cloud API"""

    def __init__(self,
                 bitrix_address: str,
                 refresh_token: str | None = None,
                 ):
        self.bitrix_address = bitrix_address
        self.refresh_token = refresh_token

    def request(self,
                param: SelectData,
                options: RequestOptions | None = None,
                ):
        if not options:
            options = self._set_default_options()
        return APIRequestor._global_instance().request(
            bitrix_address=self.bitrix_address,
            params=param,
            options=options,
        )

    async def request_async(self,
                            param: SelectData,
                            options: RequestOptions | None = None,
                            ):
        if not options:
            options = self._set_default_options()
        return await APIRequestor._global_instance().request_async(
            bitrix_address=self.bitrix_address,
            params=param,
            options=options,
        )

    def _set_default_options(self) -> RequestOptions:
        client_id = CLIENT_ID
        if not client_id or not self.refresh_token:
            raise CreateDefaultOptionsError(
                LogicErrors.CREATE_DEFAULT_OPTIONS_ERROR.value.format('CLIENT_ID'),
                )
        # OAuth request with refresh token
        oauth_token = None
        options = RequestOptions(
            oauth_token=oauth_token,
            client_id=client_id,
            high_level_domain='ru',
        )
        return options

    def refresh_tokens(self):
        """Refresh access tokens
        :return:
        """
        r = {}

        try:
            # Make call to oauth server
            r = post(
                self.oauth_url,
                params={'grant_type': 'refresh_token', 'client_id': self.client_id, 'client_secret': self.client_secret,
                        'refresh_token': self.refresh_token})
            result = loads(r.text)
            # Renew access tokens
            self.auth_token = result['access_token']
            self.refresh_token = result['refresh_token']
            info(['Tokens', self.auth_token, self.refresh_token])
            return True
        except (ValueError, KeyError):
            result = dict(error='Error on decode oauth response [' + r.text + ']')
            return result

    def get_tokens(self):
        """Get access tokens
        :return: dict
        """
        return {'auth_token': self.auth_token, 'refresh_token': self.refresh_token}
