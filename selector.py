from typing import ClassVar


class BaseSelector:
    """
    Базовый селектор
    """
    root: ClassVar[str | None] = None

    @classmethod
    def get(cls, id: str) -> None:
        ...

    def list(cls, select: list[str], filter: dict[str, str]) -> None:
        ...
