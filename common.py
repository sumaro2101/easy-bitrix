from enum import Enum


class ProductFields:

    @property
    def ID(self):
        return 'ID'

    @property
    def TITLE(self):
        return 'TITLE'

    @property
    def TYPE_ID(self):
        return 'TYPE_ID'

    @property
    def CATEGORY_ID(self):
        return 'CATEGORY_ID'

    @property
    def STAGE_ID(self):
        return 'STAGE_ID'

    @property
    def OPPORTUNITY(self):
        return 'OPPORTUNITY'

    @property
    def IS_MANUAL_OPPORTUNITY(self):
        return 'IS_MANUAL_OPPORTUNITY'

    @property
    def ASSIGNED_BY_ID(self):
        return 'ASSIGNED_BY_ID'

    @property
    def DATE_CREATE(self):
        return 'DATE_CREATE'


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


class LogicErrors(str, Enum):
    METHOD_EMPTY_ERROR = 'Method can`t be empty.'
    UNSUPPERTED_HIGH_LEVEL_DOMAIN = 'Unsupported high level domain.'
    FILTER_PARAMETER_ERROR = 'This parameter has wrong type.'


class NetworkErrors(str, Enum):
    TIMEOUT_ERROR = 'Timeout waiting expired [{} sec].'
    DECODE_ERROR = 'Error on decode api response [{}].'
    MAX_RETRIES_ERROR = 'Max retries exceeded [{}]'
    NOT_FOUND_ERROR = 'Page not found [{}]'


PRODUCT_FIELDS = ProductFields()
