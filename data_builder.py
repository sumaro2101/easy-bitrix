from typing import ClassVar

from parameters import Deal, Select, Filter
from dto import SelectGetData, SelectListData


class CRMDataExecutor:
    """
    Базовый селектор
    """

    root: ClassVar[str] = 'crm.{}.{}'

    def __init__(self, bitrix_crm_type: str):
        self._crm_type = str(bitrix_crm_type)

    def get(self, id: int) -> SelectGetData:
        method = self.root.format(self._crm_type, 'get')
        _id = Deal.ID(id)
        return SelectGetData(method=method, id=_id)

    def list(self, select: Select[str] | None = None,
             filter: Filter[dict[str, str | list[str, int, float]]] | None = None,
             order: dict[str, str] | None = None) -> SelectListData:
        method = self.root.format(self._crm_type, 'list')
        return SelectListData(
            method=method,
            select=select.compare if select else ['*'],
            filter=filter.compare if filter else dict(),
            order=order if order else dict(),
        )
