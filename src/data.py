# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class Dataset:
  name: str
  df: pd.DataFrame
  
  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return None

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return None

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return None

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    return None

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    return None

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return None

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return None

  def get_head(self, n=5):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return None

  def get_tail(self, n=5):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return None

  def get_sample(self, n=5):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return None

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
    dateformat = pd.to_datetime(self)
    return dateformat



# 

# def fnc_get_row_num(df):
#     return  df.shape[0]   # shape[0] is number of rows of dataframe


# def fnc_get_column_num(df):
#     return  df.shape[1]       # shape[1] is number of columns of dataframe

# def fnc_get_dup_num(df):
#     unique_df = df.drop_duplicates()        # total of unique rows
#     return  df.shape[0]-unique_df.shape[0]  # duplicated row = total number of rows - total number of unique rows

# def fnc_get_missing_num(df):           # get total number of missing data
#     return  df.isnull().sum().sum()

# def fnc_get_columns_name(df):             # function get the list of columns name
#     list_columns = df.columns.values.tolist()
#     return  list_columns

# def fnc_get_columns_type(df):     # get the list datatype of columns
#     rows = []
#     for i in df.columns.values.tolist():     # loop through list of column name
#         rows.append([i,df[i].dtype.name])    # get column name and data type name
#     df_type = pd.DataFrame(rows, columns=["Name","Type"]).set_index('Name')     # convert the list data types to a dataframe
#     return  df_type