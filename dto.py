from dataclasses import dataclass, Field


@dataclass
class SelectListData:
    method: str
    select: list[str] = Field(default=['*'])
    filter: dict[str, str | int | float | list[str | int | float]] = Field(default=dict())
    order: dict[str, str | int | float] = Field(default=dict())


@dataclass
class SelectGetData:
    method: str
    id: int


@dataclass
class GetFieldsData:
    method: str


@dataclass
class AddData:
    method: str
    fields: dict[str, str | int | float]
    params: dict[str, str] = Field(default=dict())


@dataclass
class UpdateData:
    method: str
    id: int
    fields: dict[str, str | int | float] = Field(default=dict())
    params: dict[str, str] = Field(default=dict())


@dataclass
class DeleteData(SelectGetData):
    ...
