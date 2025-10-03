from unittest import TestCase

from parameters import Parameter, BussParameters


class TestParameters(TestCase):

    def test_parameter(self):
        param = Parameter.ID(42)
        self.assertEqual(param, '"ID":42')

    def test_bus_param(self):
        param1 = Parameter.ID(42)
        param2 = Parameter.TITLE('"Test"')
        buss = BussParameters(param1, param2)
        self.assertEqual(buss.get_parameters(), '"ID":42&"TITLE":"Test"&')
