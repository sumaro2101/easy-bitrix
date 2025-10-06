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


class BitrixResponseErrors(str, Enum):
    NO_AUTH_FOUND = 'NO_AUTH_FOUND'
    QUERY_LIMIT_EXCEEDED = 'QUERY_LIMIT_EXCEEDED'


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


class BitrixCRMTypes(str, Enum):
    LEAD = 'lead'
    DEAL = 'deal'
    CONTACT = 'contact'
    COMPANY = 'company'
    QUOTE = 'quote'
    ADDRESS = 'address'
    STATUS = 'status'
    CURRENCY = 'currency'
