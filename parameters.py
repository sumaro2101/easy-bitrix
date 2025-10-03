from common import ProductFields


class Parameter:
    """
    The Parameter class provides static methods for formatting Bitrix24 product field parameters.
    Each method corresponds to a field in the ProductFields enum and returns a string representation
    suitable for use in Bitrix24 API requests. This class helps to build query parameters in a consistent
    and type-safe way, reducing errors and improving code readability.
    """
    @staticmethod
    def ID(value: int) -> dict[str, str]:
        return {ProductFields.ID.value: value}

    @staticmethod
    def TITLE(value: str) -> dict[str, str]:
        return {ProductFields.TITLE.value: value}

    @staticmethod
    def TYPE_ID(value: int) -> dict[str, str]:
        return {ProductFields.TYPE_ID.value: value}

    @staticmethod
    def CATEGORY_ID(value: int) -> dict[str, str]:
        return {ProductFields.CATEGORY_ID.value: value}

    @staticmethod
    def STAGE_ID(value: str) -> dict[str, str]:
        return {ProductFields.STAGE_ID.value: value}

    @staticmethod
    def OPPORTUNITY(value: float) -> dict[str, str]:
        return {ProductFields.OPPORTUNITY.value: value}

    @staticmethod
    def IS_MANUAL_OPPORTUNITY(value: bool) -> dict[str, str]:
        return {ProductFields.IS_MANUAL_OPPORTUNITY.value: 'Y' if value else 'N'}

    @staticmethod
    def ASSIGNED_BY_ID(value: int) -> dict[str, str]:
        return {ProductFields.ASSIGNED_BY_ID.value: value}

    @staticmethod
    def DATE_CREATE(value: str) -> dict[str, str]:
        return {ProductFields.DATE_CREATE.value: value}


class Select:
    """
    """
    def __init__(self, *fields: str):
        self._fields = fields

    @property
    def compare(self) -> list[str]:
        return self._fields


class Filter:
    """
    """


class Fields:
    """
    """
    def __init__(self, *fields: dict[str, str]):
        self._fields = fields

    @property
    def compare(self) -> dict[str, str]:
        fields = dict()
        for field in self._fields:
            fields.update(field)
        return fields
