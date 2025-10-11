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
