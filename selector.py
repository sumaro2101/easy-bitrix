from typing import ClassVar


class BaseSelector:
    """
    Базовый селектор
    """
    root: ClassVar[str | None] = None

    @classmethod
    def get(cls, params) -> None:
        ...

    def list(cls, params) -> None:
        ...
