from enum import Enum


class LogicErrors(str, Enum):
    METHOD_EMPTY_ERROR = 'Method can`t be empty.'
    UNSUPPERTED_HIGH_LEVEL_DOMAIN = 'Unsupported high level domain.'
    FILTER_PARAMETER_ERROR = 'This parameter has wrong type.'
    CREATE_DEFAULT_OPTIONS_ERROR = 'Default options can`t be created. You need env {} or not specified refresh token.'
    WRONG_TYPE_PARAMETER = 'Type of {} is wrong for this parameter.'
    ASYNC_IS_FLAG_TRUE = 'Used Sync client with flag "async_requests", switch to "False" before use.'


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
    INVALID_RESPONSE_BODY = 'Invalid response body from API: {} (HTTP response code was {})'


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
    ITEM = 'item'
    LEAD = 'lead'
    DEAL = 'deal'
    CONTACT = 'contact'
    COMPANY = 'company'
    REQUISITE = 'requisite'
    ACTIVITY = 'activity'
    QUOTE = 'quote'
    ADDRESS = 'address'
    STATUS = 'status'
    CURRENCY = 'currency'


class BitrixParams(str, Enum):
    REGISTER_SONET_EVENT = 'REGISTER_SONET_EVENT'
    IMPORT = 'IMPORT'


class BitrixMethods(str, Enum):
    GET = 'get'
    LIST = 'list'
    FIELDS = 'fields'
    ADD = 'add'
    UPDATE = 'update'
    DELETE = 'delete'


class BitrixStages:
    NEW = 'NEW'
    PREPARATION = 'PREPARATION'
    PREPAYMENT_INVOICE = 'PREPAYMENT_INVOICE'
    EXECUTING = 'EXECUTING'
    FINAL_INVOICE = 'FINAL_INVOICE'
    WON = 'WON'
    LOSE = '>LOSE'
    APOLOGY = 'APOLOGY'
