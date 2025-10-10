from datetime import datetime

from .fields import DEAL_FIELD
from .common import LogicErrors


class Deal[T]:
    """
    The Deal class provides static methods for formatting Bitrix24 product field parameters.
    Each method corresponds to a field in the PRODUCT_FIELD class and returns a string representation
    suitable for use in Bitrix24 API requests. This class helps to build query parameters in a consistent
    and type-safe way, reducing errors and improving code readability.
    """

    @staticmethod
    def ID(value: T) -> dict[str, T]:
        return {DEAL_FIELD.ID: value}

    @staticmethod
    def TITLE(value: T) -> dict[str, T]:
        return {DEAL_FIELD.TITLE: value}

    @staticmethod
    def TYPE_ID(value: T | list[T]) -> dict[str, T | list[T]]:
        return {DEAL_FIELD.TYPE_ID: value}

    @staticmethod
    def CATEGORY_ID(value: T | list[T]) -> dict[str, T | list[T]]:
        return {DEAL_FIELD.CATEGORY_ID: value}

    @staticmethod
    def STAGE_ID(value: T) -> dict[str, T]:
        return {DEAL_FIELD.STAGE_ID: value}

    @staticmethod
    def OPPORTUNITY(value: T) -> dict[str, T]:
        return {DEAL_FIELD.OPPORTUNITY: value}

    @staticmethod
    def IS_MANUAL_OPPORTUNITY(value: bool) -> dict[str, str]:
        return {DEAL_FIELD.IS_MANUAL_OPPORTUNITY: 'Y' if value else 'N'}

    @staticmethod
    def ASSIGNED_BY_ID(value: T | list[T]) -> dict[str, T, list[T]]:
        return {DEAL_FIELD.ASSIGNED_BY_ID: value}

    @staticmethod
    def DATE_CREATE(value: datetime | str) -> dict[str, str]:
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(LogicErrors.WRONG_TYPE_PARAMETER.format(value.__class__.__name__))
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {DEAL_FIELD.DATE_CREATE: value.isoformat()}
