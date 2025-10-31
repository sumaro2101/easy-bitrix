import json


class BitrixResponse:
    code: int
    raw_data: str
    data: object

    def __init__(self, code: int, raw_data: str):
        self.code = code
        self.raw_data = raw_data
        self.data = json.loads(raw_data)
        self.error = None
        self.time: dict | None = None
        self.total: int = 0
        self.next: int | None = self.data.get('next')
        if 'error' in self.data:
            self.error = self.data.get('error')
        else:
            if 'result' in self.data:
                self.total = self.data.get('total')
                self.time = self.data.get('time')

    def add_data(self, raw_data: str):
        data = json.loads(raw_data)
        print(self.data)
        self.next: int | None = self.data.get('next')
        if 'error' in data:
            self.error = data.get('error')
        else:
            if 'result' in data:
                if data.get('items'):
                    self.data['result']['items'].extend(data['result']['items'])
                else:
                    self.data['result']['items'].extend(data['result'])
                data['result'] = self.data
                data['time'] = self.time
                self.raw_data = json.dumps(data)
