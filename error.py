from typing import ClassVar, Any


class APIError(Exception):
    _message: ClassVar[str | None]
    http_status: ClassVar[int]
    json_body: ClassVar[dict[str, Any]]
    code: ClassVar[str]

    def __init__(self, message: str,
                 http_status: int | None = None,
                 json_body: bytes | None = None,
                 code: str | None = None,
                 ):
        self._message = message
        self.http_status = http_status
        self.json_body = json_body
        self.code = code

    @property
    def message(self):
        return self._message


class APIConnectionError(APIError):
    should_retry: ClassVar[bool]

    def __init__(self, message: str,
                 http_status: int | None = None,
                 json_body: bytes | None = None,
                 code: str | None = None,
                 should_retry: bool = False,
                 ):
        super().__init__(
            message,
            http_status,
            json_body,
            code,
        )
        self.should_retry = should_retry


class AuthenticationError(APIError):
    pass


class EmptyMethodError(APIError):
    ...


class FilterParameterError(APIError):
    ...


class UnsupportedDomain(APIError):
    ...
