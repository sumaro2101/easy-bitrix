
class Parameter:
    """
    """
    @staticmethod
    def ID(value: int) -> str:
        return '"ID":{}'.format(str(value))

    @staticmethod
    def TITLE(value: str) -> str:
        return '"TITLE":{}'.format(str(value))


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
