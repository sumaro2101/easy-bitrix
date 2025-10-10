from typing import Any, ClassVar

from datetime import datetime

from .fields import DEAL_FIELD
from .common import LogicErrors, BitrixMethods, BitrixParams
from .dto import SelectGetData, SelectListData, GetFieldsData, DeleteData, AddData, UpdateData
from .parameters import Select, Filter, Order, Fields


class BaseBitrixObject:
    """
    """
    root: ClassVar[str]
    REGISTER_SONET_EVENT_OPTION: ClassVar[bool]
    IMPORT_OPTION: ClassVar[bool]

    @classmethod
    def get(cls, id: int) -> SelectGetData:
        method = cls.root.format(BitrixMethods.GET.value)
        return SelectGetData(method=method, id=id)

    @classmethod
    def get_list(cls, select: list[str] | None = None,
                 filter: list[dict[str, str | list[str, int, float]]] | None = None,
                 order: list[dict[str, str]] | None = None,
                 start: int = 0,
                 ) -> SelectListData:
        method = cls.root.format(BitrixMethods.FIELDS.value)
        select = Select(*list(select)).compare if select else ['*', 'UF_*']
        filter_ = Filter(*list(filter)).compare if filter else dict()
        order = Order(*list(order)).compare if order else dict()
        return SelectListData(
            method=method,
            select=select,
            filter=filter_,
            order=order,
            start=start,
        )

    @classmethod
    def fields(cls) -> GetFieldsData:
        method = cls.root.format(BitrixMethods.FIELDS.value)
        return GetFieldsData(method=method)

    @classmethod
    def create(cls, fields: list[dict[str, str]], reg_sonet: bool = True, import_: bool = False) -> AddData:
        kwargs = dict()
        method = cls.root.format(BitrixMethods.ADD.value)
        fields = Fields(*list(fields)).compare
        kwargs.update(method=method, fields=fields)
        if cls.REGISTER_SONET_EVENT_OPTION:
            value = 'Y' if reg_sonet else 'N'
            kwargs.update(params={BitrixParams.REGISTER_SONET_EVENT.value: value})
        if cls.IMPORT_OPTION:
            value = 'Y' if import_ else ''
            kwargs.update(params={BitrixParams.IMPORT.value: value})
        return AddData(**kwargs)

    @classmethod
    def update(cls, fields: list[dict[str, str]], reg_sonet: bool = True, import_: bool = False) -> UpdateData:
        kwargs = dict()
        method = cls.root.format(BitrixMethods.UPDATE.value)
        fields = Fields(*list(fields)).compare
        kwargs.update(method=method, fields=fields)
        if cls.REGISTER_SONET_EVENT_OPTION:
            kwargs.update(params='Y' if reg_sonet else 'N')
        if cls.IMPORT_OPTION:
            kwargs.update(params='Y' if import_ else '')
        return UpdateData(**kwargs)

    @classmethod
    def delete(cls, id: int) -> DeleteData:
        method = cls.root.format(BitrixMethods.DELETE.value)
        return DeleteData(method=method, id=id)

    @staticmethod
    def SET_ID(value: int) -> dict[str, int]:
        return {DEAL_FIELD.ID: value}

    @staticmethod
    def SET_UF(key: str, value: Any) -> dict[str, Any]:
        return {f'UF_{key}': value}


class Deal[T](BaseBitrixObject):
    """
    The Deal class provides static methods for formatting Bitrix24 product field parameters.
    Each method corresponds to a field in the PRODUCT_FIELD class and returns a string representation
    suitable for use in Bitrix24 API requests. This class helps to build query parameters in a consistent
    and type-safe way, reducing errors and improving code readability.
    """
    root = 'crm.deal.{}'

    REGISTER_SONET_EVENT_OPTION = True
    IMPORT_OPTION = False

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
