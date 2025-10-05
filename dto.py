from dataclasses import dataclass, field


@dataclass
class SelectListData:
    method: str
    select: list[str] = field(default_factory=['*'])
    filter: dict[str, str | int | float | list[str | int | float]] = field(default_factory=dict())
    order: dict[str, str | int | float] = field(default_factory=dict())


@dataclass
class SelectGetData:
    method: str
    id: dict[str, int]


@dataclass
class GetFieldsData:
    method: str


@dataclass
class AddData:
    method: str
    fields: dict[str, str | int | float]
    params: dict[str, str] = field(default_factory=dict())


@dataclass
class UpdateData:
    method: str
    id: dict[str, int]
    fields: dict[str, str | int | float] = field(default_factory=dict())
    params: dict[str, str] = field(default_factory=dict())


@dataclass
class DeleteData(SelectGetData):
    ...
