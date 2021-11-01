from unittest import TestCase
import pandas as pd
from data import fnc_get_row_num, fnc_get_column_num, fnc_get_dup_num, \
    fnc_get_missing_num, fnc_get_columns_name

df = pd.DataFrame({'numbers': [1, None, 3,1], 'colors': ['red', 'white', None,'red']})

class TestFormatUrl(TestCase):
    def test_fnc_get_row_num(self):
        actual = fnc_get_row_num(df)
        expected = 4
        self.assertEqual(actual, expected)

    def test_fnc_get_column_num(self):
        actual = fnc_get_column_num(df)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fnc_get_dup_num(self):
        actual = fnc_get_dup_num(df)
        expected = 1
        self.assertEqual(actual, expected)

    def test_fnc_get_missing_num(self):
        actual = fnc_get_missing_num(df)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fnc_get_columns_name(self):
        actual = fnc_get_columns_name(df)
        expected = ['numbers','colors']
        self.assertEqual(actual, expected)