import json


class BitrixResponse:
    code: int
    body: str
    data: object

    def __init__(self, code: int, body: str):
        self.code = code
        self.body = body
        self.data = json.loads(body)
        self.error = None
        self.time: dict | None = None
        self.total: int = 0
        if 'error' in self.data:
            self.error = self.data.get('error')
        else:
            self.total = self.data['total']
            self.time = self.data['time']
            self.data = self.data['result']
