from common import FilterOperations


class Operation[T: dict[str, str]]:

    @staticmethod
    def LTE(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}

    @staticmethod
    def EQ(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}

    @staticmethod
    def NEQ(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}

    @staticmethod
    def GT(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}

    @staticmethod
    def GTE(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}

    @staticmethod
    def LT(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}

    @staticmethod
    def LIKE(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}

    @staticmethod
    def IN(param: dict[str, str]) -> dict[str, str]:
        key, value = next(iter(param.items()))
        new_key = FilterOperations.LTE.format(key)
        return {new_key: value}
