from enum import Enum


class LogicErrors(str, Enum):
    METHOD_EMPTY_ERROR = 'Method can`t be empty.'
    UNSUPPERTED_HIGH_LEVEL_DOMAIN = 'Unsupported high level domain.'
    FILTER_PARAMETER_ERROR = 'This parameter has wrong type.'
    CREATE_DEFAULT_OPTIONS_ERROR = 'Default options can`t be created. You need env {} or not specified refresh token.'
    WRONG_TYPE_PARAMETER = 'Type of {} is wrong for this parameter.'


class NetworkErrors(str, Enum):
    TIMEOUT_ERROR = 'Timeout waiting expired [{} sec].'
    DECODE_ERROR = 'Error on decode api response [{}].'
    MAX_RETRIES_ERROR = 'Max retries exceeded [{}]'
    NOT_FOUND_ERROR = 'Page not found [{}]'
    AUTHENTICATION_MISS_ERROR = 'There must be at least one authentication method.'
    OAUTH_TOKEN_AUTHENTICATION_ERROR = 'Miss OAuth token authentication.'
    OAUTH_CLIEND_ID_AUTHENTICATION_ERROR = 'Miss Client id authentication.'
    WEBHOOK_USER_ID_AUTHENTICATION_ERROR = 'Miss User id in webhook request process.'
    WEBHOOK_URL_AUTHENTICATION_ERROR = 'Miss Webhook url in webhook request process.'


class BitrixResponseErrors(str, Enum):
    NO_AUTH_FOUND = 'NO_AUTH_FOUND'
    QUERY_LIMIT_EXCEEDED = 'QUERY_LIMIT_EXCEEDED'


class FilterTo(str, Enum):
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


class OrderTo(str, Enum):
    ASCENDING_ORDER = 'ASC'
    DESCENDING_ORDER = 'DESC'


class BitrixCRMTypes(str, Enum):
    LEAD = 'lead'
    DEAL = 'deal'
    CONTACT = 'contact'
    COMPANY = 'company'
    QUOTE = 'quote'
    ADDRESS = 'address'
    STATUS = 'status'
    CURRENCY = 'currency'
