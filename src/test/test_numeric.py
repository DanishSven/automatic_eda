# To be filled by students
# Set up relative paths
import os, sys, unittest
import pandas as pd

if os.path.abspath('.') not in sys.path:
    sys.path.append(os.path.abspath('.'))

from src.numeric import NumericColumn

class TestSuite(unittest.TestCase):

    def test_unique(self):
        self.expected = ['foo', 'bar', 'baz']
        self.result = ['baz', 'foo', 'bar']
        self.unique = NumericColumn.get_unique(self.expected)
        self.assertCountEqual(self.unique, 0)

    # def test_missing(self):
    
    # def test_zeros(self):
        
    # def test_negatives(self):
        
    # def test_mean(self):

    # def test_std(self):
        
    # def test_min(self):

    # def test_max(self):

    # def test_median(self):
    
    # def test_histogram(self):

    # def test_freq(self):
    
    # def test_table(self):
    