from unittest import TestCase

from .parameters import Fields, Filter, Select
from .bitrix_objects import Deal
from .fields import DEAL_FIELD
from .operations import FilterOperation
from .error import FilterParameterError


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
        ready_param = FilterOperation.END_LIKE(Deal.TITLE('Tes'))
        self.assertEqual(ready_param, {'%=TITLE': '%Tes'})

    def test_containce_operations(self):
        ready_param = FilterOperation.IN(Deal.ASSIGNED_BY_ID([1, 6]))
        self.assertEqual(ready_param, {'@ASSIGNED_BY_ID': [1, 6]})

    def test_containce_operations_wrong(self):
        with self.assertRaises(FilterParameterError):
            ready_param = FilterOperation.IN(Deal.ASSIGNED_BY_ID('1'))

    def test_filter(self):
        _filter = Filter(FilterOperation.EQ(Deal.TITLE('Test')),
                         FilterOperation.GTE(Deal.OPPORTUNITY(1000.00)),
                         FilterOperation.NOT_IN(Deal.CATEGORY_ID([20, 1, 3])),
                         Deal.CATEGORY_ID(10),
                         )
        self.assertEqual(_filter.compare, {'=TITLE': 'Test', '>=OPPORTUNITY': 1000.00,
                                           "!@CATEGORY_ID": [20, 1, 3], 'CATEGORY_ID': 10})

    def test_select(self):
        select = Select(DEAL_FIELD.ASSIGNED_BY_ID, DEAL_FIELD.ID)
        self.assertEqual(select.compare, ['ASSIGNED_BY_ID', 'ID'])
