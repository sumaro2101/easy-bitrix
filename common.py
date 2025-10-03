from enum import Enum


class ProductFields(str, Enum):
    ID = 'ID'
    TITLE = 'TITLE'
    TYPE_ID = 'TYPE_ID'
    CATEGORY_ID = 'CATEGORY_ID'
    STAGE_ID = 'STAGE_ID'
    OPPORTUNITY = 'OPPORTUNITY'
    IS_MANUAL_OPPORTUNITY = 'IS_MANUAL_OPPORTUNITY'
    ASSIGNED_BY_ID = 'ASSIGNED_BY_ID'
    DATE_CREATE = 'DATE_CREATE'


class FilterOperations(str, Enum):
    EQ = '=%s'
    NEQ = '!=%s'
    GT = '>%s'
    GTE = '>=%s'
    LT = '<%s'
    LTE = '<=%s'
    START_LIKE = '%s%'
    END_LIST = ('%' + '%s')
    LIKE = ('%' + '%s' + '%')
    IN = '@%s'
    NOT_IN = '!@%s'


class LogicErrors(str, Enum):
    METHOD_EMPTY_ERROR = 'Method can`t be empty.'
    UNSUPPERTED_HIGH_LEVEL_DOMAIN = 'Unsupported high level domain.'


class NetworkErrors(str, Enum):
    TIMEOUT_ERROR = 'Timeout waiting expired [%s sec].'
    DECODE_ERROR = 'Error on decode api response [%s].'
    MAX_RETRIES_ERROR = 'Max retries exceeded [%s]'
    NOT_FOUND_ERROR = 'Page not found [%s]'
