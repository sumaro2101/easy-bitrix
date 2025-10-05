from typing import ClassVar
from parameters import Deal


class BaseSelector:
    """
    Базовый селектор
    """
    method: ClassVar[str | None] = None

    @classmethod
    def get(cls, id: int) -> None:
        ...

    def list(cls, select: list[str] | None, filter: dict[str, str] | None, order: dict[str, str] | None) -> None:
        ...


class DealSelector(BaseSelector):
    method = 'crm.deal.{}'

    @classmethod
    def get(cls, id: int) -> dict[str, str | dict[str, int]]:
        method = cls.method.format('get')
        fields = Deal.ID(id)
        return {'method': method, 'fields': fields}

    @classmethod
    def list(cls, select: list[str] | None, filter: dict[str, str] | None, order: dict[str, str] | None) -> None:
        method = cls.method.format('list')
