from enum import Enum


class LogicErrors(str, Enum):
    METHOD_EMPTY_ERROR = 'Method can`t be empty.'
    UNSUPPERTED_HIGH_LEVEL_DOMAIN = 'Unsupported high level domain.'
    FILTER_PARAMETER_ERROR = 'This parameter has wrong type.'


class NetworkErrors(str, Enum):
    TIMEOUT_ERROR = 'Timeout waiting expired [{} sec].'
    DECODE_ERROR = 'Error on decode api response [{}].'
    MAX_RETRIES_ERROR = 'Max retries exceeded [{}]'
    NOT_FOUND_ERROR = 'Page not found [{}]'


class FilterOperations(str, Enum):
    EQ = '={}'
    NEQ = '!={}'
    GT = '>{}'
    GTE = '>={}'
    LT = '<{}'
    LTE = '<={}'
    START_LIKE = '{}%'
    END_LIKE = '%{}'
    LIKE = '%{}%'
    IN = '@{}'
    NOT_IN = '!@{}'
    LIKE_OP = '%={}'
