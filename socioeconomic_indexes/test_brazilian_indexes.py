"""
This file tests functions for data collection from brazilian_indexes module
"""

from unittest import TestCase
from brazilian_indexes import brazilian_central_bank
import pandas as pd

class TestBrazilianIndexes(TestCase):

    def test_integer_code_type(self):
        """ Test functions when table_code value is an integer - function returns a pd.core.frame.DataFrame object """
        self.addTypeEqualityFunc(pd.core.frame.DataFrame, brazilian_central_bank(4380, '2012-01-01', '2022-12-01'))
        self.addTypeEqualityFunc(pd.core.frame.DataFrame, brazilian_central_bank(433, '2012-01-01', '2022-12-01'))

    def test_string_code_type(self):
        """ Test functions when table_code value is a string - function returns a pd.core.frame.DataFrame object """
        self.addTypeEqualityFunc(pd.core.frame.DataFrame, brazilian_central_bank('4380', '2012-01-01', '2022-12-01'))
        self.addTypeEqualityFunc(pd.core.frame.DataFrame, brazilian_central_bank('433', '2012-01-01', '2022-12-01'))
        
    def test_float_code_type(self):
        """ Test functions when table_code value is a float -  function raises a TypeError """
        self.assertRaises(TypeError, brazilian_central_bank, 4380.0, '2012-01-01', '2022-12-01')
        self.assertRaises(TypeError, brazilian_central_bank, 433.0, '2012-01-01', '2022-12-01')
    
    def test_bool_code_type(self):
        """ Test functions when table_code value is a bool -  function raises a TypeError """
        self.assertRaises(TypeError, brazilian_central_bank, True, '2012-01-01', '2022-12-01')
        self.assertRaises(TypeError, brazilian_central_bank, False, '2012-01-01', '2022-12-01')

    def test_integer_date_type(self):
        """ Test functions when date value is an integer - function raises a TyperError """
        self.assertRaises(TypeError, brazilian_central_bank, 4380, 20120101, '2022-12-01')
        self.assertRaises(TypeError, brazilian_central_bank, 4380, '2012-01-01', 20221201)

    def test_string_date_type(self):
        """ Test functions when date value is a string - function returns a pd.core.frame.DataFrame object """
        self.addTypeEqualityFunc(pd.core.frame.DataFrame, brazilian_central_bank(4380, '2012-01-01', '2022-12-01'))
        self.addTypeEqualityFunc(pd.core.frame.DataFrame, brazilian_central_bank(4380, '2012-01-01', '2022-12-01'))
        
    def test_float_date_type(self):
        """ Test functions when date value is a float - function raises a TypeError """
        self.assertRaises(TypeError, brazilian_central_bank, 4380, 20120101.0, '2022-12-01')
        self.assertRaises(TypeError, brazilian_central_bank, 4380, '2012-01-01', 20221201.0)
    
    def test_bool_date_type(self):
        """ Test functions when date value is a bool -  function raises a TypeError """
        self.assertRaises(TypeError, brazilian_central_bank, 4380, True, '2022-12-01')
        self.assertRaises(TypeError, brazilian_central_bank, 4380, '2012-01-01', False)

    def test_date_value(self):
        """ Test functions for date formats other than '%Y-%m-%d' - raises ValueError """
        self.assertRaises(ValueError, brazilian_central_bank, 4380, '2012/01/01', '2022-12-01')
        self.assertRaises(ValueError, brazilian_central_bank, 4380, '2012-01-01', '2022/12/01')
        self.assertRaises(ValueError, brazilian_central_bank, 4380, '20120101', '2022-12-01')
        self.assertRaises(ValueError, brazilian_central_bank, 4380, '2012-01-01', '20221201')
        self.assertRaises(ValueError, brazilian_central_bank, 4380, '2012-25-01', '2022-12-01')
        self.assertRaises(ValueError, brazilian_central_bank, 4380, '2012-01-01', '2022-25-01')

    def test_code_value(self):
        """ Test functions for table_code values - raises ValueError if <= 0 """
        self.assertRaises(ValueError, brazilian_central_bank, 0, '2012-01-01', '2022-12-01')
        self.assertRaises(ValueError, brazilian_central_bank, -4380, '2012-01-01', '2022-12-01')
        self.assertRaises(ValueError, brazilian_central_bank, '0', '2012-01-01', '2022-12-01')
        self.assertRaises(ValueError, brazilian_central_bank, '-4380', '2012-01-01', '2022-12-01')

    def test_bad_request(self):
        """ Function should return ValueError if code_value results in a bad request """
        self.assertRaises(ValueError, brazilian_central_bank, 9999999, '2012-01-01', '2022-12-01')
        self.assertRaises(ValueError, brazilian_central_bank, 123456789, '2012-01-01', '2022-12-01')