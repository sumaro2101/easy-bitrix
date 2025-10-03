from common import FilterOperations


class Operation[T: dict[str, str]]:

    @staticmethod
    def LTE(param: T) -> T:
        return _operation(param, FilterOperations.LTE)

    @staticmethod
    def EQ(param: T) -> T:
        return _operation(param, FilterOperations.EQ)

    @staticmethod
    def NEQ(param: T) -> T:
        return _operation(param, FilterOperations.NEQ)

    @staticmethod
    def GT(param: T) -> T:
        return _operation(param, FilterOperations.GT)

    @staticmethod
    def GTE(param: T) -> T:
        return _operation(param, FilterOperations.GTE)

    @staticmethod
    def LT(param: T) -> T:
        return _operation(param, FilterOperations.LT)

    @staticmethod
    def LIKE(param: T) -> T:
        return _operation(param, FilterOperations.LIKE)

    @staticmethod
    def IN(param: T) -> T:
        return _operation(param, FilterOperations.IN)


def _operation[T: dict[str, str]](param: T, opetator: str) -> T:
    key, value = next(iter(param.items()))
    new_key = opetator.format(key)
    return {new_key: value}
