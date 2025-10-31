import json
from collections.abc import Sequence


class BitrixResponse(Sequence):
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
                self.data = self.data['result']

    def add_data(self, raw_data: str):
        data = json.loads(raw_data)
        self.next: int | None = data.get('next')
        if 'error' in data:
            self.error = data.get('error')
        else:
            if 'result' in data:
                has_items = self.data.get('items')
                if data['result'].get('items'):
                    if has_items:
                        self.data['items'].extend(data['result']['items'])
                    else:
                        self.data.extend(data['result']['items'])
                else:
                    if has_items:
                        self.data['items'].extend(data['result'])
                    else:
                        self.data.extend(data['result'])
                data['result'] = self.data
                data['time'] = self.time
                self.raw_data = json.dumps(data)

    def __iter__(self):
        if self.data.get('items'):
            return iter(self.data['items'])
        elif self.data.get('item'):
            return iter([self.data['item']])
        return iter(self.data)

    def __getitem__(self, key):
        if self.data.get('items'):
            return self.data['items'][key]
        elif self.data.get('item'):
            return self.data['item']
        return self.data[key]

    def __len__(self):
        if self.data.get('items'):
            return len(self.data['items'])
        return len(self.data)
