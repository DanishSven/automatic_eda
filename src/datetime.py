from dataclasses import dataclass
import pandas as pd


@dataclass
class DateColumn:
  col_name: str
  series: pd.Series

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
    unique_dates = len(self.series.unique())

    return unique_dates

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    missing_dates = self.series.isnull().sum()

    return missing_dates

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    weekends = sum(self.series.dt.dayofweek > 4)

    return weekends

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    weekdays = sum(self.series.dt.dayofweek < 5)
    return weekdays
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    today = pd.to_datetime("today")
    future = sum(self.series > today)
    return future

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    #emptyone = sum(np.where(self.series == '1900-01-01 00:00:00',1,0))
    emptyone = self.series[self.series == '1900-01-01 00:00:00']
    emptyone = len(emptyone)
    return emptyone

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    #emptytwo = sum(np.where(self.series == '1970-01-01 00:00:00',1,0))
    emptytwo = self.series[self.series == '1970-01-01 00:00:00']
    emptytwo = len(emptytwo)
    return emptytwo

  def get_min(self):
    """
    Return the minimum date
    """
    mindate = min(self.series)
    return mindate

  def get_max(self):
    """
    Return the maximum date 
    """
    maxdate = max(self.series)
    return maxdate

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    barchart = self.series.value_counts().T
    return barchart

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    total_rows = self.series.count()
    frequency = self.series.value_counts().reset_index()
    frequency.columns = ['value', 'occurrence']
    frequency['percentage'] = frequency['occurrence']/total_rows
    return frequency.head(20)

  def construct_table(self):
        no_unique_values = self.get_unique()
        no_missing_values = self.get_missing()
        no_weekends = self.get_weekend()
        no_weekdays = self.get_weekday()
        no_future = self.get_future()
        no_emptyone = self.get_empty_1900()
        no_emptytwo = self.get_empty_1970()
        mindate = self.get_min()
        maxdate = self.get_max()
   
        table = {
            'number of unique values': [no_unique_values],
            'number of missing values': [no_missing_values],
            'number of weekends': [no_weekends],
            'number of weekdays': [no_weekdays],
            'number of future dates': [no_future],
            'number of empty 1900': [no_emptyone],
            'number of empty 1970': [no_emptytwo],
            'minimum date': [mindate],
            'maximum date': [maxdate]
        }
        table = pd.DataFrame.from_dict(table).T
        table.columns = ['value']
        return table.astype(str)