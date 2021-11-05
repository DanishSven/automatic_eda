import unittest, sys, os
import pandas as pd
from streamlit.type_util import data_frame_to_bytes

# Set up relative paths
if os.path.abspath(".") not in sys.path:
    sys.path.append(os.path.abspath("."))

from src.datetime import DateColumn

# Set up a proper DateColumn with all possible cases
date_test = ['1/1/01','2/1/01','3/1/01','3/1/01','4/1/01','5/1/01','6/1/01','01/01/1970','01/01/1900','',]
date_test = pd.Series(date_test)
date_test = pd.to_datetime(date_test)
date_test.name = 'Dates'
date_test = DateColumn('Dates',date_test)

# Set up an improper DateColumn
notdate_test = ['these','are','not','the','dates','you','are','looking','for',1977,'']
notdate_test = pd.Series(notdate_test)
notdate_test.name = 'Not Dates'
notdate_test = DateColumn('Not Dates',notdate_test)

class datetime_test(unittest.TestCase):

    def test_get_unique(self):
        unique_vals = 9
        unique_test = date_test.get_unique()
        notdate_unique = notdate_test.get_unique()

        self.assertEqual(unique_vals,unique_test)
        self.assertEqual(unique_vals,notdate_unique)

    def test_get_missing_test(self):
        missing_vals = 1
        missing_test = date_test.get_missing()
        notdate_missing = notdate_test.get_missing
        
        self.assertEqual(missing_vals,missing_test)
        self.assertEqual(missing_vals,notdate_missing)

    # def test_get_weekend_test(self):

    # def test_get_weekday_test(self):

    # def test_get_future_test(self):
    
    # def test_get_empty_1900_test(self):

    # def test_get_empty_1970_test(self):

    # def test_get_min_test(self):

    # def test_get_max_test(self):

    # def test_get_barchart_test(self):

    # def test_get_frequent_test(self):

    # def test_construct_table(_testself):

if __name__ == '__main__':
    unittest.main()