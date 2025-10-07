from typing import ClassVar

from http_client import HTTPClient
from options import RequestorOptions, GlobalRequestorOptions, RequestOptions


class APIRequestor:
    _instance: ClassVar['APIRequestor' | None] = None

    def __init__(self, options: RequestorOptions | None = None,
                 client: HTTPClient | None = None,
                 ):
        if options is None:
            options = RequestorOptions()
        self._options = options
        self._client = client

    @classmethod
    def _global_instance(cls):
        if cls._instance is None:
            cls._instance = cls(GlobalRequestorOptions())
        return cls._instance

    def _replace_options(self, options: RequestOptions | None) -> 'APIRequestor':
        options = options or {}
        new_options = self._options.to_dict()
        return APIRequestor(
            options=RequestorOptions(**new_options),
            client=self._client,
            )

    @staticmethod
    def _global_with_options(**param) -> 'APIRequestor':
        return APIRequestor._global_instance()._replace_options(param)

    async def request_async(self, method: str,
                            url: str, params=None,
                            options: RequestOptions | None = None,
                            ):
        requestor = self._replace_options(options)
        raw_body, raw_code = await requestor

    async def request_raw_async(self, method: str,
                                url: str, params=None,
                                options: RequestOptions | None = None,
                                ):
        ...