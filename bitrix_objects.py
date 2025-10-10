from typing import ClassVar

from datetime import datetime

from .fields import DEAL_FIELD
from .common import LogicErrors
from .dto import SelectGetData, SelectListData
from .parameters import Select, Filter, Order


class BaseBitrixObject:
    """
    """
    root: ClassVar[str]

    @classmethod
    def get(cls, id: int) -> SelectGetData:
        method = cls.root.format('get')
        _id = {'ID': id}
        return SelectGetData(method=method, id=_id)

    @classmethod
    def list(cls, select: list[str] | None = None,
             filter: list[dict[str, str | list[str, int, float]]] | None = None,
             order: list[dict[str, str]] | None = None,
             start: int = 0,
             ) -> SelectListData:
        method = cls.root.format('list')
        select = Select(*list(select)).compare if select else ['*']
        filter_ = Filter(*list(filter)).compare if filter else dict()
        order = Order(*list(order)).compare if order else dict()
        return SelectListData(
            method=method,
            select=select,
            filter=filter_,
            order=order,
            start=start,
        )


class Deal[T](BaseBitrixObject):
    """
    The Deal class provides static methods for formatting Bitrix24 product field parameters.
    Each method corresponds to a field in the PRODUCT_FIELD class and returns a string representation
    suitable for use in Bitrix24 API requests. This class helps to build query parameters in a consistent
    and type-safe way, reducing errors and improving code readability.
    """
    root = 'crm.deal.{}'
    ID = DEAL_FIELD.ID
    TITLE = DEAL_FIELD.TITLE
    TYPE_ID = DEAL_FIELD.TYPE_ID
    CATEGORY_ID = DEAL_FIELD.CATEGORY_ID
    STAGE_ID = DEAL_FIELD.STAGE_ID
    OPPORTUNITY = DEAL_FIELD.OPPORTUNITY
    IS_MANUAL_OPPORTUNITY = DEAL_FIELD.IS_MANUAL_OPPORTUNITY
    ASSIGNED_BY_ID = DEAL_FIELD.ASSIGNED_BY_ID
    DATE_CREATE = DEAL_FIELD.DATE_CREATE

    @staticmethod
    def SET_ID(value: T) -> dict[str, T]:
        return {DEAL_FIELD.ID: value}

    @staticmethod
    def SET_TITLE(value: T) -> dict[str, T]:
        return {DEAL_FIELD.TITLE: value}

    @staticmethod
    def SET_TYPE_ID(value: T | list[T]) -> dict[str, T | list[T]]:
        return {DEAL_FIELD.TYPE_ID: value}

    @staticmethod
    def SET_CATEGORY_ID(value: T | list[T]) -> dict[str, T | list[T]]:
        return {DEAL_FIELD.CATEGORY_ID: value}

    @staticmethod
    def SET_STAGE_ID(value: T) -> dict[str, T]:
        return {DEAL_FIELD.STAGE_ID: value}

    @staticmethod
    def SET_OPPORTUNITY(value: T) -> dict[str, T]:
        return {DEAL_FIELD.OPPORTUNITY: value}

    @staticmethod
    def SET_IS_MANUAL_OPPORTUNITY(value: bool) -> dict[str, str]:
        return {DEAL_FIELD.IS_MANUAL_OPPORTUNITY: 'Y' if value else 'N'}

    @staticmethod
    def SET_ASSIGNED_BY_ID(value: T | list[T]) -> dict[str, T, list[T]]:
        return {DEAL_FIELD.ASSIGNED_BY_ID: value}

    @staticmethod
    def SET_DATE_CREATE(value: datetime | str) -> dict[str, str]:
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(LogicErrors.WRONG_TYPE_PARAMETER.format(value.__class__.__name__))
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {DEAL_FIELD.DATE_CREATE: value.isoformat()}
