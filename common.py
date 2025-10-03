from enum import Enum


class LogicErrors(str, Enum):
    METHOD_EMPTY_ERROR = 'Method can`t be empty.'


class NetworkErrors(str, Enum):
    TIMEOUT_ERROR = 'Timeout waiting expired [%s sec].'
    DECODE_ERROR = 'Error on decode api response [%s].'
    MAX_RETRIES_ERROR = 'Max retries exceeded [%s]'
    NOT_FOUND_ERROR = 'Page not found [%s]'
