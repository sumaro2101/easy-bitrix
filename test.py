from unittest import TestCase

from parameters import Parameter, Fields
from filter_operations import Operation


class TestParameters(TestCase):

    def test_parameter(self):
        param = Parameter.ID(42)
        self.assertEqual(param, {'ID': 42})

    def test_buss_param(self):
        param1 = Parameter.ID(42)
        param2 = Parameter.TITLE('Test')
        buss = Fields(param1, param2)
        self.assertEqual(buss.compare, {'ID': 42, 'TITLE': 'Test'})

    def test_operations(self):
        ready_param = Operation.END_LIKE(Parameter.TITLE('Tes'))
        self.assertEqual(ready_param, {'%=TITLE': '%Tes'})
