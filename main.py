import json
import asyncio

from .bitrix import Bitrix24
from .options import RequestOptions
from .data_builder import CRMDataExecutor
from .parameters import Select, Filter, Deal
from .fields import DealField
from .filter_operations import Operation

site_name = 'b24-cn03c9'
user_id = '1'
webhook = 'z1jphbxwrvl7suc3'


async def main():
    options = RequestOptions(user_id=user_id, webhook_url=webhook, high_level_domain='ru')
    bitrix = Bitrix24(site_name)
    data = CRMDataExecutor('deal').list(
        Select(DealField.ID, DealField.DATE_CREATE, DealField.TITLE),
        Filter(Operation.EQ(Deal.OPPORTUNITY(25000.00)),
               Operation.EQ(Deal.TITLE('deal')),
               ),
        )
    result, status = await bitrix.request_async(param=data, options=options)
    print(f'Status is: {status}\n\n\nResponse is: {json.loads(result)}')

asyncio.run(main())
