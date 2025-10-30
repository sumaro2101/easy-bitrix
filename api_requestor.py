import time
from typing import Any, ClassVar

from .http_client import HTTPClient
from .options import RequestorOptions, GlobalRequestorOptions, RequestOptions, merge_options
from .error import AuthenticationError, UnsupportedDomain, EmptyMethodError, APIError
from .common import NetworkErrors, LogicErrors
from .logger import log_debug, log_info
from .response_object import BitrixResponse


class APIRequestor:
    _instance: ClassVar['APIRequestor|None'] = None
    RPS = 1 / 5

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

    def request(self,
                bitrix_address: str | None, params=None,
                options: RequestOptions | None = None,
                ) -> BitrixResponse:
        method = params.method
        requestor = self._replace_options(options)
        start_time = time.perf_counter()
        raw_body, raw_code = requestor.request_raw(
            bitrix_address=bitrix_address,
            params=params,
            options=options,
        )
        end_time = time.perf_counter()
        count_time = end_time - start_time
        log_info('Count time request', time=count_time)
        response = self._switch_to_object(raw_body, raw_code)
        if response.next is not None:
            params.start = response.next
            params.method = method
            if count_time < self.RPS:
                delay_time = self.RPS - count_time
                log_debug('Have time delay', delay=delay_time)
                time.sleep(delay_time)
            next_response = self.request(bitrix_address, params, options)
            response.add_data(next_response.raw_data)
        return response

    async def request_async(self,
                            bitrix_address: str, params=None,
                            options: RequestOptions | None = None,
                            ) -> BitrixResponse:
        requestor = self._replace_options(options)
        raw_body, raw_code = await requestor.request_raw_async(
            bitrix_address=bitrix_address,
            params=params,
            options=options,
        )
        response = self._switch_to_object(raw_body, raw_code)
        return response

    def request_raw(self,
                    bitrix_address: str | None, params=None,
                    options: RequestOptions | None = None,
                    ) -> tuple[bytes, int]:
        abs_url, headers, params, max_network_retries = self._args_for_request(
            bitrix_address=bitrix_address,
            params=params,
            options=options,
        )
        log_info('Request to bitrix', url=abs_url)
        log_debug('Request details', params=params)
        raw_content, raw_code = HTTPClient(async_requests=False).request_retries(
            method='post',
            url=abs_url,
            headers=headers,
            params=params,
            max_retries=max_network_retries,
        )
        return raw_content, raw_code

    async def request_raw_async(self,
                                bitrix_address: str, params=None,
                                options: RequestOptions | None = None,
                                ) -> tuple[bytes, int]:
        abs_url, headers, params, max_network_retries = self._args_for_request(
            bitrix_address=bitrix_address,
            params=params,
            options=options,
        )
        log_info('Request to bitrix', url=abs_url)
        log_debug('Request details', params=params)
        raw_content, raw_code = await HTTPClient().request_async_retries(
            method='post',
            url=abs_url,
            headers=headers,
            params=params,
            max_retries=max_network_retries,
        )
        return raw_content, raw_code

    def _args_for_request(self,
                          bitrix_address: str | None, params=None,
                          options: RequestOptions | None = None,
                          ) -> tuple[str, dict[str, str], dict[str, Any], int]:
        request_options = merge_options(self._options, options)
        log_debug('New_options', options=request_options)
        client_id = request_options.get('client_id')
        params = params.__dict__
        if not request_options.get('oauth_authorization'):
            oauth_token = request_options.get('oauth_token')
            webhook = request_options.get('webhook_url')
            user_id = request_options.get('user_id')
            method = params.pop('method')
            match (bool(client_id), bool(oauth_token), bool(webhook), bool(user_id)):
                case True, False, _, _:
                    raise AuthenticationError(NetworkErrors.OAUTH_TOKEN_AUTHENTICATION_ERROR.value)
                case False, True, _, _:
                    raise AuthenticationError(NetworkErrors.OAUTH_CLIEND_ID_AUTHENTICATION_ERROR.value)
                case _, _, True, False:
                    raise AuthenticationError(NetworkErrors.WEBHOOK_USER_ID_AUTHENTICATION_ERROR.value)
                case _, _, False, True:
                    raise AuthenticationError(NetworkErrors.WEBHOOK_URL_AUTHENTICATION_ERROR.value)
                case False, False, False, False:
                    raise AuthenticationError(NetworkErrors.AUTHENTICATION_MISS_ERROR.value)
            domain = request_options.get('high_level_domain')
            if not domain:
                raise EmptyMethodError(LogicErrors.METHOD_EMPTY_ERROR.value)
            if domain not in ['ru', 'com', 'de']:
                raise UnsupportedDomain(LogicErrors.UNSUPPERTED_HIGH_LEVEL_DOMAIN.value)
            abs_url = self._options.api_addresses['api']
            if webhook:
                webhook_params_with_method = f'{user_id}/{webhook}/{method}'
                abs_url = abs_url.format(bitrix_address, domain, webhook_params_with_method)
            else:
                abs_url = abs_url.format(bitrix_address, domain, method)
        else:
            abs_url = self._options.api_addresses['oauth']
        max_network_retries = request_options.get('max_network_retries')
        headers = {'Content-Type': 'application/json'}
        return abs_url, headers, params, max_network_retries

    def _switch_to_object(self, body: str | bytes, code: str) -> BitrixResponse:
        try:
            if hasattr(body, 'decode'):
                body = body.decode('utf-8')
            response = BitrixResponse(
                code=code,
                raw_data=body,
            )
        except Exception:
            raise APIError(
                NetworkErrors.INVALID_RESPONSE_BODY.format(body, code),
                http_status=code,
                json_body=body,
                )
        return response
