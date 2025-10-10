from unittest import TestCase

from .parameters import Fields, Filter, Select
from .bitrix_objects import Deal
from .fields import DEAL_FIELD
from .filter_operations import Operation
from .error import FilterParameterError
from .data_builder import CRMDataExecutor
from .common import BitrixCRMTypes


class TestParameters(TestCase):

    def test_parameter(self):
        param = Deal.ID(42)
        self.assertEqual(param, {'ID': 42})

    def test_buss_param(self):
        param1 = Deal.ID(42)
        param2 = Deal.TITLE('Test')
        buss = Fields(param1, param2)
        self.assertEqual(buss.compare, {'ID': 42, 'TITLE': 'Test'})

    def test_operations(self):
        ready_param = Operation.END_LIKE(Deal.TITLE('Tes'))
        self.assertEqual(ready_param, {'%=TITLE': '%Tes'})

    def test_containce_operations(self):
        ready_param = Operation.IN(Deal.ASSIGNED_BY_ID([1, 6]))
        self.assertEqual(ready_param, {'@ASSIGNED_BY_ID': [1, 6]})

    def test_containce_operations_wrong(self):
        with self.assertRaises(FilterParameterError):
            ready_param = Operation.IN(Deal.ASSIGNED_BY_ID('1'))

    def test_filter(self):
        _filter = Filter(Operation.EQ(Deal.TITLE('Test')),
                         Operation.GTE(Deal.OPPORTUNITY(1000.00)),
                         Operation.NOT_IN(Deal.CATEGORY_ID([20, 1, 3])),
                         Deal.CATEGORY_ID(10),
                         )
        self.assertEqual(_filter.compare, {'=TITLE': 'Test', '>=OPPORTUNITY': 1000.00,
                                           "!@CATEGORY_ID": [20, 1, 3], 'CATEGORY_ID': 10})

    def test_select(self):
        select = Select(DEAL_FIELD.ASSIGNED_BY_ID, DEAL_FIELD.ID)
        self.assertEqual(select.compare, ['ASSIGNED_BY_ID', 'ID'])

    def test_data_builer_get(self):
        data = CRMDataExecutor(BitrixCRMTypes.DEAL.value).get(30)
        self.assertEqual(data.method, 'crm.deal.get')
        self.assertEqual(data.id, {'ID': 30})

    def test_data_builder_list(self):
        select = Select(DEAL_FIELD.ID, DEAL_FIELD.TITLE, DEAL_FIELD.DATE_CREATE)
        _filter = Filter(Operation.LTE(Deal.OPPORTUNITY(10000.00)),
                         Operation.END_LIKE(Deal.TITLE('_low')))
        data = CRMDataExecutor(BitrixCRMTypes.DEAL.value).list(
            select=select,
            filter=_filter,
        )
        self.assertEqual(data.method, 'crm.deal.list')
        self.assertEqual(data.select, ['ID', 'TITLE', 'DATE_CREATE'])
        self.assertEqual(data.filter, {'<=OPPORTUNITY': 10000.00, '%=TITLE': '%_low'})
        self.assertEqual(data.order, dict())
        self.assertEqual({**data.__dict__}['select'], ['ID', 'TITLE', 'DATE_CREATE'])
