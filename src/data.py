from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
#class Dataset:
#   name: str
#   df: pd.DataFrame
#   datetime_col: list

  class FileReader():

    def __init__(self, file_name, data):
        self.file_name = file_name  # initialize file_name attribute
        self.data = data  # initialize data attribute

    def get_name(self):
        """
      Return filename of loaded dataset
      """
        return self.file_name

    def get_n_rows(self):
        """
        Return number of rows of loaded dataset
      """
        return self.data.shape[0]

    def get_n_cols(self):
        """
        Return number of columns of loaded dataset
      """
        return self.data.shape[1]

    def get_cols_list(self):
        """
        Return list column names of loaded dataset
      """
        return self.data.columns.values.tolist()

    def get_cols_dtype(self):
        """
        Return dictionary with column name as keys and data type as values
      """
        # get all column name as keys and data type as values
        keys_values = self.data.dtypes.to_dict().items()

        # convert data type value to string then return dictionary
        dict = {key: str(value) for key, value in keys_values}

        return dict

    def get_n_duplicates(self):
        """
        Return number of duplicated rows of loaded dataset
      """
        unique_df = self.data.drop_duplicates()  # get unique rows
        # duplicated row = total number of rows - total number of unique rows
        return self.data.shape[0] - unique_df.shape[0]

    def get_n_missing(self):
        """
        Return number of rows with missing values of loaded dataset
      """
        return self.data.isnull().sum().sum()

    def get_head(self, n=5):
        """
        Return Pandas Dataframe with top rows of loaded dataset
      """
        return self.data.head(n)

    def get_tail(self, n=5):
        """
        Return Pandas Dataframe with bottom rows of loaded dataset
      """
        return self.data.tail(n)

    def get_sample(self, n=5):
        """
        Return Pandas Dataframe with random sampled rows of loaded dataset
      """
        return self.data.sample(n)
  
    
    #def get_name(self):
     #   """
      #Return filename of loaded dataset
      #"""
       # return None

    #def get_n_rows(self):
     #   """
      #  Return number of rows of loaded dataset
      #"""
       # return None

    #def get_n_cols(self):
     #   """
      #  Return number of columns of loaded dataset
     # """
      #  return None

    #def get_cols_list(self):
     #   """
      #  Return list column names of loaded dataset
      #"""
       # return None

    #def get_cols_dtype(self):
     #   """
      #  Return dictionary with column name as keys and data type as values
      #"""
       # return None

    #def get_n_duplicates(self):
     #   """
      #  Return number of duplicated rows of loaded dataset
      #"""
       # return None

    #def get_n_missing(self):
     #   """
      #  Return number of rows with missing values of loaded dataset
      #"""
       # return None

    #def get_head(self, n=5):
     #   """
      #  Return Pandas Dataframe with top rows of loaded dataset
      #"""
       # return None

    #def get_tail(self, n=5):
     #   """
      #  Return Pandas Dataframe with bottom rows of loaded dataset
      #"""
       # return None

    #def get_sample(self, n=5):
     #   """
      #  Return Pandas Dataframe with random sampled rows of loaded dataset
      #"""
       # return None

    def get_numeric_columns(self):
        """
        Return list column names of numeric type from loaded dataset
      """
        # numerics = [i for i in self.columns if (self.dtypes[i] == np.float_ | self.dtypes[i] == np.int_)]
        # return numerics
        return None

    def get_text_columns(self): # TODO modified, add part to filter to text columns
      """
        Return list column names of text type from loaded dataset
      """
      df_types = pd.DataFrame(self.df.dtypes, columns=['Data Type'])
      df_types = df_types.astype(str)
      text_cols = df_types[df_types['Data Type'].isin(['object', 'bool'])].index.values
      texts = self.df[text_cols]
      texts = texts.drop(columns=self.datetime_col)
      return texts

    def get_date_columns(self):
        """
        Return list column names of datetime type from loaded dataset
      """
        # dates = [i for i in self.columns if self.dtypes[i] == np.datetime64]
        dates = self.df[
            self.df.columns.intersection(
                self.datetime_col)]  # TODO modified, change df -> self.df, added self.datetime_col
        dates = dates.apply(pd.to_datetime)
        return dates
