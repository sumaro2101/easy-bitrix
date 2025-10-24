from typing import Any, ClassVar, Literal

from datetime import datetime

from .fields import (
    DEAL_FIELD,
    CONTACT_FIELD,
    ITEM_FIELD,
    LEAD_FIELD,
    COMPANY_FIELD,
    REQUISITE_FIELD,
    ACTIVITY_FIELD,
)
from .common import LogicErrors, BitrixMethods, BitrixParams, BitrixCRMTypes
from . import dto
from .parameters import Select, Filter, Order, Fields


class BaseBitrixObject:
    """
    """
    NAME_OBJECT_ACTION: ClassVar[str]
    REGISTER_SONET_EVENT_OPTION: ClassVar[bool]
    IMPORT_OPTION: ClassVar[bool]

    root: ClassVar[str]

    @classmethod
    def get(cls, id: int) -> dto.SelectGetData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION,
                                 BitrixMethods.GET.value)
        return dto.SelectGetData(method=method, id=id)

    @classmethod
    def get_list(cls, select: list[str] | None = None,
                 filter: list[dict[
                     str, str | list[str, int, float]]] | None = None,
                 order: list[dict[str, str]] | None = None,
                 start: int = 0,
                 ) -> dto.SelectListData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION,
                                 BitrixMethods.LIST.value)
        select = Select(*list(select)).compare if select else ['*', 'UF_*']
        filter_ = Filter(*list(filter)).compare if filter else dict()
        order = Order(*list(order)).compare if order else dict()
        return dto.SelectListData(
            method=method,
            select=select,
            filter=filter_,
            order=order,
            start=start,
        )

    @classmethod
    def fields(cls) -> dto.GetFieldsData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION,
                                 BitrixMethods.FIELDS.value)
        return dto.GetFieldsData(method=method)

    @classmethod
    def create(cls, fields: list[dict[str, str]], reg_sonet: bool = True,
               import_: bool = False) -> dto.AddData:
        kwargs = dict()
        method = cls.root.format(cls.NAME_OBJECT_ACTION,
                                 BitrixMethods.ADD.value)
        fields = Fields(*list(fields)).compare
        kwargs.update(method=method, fields=fields)
        if cls.REGISTER_SONET_EVENT_OPTION:
            value = 'Y' if reg_sonet else 'N'
            kwargs.update(
                params={BitrixParams.REGISTER_SONET_EVENT.value: value})
        if cls.IMPORT_OPTION:
            value = 'Y' if import_ else ''
            kwargs.update(params={BitrixParams.IMPORT.value: value})
        return dto.AddData(**kwargs)

    @classmethod
    def update(cls, fields: list[dict[str, str]], reg_sonet: bool = True,
               import_: bool = False) -> dto.UpdateData:
        kwargs = dict()
        method = cls.root.format(cls.NAME_OBJECT_ACTION,
                                 BitrixMethods.UPDATE.value)
        fields = Fields(*list(fields)).compare
        kwargs.update(method=method, fields=fields)
        if cls.REGISTER_SONET_EVENT_OPTION:
            kwargs.update(params='Y' if reg_sonet else 'N')
        if cls.IMPORT_OPTION:
            kwargs.update(params='Y' if import_ else '')
        return dto.UpdateData(**kwargs)

    @classmethod
    def delete(cls, id: int) -> dto.DeleteData:
        method = cls.root.format(cls.NAME_OBJECT_ACTION,
                                 BitrixMethods.DELETE.value)
        return dto.DeleteData(method=method, id=id)

    @staticmethod
    def SET_UF(key: str, value: Any) -> dict[str, Any]:
        return {f'UF_{key}': value}


class Item(BaseBitrixObject):
    NAME_OBJECT_ACTION = BitrixCRMTypes.ITEM.value

    ID = ITEM_FIELD.ID
    ENTITY_TYPE_ID = ITEM_FIELD.ENTITY_TYPE_ID
    USE_ORIGINAL_UF_NAMES = ITEM_FIELD.USE_ORIGINAL_UF_NAMES

    root = 'crm.{}.{}'

    @staticmethod
    def SET_ID(value: int) -> dict[str, int]:
        """Unique deal ID."""
        return {ITEM_FIELD.ID: int(value)}

    @staticmethod
    def SET_ENTITY_TYPE_ID(value: int) -> dict[str, int]:
        return {ITEM_FIELD.ENTITY_TYPE_ID: int(value)}

    @staticmethod
    def SET_USE_ORIGINAL_UF_NAMES(value: bool) -> dict[str, str]:
        return 'Y' if value else 'N'

    @classmethod
    def get(cls, type_id: int, id: int) -> dto.GetFieldsItemData:
        data = super().get(id=id)
        return dto.GetFieldsItemData(entityTypeId=type_id, **data.__dict__)

    @classmethod
    def get_list(cls, type_id: int, select=None, filter=None, order=None, start=0):
        data = super().get_list(select, filter, order, start)
        return dto.SelectListItemData(entityTypeId=type_id, **data.__dict__)

    @classmethod
    def create(cls, type_id: int, fields):
        data = super().create(fields)
        return dto.AddItemData(entityTypeId=type_id, **data.__dict__)

    @classmethod
    def update(cls, type_id: int, id: int, fields):
        data = super().update(fields)
        return dto.UpdateItemData(id=id, type_id=type_id, **data.__dict__)

    @classmethod
    def fields(cls, type_id: int) -> dto.GetFieldsItemData:
        data = super().fields()
        return dto.GetFieldsItemData(entityTypeId=type_id, **data.__dict__)

    @classmethod
    def delete(cls, type_id: int, id: int) -> dto.DeleteItemData:
        data = super().delete(id=id)
        return dto.DeleteItemData(entityTypeId=type_id, **data.__dict__)


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
    IS_RETURN_CUSTOMER = DEAL_FIELD.IS_RETURN_CUSTOMER
    CONTACT_IDS = DEAL_FIELD.CONTACT_IDS
    TAX_VALUE = DEAL_FIELD.TAX_VALUE
    CLOSED = DEAL_FIELD.CLOSED
    ADDITIONAL_INFO = DEAL_FIELD.ADDITIONAL_INFO
    LOCATION_ID = DEAL_FIELD.LOCATION_ID
    IS_REPEATED_APPROACH = DEAL_FIELD.IS_REPEATED_APPROACH
    IS_NEW = DEAL_FIELD.IS_NEW
    QUOTE_ID = DEAL_FIELD.QUOTE_ID
    CREATED_BY_ID = DEAL_FIELD.CREATED_BY_ID
    MODIFY_BY_ID = DEAL_FIELD.MODIFY_BY_ID
    MOVED_BY_ID = DEAL_FIELD.MOVED_BY_ID
    DATE_MODIFY = DEAL_FIELD.DATE_MODIFY
    MOVED_TIME = DEAL_FIELD.MOVED_TIME
    LEAD_ID = DEAL_FIELD.LEAD_ID
    LAST_ACTIVITY_BY = DEAL_FIELD.LAST_ACTIVITY_BY
    LAST_ACTIVITY_TIME = DEAL_FIELD.LAST_ACTIVITY_TIME

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
    def SET_PROBABILITY(value: int) -> dict[str, int]:
        """Probability of successful deal completion, as a percentage (0-100)."""
        return {DEAL_FIELD.PROBABILITY: int(value)}

    @staticmethod
    def SET_BEGINDATE(value: datetime | str) -> dict[str, str]:
        """Planned start date of the deal. Format: ISO 8601 string or datetime object."""
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(
                    LogicErrors.WRONG_TYPE_PARAMETER.format(
                        value.__class__.__name__)
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
                    LogicErrors.WRONG_TYPE_PARAMETER.format(
                        value.__class__.__name__)
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

    @staticmethod
    def SET_IS_RETURN_CUSTOMER(value: bool) -> dict[str, str]:
        """Indicates if the deal is for a returning customer (`Y` or `N`)."""
        return {DEAL_FIELD.IS_RETURN_CUSTOMER: 'Y' if value else 'N'}

    @staticmethod
    def SET_CONTACT_IDS(value: list[int]) -> dict[str, list[int]]:
        """List of contact IDs associated with the deal."""
        return {DEAL_FIELD.CONTACT_IDS: value}

    @staticmethod
    def SET_TAX_VALUE(value: float) -> dict[str, float]:
        """Tax value for the deal."""
        return {DEAL_FIELD.TAX_VALUE: float(value)}

    @staticmethod
    def SET_CLOSED(value: bool) -> dict[str, str]:
        """Indicates if the deal is closed (`Y` or `N`)."""
        return {DEAL_FIELD.CLOSED: 'Y' if value else 'N'}

    @staticmethod
    def SET_ADDITIONAL_INFO(value: str) -> dict[str, str]:
        """Additional information for the deal."""
        return {DEAL_FIELD.ADDITIONAL_INFO: str(value)}

    @staticmethod
    def SET_LOCATION_ID(value: int) -> dict[str, int]:
        """Location ID for the deal."""
        return {DEAL_FIELD.LOCATION_ID: int(value)}

    @staticmethod
    def SET_IS_REPEATED_APPROACH(value: bool) -> dict[str, str]:
        """Indicates if the deal is a repeated approach (`Y` or `N`)."""
        return {DEAL_FIELD.IS_REPEATED_APPROACH: 'Y' if value else 'N'}

    @staticmethod
    def SET_LAST_ACTIVITY_BY(value: int) -> dict[str, int]:
        return {DEAL_FIELD.LAST_ACTIVITY_BY: int(value)}

    @staticmethod
    def SET_LAST_ACTIVITY_TIME(value: str | datetime) -> dict[str, str]:
        try:
            if not isinstance(value, (datetime, str)):
                raise ValueError(
                    LogicErrors.WRONG_TYPE_PARAMETER.format(
                        value.__class__.__name__)
                )
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {DEAL_FIELD.LAST_ACTIVITY_TIME: value.isoformat()}

    @staticmethod
    def PARENT_ID(value: int) -> str:
        value = str(value)
        return "PARENT_ID_" + value

    @staticmethod
    def SET_PARENT_ID(value: int) -> dict[str, int]:
        value = str(value)
        return {f'PARENT_ID_ + {value}': int(value)}


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
                    LogicErrors.WRONG_TYPE_PARAMETER.format(
                        value.__class__.__name__)
                )
            if isinstance(value, str):
                value = datetime.fromisoformat(value)
        except ValueError as e:
            raise e
        return {CONTACT_FIELD.BIRTHDATE: value.isoformat()}

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


class Lead(BaseBitrixObject):
    NAME_OBJECT_ACTION = BitrixCRMTypes.LEAD.value
    REGISTER_SONET_EVENT_OPTION = True
    IMPORT_OPTION = True

    ID = LEAD_FIELD.ID
    TITLE = LEAD_FIELD.TITLE
    HONORIFIC = LEAD_FIELD.HONORIFIC
    NAME = LEAD_FIELD.NAME
    SECOND_NAME = LEAD_FIELD.SECOND_NAME
    LAST_NAME = LEAD_FIELD.LAST_NAME
    BIRTHDATE = LEAD_FIELD.BIRTHDATE
    COMPANY_TITLE = LEAD_FIELD.COMPANY_TITLE
    SOURCE_ID = LEAD_FIELD.SOURCE_ID
    SOURCE_DESCRIPTION = LEAD_FIELD.SOURCE_DESCRIPTION
    STATUS_ID = LEAD_FIELD.STATUS_ID
    STATUS_DESCRIPTION = LEAD_FIELD.STATUS_DESCRIPTION
    STATUS_SEMANTIC_ID = LEAD_FIELD.STATUS_SEMANTIC_ID
    POST = LEAD_FIELD.POST
    ADDRESS = LEAD_FIELD.ADDRESS
    ADDRESS_2 = LEAD_FIELD.ADDRESS_2
    ADDRESS_CITY = LEAD_FIELD.ADDRESS_CITY
    ADDRESS_POSTAL_CODE = LEAD_FIELD.ADDRESS_POSTAL_CODE
    ADDRESS_REGION = LEAD_FIELD.ADDRESS_REGION
    ADDRESS_PROVINCE = LEAD_FIELD.ADDRESS_PROVINCE
    ADDRESS_COUNTRY = LEAD_FIELD.ADDRESS_COUNTRY
    ADDRESS_COUNTRY_CODE = LEAD_FIELD.ADDRESS_COUNTRY_CODE
    ADDRESS_LOC_ADDR_ID = LEAD_FIELD.ADDRESS_LOC_ADDR_ID
    CURRENCY_ID = LEAD_FIELD.CURRENCY_ID
    OPPORTUNITY = LEAD_FIELD.OPPORTUNITY
    IS_MANUAL_OPPORTUNITY = LEAD_FIELD.IS_MANUAL_OPPORTUNITY
    OPENED = LEAD_FIELD.OPENED
    COMMENTS = LEAD_FIELD.COMMENTS
    HAS_PHONE = LEAD_FIELD.HAS_PHONE
    HAS_EMAIL = LEAD_FIELD.HAS_EMAIL
    HAS_IMOL = LEAD_FIELD.HAS_IMOL
    ASSIGNED_BY_ID = LEAD_FIELD.ASSIGNED_BY_ID
    CREATED_BY_ID = LEAD_FIELD.CREATED_BY_ID
    MODIFY_BY_ID = LEAD_FIELD.MODIFY_BY_ID
    MOVED_BY_ID = LEAD_FIELD.MOVED_BY_ID
    DATE_CREATE = LEAD_FIELD.DATE_CREATE
    DATE_MODIFY = LEAD_FIELD.DATE_MODIFY
    MOVED_TIME = LEAD_FIELD.MOVED_TIME
    COMPANY_ID = LEAD_FIELD.COMPANY_ID
    CONTACT_ID = LEAD_FIELD.CONTACT_ID
    CONTACT_IDS = LEAD_FIELD.CONTACT_IDS
    IS_RETURN_CUSTOMER = LEAD_FIELD.IS_RETURN_CUSTOMER
    DATE_CLOSED = LEAD_FIELD.DATE_CLOSED
    ORIGINATOR_ID = LEAD_FIELD.ORIGINATOR_ID
    ORIGIN_ID = LEAD_FIELD.ORIGIN_ID
    UTM_SOURCE = LEAD_FIELD.UTM_SOURCE
    UTM_MEDIUM = LEAD_FIELD.UTM_MEDIUM
    UTM_CAMPAIGN = LEAD_FIELD.UTM_CAMPAIGN
    UTM_CONTENT = LEAD_FIELD.UTM_CONTENT
    UTM_TERM = LEAD_FIELD.UTM_TERM
    LAST_ACTIVITY_TIME = LEAD_FIELD.LAST_ACTIVITY_TIME
    LAST_ACTIVITY_BY = LEAD_FIELD.LAST_ACTIVITY_BY

    # multiple fields by bitrix
    PHONE = LEAD_FIELD.PHONE
    EMAIL = LEAD_FIELD.EMAIL
    WEB = LEAD_FIELD.WEB
    IM = LEAD_FIELD.IM
    LINK = LEAD_FIELD.LINK

    root = 'crm.{}.{}'

    # @staticmethod
    # def SET_ID(value: int) -> dict[str, int]:
    #     return {LEAD_FIELD.ID: value}

    @staticmethod
    def SET_TITLE(value: str) -> dict[str, str]:
        return {LEAD_FIELD.TITLE: value}

    @staticmethod
    def SET_HONORIFIC(value: str) -> dict[str, str]:
        return {LEAD_FIELD.HONORIFIC: value}

    @staticmethod
    def SET_NAME(value: str) -> dict[str, str]:
        return {LEAD_FIELD.NAME: value}

    @staticmethod
    def SET_SECOND_NAME(value: str) -> dict[str, str]:
        return {LEAD_FIELD.SECOND_NAME: value}

    @staticmethod
    def SET_LAST_NAME(value: str) -> dict[str, str]:
        return {LEAD_FIELD.LAST_NAME: value}

    @staticmethod
    def SET_BIRTHDATE(value: datetime | str) -> dict[str, str]:
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        return {LEAD_FIELD.BIRTHDATE: value.isoformat()}

    @staticmethod
    def SET_COMPANY_TITLE(value: str) -> dict[str, str]:
        return {LEAD_FIELD.COMPANY_TITLE: value}

    @staticmethod
    def SET_SOURCE_ID(value: str) -> dict[str, str]:
        return {LEAD_FIELD.SOURCE_ID: value}

    @staticmethod
    def SET_SOURCE_DESCRIPTION(value: str) -> dict[str, str]:
        return {LEAD_FIELD.SOURCE_DESCRIPTION: value}

    @staticmethod
    def SET_STATUS_ID(value: str) -> dict[str, str]:
        return {LEAD_FIELD.STATUS_ID: value}

    @staticmethod
    def SET_STATUS_DESCRIPTION(value: str) -> dict[str, str]:
        return {LEAD_FIELD.STATUS_DESCRIPTION: value}

    # @staticmethod
    # def SET_STATUS_SEMANTIC_ID(value: str) -> dict[str, str]:
    # 	return {LEAD_FIELD.STATUS_SEMANTIC_ID: value}

    @staticmethod
    def SET_POST(value: str) -> dict[str, str]:
        return {LEAD_FIELD.POST: value}

    @staticmethod
    def SET_ADDRESS(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS: value}

    @staticmethod
    def SET_ADDRESS_2(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS_2: value}

    @staticmethod
    def SET_ADDRESS_CITY(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS_CITY: value}

    @staticmethod
    def SET_ADDRESS_POSTAL_CODE(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS_POSTAL_CODE: value}

    @staticmethod
    def SET_ADDRESS_REGION(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS_REGION: value}

    @staticmethod
    def SET_ADDRESS_PROVINCE(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS_PROVINCE: value}

    @staticmethod
    def SET_ADDRESS_COUNTRY(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS_COUNTRY: value}

    @staticmethod
    def SET_ADDRESS_COUNTRY_CODE(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ADDRESS_COUNTRY_CODE: value}

    @staticmethod
    def SET_ADDRESS_LOC_ADDR_ID(value: int) -> dict[str, int]:
        return {LEAD_FIELD.ADDRESS_LOC_ADDR_ID: value}

    @staticmethod
    def SET_CURRENCY_ID(value: int) -> dict[str, int]:
        return {LEAD_FIELD.CURRENCY_ID: value}

    @staticmethod
    def SET_OPPORTUNITY(value: float) -> dict[str, float]:
        return {LEAD_FIELD.OPPORTUNITY: value}

    @staticmethod
    def SET_IS_MANUAL_OPPORTUNITY(value: bool) -> dict[str, str]:
        return {LEAD_FIELD.IS_MANUAL_OPPORTUNITY: 'Y' if value else 'N'}

    @staticmethod
    def SET_OPENED(value: bool) -> dict[str, str]:
        return {LEAD_FIELD.OPENED: 'Y' if value else 'N'}

    @staticmethod
    def SET_COMMENTS(value: str) -> dict[str, str]:
        return {LEAD_FIELD.COMMENTS: value}

    # @staticmethod
    # def SET_HAS_PHONE(value: bool) -> dict[str, str]:
    #     return {LEAD_FIELD.HAS_PHONE: 'Y' if value else 'N'}
    #
    # @staticmethod
    # def SET_HAS_EMAIL(value: bool) -> dict[str, str]:
    #     return {LEAD_FIELD.HAS_EMAIL: 'Y' if value else 'N'}
    #
    # @staticmethod
    # def SET_HAS_IMOL(value: bool) -> dict[str, str]:
    #     return {LEAD_FIELD.HAS_IMOL: 'Y' if value else 'N'}

    @staticmethod
    def SET_ASSIGNED_BY_ID(value: int) -> dict[str, int]:
        return {LEAD_FIELD.ASSIGNED_BY_ID: value}

    # @staticmethod
    # def SET_CREATED_BY_ID(value: int) -> dict[str, int]:
    # 	return {LEAD_FIELD.CREATED_BY_ID: value}

    # @staticmethod
    # def SET_MODIFY_BY_ID(value: int) -> dict[str, int]:
    # 	return {LEAD_FIELD.MODIFY_BY_ID: value}

    # @staticmethod
    # def SET_MOVED_BY_ID(value: int) -> dict[str, int]:
    # 	return {LEAD_FIELD.MOVED_BY_ID: value}

    # @staticmethod
    # def SET_DATE_CREATE(value: datetime | str) -> dict[str, str]:
    # 	if isinstance(value, str):
    # 		value = datetime.fromisoformat(value)
    # 	return {LEAD_FIELD.DATE_CREATE: value.isoformat()}

    # @staticmethod
    # def SET_DATE_MODIFY(value: datetime | str) -> dict[str, str]:
    # 	if isinstance(value, str):
    # 		value = datetime.fromisoformat(value)
    # 	return {LEAD_FIELD.DATE_MODIFY: value.isoformat()}

    # @staticmethod
    # def SET_MOVED_TIME(value: datetime | str) -> dict[str, str]:
    # 	if isinstance(value, str):
    # 		value = datetime.fromisoformat(value)
    # 	return {LEAD_FIELD.MOVED_TIME: value.isoformat()}

    @staticmethod
    def SET_COMPANY_ID(value: int) -> dict[str, int]:
        return {LEAD_FIELD.COMPANY_ID: value}

    @staticmethod
    def SET_CONTACT_ID(value: int) -> dict[str, int]:
        return {LEAD_FIELD.CONTACT_ID: value}

    @staticmethod
    def SET_CONTACT_IDS(value: list[int]) -> dict[str, list[int]]:
        return {LEAD_FIELD.CONTACT_IDS: value}

    # @staticmethod
    # def SET_IS_RETURN_CUSTOMER(value: bool) -> dict[str, str]:
    # 	return {LEAD_FIELD.IS_RETURN_CUSTOMER: 'Y' if value else 'N'}
    #
    # @staticmethod
    # def SET_DATE_CLOSED(value: datetime | str) -> dict[str, str]:
    # 	if isinstance(value, str):
    # 		value = datetime.fromisoformat(value)
    # 	return {LEAD_FIELD.DATE_CLOSED: value.isoformat()}

    @staticmethod
    def SET_ORIGINATOR_ID(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ORIGINATOR_ID: value}

    @staticmethod
    def SET_ORIGIN_ID(value: str) -> dict[str, str]:
        return {LEAD_FIELD.ORIGIN_ID: value}

    @staticmethod
    def SET_UTM_SOURCE(value: str) -> dict[str, str]:
        return {LEAD_FIELD.UTM_SOURCE: value}

    @staticmethod
    def SET_UTM_MEDIUM(value: str) -> dict[str, str]:
        return {LEAD_FIELD.UTM_MEDIUM: value}

    @staticmethod
    def SET_UTM_CAMPAIGN(value: str) -> dict[str, str]:
        return {LEAD_FIELD.UTM_CAMPAIGN: value}

    @staticmethod
    def SET_UTM_CONTENT(value: str) -> dict[str, str]:
        return {LEAD_FIELD.UTM_CONTENT: value}

    @staticmethod
    def SET_UTM_TERM(value: str) -> dict[str, str]:
        return {LEAD_FIELD.UTM_TERM: value}

    # @staticmethod
    # def SET_LAST_ACTIVITY_TIME(value: datetime | str) -> dict[str, str]:
    # 	if isinstance(value, str):
    # 		value = datetime.fromisoformat(value)
    # 	return {LEAD_FIELD.LAST_ACTIVITY_TIME: value.isoformat()}
    #
    # @staticmethod
    # def SET_LAST_ACTIVITY_BY(value: str) -> dict[str, str]:
    # 	return {LEAD_FIELD.LAST_ACTIVITY_BY: value}

    # Множественные поля
    @staticmethod
    def SET_PHONE(value: list[str]) -> dict[str, list[str]]:
        return {LEAD_FIELD.PHONE: value}

    @staticmethod
    def SET_EMAIL(value: list[str]) -> dict[str, list[str]]:
        return {LEAD_FIELD.EMAIL: value}

    @staticmethod
    def SET_WEB(value: list[str]) -> dict[str, list[str]]:
        return {LEAD_FIELD.WEB: value}

    @staticmethod
    def SET_IM(value: list[str]) -> dict[str, list[str]]:
        return {LEAD_FIELD.IM: value}

    @staticmethod
    def SET_LINK(value: list[str]) -> dict[str, list[str]]:
        return {LEAD_FIELD.LINK: value}

    @staticmethod
    def SET_UF(key: str, value: Any) -> dict[str, Any]:
        return {f'UF_CRM_{key}': value}

    @staticmethod
    def SET_PARENT_ID(field_name: str, value: int) -> dict[str, int]:
        return {f'PARENT_ID_{field_name}': value}


class Company(BaseBitrixObject):
    NAME_OBJECT_ACTION = BitrixCRMTypes.COMPANY.value
    REGISTER_SONET_EVENT_OPTION = True
    IMPORT_OPTION = True

    ID = COMPANY_FIELD.ID
    TITLE = COMPANY_FIELD.TITLE
    COMPANY_TYPE = COMPANY_FIELD.COMPANY_TYPE
    LOGO = COMPANY_FIELD.LOGO
    ADDRESS = COMPANY_FIELD.ADDRESS
    ADDRESS_2 = COMPANY_FIELD.ADDRESS_2
    ADDRESS_CITY = COMPANY_FIELD.ADDRESS_CITY
    ADDRESS_POSTAL_CODE = COMPANY_FIELD.ADDRESS_POSTAL_CODE
    ADDRESS_REGION = COMPANY_FIELD.ADDRESS_REGION
    ADDRESS_PROVINCE = COMPANY_FIELD.ADDRESS_PROVINCE
    ADDRESS_COUNTRY = COMPANY_FIELD.ADDRESS_COUNTRY
    ADDRESS_COUNTRY_CODE = COMPANY_FIELD.ADDRESS_COUNTRY_CODE
    ADDRESS_LOC_ADDR_ID = COMPANY_FIELD.ADDRESS_LOC_ADDR_ID
    ADDRESS_LEGAL = COMPANY_FIELD.ADDRESS_LEGAL
    REG_ADDRESS = COMPANY_FIELD.REG_ADDRESS
    REG_ADDRESS_2 = COMPANY_FIELD.REG_ADDRESS_2
    REG_ADDRESS_CITY = COMPANY_FIELD.REG_ADDRESS_CITY
    REG_ADDRESS_POSTAL_CODE = COMPANY_FIELD.REG_ADDRESS_POSTAL_CODE
    REG_ADDRESS_REGION = COMPANY_FIELD.REG_ADDRESS_REGION
    REG_ADDRESS_PROVINCE = COMPANY_FIELD.REG_ADDRESS_PROVINCE
    REG_ADDRESS_COUNTRY = COMPANY_FIELD.REG_ADDRESS_COUNTRY
    REG_ADDRESS_COUNTRY_CODE = COMPANY_FIELD.REG_ADDRESS_COUNTRY_CODE
    REG_ADDRESS_LOC_ADDR_ID = COMPANY_FIELD.REG_ADDRESS_LOC_ADDR_ID
    BANKING_DETAILS = COMPANY_FIELD.BANKING_DETAILS
    INDUSTRY = COMPANY_FIELD.INDUSTRY
    EMPLOYEES = COMPANY_FIELD.EMPLOYEES
    CURRENCY_ID = COMPANY_FIELD.CURRENCY_ID
    REVENUE = COMPANY_FIELD.REVENUE
    OPENED = COMPANY_FIELD.OPENED
    COMMENTS = COMPANY_FIELD.COMMENTS
    IS_MY_COMPANY = COMPANY_FIELD.IS_MY_COMPANY
    ASSIGNED_BY_ID = COMPANY_FIELD.ASSIGNED_BY_ID
    CONTACT_ID = COMPANY_FIELD.CONTACT_ID
    ORIGINATOR_ID = COMPANY_FIELD.ORIGINATOR_ID
    ORIGIN_ID = COMPANY_FIELD.ORIGIN_ID
    ORIGIN_VERSION = COMPANY_FIELD.ORIGIN_VERSION
    UTM_SOURCE = COMPANY_FIELD.UTM_SOURCE
    UTM_MEDIUM = COMPANY_FIELD.UTM_MEDIUM
    UTM_CAMPAIGN = COMPANY_FIELD.UTM_CAMPAIGN
    UTM_CONTENT = COMPANY_FIELD.UTM_CONTENT
    UTM_TERM = COMPANY_FIELD.UTM_TERM
    PARENT_ID = COMPANY_FIELD.PARENT_ID
    PHONE = COMPANY_FIELD.PHONE
    EMAIL = COMPANY_FIELD.EMAIL
    WEB = COMPANY_FIELD.WEB
    IM = COMPANY_FIELD.IM
    LINK = COMPANY_FIELD.LINK

    root = 'crm.{}.{}'

    # @staticmethod
    # def SET_ID(value: int) -> dict[str, int]:
    #     return {'ID': value}

    @staticmethod
    def SET_TITLE(value: str) -> dict[str, str]:
        return {'TITLE': value}

    @staticmethod
    def SET_COMPANY_TYPE(value: str) -> dict[str, str]:
        return {'COMPANY_TYPE': value}

    @staticmethod
    def SET_LOGO(value: str) -> dict[str, str]:
        return {'LOGO': value}

    @staticmethod
    def SET_ADDRESS(value: str) -> dict[str, str]:
        return {'ADDRESS': value}

    @staticmethod
    def SET_ADDRESS_2(value: str) -> dict[str, str]:
        return {'ADDRESS_2': value}

    @staticmethod
    def SET_ADDRESS_CITY(value: str) -> dict[str, str]:
        return {'ADDRESS_CITY': value}

    @staticmethod
    def SET_ADDRESS_POSTAL_CODE(value: str) -> dict[str, str]:
        return {'ADDRESS_POSTAL_CODE': value}

    @staticmethod
    def SET_ADDRESS_REGION(value: str) -> dict[str, str]:
        return {'ADDRESS_REGION': value}

    @staticmethod
    def SET_ADDRESS_PROVINCE(value: str) -> dict[str, str]:
        return {'ADDRESS_PROVINCE': value}

    @staticmethod
    def SET_ADDRESS_COUNTRY(value: str) -> dict[str, str]:
        return {'ADDRESS_COUNTRY': value}

    @staticmethod
    def SET_ADDRESS_COUNTRY_CODE(value: str) -> dict[str, str]:
        return {'ADDRESS_COUNTRY_CODE': value}

    @staticmethod
    def SET_ADDRESS_LOC_ADDR_ID(value: int) -> dict[str, int]:
        return {'ADDRESS_LOC_ADDR_ID': value}

    @staticmethod
    def SET_ADDRESS_LEGAL(value: str) -> dict[str, str]:
        return {'ADDRESS_LEGAL': value}

    @staticmethod
    def SET_REG_ADDRESS(value: str) -> dict[str, str]:
        return {'REG_ADDRESS': value}

    @staticmethod
    def SET_REG_ADDRESS_2(value: str) -> dict[str, str]:
        return {'REG_ADDRESS_2': value}

    @staticmethod
    def SET_REG_ADDRESS_CITY(value: str) -> dict[str, str]:
        return {'REG_ADDRESS_CITY': value}

    @staticmethod
    def SET_REG_ADDRESS_POSTAL_CODE(value: str) -> dict[str, str]:
        return {'REG_ADDRESS_POSTAL_CODE': value}

    @staticmethod
    def SET_REG_ADDRESS_REGION(value: str) -> dict[str, str]:
        return {'REG_ADDRESS_REGION': value}

    @staticmethod
    def SET_REG_ADDRESS_PROVINCE(value: str) -> dict[str, str]:
        return {'REG_ADDRESS_PROVINCE': value}

    @staticmethod
    def SET_REG_ADDRESS_COUNTRY(value: str) -> dict[str, str]:
        return {'REG_ADDRESS_COUNTRY': value}

    @staticmethod
    def SET_REG_ADDRESS_COUNTRY_CODE(value: str) -> dict[str, str]:
        return {'REG_ADDRESS_COUNTRY_CODE': value}

    @staticmethod
    def SET_REG_ADDRESS_LOC_ADDR_ID(value: int) -> dict[str, int]:
        return {'REG_ADDRESS_LOC_ADDR_ID': value}

    @staticmethod
    def SET_BANKING_DETAILS(value: str) -> dict[str, str]:
        return {'BANKING_DETAILS': value}

    @staticmethod
    def SET_INDUSTRY(value: str) -> dict[str, str]:
        return {'INDUSTRY': value}

    @staticmethod
    def SET_EMPLOYEES(value: str) -> dict[str, str]:
        return {'EMPLOYEES': value}

    @staticmethod
    def SET_CURRENCY_ID(value: str) -> dict[str, str]:
        return {'CURRENCY_ID': value}

    @staticmethod
    def SET_REVENUE(value: float) -> dict[str, float]:
        return {'REVENUE': value}

    @staticmethod
    def SET_OPENED(value: str) -> dict[str, str]:
        return {'OPENED': value}

    @staticmethod
    def SET_COMMENTS(value: str) -> dict[str, str]:
        return {'COMMENTS': value}

    # @staticmethod
    # def SET_HAS_PHONE(value: str) -> dict[str, str]:
    #     return {'HAS_PHONE': value}
    #
    # @staticmethod
    # def SET_HAS_EMAIL(value: str) -> dict[str, str]:
    #     return {'HAS_EMAIL': value}
    #
    # @staticmethod
    # def SET_HAS_IMOL(value: str) -> dict[str, str]:
    #     return {'HAS_IMOL': value}

    @staticmethod
    def SET_IS_MY_COMPANY(value: str) -> dict[str, str]:
        return {'IS_MY_COMPANY': value}

    @staticmethod
    def SET_ASSIGNED_BY_ID(value: int) -> dict[str, int]:
        return {'ASSIGNED_BY_ID': value}

    # @staticmethod
    # def SET_CREATED_BY_ID(value: int) -> dict[str, int]:
    # 	return {'CREATED_BY_ID': value}
    #
    # @staticmethod
    # def SET_MODIFY_BY_ID(value: int) -> dict[str, int]:
    # 	return {'MODIFY_BY_ID': value}
    #
    # @staticmethod
    # def SET_DATE_CREATE(value: str) -> dict[str, str]:
    # 	return {'DATE_CREATE': value}
    #
    # @staticmethod
    # def SET_DATE_MODIFY(value: str) -> dict[str, str]:
    # 	return {'DATE_MODIFY': value}

    @staticmethod
    def SET_CONTACT_ID(value: str) -> dict[str, str]:
        return {'CONTACT_ID': value}

    # @staticmethod
    # def SET_LEAD_ID(value: int) -> dict[str, int]:
    # 	return {'LEAD_ID': value}

    @staticmethod
    def SET_ORIGINATOR_ID(value: str) -> dict[str, str]:
        return {'ORIGINATOR_ID': value}

    @staticmethod
    def SET_ORIGIN_ID(value: str) -> dict[str, str]:
        return {'ORIGIN_ID': value}

    @staticmethod
    def SET_ORIGIN_VERSION(value: str) -> dict[str, str]:
        return {'ORIGIN_VERSION': value}

    @staticmethod
    def SET_UTM_SOURCE(value: str) -> dict[str, str]:
        return {'UTM_SOURCE': value}

    @staticmethod
    def SET_UTM_MEDIUM(value: str) -> dict[str, str]:
        return {'UTM_MEDIUM': value}

    @staticmethod
    def SET_UTM_CAMPAIGN(value: str) -> dict[str, str]:
        return {'UTM_CAMPAIGN': value}

    @staticmethod
    def SET_UTM_CONTENT(value: str) -> dict[str, str]:
        return {'UTM_CONTENT': value}

    @staticmethod
    def SET_UTM_TERM(value: str) -> dict[str, str]:
        return {'UTM_TERM': value}

    @staticmethod
    def SET_PARENT_ID(value: int) -> dict[str, int]:
        return {'PARENT_ID_xxx': value}

    # @staticmethod
    # def SET_LAST_ACTIVITY_TIME(value: str) -> dict[str, str]:
    # 	return {'LAST_ACTIVITY_TIME': value}
    #
    # @staticmethod
    # def SET_LAST_ACTIVITY_BY(value: str) -> dict[str, str]:
    # 	return {'LAST_ACTIVITY_BY': value}

    @staticmethod
    def SET_PHONE(value: list[dict]) -> dict[str, list[dict]]:
        return {'PHONE': value}

    @staticmethod
    def SET_EMAIL(value: list[dict]) -> dict[str, list[dict]]:
        return {'EMAIL': value}

    @staticmethod
    def SET_WEB(value: list[dict]) -> dict[str, list[dict]]:
        return {'WEB': value}

    @staticmethod
    def SET_IM(value: list[dict]) -> dict[str, list[dict]]:
        return {'IM': value}

    @staticmethod
    def SET_LINK(value: list[dict]) -> dict[str, list[dict]]:
        return {'LINK': value}


class Requisite(BaseBitrixObject):
    """
    """
    NAME_OBJECT_ACTION = BitrixCRMTypes.REQUISITE.value
    REGISTER_SONET_EVENT_OPTION = True
    IMPORT_OPTION = True

    ID = REQUISITE_FIELD.ID
    ENTITY_TYPE_ID = REQUISITE_FIELD.ENTITY_TYPE_ID
    ENTITY_ID = REQUISITE_FIELD.ENTITY_ID
    PRESET_ID = REQUISITE_FIELD.PRESET_ID
    DATE_CREATE = REQUISITE_FIELD.DATE_CREATE
    DATE_MODIFY = REQUISITE_FIELD.DATE_MODIFY
    CREATED_BY_ID = REQUISITE_FIELD.CREATED_BY_ID
    MODIFY_BY_ID = REQUISITE_FIELD.MODIFY_BY_ID
    NAME = REQUISITE_FIELD.NAME
    CODE = REQUISITE_FIELD.CODE
    XML_ID = REQUISITE_FIELD.XML_ID
    ORIGINATOR_ID = REQUISITE_FIELD.ORIGINATOR_ID
    ACTIVE = REQUISITE_FIELD.ACTIVE
    ADDRESS_ONLY = REQUISITE_FIELD.ADDRESS_ONLY
    SORT = REQUISITE_FIELD.SORT
    RQ_NAME = REQUISITE_FIELD.RQ_NAME
    RQ_FIRST_NAME = REQUISITE_FIELD.RQ_FIRST_NAME
    RQ_LAST_NAME = REQUISITE_FIELD.RQ_LAST_NAME
    RQ_SECOND_NAME = REQUISITE_FIELD.RQ_SECOND_NAME
    RQ_COMPANY_ID = REQUISITE_FIELD.RQ_COMPANY_ID
    RQ_COMPANY_NAME = REQUISITE_FIELD.RQ_COMPANY_NAME
    RQ_COMPANY_FULL_NAME = REQUISITE_FIELD.RQ_COMPANY_FULL_NAME
    RQ_COMPANY_REG_DATE = REQUISITE_FIELD.RQ_COMPANY_REG_DATE
    RQ_DIRECTOR = REQUISITE_FIELD.RQ_DIRECTOR
    RQ_ACCOUNTANT = REQUISITE_FIELD.RQ_ACCOUNTANT
    RQ_CEO_NAME = REQUISITE_FIELD.RQ_CEO_NAME
    RQ_CEO_WORK_POS = REQUISITE_FIELD.RQ_CEO_WORK_POS
    RQ_CONTACT = REQUISITE_FIELD.RQ_CONTACT
    RQ_EMAIL = REQUISITE_FIELD.RQ_EMAIL
    RQ_PHONE = REQUISITE_FIELD.RQ_PHONE
    RQ_FAX = REQUISITE_FIELD.RQ_FAX
    RQ_IDENT_TYPE = REQUISITE_FIELD.RQ_IDENT_TYPE
    RQ_IDENT_DOC = REQUISITE_FIELD.RQ_IDENT_DOC
    RQ_IDENT_DOC_SER = REQUISITE_FIELD.RQ_IDENT_DOC_SER
    RQ_IDENT_DOC_NUM = REQUISITE_FIELD.RQ_IDENT_DOC_NUM
    RQ_IDENT_DOC_PERS_NUM = REQUISITE_FIELD.RQ_IDENT_DOC_PERS_NUM
    RQ_IDENT_DOC_DATE = REQUISITE_FIELD.RQ_IDENT_DOC_DATE
    RQ_IDENT_DOC_ISSUED_BY = REQUISITE_FIELD.RQ_IDENT_DOC_ISSUED_BY
    RQ_IDENT_DOC_DEP_CODE = REQUISITE_FIELD.RQ_IDENT_DOC_DEP_CODE
    RQ_INN = REQUISITE_FIELD.RQ_INN
    RQ_KPP = REQUISITE_FIELD.RQ_KPP
    RQ_USRLE = REQUISITE_FIELD.RQ_USRLE
    RQ_IFNS = REQUISITE_FIELD.RQ_IFNS
    RQ_OGRN = REQUISITE_FIELD.RQ_OGRN
    RQ_OGRNIP = REQUISITE_FIELD.RQ_OGRNIP
    RQ_OKPO = REQUISITE_FIELD.RQ_OKPO
    RQ_OKTMO = REQUISITE_FIELD.RQ_OKTMO
    RQ_OKVED = REQUISITE_FIELD.RQ_OKVED
    RQ_EDRPOU = REQUISITE_FIELD.RQ_EDRPOU
    RQ_DRFO = REQUISITE_FIELD.RQ_DRFO
    RQ_KBE = REQUISITE_FIELD.RQ_KBE
    RQ_IIN = REQUISITE_FIELD.RQ_IIN
    RQ_BIN = REQUISITE_FIELD.RQ_BIN
    RQ_ST_CERT_SER = REQUISITE_FIELD.RQ_ST_CERT_SER
    RQ_ST_CERT_NUM = REQUISITE_FIELD.RQ_ST_CERT_NUM
    RQ_ST_CERT_DATE = REQUISITE_FIELD.RQ_ST_CERT_DATE
    RQ_VAT_PAYER = REQUISITE_FIELD.RQ_VAT_PAYER
    RQ_VAT_ID = REQUISITE_FIELD.RQ_VAT_ID
    RQ_VAT_CERT_SER = REQUISITE_FIELD.RQ_VAT_CERT_SER
    RQ_VAT_CERT_NUM = REQUISITE_FIELD.RQ_VAT_CERT_NUM
    RQ_VAT_CERT_DATE = REQUISITE_FIELD.RQ_VAT_CERT_DATE
    RQ_RESIDENCE_COUNTRY = REQUISITE_FIELD.RQ_RESIDENCE_COUNTRY
    RQ_BASE_DOC = REQUISITE_FIELD.RQ_BASE_DOC
    RQ_REGON = REQUISITE_FIELD.RQ_REGON
    RQ_KRS = REQUISITE_FIELD.RQ_KRS
    RQ_PESEL = REQUISITE_FIELD.RQ_PESEL
    RQ_LEGAL_FORM = REQUISITE_FIELD.RQ_LEGAL_FORM
    RQ_SIRET = REQUISITE_FIELD.RQ_SIRET
    RQ_SIREN = REQUISITE_FIELD.RQ_SIREN
    RQ_CAPITAL = REQUISITE_FIELD.RQ_CAPITAL
    RQ_RCS = REQUISITE_FIELD.RQ_RCS
    RQ_CNPJ = REQUISITE_FIELD.RQ_CNPJ
    RQ_STATE_REG = REQUISITE_FIELD.RQ_STATE_REG
    RQ_MNPL_REG = REQUISITE_FIELD.RQ_MNPL_REG
    RQ_CPF = REQUISITE_FIELD.RQ_CPF
    UF_CRM = REQUISITE_FIELD.UF_CRM

    root = 'crm.{}.{}'

    # @staticmethod
    # def SET_ID(value: int) -> dict[str, int]:
    #     return {REQUISITE_FIELD.ID: int(value)}

    @staticmethod
    def SET_ENTITY_TYPE_ID(value: int) -> dict[str, int]:
        return {REQUISITE_FIELD.ENTITY_TYPE_ID: int(value)}

    @staticmethod
    def SET_ENTITY_ID(value: int) -> dict[str, int]:
        return {REQUISITE_FIELD.ENTITY_ID: int(value)}

    @staticmethod
    def SET_PRESET_ID(value: int) -> dict[str, int]:
        return {REQUISITE_FIELD.PRESET_ID: int(value)}

    # @staticmethod
    # def SET_DATE_CREATE(value: datetime | str) -> dict[str, str]:
    #     if isinstance(value, datetime):
    #         value = value.isoformat()
    #     return {REQUISITE_FIELD.DATE_CREATE: str(value)}
    #
    # @staticmethod
    # def SET_DATE_MODIFY(value: datetime | str) -> dict[str, str]:
    #     if isinstance(value, datetime):
    #         value = value.isoformat()
    #     return {REQUISITE_FIELD.DATE_MODIFY: str(value)}
    #
    # @staticmethod
    # def SET_CREATED_BY_ID(value: int) -> dict[str, int]:
    #     return {REQUISITE_FIELD.CREATED_BY_ID: int(value)}
    #
    # @staticmethod
    # def SET_MODIFY_BY_ID(value: int) -> dict[str, int]:
    #     return {REQUISITE_FIELD.MODIFY_BY_ID: int(value)}

    @staticmethod
    def SET_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.NAME: str(value)}

    @staticmethod
    def SET_CODE(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.CODE: str(value)}

    @staticmethod
    def SET_XML_ID(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.XML_ID: str(value)}

    @staticmethod
    def SET_ORIGINATOR_ID(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.ORIGINATOR_ID: str(value)}

    @staticmethod
    def SET_ACTIVE(value: bool) -> dict[str, str]:
        return {REQUISITE_FIELD.ACTIVE: 'Y' if value else 'N'}

    @staticmethod
    def SET_ADDRESS_ONLY(value: bool) -> dict[str, str]:
        return {REQUISITE_FIELD.ADDRESS_ONLY: 'Y' if value else 'N'}

    @staticmethod
    def SET_SORT(value: int) -> dict[str, int]:
        return {REQUISITE_FIELD.SORT: int(value)}

    # -------------------- RQ_ Fields --------------------
    @staticmethod
    def SET_RQ_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_NAME: str(value)}

    @staticmethod
    def SET_RQ_FIRST_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_FIRST_NAME: str(value)}

    @staticmethod
    def SET_RQ_LAST_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_LAST_NAME: str(value)}

    @staticmethod
    def SET_RQ_SECOND_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_SECOND_NAME: str(value)}

    @staticmethod
    def SET_RQ_COMPANY_ID(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_COMPANY_ID: str(value)}

    @staticmethod
    def SET_RQ_COMPANY_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_COMPANY_NAME: str(value)}

    @staticmethod
    def SET_RQ_COMPANY_FULL_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_COMPANY_FULL_NAME: str(value)}

    @staticmethod
    def SET_RQ_COMPANY_REG_DATE(value: datetime | str) -> dict[str, str]:
        if isinstance(value, datetime):
            value = value.isoformat()
        return {REQUISITE_FIELD.RQ_COMPANY_REG_DATE: str(value)}

    @staticmethod
    def SET_RQ_DIRECTOR(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_DIRECTOR: str(value)}

    @staticmethod
    def SET_RQ_ACCOUNTANT(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_ACCOUNTANT: str(value)}

    @staticmethod
    def SET_RQ_CEO_NAME(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_CEO_NAME: str(value)}

    @staticmethod
    def SET_RQ_CEO_WORK_POS(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_CEO_WORK_POS: str(value)}

    @staticmethod
    def SET_RQ_CONTACT(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_CONTACT: str(value)}

    @staticmethod
    def SET_RQ_EMAIL(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_EMAIL: str(value)}

    @staticmethod
    def SET_RQ_PHONE(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_PHONE: str(value)}

    @staticmethod
    def SET_RQ_FAX(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_FAX: str(value)}

    @staticmethod
    def SET_RQ_IDENT_TYPE(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IDENT_TYPE: str(value)}

    @staticmethod
    def SET_RQ_IDENT_DOC(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IDENT_DOC: str(value)}

    @staticmethod
    def SET_RQ_IDENT_DOC_SER(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IDENT_DOC_SER: str(value)}

    @staticmethod
    def SET_RQ_IDENT_DOC_NUM(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IDENT_DOC_NUM: str(value)}

    @staticmethod
    def SET_RQ_IDENT_DOC_PERS_NUM(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IDENT_DOC_PERS_NUM: str(value)}

    @staticmethod
    def SET_RQ_IDENT_DOC_DATE(value: datetime | str) -> dict[str, str]:
        if isinstance(value, datetime):
            value = value.isoformat()
        return {REQUISITE_FIELD.RQ_IDENT_DOC_DATE: str(value)}

    @staticmethod
    def SET_RQ_IDENT_DOC_ISSUED_BY(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IDENT_DOC_ISSUED_BY: str(value)}

    @staticmethod
    def SET_RQ_IDENT_DOC_DEP_CODE(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IDENT_DOC_DEP_CODE: str(value)}

    @staticmethod
    def SET_RQ_INN(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_INN: str(value)}

    @staticmethod
    def SET_RQ_KPP(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_KPP: str(value)}

    @staticmethod
    def SET_RQ_USRLE(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_USRLE: str(value)}

    @staticmethod
    def SET_RQ_IFNS(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IFNS: str(value)}

    @staticmethod
    def SET_RQ_OGRN(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_OGRN: str(value)}

    @staticmethod
    def SET_RQ_OGRNIP(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_OGRNIP: str(value)}

    @staticmethod
    def SET_RQ_OKPO(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_OKPO: str(value)}

    @staticmethod
    def SET_RQ_OKTMO(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_OKTMO: str(value)}

    @staticmethod
    def SET_RQ_OKVED(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_OKVED: str(value)}

    @staticmethod
    def SET_RQ_EDRPOU(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_EDRPOU: str(value)}

    @staticmethod
    def SET_RQ_DRFO(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_DRFO: str(value)}

    @staticmethod
    def SET_RQ_KBE(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_KBE: str(value)}

    @staticmethod
    def SET_RQ_IIN(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_IIN: str(value)}

    @staticmethod
    def SET_RQ_BIN(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_BIN: str(value)}

    @staticmethod
    def SET_RQ_ST_CERT_SER(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_ST_CERT_SER: str(value)}

    @staticmethod
    def SET_RQ_ST_CERT_NUM(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_ST_CERT_NUM: str(value)}

    @staticmethod
    def SET_RQ_ST_CERT_DATE(value: datetime | str) -> dict[str, str]:
        if isinstance(value, datetime):
            value = value.isoformat()
        return {REQUISITE_FIELD.RQ_ST_CERT_DATE: str(value)}

    @staticmethod
    def SET_RQ_VAT_PAYER(value: bool) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_VAT_PAYER: 'Y' if value else 'N'}

    @staticmethod
    def SET_RQ_VAT_ID(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_VAT_ID: str(value)}

    @staticmethod
    def SET_RQ_VAT_CERT_SER(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_VAT_CERT_SER: str(value)}

    @staticmethod
    def SET_RQ_VAT_CERT_NUM(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_VAT_CERT_NUM: str(value)}

    @staticmethod
    def SET_RQ_VAT_CERT_DATE(value: datetime | str) -> dict[str, str]:
        if isinstance(value, datetime):
            value = value.isoformat()
        return {REQUISITE_FIELD.RQ_VAT_CERT_DATE: str(value)}

    @staticmethod
    def SET_RQ_RESIDENCE_COUNTRY(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_RESIDENCE_COUNTRY: str(value)}

    @staticmethod
    def SET_RQ_BASE_DOC(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_BASE_DOC: str(value)}

    @staticmethod
    def SET_RQ_REGON(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_REGON: str(value)}

    @staticmethod
    def SET_RQ_KRS(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_KRS: str(value)}

    @staticmethod
    def SET_RQ_PESEL(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_PESEL: str(value)}

    @staticmethod
    def SET_RQ_LEGAL_FORM(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_LEGAL_FORM: str(value)}

    @staticmethod
    def SET_RQ_SIRET(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_SIRET: str(value)}

    @staticmethod
    def SET_RQ_SIREN(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_SIREN: str(value)}

    @staticmethod
    def SET_RQ_CAPITAL(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_CAPITAL: str(value)}

    @staticmethod
    def SET_RQ_RCS(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_RCS: str(value)}

    @staticmethod
    def SET_RQ_CNPJ(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_CNPJ: str(value)}

    @staticmethod
    def SET_RQ_STATE_REG(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_STATE_REG: str(value)}

    @staticmethod
    def SET_RQ_MNPL_REG(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_MNPL_REG: str(value)}

    @staticmethod
    def SET_RQ_CPF(value: str) -> dict[str, str]:
        return {REQUISITE_FIELD.RQ_CPF: str(value)}

    @staticmethod
    def SET_UF_CRM(name: str, value: Any) -> dict[str, Any]:
        return {name: value}


class Activity(BaseBitrixObject):
    """
    """

    NAME_OBJECT_ACTION = BitrixCRMTypes.ACTIVITY.value
    REGISTER_SONET_EVENT_OPTION = True
    IMPORT_OPTION = True

    ID = ACTIVITY_FIELD.ID
    OWNER_ID = ACTIVITY_FIELD.OWNER_ID
    OWNER_TYPE_ID = ACTIVITY_FIELD.OWNER_TYPE_ID
    TYPE_ID = ACTIVITY_FIELD.TYPE_ID
    PROVIDER_ID = ACTIVITY_FIELD.PROVIDER_ID
    PROVIDER_TYPE_ID = ACTIVITY_FIELD.PROVIDER_TYPE_ID
    PROVIDER_GROUP_ID = ACTIVITY_FIELD.PROVIDER_GROUP_ID
    ASSOCIATED_ENTITY_ID = ACTIVITY_FIELD.ASSOCIATED_ENTITY_ID
    SUBJECT = ACTIVITY_FIELD.SUBJECT
    START_TIME = ACTIVITY_FIELD.START_TIME
    END_TIME = ACTIVITY_FIELD.END_TIME
    DEADLINE = ACTIVITY_FIELD.DEADLINE
    COMPLETED = ACTIVITY_FIELD.COMPLETED
    STATUS = ACTIVITY_FIELD.STATUS
    RESPONSIBLE_ID = ACTIVITY_FIELD.RESPONSIBLE_ID
    PRIORITY = ACTIVITY_FIELD.PRIORITY
    NOTIFY_TYPE = ACTIVITY_FIELD.NOTIFY_TYPE
    NOTIFY_VALUE = ACTIVITY_FIELD.NOTIFY_VALUE
    DESCRIPTION = ACTIVITY_FIELD.DESCRIPTION
    DESCRIPTION_TYPE = ACTIVITY_FIELD.DESCRIPTION_TYPE
    DIRECTION = ACTIVITY_FIELD.DIRECTION
    LOCATION = ACTIVITY_FIELD.LOCATION
    CREATED = ACTIVITY_FIELD.CREATED
    AUTHOR_ID = ACTIVITY_FIELD.AUTHOR_ID
    LAST_UPDATED = ACTIVITY_FIELD.LAST_UPDATED
    EDITOR_ID = ACTIVITY_FIELD.EDITOR_ID
    SETTINGS = ACTIVITY_FIELD.SETTINGS
    ORIGIN_ID = ACTIVITY_FIELD.ORIGIN_ID
    ORIGINATOR_ID = ACTIVITY_FIELD.ORIGINATOR_ID
    RESULT_STATUS = ACTIVITY_FIELD.RESULT_STATUS
    RESULT_STREAM = ACTIVITY_FIELD.RESULT_STREAM
    RESULT_SOURCE_ID = ACTIVITY_FIELD.RESULT_SOURCE_ID
    PROVIDER_PARAMS = ACTIVITY_FIELD.PROVIDER_PARAMS
    PROVIDER_DATA = ACTIVITY_FIELD.PROVIDER_DATA
    RESULT_MARK = ACTIVITY_FIELD.RESULT_MARK
    RESULT_VALUE = ACTIVITY_FIELD.RESULT_VALUE
    RESULT_SUM = ACTIVITY_FIELD.RESULT_SUM
    RESULT_CURRENCY_ID = ACTIVITY_FIELD.RESULT_CURRENCY_ID
    AUTOCOMPLETE_RULE = ACTIVITY_FIELD.AUTOCOMPLETE_RULE
    BINDINGS = ACTIVITY_FIELD.BINDINGS
    COMMUNICATIONS = ACTIVITY_FIELD.COMMUNICATIONS
    FILES = ACTIVITY_FIELD.FILES
    WEBDAV_ELEMENTS = ACTIVITY_FIELD.WEBDAV_ELEMENTS
    IS_INCOMING_CHANNEL = ACTIVITY_FIELD.IS_INCOMING_CHANNEL

    root = 'crm.{}.{}'

    # @staticmethod
    # def SET_ID(value: int) -> dict[str, int]:
    #     """Unique activity ID (read-only)."""
    #     return {ACTIVITY_FIELD.ID: int(value)}

    @staticmethod
    def SET_OWNER_ID(value: int) -> dict[str, int]:
        """Owner entity ID (e.g. Lead, Deal, Contact)."""
        return {ACTIVITY_FIELD.OWNER_ID: int(value)}

    @staticmethod
    def SET_OWNER_TYPE_ID(value: int) -> dict[str, int]:
        """Owner entity type ID (crm.enum.ownertype)."""
        return {ACTIVITY_FIELD.OWNER_TYPE_ID: int(value)}

    @staticmethod
    def SET_TYPE_ID(value: int) -> dict[str, int]:
        """Activity type (crm_enum_activitytype)."""
        return {ACTIVITY_FIELD.TYPE_ID: int(value)}

    @staticmethod
    def SET_PROVIDER_ID(value: str) -> dict[str, str]:
        """Activity provider ID."""
        return {ACTIVITY_FIELD.PROVIDER_ID: str(value)}

    @staticmethod
    def SET_PROVIDER_TYPE_ID(value: str) -> dict[str, str]:
        """Activity provider type ID."""
        return {ACTIVITY_FIELD.PROVIDER_TYPE_ID: str(value)}

    @staticmethod
    def SET_PROVIDER_GROUP_ID(value: str) -> dict[str, str]:
        """Provider group / connector type."""
        return {ACTIVITY_FIELD.PROVIDER_GROUP_ID: str(value)}

    # @staticmethod
    # def SET_ASSOCIATED_ENTITY_ID(value: int) -> dict[str, int]:
    #     """ID of entity associated with activity."""
    #     return {ACTIVITY_FIELD.ASSOCIATED_ENTITY_ID: int(value)}

    @staticmethod
    def SET_SUBJECT(value: str) -> dict[str, str]:
        """Activity subject/title."""
        return {ACTIVITY_FIELD.SUBJECT: str(value)}

    @staticmethod
    def SET_START_TIME(value: datetime | str) -> dict[str, str]:
        """Start time of activity (datetime or ISO string)."""
        return {ACTIVITY_FIELD.START_TIME: value if isinstance(value, str) else value.isoformat()}

    @staticmethod
    def SET_END_TIME(value: datetime | str) -> dict[str, str]:
        """End time of activity (datetime or ISO string)."""
        return {ACTIVITY_FIELD.END_TIME: value if isinstance(value, str) else value.isoformat()}

    @staticmethod
    def SET_DEADLINE(value: datetime | str) -> dict[str, str]:
        """Deadline for activity."""
        return {ACTIVITY_FIELD.DEADLINE: value if isinstance(value, str) else value.isoformat()}

    @staticmethod
    def SET_COMPLETED(value: bool) -> dict[str, str]:
        """Is activity completed ('Y' or 'N')."""
        return {ACTIVITY_FIELD.COMPLETED: 'Y' if value else 'N'}

    @staticmethod
    def SET_STATUS(value: int) -> dict[str, int]:
        """Activity status (crm_enum_activitystatus)."""
        return {ACTIVITY_FIELD.STATUS: int(value)}

    @staticmethod
    def SET_RESPONSIBLE_ID(value: int) -> dict[str, int]:
        """Responsible user ID."""
        return {ACTIVITY_FIELD.RESPONSIBLE_ID: int(value)}

    @staticmethod
    def SET_PRIORITY(value: int) -> dict[str, int]:
        """Activity priority (crm.enum.activitypriority)."""
        return {ACTIVITY_FIELD.PRIORITY: int(value)}

    @staticmethod
    def SET_NOTIFY_TYPE(value: int) -> dict[str, int]:
        """Notification type (crm.enum.activitynotifytype)."""
        return {ACTIVITY_FIELD.NOTIFY_TYPE: int(value)}

    @staticmethod
    def SET_NOTIFY_VALUE(value: int) -> dict[str, int]:
        """Notification value (minutes)."""
        return {ACTIVITY_FIELD.NOTIFY_VALUE: int(value)}

    @staticmethod
    def SET_DESCRIPTION(value: str) -> dict[str, str]:
        """Activity description."""
        return {ACTIVITY_FIELD.DESCRIPTION: str(value)}

    @staticmethod
    def SET_DESCRIPTION_TYPE(value: int) -> dict[str, int]:
        """Description type (crm.enum.contenttype)."""
        return {ACTIVITY_FIELD.DESCRIPTION_TYPE: int(value)}

    @staticmethod
    def SET_DIRECTION(value: int) -> dict[str, int]:
        """Activity direction (crm.enum.activitydirection)."""
        return {ACTIVITY_FIELD.DIRECTION: int(value)}

    @staticmethod
    def SET_LOCATION(value: str) -> dict[str, str]:
        """Activity location (for meetings)."""
        return {ACTIVITY_FIELD.LOCATION: str(value)}

    # @staticmethod
    # def SET_CREATED(value: datetime | str) -> dict[str, str]:
    #     """Creation date (read-only)."""
    #     return {ACTIVITY_FIELD.CREATED: value if isinstance(value, str) else value.isoformat()}

    @staticmethod
    def SET_AUTHOR_ID(value: int) -> dict[str, int]:
        """Creator of the activity."""
        return {ACTIVITY_FIELD.AUTHOR_ID: int(value)}

    # @staticmethod
    # def SET_LAST_UPDATED(value: datetime | str) -> dict[str, str]:
    #     """Last update date (read-only)."""
    #     return {ACTIVITY_FIELD.LAST_UPDATED: value if isinstance(value, str) else value.isoformat()}
	#
    # @staticmethod
    # def SET_EDITOR_ID(value: int) -> dict[str, int]:
    #     """Editor ID (read-only)."""
    #     return {ACTIVITY_FIELD.EDITOR_ID: int(value)}

    @staticmethod
    def SET_SETTINGS(value: dict) -> dict[str, dict]:
        """Activity settings."""
        return {ACTIVITY_FIELD.SETTINGS: value}

    @staticmethod
    def SET_ORIGIN_ID(value: str) -> dict[str, str]:
        """External source item ID."""
        return {ACTIVITY_FIELD.ORIGIN_ID: str(value)}

    @staticmethod
    def SET_ORIGINATOR_ID(value: str) -> dict[str, str]:
        """External system originator ID."""
        return {ACTIVITY_FIELD.ORIGINATOR_ID: str(value)}

    @staticmethod
    def SET_RESULT_STATUS(value: int) -> dict[str, int]:
        """Result status (compatibility field)."""
        return {ACTIVITY_FIELD.RESULT_STATUS: int(value)}

    @staticmethod
    def SET_RESULT_STREAM(value: int) -> dict[str, int]:
        """Result stream (report statistics)."""
        return {ACTIVITY_FIELD.RESULT_STREAM: int(value)}

    @staticmethod
    def SET_RESULT_SOURCE_ID(value: str) -> dict[str, str]:
        """Result source ID (compatibility)."""
        return {ACTIVITY_FIELD.RESULT_SOURCE_ID: str(value)}

    @staticmethod
    def SET_PROVIDER_PARAMS(value: dict) -> dict[str, dict]:
        """Provider parameters."""
        return {ACTIVITY_FIELD.PROVIDER_PARAMS: value}

    @staticmethod
    def SET_PROVIDER_DATA(value: str) -> dict[str, str]:
        """Provider data."""
        return {ACTIVITY_FIELD.PROVIDER_DATA: str(value)}

    @staticmethod
    def SET_RESULT_MARK(value: int) -> dict[str, int]:
        """Result mark (compatibility)."""
        return {ACTIVITY_FIELD.RESULT_MARK: int(value)}

    @staticmethod
    def SET_RESULT_VALUE(value: float) -> dict[str, float]:
        """Result value (compatibility)."""
        return {ACTIVITY_FIELD.RESULT_VALUE: float(value)}

    @staticmethod
    def SET_RESULT_SUM(value: float) -> dict[str, float]:
        """Result sum (compatibility)."""
        return {ACTIVITY_FIELD.RESULT_SUM: float(value)}

    @staticmethod
    def SET_RESULT_CURRENCY_ID(value: str) -> dict[str, str]:
        """Result currency ID (compatibility)."""
        return {ACTIVITY_FIELD.RESULT_CURRENCY_ID: str(value)}

    @staticmethod
    def SET_AUTOCOMPLETE_RULE(value: int) -> dict[str, int]:
        """Autocomplete rule."""
        return {ACTIVITY_FIELD.AUTOCOMPLETE_RULE: int(value)}

    # @staticmethod
    # def SET_BINDINGS(value: list[dict]) -> dict[str, list[dict]]:
    #     """Activity bindings (crm_activity_binding)."""
    #     return {ACTIVITY_FIELD.BINDINGS: value}

    @staticmethod
    def SET_COMMUNICATIONS(value: list[dict]) -> dict[str, list[dict]]:
        """Activity communications (crm_activity_communication)."""
        return {ACTIVITY_FIELD.COMMUNICATIONS: value}

    @staticmethod
    def SET_FILES(value: list[str]) -> dict[str, list[str]]:
        """Attached files (diskfile)."""
        return {ACTIVITY_FIELD.FILES: value}

    @staticmethod
    def SET_WEBDAV_ELEMENTS(value: list[str]) -> dict[str, list[str]]:
        """WebDAV elements (diskfile, deprecated)."""
        return {ACTIVITY_FIELD.WEBDAV_ELEMENTS: value}

    # @staticmethod
    # def SET_IS_INCOMING_CHANNEL(value: bool) -> dict[str, str]:
    #     """Is incoming channel ('Y' or 'N')."""
    #     return {ACTIVITY_FIELD.IS_INCOMING_CHANNEL: 'Y' if value else 'N'}
