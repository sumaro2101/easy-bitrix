from typing import Generic, TypeVar


T = TypeVar('T')


class Select(Generic[T]):
    """
    """
    def __init__(self, *fields: T):
        self._fields = fields

    @property
    def compare(self) -> list[T]:
        return list(self._fields)


class Filter(Generic[T]):
    """
    """
    def __init__(self, *filters: T):
        self._filters = filters

    @property
    def compare(self) -> T:
        return _compare_params(self._filters)


class Order:
    """
    """
    def __init__(self, *orders):
        self._orders = orders

    @property
    def compare(self) -> dict[str, str]:
        return _compare_params(self._orders)


class Fields(Generic[T]):
    """
    """
    def __init__(self, *fields: T):
        self._fields = fields

    @property
    def compare(self) -> T:
        return _compare_params(self._fields)


def _compare_params[_TP: dict[str, str]](params: tuple[_TP]) -> _TP:
    compare_params = dict()
    for param in params:
        compare_params.update(param)
    return compare_params
