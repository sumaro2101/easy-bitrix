# easy-bitrix

**easy-bitrix** is a universal Python library for working with the Bitrix24 REST API. It supports asynchronous requests, OAuth authentication, convenient CRM object management, and Pythonic query building for Bitrix24.

## Features

- Asynchronous and synchronous requests to Bitrix24 REST API
- OAuth authentication support
- Convenient classes for CRM entities: Deal, Contact, and more
- Flexible filtering, selection, and ordering
- Easy integration and extension for your projects

## Installation

```bash
pip install easy-bitrix
```

## Quick Start

### Get a list of deals

Example from `main.py`:

```python
from easy_bitrix.bitrix import Bitrix24
from easy_bitrix.options import RequestOptions
from easy_bitrix.bitrix_objects import Deal
from easy_bitrix.operations import FilterOperation, OrderOperations

site_name = 'bitrix_portal'
user_id = '1'
webhook = 'webhook'

def main():
    options = RequestOptions(user_id=user_id, webhook_url=webhook, high_level_domain='ru')
    bitrix = Bitrix24(bitrix_address=site_name)
    response = bitrix.request(param=Deal.get_list(
        select=[Deal.ID, Deal.TITLE, Deal.DATE_CREATE],
        filter=[FilterOperation.END_LIKE(Deal.SET_TITLE('_like'))],
        order=[OrderOperations.DESCENDING_ORDER(Deal.DATE_CREATE)],
    ), options=options)
    print(f'Status is: {response.code}\nResponse is: {response.data}")

main()
```

### Asynchronous requests

```python
import asyncio
from easy_bitrix.bitrix import Bitrix24
from easy_bitrix.options import RequestOptions
from easy_bitrix.bitrix_objects import Deal

async def main():
    options = RequestOptions(user_id='1', webhook_url='webhook', high_level_domain='ru')
    bitrix = Bitrix24('bitrix_portal')
    data = Deal.create(fields=[
        Deal.SET_TITLE('New Deal'),
        Deal.SET_OPPORTUNITY(10000),
        Deal.SET_TYPE_ID('SALE'),
        Deal.SET_STAGE_ID('NEW')
    ])
    result, status = await bitrix.request_async(param=data, options=options)
    print(f'Status: {status}\nResponse: {result}')

asyncio.run(main())
```

### OAuth authentication

```python
from easy_bitrix.oauth import OAuth

assess_token = OAuth.get_access_token(
    client_id=client_id,
    client_secret=client_secret,
    code=code,
)
print(assess_token)
```

## Main Classes

- `Bitrix24` — main class for API interaction
- `Deal`, `Contact` — classes for CRM objects
- `RequestOptions` — connection parameters
- `FilterOperation`, `OrderOperations` — filtering and ordering operations

## Documentation

- [Bitrix24 REST API](https://apidocs.bitrix24.com/)
- [Usage examples](#quick-start)

## License

MIT License

Copyright (c) 2024 Alex Pavlov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
