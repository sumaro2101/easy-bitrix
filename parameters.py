from common import ProductFields


class Parameter:
    """
    """
    @staticmethod
    def ID(value: int) -> str:
        return f'{ProductFields.ID.value}:{str(value)}'

    @staticmethod
    def TITLE(value: str) -> str:
        return f'{ProductFields.TITLE.value}:"{str(value)}"'

    @staticmethod
    def TYPE_ID(value: int) -> str:
        return f'{ProductFields.TYPE_ID.value}:{str(value)}'

    @staticmethod
    def CATEGORY_ID(value: int) -> str:
        return f'{ProductFields.CATEGORY_ID.value}:{str(value)}'

    @staticmethod
    def STAGE_ID(value: str) -> str:
        return f'{ProductFields.STAGE_ID.value}:"{str(value)}"'

    @staticmethod
    def OPPORTUNITY(value: float) -> str:
        return f'{ProductFields.OPPORTUNITY.value}:{str(value)}'

    @staticmethod
    def IS_MANUAL_OPPORTUNITY(value: bool) -> str:
        return f'{ProductFields.IS_MANUAL_OPPORTUNITY.value}:{str(int(value))}'

    @staticmethod
    def ASSIGNED_BY_ID(value: int) -> str:
        return f'{ProductFields.ASSIGNED_BY_ID.value}:{str(value)}'

    @staticmethod
    def DATE_CREATE(value: str) -> str:
        return f'{ProductFields.DATE_CREATE.value}:"{str(value)}"'


class BussParameters:
    """
    """
    def __init__(self, *parameters: str):
        self.parameters = parameters

    def _compile_parameters(self):
        urls_params = ''
        for param in self.parameters:
            urls_params += f'{param}&'
        return urls_params

    def get_parameters(self):
        return self._compile_parameters()
