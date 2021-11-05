import unittest, sys, os
import pandas as pd
from streamlit.type_util import data_frame_to_bytes

# Set up relative paths
if os.path.abspath(".") not in sys.path:
    sys.path.append(os.path.abspath("."))

from src.datetime import DateColumn

# Set up a proper DateColumn with all possible cases
date_test = ['1/1/01','2/1/01','3/1/01','3/1/01','4/1/22','5/1/01','6/1/01','7/1/01','01/01/1970','01/01/1900','',]
date_test = pd.Series(date_test)
date_test = pd.to_datetime(date_test)
date_test.name = 'Dates'
date_test = DateColumn('Dates',date_test)

print(date_test.get_weekend())

class datetime_test(unittest.TestCase):

    def test_get_unique(self):
        unique_vals = 10
        unique_test = date_test.get_unique()

        self.assertEqual(unique_vals,unique_test)

    def test_get_missing_test(self):
        missing_vals = 1
        missing_test = date_test.get_missing()
        
        self.assertEqual(missing_vals,missing_test)

    def test_get_weekend_test(self):
        no_weekends = 1
        weekend_test = date_test.get_weekend()

        self.assertEqual(no_weekends,weekend_test)

    def test_get_weekday_test(self):
        no_weekdays = 9
        weekday_test = date_test.get_weekday()

        self.assertEqual(no_weekdays,weekday_test)

    def test_get_future_test(self):
        future_dates = 1
        future_test = date_test.get_future()

        self.assertEqual(future_dates,future_test)
    
    def test_get_empty_1900_test(self):
        emptyone = 1
        emptyone_test = date_test.get_empty_1900()

        self.assertEqual(emptyone,emptyone_test)

    def test_get_empty_1970_test(self):
        emptytwo = 1
        emptytwo_test = date_test.get_empty_1970()

        self.assertEqual(emptytwo,emptytwo_test)

    def test_get_min_test(self):
        minimum = pd.to_datetime('1900-01-01 00:00:00')
        min_test = date_test.get_min()

        self.assertEqual(minimum,min_test)

    def test_get_max_test(self):
        maximum = pd.to_datetime('2022-04-01 00:00:00')
        max_test = date_test.get_max()

        self.assertEqual(maximum,max_test)

    def test_get_barchart_test(self):
        test_index = ['2001-03-01', '2001-01-01', '2001-02-01', '2022-04-01',
               '2001-05-01', '2001-06-01', '2001-07-01', '1970-01-01',
               '1900-01-01']
        test_index = len(test_index)
        barchart_test = len(date_test.get_barchart().index)

        self.assertEqual(test_index,barchart_test)

    def test_get_frequent_test(self):
        test_table = date_test.get_frequent()

        self.assertEqual(2, test_table.occurrence[test_table.value == '2001-03-01'].values[0])
        self.assertEqual(0.2, test_table.percentage[test_table.value == '2001-03-01'].values[0])
        
    def test_construct_table(self):
        test_table = date_test.construct_table()

        self.assertEqual(9, test_table.shape[0])
        self.assertEqual(1, test_table.shape[1])

        self.assertEqual(test_table.value[test_table.index == 'number of unique values'].values[0], '10')
        self.assertEqual(test_table.value[test_table.index == 'number of missing values'].values[0], '1')
        self.assertEqual(test_table.value[test_table.index == 'number of weekends'].values[0], '1')
        self.assertEqual(test_table.value[test_table.index == 'number of weekdays'].values[0], '9')
        self.assertEqual(test_table.value[test_table.index == 'number of future dates'].values[0], '1')
        self.assertEqual(test_table.value[test_table.index == 'number of empty 1900'].values[0], '1')
        self.assertEqual(test_table.value[test_table.index == 'number of empty 1970'].values[0], '1')
        self.assertEqual(test_table.value[test_table.index == 'minimum date'].values[0], '1900-01-01 00:00:00')
        self.assertEqual(test_table.value[test_table.index == 'maximum date'].values[0], '2022-04-01 00:00:00')

if __name__ == '__main__':
    unittest.main()