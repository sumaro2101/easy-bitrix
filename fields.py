class ItemField:
    @property
    def ID(self) -> str:
        return 'ID'

    @property
    def ENTITY_TYPE_ID(self) -> str:
        return 'entityTypeId'

    @property
    def USE_ORIGINAL_UF_NAMES(self):
        return 'useOriginalUfNames'


class DealField:

    @property
    def ID(self) -> str:
        return 'ID'

    @property
    def TITLE(self) -> str:
        return 'TITLE'

    @property
    def TYPE_ID(self) -> str:
        return 'TYPE_ID'

    @property
    def CATEGORY_ID(self) -> str:
        return 'CATEGORY_ID'

    @property
    def STAGE_ID(self) -> str:
        return 'STAGE_ID'

    @property
    def IS_NEW(self) -> str:
        return 'IS_NEW'

    @property
    def COMPANY_ID(self):
        return 'COMPANY_ID'

    @property
    def IS_RECURRING(self) -> str:
        return 'IS_RECURRING'

    @property
    def OPPORTUNITY(self) -> str:
        return 'OPPORTUNITY'

    @property
    def IS_MANUAL_OPPORTUNITY(self) -> str:
        return 'IS_MANUAL_OPPORTUNITY'

    @property
    def IS_RETURN_CUSTOMER(self):
        return 'IS_RETURN_CUSTOMER'

    @property
    def CURRENCY_ID(self):
        return 'CURRENCY_ID'

    @property
    def ASSIGNED_BY_ID(self) -> str:
        return 'ASSIGNED_BY_ID'

    @property
    def CONTACT_IDS(self):
        return 'CONTACT_IDS'

    @property
    def QUOTE_ID(self):
        return 'QUOTE_ID'

    @property
    def COMMENTS(self):
        return 'COMMENTS'

    @property
    def DATE_CREATE(self) -> str:
        return 'DATE_CREATE'

    @property
    def DATE_MODIFY(self):
        return 'DATE_MODIFY'

    @property
    def MOVED_TIME(self):
        return 'MOVED_TIME'

    @property
    def OPENED(self):
        return 'OPENED'

    @property
    def IS_REPEATED_APPROACH(self) -> str:
        return 'IS_REPEATED_APPROACH'

    @property
    def PROBABILITY(self) -> str:
        return 'PROBABILITY'

    @property
    def TAX_VALUE(self) -> str:
        return 'TAX_VALUE'

    @property
    def BEGINDATE(self) -> str:
        return 'BEGINDATE'

    @property
    def CLOSEDATE(self) -> str:
        return 'CLOSEDATE'

    @property
    def CLOSED(self) -> str:
        return 'CLOSED'

    @property
    def CREATED_BY_ID(self):
        return 'CREATED_BY_ID'

    @property
    def MODIFY_BY_ID(self):
        return 'MODIFY_BY_ID'

    @property
    def MOVED_BY_ID(self):
        return 'MOVED_BY_ID'

    @property
    def ADDITIONAL_INFO(self) -> str:
        return 'ADDITIONAL_INFO'

    @property
    def LEAD_ID(self) -> str:
        return 'LEAD_ID'

    @property
    def LOCATION_ID(self) -> str:
        return 'LOCATION_ID'

    @property
    def SOURCE_ID(self):
        return 'SOURCE_ID'

    @property
    def SOURCE_DESCRIPTION(self):
        return 'SOURCE_DESCRIPTION'

    @property
    def ORIGINATOR_ID(self):
        return 'ORIGINATOR_ID'

    @property
    def ORIGIN_ID(self):
        return 'ORIGIN_ID'

    @property
    def UTM_SOURCE(self):
        return 'UTM_SOURCE'

    @property
    def UTM_MEDIUM(self):
        return 'UTM_MEDIUM'

    @property
    def UTM_CAMPAIGN(self):
        return 'UTM_CAMPAIGN'

    @property
    def UTM_CONTENT(self):
        return 'UTM_CONTENT'

    @property
    def UTM_TERM(self):
        return 'UTM_TERM'

    @property
    def LAST_ACTIVITY_BY(self):
        return 'LAST_ACTIVITY_BY'

    @property
    def LAST_ACTIVITY_TIME(self):
        return 'LAST_ACTIVITY_TIME'


class ContactField:

    @property
    def ID(self):
        return 'ID'

    @property
    def HONORIFIC(self):
        return 'HONORIFIC'

    @property
    def NAME(self):
        return 'NAME'

    @property
    def SECOND_NAME(self):
        return 'SECOND_NAME'

    @property
    def LAST_NAME(self):
        return 'LAST_NAME'

    @property
    def PHOTO(self):
        return 'PHOTO'

    @property
    def BIRTHDATE(self):
        return 'BIRTHDATE'

    @property
    def TYPE_ID(self):
        return 'TYPE_ID'

    @property
    def SOURCE_ID(self):
        return 'SOURCE_ID'

    @property
    def SOURCE_DESCRIPTION(self):
        return 'SOURCE_DESCRIPTION'

    @property
    def POST(self):
        return 'POST'

    @property
    def COMMENTS(self):
        return 'COMMENTS'

    @property
    def OPENED(self):
        return 'OPENED'

    @property
    def EXPORT(self):
        return 'EXPORT'

    @property
    def ASSIGNED_BY_ID(self):
        return 'ASSIGNED_BY_ID'

    @property
    def COMPANY_ID(self):
        return 'COMPANY_ID'

    @property
    def COMPANY_IDS(self):
        return 'COMPANY_IDS'

    @property
    def UTM_SOURCE(self):
        return 'UTM_SOURCE'

    @property
    def UTM_MEDIUM(self):
        return 'UTM_MEDIUM'

    @property
    def UTM_CAMPAIGN(self):
        return 'UTM_CAMPAIGN'

    @property
    def UTM_CONTENT(self):
        return 'UTM_CONTENT'

    @property
    def UTM_TERM(self):
        return 'UTM_TERM'

    @property
    def TRACE(self):
        return 'TRACE'

    @property
    def PHONE(self):
        return 'PHONE'

    @property
    def EMAIL(self):
        return 'EMAIL'

    @property
    def WEB(self):
        return 'WEB'

    @property
    def IM(self):
        return 'IM'

    @property
    def LINK(self):
        return 'LINK'


class LeadField:

    @property
    def ID(self):
        return 'ID'

    @property
    def TITLE(self):
        return 'TITLE'

    @property
    def HONORIFIC(self):
        return 'HONORIFIC'

    @property
    def NAME(self):
        return 'NAME'

    @property
    def SECOND_NAME(self):
        return 'SECOND_NAME'

    @property
    def LAST_NAME(self):
        return 'LAST_NAME'

    @property
    def BIRTHDATE(self):
        return 'BIRTHDATE'

    @property
    def COMPANY_TITLE(self):
        return 'COMPANY_TITLE'

    @property
    def SOURCE_ID(self):
        return 'SOURCE_ID'

    @property
    def SOURCE_DESCRIPTION(self):
        return 'SOURCE_DESCRIPTION'

    @property
    def STATUS_ID(self):
        return 'STATUS_ID'

    @property
    def STATUS_DESCRIPTION(self):
        return 'STATUS_DESCRIPTION'

    @property
    def STATUS_SEMANTIC_ID(self):
        return 'STATUS_SEMANTIC_ID'

    @property
    def POST(self):
        return 'POST'

    @property
    def ADDRESS(self):
        return 'ADDRESS'

    @property
    def ADDRESS_2(self):
        return 'ADDRESS_2'

    @property
    def ADDRESS_CITY(self):
        return 'ADDRESS_CITY'

    @property
    def ADDRESS_POSTAL_CODE(self):
        return 'ADDRESS_POSTAL_CODE'

    @property
    def ADDRESS_REGION(self):
        return 'ADDRESS_REGION'

    @property
    def ADDRESS_PROVINCE(self):
        return 'ADDRESS_PROVINCE'

    @property
    def ADDRESS_COUNTRY(self):
        return 'ADDRESS_COUNTRY'

    @property
    def ADDRESS_COUNTRY_CODE(self):
        return 'ADDRESS_COUNTRY_CODE'

    @property
    def ADDRESS_LOC_ADDR_ID(self):
        return 'ADDRESS_LOC_ADDR_ID'

    @property
    def CURRENCY_ID(self):
        return 'CURRENCY_ID'

    @property
    def OPPORTUNITY(self):
        return 'OPPORTUNITY'

    @property
    def IS_MANUAL_OPPORTUNITY(self):
        return 'IS_MANUAL_OPPORTUNITY'

    @property
    def OPENED(self):
        return 'OPENED'

    @property
    def COMMENTS(self):
        return 'COMMENTS'

    @property
    def HAS_PHONE(self):
        return 'HAS_PHONE'

    @property
    def HAS_EMAIL(self):
        return 'HAS_EMAIL'

    @property
    def HAS_IMOL(self):
        return 'HAS_IMOL'

    @property
    def ASSIGNED_BY_ID(self):
        return 'ASSIGNED_BY_ID'

    @property
    def CREATED_BY_ID(self):
        return 'CREATED_BY_ID'

    @property
    def MODIFY_BY_ID(self):
        return 'MODIFY_BY_ID'

    @property
    def MOVED_BY_ID(self):
        return 'MOVED_BY_ID'

    @property
    def DATE_CREATE(self):
        return 'DATE_CREATE'

    @property
    def DATE_MODIFY(self):
        return 'DATE_MODIFY'

    @property
    def MOVED_TIME(self):
        return 'MOVED_TIME'

    @property
    def COMPANY_ID(self):
        return 'COMPANY_ID'

    @property
    def CONTACT_ID(self):
        return 'CONTACT_ID'

    @property
    def CONTACT_IDS(self):
        return 'CONTACT_IDS'

    @property
    def IS_RETURN_CUSTOMER(self):
        return 'IS_RETURN_CUSTOMER'

    @property
    def DATE_CLOSED(self):
        return 'DATE_CLOSED'

    @property
    def ORIGINATOR_ID(self):
        return 'ORIGINATOR_ID'

    @property
    def ORIGIN_ID(self):
        return 'ORIGIN_ID'

    @property
    def UTM_SOURCE(self):
        return 'UTM_SOURCE'

    @property
    def UTM_MEDIUM(self):
        return 'UTM_MEDIUM'

    @property
    def UTM_CAMPAIGN(self):
        return 'UTM_CAMPAIGN'

    @property
    def UTM_CONTENT(self):
        return 'UTM_CONTENT'

    @property
    def UTM_TERM(self):
        return 'UTM_TERM'

    @property
    def LAST_ACTIVITY_TIME(self):
        return 'LAST_ACTIVITY_TIME'

    @property
    def LAST_ACTIVITY_BY(self):
        return 'LAST_ACTIVITY_BY'

    @property
    def PHONE(self):
        return 'PHONE'

    @property
    def EMAIL(self):
        return 'EMAIL'

    @property
    def WEB(self):
        return 'WEB'

    @property
    def IM(self):
        return 'IM'

    @property
    def LINK(self):
        return 'LINK'


class CompanyField:

    @property
    def ID(self):
        return 'ID'

    @property
    def TITLE(self):
        return 'TITLE'

    @property
    def COMPANY_TYPE(self):
        return 'COMPANY_TYPE'

    @property
    def LOGO(self):
        return 'LOGO'

    @property
    def ADDRESS(self):
        return 'ADDRESS'

    @property
    def ADDRESS_2(self):
        return 'ADDRESS_2'

    @property
    def ADDRESS_CITY(self):
        return 'ADDRESS_CITY'

    @property
    def ADDRESS_POSTAL_CODE(self):
        return 'ADDRESS_POSTAL_CODE'

    @property
    def ADDRESS_REGION(self):
        return 'ADDRESS_REGION'

    @property
    def ADDRESS_PROVINCE(self):
        return 'ADDRESS_PROVINCE'

    @property
    def ADDRESS_COUNTRY(self):
        return 'ADDRESS_COUNTRY'

    @property
    def ADDRESS_COUNTRY_CODE(self):
        return 'ADDRESS_COUNTRY_CODE'

    @property
    def ADDRESS_LOC_ADDR_ID(self):
        return 'ADDRESS_LOC_ADDR_ID'

    @property
    def ADDRESS_LEGAL(self):
        return 'ADDRESS_LEGAL'

    @property
    def REG_ADDRESS(self):
        return 'REG_ADDRESS'

    @property
    def REG_ADDRESS_2(self):
        return 'REG_ADDRESS_2'

    @property
    def REG_ADDRESS_CITY(self):
        return 'REG_ADDRESS_CITY'

    @property
    def REG_ADDRESS_POSTAL_CODE(self):
        return 'REG_ADDRESS_POSTAL_CODE'

    @property
    def REG_ADDRESS_REGION(self):
        return 'REG_ADDRESS_REGION'

    @property
    def REG_ADDRESS_PROVINCE(self):
        return 'REG_ADDRESS_PROVINCE'

    @property
    def REG_ADDRESS_COUNTRY(self):
        return 'REG_ADDRESS_COUNTRY'

    @property
    def REG_ADDRESS_COUNTRY_CODE(self):
        return 'REG_ADDRESS_COUNTRY_CODE'

    @property
    def REG_ADDRESS_LOC_ADDR_ID(self):
        return 'REG_ADDRESS_LOC_ADDR_ID'

    @property
    def BANKING_DETAILS(self):
        return 'BANKING_DETAILS'

    @property
    def INDUSTRY(self):
        return 'INDUSTRY'

    @property
    def EMPLOYEES(self):
        return 'EMPLOYEES'

    @property
    def CURRENCY_ID(self):
        return 'CURRENCY_ID'

    @property
    def REVENUE(self):
        return 'REVENUE'

    @property
    def OPENED(self):
        return 'OPENED'

    @property
    def COMMENTS(self):
        return 'COMMENTS'

    @property
    def HAS_PHONE(self):
        return 'HAS_PHONE'

    @property
    def HAS_EMAIL(self):
        return 'HAS_EMAIL'

    @property
    def HAS_IMOL(self):
        return 'HAS_IMOL'

    @property
    def IS_MY_COMPANY(self):
        return 'IS_MY_COMPANY'

    @property
    def ASSIGNED_BY_ID(self):
        return 'ASSIGNED_BY_ID'

    @property
    def CREATED_BY_ID(self):
        return 'CREATED_BY_ID'

    @property
    def MODIFY_BY_ID(self):
        return 'MODIFY_BY_ID'

    @property
    def DATE_CREATE(self):
        return 'DATE_CREATE'

    @property
    def DATE_MODIFY(self):
        return 'DATE_MODIFY'

    @property
    def CONTACT_ID(self):
        return 'CONTACT_ID'

    @property
    def LEAD_ID(self):
        return 'LEAD_ID'

    @property
    def ORIGINATOR_ID(self):
        return 'ORIGINATOR_ID'

    @property
    def ORIGIN_ID(self):
        return 'ORIGIN_ID'

    @property
    def ORIGIN_VERSION(self):
        return 'ORIGIN_VERSION'

    @property
    def UTM_SOURCE(self):
        return 'UTM_SOURCE'

    @property
    def UTM_MEDIUM(self):
        return 'UTM_MEDIUM'

    @property
    def UTM_CAMPAIGN(self):
        return 'UTM_CAMPAIGN'

    @property
    def UTM_CONTENT(self):
        return 'UTM_CONTENT'

    @property
    def UTM_TERM(self):
        return 'UTM_TERM'

    @property
    def PARENT_ID(self):
        return 'PARENT_ID'

    @property
    def LAST_ACTIVITY_TIME(self):
        return 'LAST_ACTIVITY_TIME'

    @property
    def LAST_ACTIVITY_BY(self):
        return 'LAST_ACTIVITY_BY'

    @property
    def PHONE(self):
        return 'PHONE'

    @property
    def EMAIL(self):
        return 'EMAIL'

    @property
    def WEB(self):
        return 'WEB'

    @property
    def IM(self):
        return 'IM'

    @property
    def LINK(self):
        return 'LINK'


class RequisiteField:

    @property
    def ID(self):
        return 'ID'

    @property
    def ENTITY_TYPE_ID(self):
        return 'ENTITY_TYPE_ID'

    @property
    def ENTITY_ID(self):
        return 'ENTITY_ID'

    @property
    def PRESET_ID(self):
        return 'PRESET_ID'

    @property
    def DATE_CREATE(self):
        return 'DATE_CREATE'

    @property
    def DATE_MODIFY(self):
        return 'DATE_MODIFY'

    @property
    def CREATED_BY_ID(self):
        return 'CREATED_BY_ID'

    @property
    def MODIFY_BY_ID(self):
        return 'MODIFY_BY_ID'

    @property
    def NAME(self):
        return 'NAME'

    @property
    def CODE(self):
        return 'CODE'

    @property
    def XML_ID(self):
        return 'XML_ID'

    @property
    def ORIGINATOR_ID(self):
        return 'ORIGINATOR_ID'

    @property
    def ACTIVE(self):
        return 'ACTIVE'

    @property
    def ADDRESS_ONLY(self):
        return 'ADDRESS_ONLY'

    @property
    def SORT(self):
        return 'SORT'

    @property
    def RQ_NAME(self):
        return 'RQ_NAME'

    @property
    def RQ_FIRST_NAME(self):
        return 'RQ_FIRST_NAME'

    @property
    def RQ_LAST_NAME(self):
        return 'RQ_LAST_NAME'

    @property
    def RQ_SECOND_NAME(self):
        return 'RQ_SECOND_NAME'

    @property
    def RQ_COMPANY_ID(self):
        return 'RQ_COMPANY_ID'

    @property
    def RQ_COMPANY_NAME(self):
        return 'RQ_COMPANY_NAME'

    @property
    def RQ_COMPANY_FULL_NAME(self):
        return 'RQ_COMPANY_FULL_NAME'

    @property
    def RQ_COMPANY_REG_DATE(self):
        return 'RQ_COMPANY_REG_DATE'

    @property
    def RQ_DIRECTOR(self):
        return 'RQ_DIRECTOR'

    @property
    def RQ_ACCOUNTANT(self):
        return 'RQ_ACCOUNTANT'

    @property
    def RQ_CEO_NAME(self):
        return 'RQ_CEO_NAME'

    @property
    def RQ_CEO_WORK_POS(self):
        return 'RQ_CEO_WORK_POS'

    @property
    def RQ_CONTACT(self):
        return 'RQ_CONTACT'

    @property
    def RQ_EMAIL(self):
        return 'RQ_EMAIL'

    @property
    def RQ_PHONE(self):
        return 'RQ_PHONE'

    @property
    def RQ_FAX(self):
        return 'RQ_FAX'

    @property
    def RQ_IDENT_TYPE(self):
        return 'RQ_IDENT_TYPE'

    @property
    def RQ_IDENT_DOC(self):
        return 'RQ_IDENT_DOC'

    @property
    def RQ_IDENT_DOC_SER(self):
        return 'RQ_IDENT_DOC_SER'

    @property
    def RQ_IDENT_DOC_NUM(self):
        return 'RQ_IDENT_DOC_NUM'

    @property
    def RQ_IDENT_DOC_PERS_NUM(self):
        return 'RQ_IDENT_DOC_PERS_NUM'

    @property
    def RQ_IDENT_DOC_DATE(self):
        return 'RQ_IDENT_DOC_DATE'

    @property
    def RQ_IDENT_DOC_ISSUED_BY(self):
        return 'RQ_IDENT_DOC_ISSUED_BY'

    @property
    def RQ_IDENT_DOC_DEP_CODE(self):
        return 'RQ_IDENT_DOC_DEP_CODE'

    @property
    def RQ_INN(self):
        return 'RQ_INN'

    @property
    def RQ_KPP(self):
        return 'RQ_KPP'

    @property
    def RQ_USRLE(self):
        return 'RQ_USRLE'

    @property
    def RQ_IFNS(self):
        return 'RQ_IFNS'

    @property
    def RQ_OGRN(self):
        return 'RQ_OGRN'

    @property
    def RQ_OGRNIP(self):
        return 'RQ_OGRNIP'

    @property
    def RQ_OKPO(self):
        return 'RQ_OKPO'

    @property
    def RQ_OKTMO(self):
        return 'RQ_OKTMO'

    @property
    def RQ_OKVED(self):
        return 'RQ_OKVED'

    @property
    def RQ_EDRPOU(self):
        return 'RQ_EDRPOU'

    @property
    def RQ_DRFO(self):
        return 'RQ_DRFO'

    @property
    def RQ_KBE(self):
        return 'RQ_KBE'

    @property
    def RQ_IIN(self):
        return 'RQ_IIN'

    @property
    def RQ_BIN(self):
        return 'RQ_BIN'

    @property
    def RQ_ST_CERT_SER(self):
        return 'RQ_ST_CERT_SER'

    @property
    def RQ_ST_CERT_NUM(self):
        return 'RQ_ST_CERT_NUM'

    @property
    def RQ_ST_CERT_DATE(self):
        return 'RQ_ST_CERT_DATE'

    @property
    def RQ_VAT_PAYER(self):
        return 'RQ_VAT_PAYER'

    @property
    def RQ_VAT_ID(self):
        return 'RQ_VAT_ID'

    @property
    def RQ_VAT_CERT_SER(self):
        return 'RQ_VAT_CERT_SER'

    @property
    def RQ_VAT_CERT_NUM(self):
        return 'RQ_VAT_CERT_NUM'

    @property
    def RQ_VAT_CERT_DATE(self):
        return 'RQ_VAT_CERT_DATE'

    @property
    def RQ_RESIDENCE_COUNTRY(self):
        return 'RQ_RESIDENCE_COUNTRY'

    @property
    def RQ_BASE_DOC(self):
        return 'RQ_BASE_DOC'

    @property
    def RQ_REGON(self):
        return 'RQ_REGON'

    @property
    def RQ_KRS(self):
        return 'RQ_KRS'

    @property
    def RQ_PESEL(self):
        return 'RQ_PESEL'

    @property
    def RQ_LEGAL_FORM(self):
        return 'RQ_LEGAL_FORM'

    @property
    def RQ_SIRET(self):
        return 'RQ_SIRET'

    @property
    def RQ_SIREN(self):
        return 'RQ_SIREN'

    @property
    def RQ_CAPITAL(self):
        return 'RQ_CAPITAL'

    @property
    def RQ_RCS(self):
        return 'RQ_RCS'

    @property
    def RQ_CNPJ(self):
        return 'RQ_CNPJ'

    @property
    def RQ_STATE_REG(self):
        return 'RQ_STATE_REG'

    @property
    def RQ_MNPL_REG(self):
        return 'RQ_MNPL_REG'

    @property
    def RQ_CPF(self):
        return 'RQ_CPF'

    @property
    def UF_CRM(self):
        return 'UF_CRM_...'


class ActivityField:

    @property
    def ID(self):
        return 'ID'

    @property
    def OWNER_ID(self):
        return 'OWNER_ID'

    @property
    def OWNER_TYPE_ID(self):
        return 'OWNER_TYPE_ID'

    @property
    def TYPE_ID(self):
        return 'TYPE_ID'

    @property
    def PROVIDER_ID(self):
        return 'PROVIDER_ID'

    @property
    def PROVIDER_TYPE_ID(self):
        return 'PROVIDER_TYPE_ID'

    @property
    def PROVIDER_GROUP_ID(self):
        return 'PROVIDER_GROUP_ID'

    @property
    def ASSOCIATED_ENTITY_ID(self):
        return 'ASSOCIATED_ENTITY_ID'

    @property
    def SUBJECT(self):
        return 'SUBJECT'

    @property
    def START_TIME(self):
        return 'START_TIME'

    @property
    def END_TIME(self):
        return 'END_TIME'

    @property
    def DEADLINE(self):
        return 'DEADLINE'

    @property
    def COMPLETED(self):
        return 'COMPLETED'

    @property
    def STATUS(self):
        return 'STATUS'

    @property
    def RESPONSIBLE_ID(self):
        return 'RESPONSIBLE_ID'

    @property
    def PRIORITY(self):
        return 'PRIORITY'

    @property
    def NOTIFY_TYPE(self):
        return 'NOTIFY_TYPE'

    @property
    def NOTIFY_VALUE(self):
        return 'NOTIFY_VALUE'

    @property
    def DESCRIPTION(self):
        return 'DESCRIPTION'

    @property
    def DESCRIPTION_TYPE(self):
        return 'DESCRIPTION_TYPE'

    @property
    def DIRECTION(self):
        return 'DIRECTION'

    @property
    def LOCATION(self):
        return 'LOCATION'

    @property
    def CREATED(self):
        return 'CREATED'

    @property
    def AUTHOR_ID(self):
        return 'AUTHOR_ID'

    @property
    def LAST_UPDATED(self):
        return 'LAST_UPDATED'

    @property
    def EDITOR_ID(self):
        return 'EDITOR_ID'

    @property
    def SETTINGS(self):
        return 'SETTINGS'

    @property
    def ORIGIN_ID(self):
        return 'ORIGIN_ID'

    @property
    def ORIGINATOR_ID(self):
        return 'ORIGINATOR_ID'

    @property
    def RESULT_STATUS(self):
        return 'RESULT_STATUS'

    @property
    def RESULT_STREAM(self):
        return 'RESULT_STREAM'

    @property
    def RESULT_SOURCE_ID(self):
        return 'RESULT_SOURCE_ID'

    @property
    def PROVIDER_PARAMS(self):
        return 'PROVIDER_PARAMS'

    @property
    def PROVIDER_DATA(self):
        return 'PROVIDER_DATA'

    @property
    def RESULT_MARK(self):
        return 'RESULT_MARK'

    @property
    def RESULT_VALUE(self):
        return 'RESULT_VALUE'

    @property
    def RESULT_SUM(self):
        return 'RESULT_SUM'

    @property
    def RESULT_CURRENCY_ID(self):
        return 'RESULT_CURRENCY_ID'

    @property
    def AUTOCOMPLETE_RULE(self):
        return 'AUTOCOMPLETE_RULE'

    @property
    def BINDINGS(self):
        return 'BINDINGS'

    @property
    def COMMUNICATIONS(self):
        return 'COMMUNICATIONS'

    @property
    def FILES(self):
        return 'FILES'

    @property
    def WEBDAV_ELEMENTS(self):
        return 'WEBDAV_ELEMENTS'

    @property
    def IS_INCOMING_CHANNEL(self):
        return 'IS_INCOMING_CHANNEL'


DEAL_FIELD = DealField()
LEAD_FIELD = LeadField()
CONTACT_FIELD = ContactField()
ITEM_FIELD = ItemField()
COMPANY_FIELD = CompanyField()
REQUISITE_FIELD = RequisiteField()
ACTIVITY_FIELD = ActivityField()
