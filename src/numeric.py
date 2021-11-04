# To be filled by students
import matplotlib.pyplot as plt
from dataclasses import dataclass
import pandas as pd

@dataclass
class NumericColumn:
  col_name: str
  # series: pd.Series
  df: pd.DataFrame

  # def get_name(self):
  #   """
  #   Return name of selected column
  #   """
  #   name = self.name
  #   return name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    unique_values = len(self.df[self.col_name].unique())
    return unique_values

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    missing_values = self.df[self.col_name].isnull().sum()
    return missing_values

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    zero_values = self.df[self.col_name].isin([0]).sum(axis=0)
    return zero_values

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    negative_values = (self.df[self.col_name]<0).sum()
    return negative_values

  def get_mean(self):
    """
    Return the average value for selected column
    """
    average = self.df[self.col_name].mean()
    return average

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    std_value = self.df[self.col_name].std()
    return std_value
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    min_value= self.df[self.col_name].min()
    return min_value

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    max_value= self.df[self.col_name].max()
    return max_value

  def get_median(self):
    """
    Return the median value for selected column
    """
    med_value= self.df[self.col_name].median()
    return med_value

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    n_rows = self.df.shape[0]
    if n_rows > 250:
      fig, ax = plt.subplots()
      ax.hist(self.df[self.col_name], bins=50)
    else: 
      fig, ax = plt.subplots()
      ax.hist(self.df[self.col_name], bins=int(round(n_rows/5,0)))
    return fig


  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    total_rows = self.df[self.col_name].count()
    frequency = self.df[self.col_name].value_counts().reset_index()
    frequency.columns = ['value', 'occurrence']
    frequency['percentage'] = frequency['occurrence']/total_rows
    return frequency.head(20)

  def construct_table(self):
    unique_values = self.get_unique()
    missing_values = self.get_missing()
    zero_values = self.get_zeros()
    negative_values = self.get_negatives()
    average = self.get_mean()
    std_value= self.get_std()
    min_value = self.get_min()
    max_value = self.get_max()
    med_value = self.get_median()

    table = {
      'number of unique values': [unique_values],
      'number of missing values': [missing_values],
      'number of rows with zero values': [zero_values],
      'number of rows with negative values': [negative_values],
      'Average': [average],
      'Standard Deviation': [std_value],
      'Minimum': [min_value],
      'Maximum': [max_value],
      'Median': [med_value]
    }
    table = pd.DataFrame.from_dict(table).T
    table.columns = ['value']
    return table.astype(str)        
