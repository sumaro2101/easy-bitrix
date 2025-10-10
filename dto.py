from dataclasses import dataclass, field


@dataclass
class SelectData:
    method: str


@dataclass
class SelectListData(SelectData):
    select: list[str] = field(default_factory=['*'])
    filter: dict[str, str | int | float | list[str | int | float]] = field(default_factory=dict())
    order: dict[str, str | int | float] = field(default_factory=dict())
    start: int = field(default=0)


@dataclass
class SelectGetData(SelectData):
    id: dict[str, int]


@dataclass
class GetFieldsData(SelectData):
    ...


@dataclass
class AddData(SelectData):
    fields: dict[str, str | int | float]
    params: dict[str, str] = field(default_factory=dict())


@dataclass
class UpdateData(SelectData):
    id: dict[str, int]
    fields: dict[str, str | int | float] = field(default_factory=dict())
    params: dict[str, str] = field(default_factory=dict())


@dataclass
class DeleteData(SelectData):
    id: dict[str, int]
