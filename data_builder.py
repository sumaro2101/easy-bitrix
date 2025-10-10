from abc import ABC, abstractmethod
from typing import ClassVar

from .parameters import Select, Filter, Order
from .dto import SelectGetData, SelectListData, SelectData


class DataExecutor(ABC):
    root: ClassVar[str]

    @abstractmethod
    def get(self, id: int) -> SelectData: ...

    @abstractmethod
    def list(self, select: ..., filter: ..., order: ...) -> SelectData: ...


class CRMDataExecutor(DataExecutor):
    """
    """

    root: ClassVar[str] = 'crm.{}.{}'

    def __init__(self, bitrix_crm_type: str):
        self._crm_type = str(bitrix_crm_type)

    def get(self, id: int) -> SelectGetData:
        method = self.root.format(self._crm_type, 'get')
        _id = {'ID': id}
        return SelectGetData(method=method, id=_id)

    def list(self, select: Select[str] | None = None,
             filter: Filter[dict[str, str | list[str, int, float]]] | None = None,
             order: Order | None = None) -> SelectListData:
        method = self.root.format(self._crm_type, 'list')
        return SelectListData(
            method=method,
            select=select.compare if select else ['*'],
            filter=filter.compare if filter else dict(),
            order=order.compare if order else dict(),
        )
