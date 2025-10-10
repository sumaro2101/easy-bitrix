from .common import FilterTo, LogicErrors, OrderTo
from .error import FilterParameterError


class FilterOperation[T: dict[str, str]]:
    """
    The Operation class provides convenient static methods for setting up
    filters for any parameter in Bitrix24.

    Each method corresponds to a specific filter operation (e.g., EQ, NEQ,
    GT, LIKE, IN) and returns a properly formatted dictionary for use in
    Bitrix24 API queries.

    This class simplifies the process of building complex filter expressions
    and ensures type safety and consistency across your codebase.
    """
    @staticmethod
    def LTE(param: T) -> T:
        return _base_operation(param, FilterTo.LTE)

    @staticmethod
    def EQ(param: T) -> T:
        return _base_operation(param, FilterTo.EQ)

    @staticmethod
    def NEQ(param: T) -> T:
        return _base_operation(param, FilterTo.NEQ)

    @staticmethod
    def GT(param: T) -> T:
        return _base_operation(param, FilterTo.GT)

    @staticmethod
    def GTE(param: T) -> T:
        return _base_operation(param, FilterTo.GTE)

    @staticmethod
    def LT(param: T) -> T:
        return _base_operation(param, FilterTo.LT)

    @staticmethod
    def IN(param: T) -> T:
        return _contains_operation(param, FilterTo.IN)

    @staticmethod
    def NOT_IN(param: T) -> T:
        return _contains_operation(param, FilterTo.NOT_IN)

    @staticmethod
    def LIKE(param: T) -> T:
        return _like_operation(param, FilterTo.LIKE)

    @staticmethod
    def START_LIKE(param: T) -> T:
        return _like_operation(param, FilterTo.START_LIKE)

    @staticmethod
    def END_LIKE(param: T) -> T:
        return _like_operation(param, FilterTo.END_LIKE)


class OrderOperations:
    """
    """
    @staticmethod
    def ASCENDING_ORDER(key: str) -> dict[str, str]:
        return {key: OrderTo.ASCENDING_ORDER.value}

    @staticmethod
    def DESCENDING_ORDER(key: str) -> dict[str, str]:
        return {key: OrderTo.DESCENDING_ORDER.value}


def _like_operation[T: dict[str, str]](param: T,
                                       opetator: str,
                                       like_op: str = FilterTo.LIKE_OP,
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
    if not isinstance(value, (list, tuple, set)):
        raise FilterParameterError(LogicErrors.FILTER_PARAMETER_ERROR.value)
    new_value = list(value)
    return {new_key: new_value}


def _base_operation[T: dict[str, str]](param: T, opetator: str) -> T:
    key, value = next(iter(param.items()))
    new_key = opetator.format(key)
    return {new_key: value}
