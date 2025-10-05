from typing import ClassVar

from parameters import Deal
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

    def list(self, select: list[str] | None, filter: dict[str, str] | None, order: dict[str, str] | None) -> SelectListData:
        method = self.root.format(self._crm_type, 'list')
