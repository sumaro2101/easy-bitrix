from unittest import TestCase

from parameters import Product, Fields, Filter, Select
from fields import PRODUCT_FIELD
from filter_operations import Operation
from exeptions import FilterParameterError


class TestParameters(TestCase):

    def test_parameter(self):
        param = Product.ID(42)
        self.assertEqual(param, {'ID': 42})

    def test_buss_param(self):
        param1 = Product.ID(42)
        param2 = Product.TITLE('Test')
        buss = Fields(param1, param2)
        self.assertEqual(buss.compare, {'ID': 42, 'TITLE': 'Test'})

    def test_operations(self):
        ready_param = Operation.END_LIKE(Product.TITLE('Tes'))
        self.assertEqual(ready_param, {'%=TITLE': '%Tes'})

    def test_containce_operations(self):
        ready_param = Operation.IN(Product.ASSIGNED_BY_ID([1, 6]))
        self.assertEqual(ready_param, {'@ASSIGNED_BY_ID': [1, 6]})

    def test_containce_operations_wrong(self):
        with self.assertRaises(FilterParameterError):
            ready_param = Operation.IN(Product.ASSIGNED_BY_ID('1'))

    def test_filter(self):
        _filter = Filter(Operation.EQ(Product.TITLE('Test')),
                         Operation.GTE(Product.OPPORTUNITY(1000.00)),
                         Operation.NOT_IN(Product.CATEGORY_ID([20, 1, 3])),
                         Product.CATEGORY_ID(10),
                         )
        self.assertEqual(_filter.compare, {'=TITLE': 'Test', '>=OPPORTUNITY': 1000.00,
                                           "!@CATEGORY_ID": [20, 1, 3], 'CATEGORY_ID': 10})

    def test_select(self):
        select = Select(PRODUCT_FIELD.ASSIGNED_BY_ID, PRODUCT_FIELD.ID)
        self.assertEqual(select.compare, ['ASSIGNED_BY_ID', 'ID'])
