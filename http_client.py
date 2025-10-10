import time
import textwrap
import random
import anyio
from httpx import AsyncClient, Client

from typing import ClassVar, NoReturn

from .error import APIConnectionError
from .logger import log_info
from .common import LogicErrors


class HTTPClient:
    MAX_DELAY: ClassVar[int] = 5
    INITIAL_DELAY: ClassVar[float] = 0.5
    MAX_RETRY_AFTER: ClassVar[int] = 60

    def __init__(self, timeout: int | None = 60,
                 async_requests: bool = True, **kwargs,
                 ):
        self._httpx = None
        self._client = None
        self._async_client = None
        if not async_requests:
            self._client = Client(**kwargs)
        else:
            self._async_client = AsyncClient(**kwargs)
        self._timeout = timeout

    def request_retries(self,
                        method: str,
                        url: str,
                        headers: dict[str, str],
                        params,
                        max_retries: int | None = None,
                        ):
        return self._request_retries(
            method=method,
            url=url,
            headers=headers,
            params=params,
            max_retries=max_retries,
        )

    async def request_async_retries(self, method: str,
                                    url: str, headers: dict[str, str],
                                    params, max_retries: int | None = None,
                                    ):
        return await self._request_async_retries(
            method=method,
            url=url,
            headers=headers,
            params=params,
            max_retries=max_retries,
        )

    def _request_retries(self,
                         method: str,
                         url: str,
                         headers: dict[str, str],
                         params,
                         max_retries: int | None,
                         ):
        num_retries = 0

        while True:
            try:
                response = self.request(method, url, headers, params)
                connection_error = None
                log_info('Request is sussess', code=response[-1])
            except APIConnectionError as e:
                connection_error = e
                log_info('Requests has exception', except_=e.message)
                response = None
            if self._should_retry(response, connection_error, num_retries, max_retries):
                num_retries += 1
                sleep_time = self._sleep_time_seconds(num_retries)
                log_info('Retrie request after seconds', seconds=sleep_time)
                time.sleep(sleep_time)
            else:
                if response is not None:
                    return response
                raise connection_error

    async def _request_async_retries(self,
                                     method: str,
                                     url: str,
                                     headers: dict[str, str],
                                     params,
                                     max_retries: int | None,
                                     ):
        num_retries = 0

        while True:
            try:
                response = await self.request_async(method, url, headers, params)
                connection_error = None
                log_info('Request is sussess', code=response[-1])
            except APIConnectionError as e:
                connection_error = e
                log_info('Requests has exception', except_=e.message)
                response = None
            if self._should_retry(response, connection_error, num_retries, max_retries):
                num_retries += 1
                sleep_time = self._sleep_time_seconds(num_retries)
                log_info('Retrie request after seconds', seconds=sleep_time)
                await anyio.sleep(sleep_time)
            else:
                if response is not None:
                    return response
                raise connection_error

    def _sleep_time_seconds(self, num_retries: int) -> float:
        sleep_seconds = min(self.INITIAL_DELAY * (2 ** (num_retries - 1)), self.MAX_DELAY)
        jitter_sleep_seconds = self._add_jitter_time(sleep_seconds)
        max_sleep_time = max(self.INITIAL_DELAY, jitter_sleep_seconds)
        return max_sleep_time

    def _add_jitter_time(self, sleep_seconds: float) -> float:
        sleep_seconds *= 0.5 * (1 + random.uniform(0, 1))
        return sleep_seconds

    def _should_retry(self, response: tuple[bytes, int] | None,
                      api_connection_error: APIConnectionError | None,
                      num_retries: int,
                      max_network_retries: int | None,
                      ):
        max_network_retries = (
            max_network_retries if max_network_retries is not None else 0
        )
        if num_retries >= max_network_retries:
            return False
        if response is None:
            return api_connection_error.should_retry
        _, status_code = response
        if status_code == 409 or status_code >= 500:
            return True
        return False

    def _get_request_args_kwargs(self, method: str, url: str, headers: dict[str, str], params):
        kwargs = dict()

        if self._timeout:
            kwargs['timeout'] = self._timeout
        return [(method, url), {'json': params or {}, 'headers': headers, **kwargs}]

    def _handle_request_error(self, e: Exception) -> NoReturn:
        msg = (
            'Unexpected error communication with Bitrix24.'
        )
        err = f'A {type(e).__name__} was raised'
        should_retry = type(e) not in [AttributeError, TypeError, ValueError, LookupError, OSError, SyntaxError]
        msg = textwrap.fill(msg) + f'\n\n(Network error: {err})'
        raise APIConnectionError(msg, should_retry=should_retry) from e

    def request(self,
                method: str,
                url: str,
                headers: dict[str, str],
                params,
                ) -> tuple[bytes, int]:
        if not self._client:
            raise RuntimeError(
                LogicErrors.ASYNC_IS_FLAG_TRUE.value,
            )
        args, kwargs = self._get_request_args_kwargs(
            method=method,
            url=url,
            headers=headers,
            params=params,
        )
        try:
            response = self._client.request(*args, **kwargs)
            result = response.content
            status_code = response.status_code
        except Exception as e:
            self._handle_request_error(e)
        return result, status_code

    async def request_async(self,
                            method: str,
                            url: str,
                            headers: dict[str, str],
                            params,
                            ) -> tuple[bytes, int]:
        args, kwargs = self._get_request_args_kwargs(
            method=method,
            url=url,
            headers=headers,
            params=params,
        )
        try:
            response = await self._async_client.request(*args, **kwargs)
            result = response.content
            status_code = response.status_code
        except Exception as e:
            self._handle_request_error(e)
        return result, status_code

    def close(self):
        if self._client is not None:
            self._client.close()

    async def close_async(self):
        await self._async_client.aclose()
