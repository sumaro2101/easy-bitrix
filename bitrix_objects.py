from typing import Any, ClassVar, Literal

from datetime import datetime

from .fields import DEAL_FIELD, CONTACT_FIELD
from .common import LogicErrors, BitrixMethods, BitrixParams, BitrixCRMTypes
from .dto import SelectGetData, SelectListData, GetFieldsData, DeleteData, AddData, UpdateData
from .parameters import Select, Filter, Order, Fields


class BaseBitrixObject:
    """
    """
    NAME_OBJECT_ACTION: ClassVar[str]
    REGISTER_SONET_EVENT_OPTION: ClassVar[bool]
    IMPORT_OPTION: ClassVar[bool]

    root: ClassVar[str]

    @classmethod
    def get(cls, id: int) -> SelectGetData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION, BitrixMethods.GET.value)
        return SelectGetData(method=method, id=id)

    @classmethod
    def get_list(cls, select: list[str] | None = None,
                 filter: list[dict[str, str | list[str, int, float]]] | None = None,
                 order: list[dict[str, str]] | None = None,
                 start: int = 0,
                 ) -> SelectListData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION, BitrixMethods.LIST.value)
        select = Select(*list(select)).compare if select else ['*', 'UF_*']
        filter_ = Filter(*list(filter)).compare if filter else dict()
        order = Order(*list(order)).compare if order else dict()
        return SelectListData(
            method=method,
            select=select,
            filter=filter_,
            order=order,
            start=start,
        )

    @classmethod
    def fields(cls) -> GetFieldsData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION, BitrixMethods.FIELDS.value)
        return GetFieldsData(method=method)

    @classmethod
    def create(cls, fields: list[dict[str, str]], reg_sonet: bool = True, import_: bool = False) -> AddData:
        kwargs = dict()
        method = cls.root.format(cls.NAME_OBJECT_ACTION, BitrixMethods.ADD.value)
        fields = Fields(*list(fields)).compare
        kwargs.update(method=method, fields=fields)
        if cls.REGISTER_SONET_EVENT_OPTION:
            value = 'Y' if reg_sonet else 'N'
            kwargs.update(params={BitrixParams.REGISTER_SONET_EVENT.value: value})
        if cls.IMPORT_OPTION:
            value = 'Y' if import_ else ''
            kwargs.update(params={BitrixParams.IMPORT.value: value})
        return AddData(**kwargs)

    @classmethod
    def update(cls, fields: list[dict[str, str]], reg_sonet: bool = True, import_: bool = False) -> UpdateData:
        kwargs = dict()
        method = cls.root.format(cls.NAME_OBJECT_ACTION, BitrixMethods.UPDATE.value)
        fields = Fields(*list(fields)).compare
        kwargs.update(method=method, fields=fields)
        if cls.REGISTER_SONET_EVENT_OPTION:
            kwargs.update(params='Y' if reg_sonet else 'N')
        if cls.IMPORT_OPTION:
            kwargs.update(params='Y' if import_ else '')
        return UpdateData(**kwargs)

    @classmethod
    def delete(cls, id: int) -> DeleteData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION, BitrixMethods.DELETE.value)
        return DeleteData(method=method, id=id)

    @staticmethod
    def SET_UF(key: str, value: Any) -> dict[str, Any]:
        return {f'UF_{key}': value}


class Deal[T](BaseBitrixObject):
    """
    The Deal class provides static methods for formatting Bitrix24 product field parameters.
    Each method corresponds to a field in the PRODUCT_FIELD class and returns a string representation
    suitable for use in Bitrix24 API requests. This class helps to build query parameters in a consistent
    and type-safe way, reducing errors and improving code readability.
    """
    NAME_OBJECT_ACTION = BitrixCRMTypes.DEAL.value
    REGISTER_SONET_EVENT_OPTION = True
    IMPORT_OPTION = False

    ID = DEAL_FIELD.ID
    TITLE = DEAL_FIELD.TITLE
    TYPE_ID = DEAL_FIELD.TYPE_ID
    CATEGORY_ID = DEAL_FIELD.CATEGORY_ID
    STAGE_ID = DEAL_FIELD.STAGE_ID
    OPPORTUNITY = DEAL_FIELD.OPPORTUNITY
    IS_MANUAL_OPPORTUNITY = DEAL_FIELD.IS_MANUAL_OPPORTUNITY
    ASSIGNED_BY_ID = DEAL_FIELD.ASSIGNED_BY_ID
    DATE_CREATE = DEAL_FIELD.DATE_CREATE
    PROBABILITY = DEAL_FIELD.PROBABILITY
    BEGINDATE = DEAL_FIELD.BEGINDATE
    CLOSEDATE = DEAL_FIELD.CLOSEDATE
    CURRENCY_ID = DEAL_FIELD.CURRENCY_ID
    COMPANY_ID = DEAL_FIELD.COMPANY_ID
    SOURCE_ID = DEAL_FIELD.SOURCE_ID
    SOURCE_DESCRIPTION = DEAL_FIELD.SOURCE_DESCRIPTION
    COMMENTS = DEAL_FIELD.COMMENTS
    OPENED = DEAL_FIELD.OPENED
    IS_RECURRING = DEAL_FIELD.IS_RECURRING
    ORIGINATOR_ID = DEAL_FIELD.ORIGINATOR_ID
    ORIGIN_ID = DEAL_FIELD.ORIGIN_ID
    UTM_SOURCE = DEAL_FIELD.UTM_SOURCE
    UTM_MEDIUM = DEAL_FIELD.UTM_MEDIUM
    UTM_CAMPAIGN = DEAL_FIELD.UTM_CAMPAIGN
    UTM_CONTENT = DEAL_FIELD.UTM_CONTENT
    UTM_TERM = DEAL_FIELD.UTM_TERM
    TRACE = DEAL_FIELD.TRACE

    root = 'crm.{}.{}'

    @staticmethod
    def SET_ID(value: int) -> dict[str, int]:
        """Unique deal ID."""
        return {DEAL_FIELD.ID: value}

    @staticmethod
    def SET_TITLE(value: T) -> dict[str, T]:
        """Title of the deal."""
        return {DEAL_FIELD.TITLE: value}

    @staticmethod
    def SET_TYPE_ID(value: T | list[T]) -> dict[str, T | list[T]]:
        """Deal type identifier (crm_status). Use crm.status.list with filter {ENTITY_ID: "DEAL_TYPE"}."""
        return {DEAL_FIELD.TYPE_ID: value}

    @staticmethod
    def SET_CATEGORY_ID(value: T | list[T]) -> dict[str, T | list[T]]:
        """Deal category (funnel) identifier. Use crm.category.list with entityTypeId=2."""
        return {DEAL_FIELD.CATEGORY_ID: value}

    @staticmethod
    def SET_STAGE_ID(value: T) -> dict[str, T]:
        """Deal stage identifier. Use crm.status.list with filter {ENTITY_ID: "DEAL_STAGE"}."""
        return {DEAL_FIELD.STAGE_ID: value}

    @staticmethod
    def SET_OPPORTUNITY(value: T) -> dict[str, T]:
        """Deal amount."""
        return {DEAL_FIELD.OPPORTUNITY: value}

    @staticmethod
    def SET_IS_MANUAL_OPPORTUNITY(value: bool) -> dict[str, str]:
        """Indicates if the opportunity is set manually. Accepts 'Y' or 'N'."""
        return {DEAL_FIELD.IS_MANUAL_OPPORTUNITY: 'Y' if value else 'N'}

    @staticmethod
    def SET_ASSIGNED_BY_ID(value: T | list[T]) -> dict[str, T, list[T]]:
        """User ID of the responsible person for the deal."""
        return {DEAL_FIELD.ASSIGNED_BY_ID: value}

    @staticmethod
    def SET_DATE_CREATE(value: datetime | str) -> dict[str, str]:
        """Date and time when the deal was created. Format: ISO 8601 string or datetime object."""
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(
                    LogicErrors.WRONG_TYPE_PARAMETER.format(value.__class__.__name__)
                )
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {DEAL_FIELD.DATE_CREATE: value.isoformat()}

    @staticmethod
    def SET_PROBABILITY(value: int) -> dict[str, int]:
        """Probability of successful deal completion, as a percentage (0-100)."""
        return {DEAL_FIELD.PROBABILITY: int(value)}

    @staticmethod
    def SET_BEGINDATE(value: datetime | str) -> dict[str, str]:
        """Planned start date of the deal. Format: ISO 8601 string or datetime object."""
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(
                    LogicErrors.WRONG_TYPE_PARAMETER.format(value.__class__.__name__)
                )
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {DEAL_FIELD.BEGINDATE: value.isoformat()}

    @staticmethod
    def SET_CLOSEDATE(value: datetime | str) -> dict[str, str]:
        """Planned close date of the deal. Format: ISO 8601 string or datetime object."""
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(
                    LogicErrors.WRONG_TYPE_PARAMETER.format(value.__class__.__name__)
                )
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {DEAL_FIELD.CLOSEDATE: value.isoformat()}

    @staticmethod
    def SET_CURRENCY_ID(value: int) -> dict[str, int]:
        """Currency identifier for the deal. Use crm.currency.list."""
        return {DEAL_FIELD.CURRENCY_ID: int(value)}

    @staticmethod
    def SET_ACCOUNT_ID(value: int) -> dict[str, int]:
        """Account identifier associated with the deal."""
        return {DEAL_FIELD.ACCOUNT_ID: int(value)}

    @staticmethod
    def SET_CONTACT_ID(value: int | list[int]) -> dict[str, int | list[int]]:
        """Contact ID(s) associated with the deal."""
        return {DEAL_FIELD.CONTACT_ID: value}

    @staticmethod
    def SET_COMPANY_ID(value: int | list[int]) -> dict[str, int | list[int]]:
        """Company ID(s) associated with the deal."""
        return {DEAL_FIELD.COMPANY_ID: value}

    @staticmethod
    def SET_SOURCE_ID(value: int) -> dict[str, int]:
        """Source identifier (crm_status). Use crm.status.list with filter {ENTITY_ID: "SOURCE"}."""
        return {DEAL_FIELD.SOURCE_ID: int(value)}

    @staticmethod
    def SET_SOURCE_DESCRIPTION(value: str) -> dict[str, str]:
        """Additional information about the deal source."""
        return {DEAL_FIELD.SOURCE_DESCRIPTION: str(value)}

    @staticmethod
    def SET_COMMENTS(value: str) -> dict[str, str]:
        """Comments for the deal. Supports BB codes."""
        return {DEAL_FIELD.COMMENTS: str(value)}

    @staticmethod
    def SET_OPENED(value: bool) -> dict[str, str]:
        """Indicates if the deal is available to all users ('Y' or 'N')."""
        return {DEAL_FIELD.OPENED: 'Y' if value else 'N'}

    @staticmethod
    def SET_IS_RECURRING(value: bool) -> dict[str, str]:
        """Indicates if the deal is recurring ('Y' or 'N')."""
        return {DEAL_FIELD.IS_RECURRING: 'Y' if value else 'N'}

    @staticmethod
    def SET_ORIGINATOR_ID(value: str) -> dict[str, str]:
        """External system originator identifier for the deal."""
        return {DEAL_FIELD.ORIGINATOR_ID: str(value)}

    @staticmethod
    def SET_ORIGIN_ID(value: str) -> dict[str, str]:
        """External system origin identifier for the deal."""
        return {DEAL_FIELD.ORIGIN_ID: str(value)}

    @staticmethod
    def SET_UTM_SOURCE(value: str) -> dict[str, str]:
        """UTM Source parameter for the deal."""
        return {DEAL_FIELD.UTM_SOURCE: str(value)}

    @staticmethod
    def SET_UTM_MEDIUM(value: str) -> dict[str, str]:
        """UTM Medium parameter for the deal."""
        return {DEAL_FIELD.UTM_MEDIUM: str(value)}

    @staticmethod
    def SET_UTM_CAMPAIGN(value: str) -> dict[str, str]:
        """UTM Campaign parameter for the deal."""
        return {DEAL_FIELD.UTM_CAMPAIGN: str(value)}

    @staticmethod
    def SET_UTM_CONTENT(value: str) -> dict[str, str]:
        """UTM Content parameter for the deal."""
        return {DEAL_FIELD.UTM_CONTENT: str(value)}

    @staticmethod
    def SET_UTM_TERM(value: str) -> dict[str, str]:
        """UTM Term parameter for the deal."""
        return {DEAL_FIELD.UTM_TERM: str(value)}

    @staticmethod
    def SET_TRACE(value: str) -> dict[str, str]:
        """Trace information for the deal."""
        return {DEAL_FIELD.TRACE: str(value)}


class Contact(BaseBitrixObject):
    """
    The Contact class provides static methods for formatting Bitrix24 contact
    field parameters. Each method corresponds to a field in the ContactField
    class and returns a string representation suitable for use in Bitrix24 API
    requests.
    """
    NAME_OBJECT_ACTION = BitrixCRMTypes.CONTACT.value
    REGISTER_SONET_EVENT_OPTION = True
    IMPORT_OPTION = True

    ID = CONTACT_FIELD.ID
    HONORIFIC = CONTACT_FIELD.HONORIFIC
    NAME = CONTACT_FIELD.NAME
    SECOND_NAME = CONTACT_FIELD.SECOND_NAME
    LAST_NAME = CONTACT_FIELD.LAST_NAME
    PHOTO = CONTACT_FIELD.PHOTO
    BIRTHDATE = CONTACT_FIELD.BIRTHDATE
    TYPE_ID = CONTACT_FIELD.TYPE_ID
    SOURCE_ID = CONTACT_FIELD.SOURCE_ID
    SOURCE_DESCRIPTION = CONTACT_FIELD.SOURCE_DESCRIPTION
    POST = CONTACT_FIELD.POST
    COMMENTS = CONTACT_FIELD.COMMENTS
    OPENED = CONTACT_FIELD.OPENED
    EXPORT = CONTACT_FIELD.EXPORT
    ASSIGNED_BY_ID = CONTACT_FIELD.ASSIGNED_BY_ID
    COMPANY_ID = CONTACT_FIELD.COMPANY_ID
    COMPANY_IDS = CONTACT_FIELD.COMPANY_IDS
    UTM_SOURCE = CONTACT_FIELD.UTM_SOURCE
    UTM_MEDIUM = CONTACT_FIELD.UTM_MEDIUM
    UTM_CAMPAIGN = CONTACT_FIELD.UTM_CAMPAIGN
    UTM_CONTENT = CONTACT_FIELD.UTM_CONTENT
    UTM_TERM = CONTACT_FIELD.UTM_TERM
    TRACE = CONTACT_FIELD.TRACE
    PHONE = CONTACT_FIELD.PHONE
    EMAIL = CONTACT_FIELD.EMAIL
    WEB = CONTACT_FIELD.WEB
    IM = CONTACT_FIELD.IM
    LINK = CONTACT_FIELD.LINK

    root = 'crm.{}.{}'

    @staticmethod
    def SET_ID(value: int) -> dict[str, int]:
        """Unique contact ID."""
        return {CONTACT_FIELD.ID: int(value)}

    @staticmethod
    def SET_HONORIFIC(value: str) -> dict[str, str]:
        """Contact honorific. Use `crm.status.list` with `ENTITY_ID=HONORIFIC`."""
        return {CONTACT_FIELD.HONORIFIC: str(value)}

    @staticmethod
    def SET_NAME(value: str) -> dict[str, str]:
        """Contact first name."""
        return {CONTACT_FIELD.NAME: str(value)}

    @staticmethod
    def SET_SECOND_NAME(value: str) -> dict[str, str]:
        """Contact middle name."""
        return {CONTACT_FIELD.SECOND_NAME: str(value)}

    @staticmethod
    def SET_LAST_NAME(value: str) -> dict[str, str]:
        """Contact last name."""
        return {CONTACT_FIELD.LAST_NAME: str(value)}

    @staticmethod
    def SET_PHOTO(value: str) -> dict[str, str]:
        """Contact photo file ID."""
        return {CONTACT_FIELD.PHOTO: str(value)}

    @staticmethod
    def SET_BIRTHDATE(value: datetime | str) -> dict[str, str]:
        """Contact birthdate. Format: `datatime`."""
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(
                    LogicErrors.WRONG_TYPE_PARAMETER.format(value.__class__.__name__)
                )
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {DEAL_FIELD.BEGINDATE: value.isoformat()}

    @staticmethod
    def SET_TYPE_ID(value: str) -> dict[str, str]:
        """Contact type. Use `crm.status.list` with `ENTITY_ID=CONTACT_TYPE`."""
        return {CONTACT_FIELD.TYPE_ID: str(value)}

    @staticmethod
    def SET_SOURCE_ID(value: int) -> dict[str, int]:
        """Contact source. Use `crm.status.list` with `ENTITY_ID=SOURCE`."""
        return {CONTACT_FIELD.SOURCE_ID: int(value)}

    @staticmethod
    def SET_SOURCE_DESCRIPTION(value: str) -> dict[str, str]:
        """Additional info about contact source."""
        return {CONTACT_FIELD.SOURCE_DESCRIPTION: str(value)}

    @staticmethod
    def SET_POST(value: str) -> dict[str, str]:
        """Contact job position."""
        return {CONTACT_FIELD.POST: str(value)}

    @staticmethod
    def SET_COMMENTS(value: str) -> dict[str, str]:
        """Contact comments. Supports BB codes."""
        return {CONTACT_FIELD.COMMENTS: str(value)}

    @staticmethod
    def SET_OPENED(value: bool) -> dict[str, str]:
        """Is contact available to all users (`Y` or `N`)."""
        return {CONTACT_FIELD.OPENED: 'Y' if value else 'N'}

    @staticmethod
    def SET_EXPORT(value: bool) -> dict[str, str]:
        """Is contact available for export (`Y` or `N`)."""
        return {CONTACT_FIELD.EXPORT: 'Y' if value else 'N'}

    @staticmethod
    def SET_ASSIGNED_BY_ID(value: int) -> dict[str, int]:
        """Responsible user ID."""
        return {CONTACT_FIELD.ASSIGNED_BY_ID: int(value)}

    @staticmethod
    def SET_COMPANY_ID(value: int) -> dict[str, int]:
        """Company ID associated with contact."""
        return {CONTACT_FIELD.COMPANY_ID: int(value)}

    @staticmethod
    def SET_COMPANY_IDS(value: list[int]) -> dict[str, list[int]]:
        """List of company IDs associated with contact."""
        return {CONTACT_FIELD.COMPANY_IDS: list(value)}

    @staticmethod
    def SET_UTM_SOURCE(value: str) -> dict[str, str]:
        """UTM source for contact."""
        return {CONTACT_FIELD.UTM_SOURCE: str(value)}

    @staticmethod
    def SET_UTM_MEDIUM(value: Literal['CPC', 'CPM']) -> dict[str, str]:
        """UTM medium for contact."""
        return {CONTACT_FIELD.UTM_MEDIUM: str(value)}

    @staticmethod
    def SET_UTM_CAMPAIGN(value: str) -> dict[str, str]:
        """UTM campaign for contact."""
        return {CONTACT_FIELD.UTM_CAMPAIGN: str(value)}

    @staticmethod
    def SET_UTM_CONTENT(value: str) -> dict[str, str]:
        """UTM content for contact."""
        return {CONTACT_FIELD.UTM_CONTENT: str(value)}

    @staticmethod
    def SET_UTM_TERM(value: str) -> dict[str, str]:
        """UTM term for contact."""
        return {CONTACT_FIELD.UTM_TERM: str(value)}

    @staticmethod
    def SET_TRACE(value: str) -> dict[str, str]:
        """Trace info for contact."""
        return {CONTACT_FIELD.TRACE: str(value)}

    @staticmethod
    def SET_PHONE(value: list[str]) -> dict[str, list[str]]:
        """List of contact phone numbers."""
        return {CONTACT_FIELD.PHONE: value}

    @staticmethod
    def SET_EMAIL(value: list[str]) -> dict[str, list[str]]:
        """List of contact email addresses."""
        return {CONTACT_FIELD.EMAIL: value}

    @staticmethod
    def SET_WEB(value: list[str]) -> dict[str, list[str]]:
        """List of contact web addresses."""
        return {CONTACT_FIELD.WEB: value}

    @staticmethod
    def SET_IM(value: list[str]) -> dict[str, list[str]]:
        """List of contact instant messenger IDs."""
        return {CONTACT_FIELD.IM: value}

    @staticmethod
    def SET_LINK(value: list[str]) -> dict[str, list[str]]:
        """List of contact links."""
        return {CONTACT_FIELD.LINK: value}
