from common import PRODUCT_FIELDS


class Product:
    """
    The Product class provides static methods for formatting Bitrix24 product field parameters.
    Each method corresponds to a field in the PRODUCT_FIELDS class and returns a string representation
    suitable for use in Bitrix24 API requests. This class helps to build query parameters in a consistent
    and type-safe way, reducing errors and improving code readability.
    """
    @staticmethod
    def ID(value: int) -> dict[str, str]:
        return {PRODUCT_FIELDS.ID: value}

    @staticmethod
    def TITLE(value: str) -> dict[str, str]:
        return {PRODUCT_FIELDS.TITLE: value}

    @staticmethod
    def TYPE_ID(value: str | list[str]) -> dict[str, str | list[str]]:
        return {PRODUCT_FIELDS.TYPE_ID: value}

    @staticmethod
    def CATEGORY_ID(value: int | list[int]) -> dict[str, str | list[int]]:
        return {PRODUCT_FIELDS.CATEGORY_ID: value}

    @staticmethod
    def STAGE_ID(value: str) -> dict[str, str]:
        return {PRODUCT_FIELDS.STAGE_ID: value}

    @staticmethod
    def OPPORTUNITY(value: float) -> dict[str, str]:
        return {PRODUCT_FIELDS.OPPORTUNITY: value}

    @staticmethod
    def IS_MANUAL_OPPORTUNITY(value: bool) -> dict[str, str]:
        return {PRODUCT_FIELDS.IS_MANUAL_OPPORTUNITY: 'Y' if value else 'N'}

    @staticmethod
    def ASSIGNED_BY_ID(value: int | list[int]) -> dict[str, list[int]]:
        return {PRODUCT_FIELDS.ASSIGNED_BY_ID: value}

    @staticmethod
    def DATE_CREATE(value: str) -> dict[str, str]:
        return {PRODUCT_FIELDS.DATE_CREATE: value}


class Select:
    """
    """
    def __init__(self, *fields: str):
        self._fields = fields

    @property
    def compare(self) -> list[str]:
        return list(self._fields)


class Filter[T: dict[str, str | list[str]]]:
    """
    """
    def __init__(self, *filters: T):
        self._filters = filters

    @property
    def compare(self) -> T:
        filters = dict()
        for _filter in self._filters:
            filters.update(_filter)
        return filters


class Fields[T: dict[str, str]]:
    """
    """
    def __init__(self, *fields: T):
        self._fields = fields

    @property
    def compare(self) -> T:
        fields = dict()
        for field in self._fields:
            fields.update(field)
        return fields
