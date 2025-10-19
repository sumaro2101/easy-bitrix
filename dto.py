from dataclasses import dataclass, field
from typing import Literal


@dataclass
class SelectData:
    method: str


@dataclass
class IDAddition:
    id: int


@dataclass
class EntityTypeIdAddtion:
    entityTypeId: int


@dataclass
class SelectListData(SelectData):
    select: list[str] = field(default_factory=['*'])
    filter: dict[str, str | int | float | list[str | int | float]] = field(default_factory=dict())
    order: dict[str, str | int | float] = field(default_factory=dict())
    start: int = field(default=0)


@dataclass
class SelectGetData(IDAddition, SelectData):
    ...


@dataclass
class SelectGetItemData(IDAddition, SelectData):
    ...


@dataclass
class GetFieldsData(SelectData):
    ...


@dataclass
class GetFieldsItemData(EntityTypeIdAddtion, SelectData):
    ...


@dataclass
class AddData(SelectData):
    fields: dict[str, str | int | float]
    params: dict[str, str] = field(default_factory=dict())


@dataclass
class UpdateData(IDAddition, SelectData):
    fields: dict[str, str | int | float] = field(default_factory=dict())
    params: dict[str, str] = field(default_factory=dict())


@dataclass
class DeleteData(IDAddition, SelectData):
    ...


@dataclass
class DeleteItemData(EntityTypeIdAddtion, SelectData):
    ...


@dataclass
class OAuthData:
    grant_type: Literal['authorization_code', 'refresh_token']
    client_id: str
    client_secret: str


@dataclass
class RequestOAuthAssessToken(OAuthData):
    code: str


@dataclass
class RequestOAuthRefreshToken(OAuthData):
    refresh_token: str
