from common import FilterOperations, LogicErrors

from exeptions import FilterParameterError


class Operation[T: dict[str, str]]:

    @staticmethod
    def LTE(param: T) -> T:
        return _base_operation(param, FilterOperations.LTE)

    @staticmethod
    def EQ(param: T) -> T:
        return _base_operation(param, FilterOperations.EQ)

    @staticmethod
    def NEQ(param: T) -> T:
        return _base_operation(param, FilterOperations.NEQ)

    @staticmethod
    def GT(param: T) -> T:
        return _base_operation(param, FilterOperations.GT)

    @staticmethod
    def GTE(param: T) -> T:
        return _base_operation(param, FilterOperations.GTE)

    @staticmethod
    def LT(param: T) -> T:
        return _base_operation(param, FilterOperations.LT)

    @staticmethod
    def IN(param: T) -> T:
        return _contains_operation(param, FilterOperations.IN)

    @staticmethod
    def NOT_IN(param: T) -> T:
        return _contains_operation(param, FilterOperations.NOT_IN)

    @staticmethod
    def LIKE(param: T) -> T:
        return _like_operation(param, FilterOperations.LIKE)

    @staticmethod
    def START_LIKE(param: T) -> T:
        return _like_operation(param, FilterOperations.START_LIKE)

    @staticmethod
    def END_LIKE(param: T) -> T:
        return _like_operation(param, FilterOperations.END_LIKE)


def _like_operation[T: dict[str, str]](param: T,
                                       opetator: str,
                                       like_op: str = FilterOperations.LIKE_OP,
                                       ) -> T:
    key, value = next(iter(param.items()))
    new_key = like_op.format(key)
    new_value = opetator.format(value)
    return {new_key: new_value}


def _contains_operation[T: dict[str, str]](param: T,
                                           opetator: str,
                                           ) -> T:
    key, value = next(iter(param.items()))
    new_key = opetator.format(key)
    try:
        new_value = list(value)
    except TypeError:
        raise FilterParameterError(LogicErrors.FILTER_PARAMETER_ERROR.value)
    return {new_key: new_value}


def _base_operation[T: dict[str, str]](param: T, opetator: str) -> T:
    key, value = next(iter(param.items()))
    new_key = opetator.format(key)
    return {new_key: value}
