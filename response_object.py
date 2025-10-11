import json

from collections import OrderedDict


class BitrixResponse:
    code: int
    body: str
    data: object

    def __init__(self, code: int, body: str):
        self.code = code
        self.body = body
        self.data = json.loads(body, object_pairs_hook=OrderedDict)
