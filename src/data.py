# To be filled by students
from dataclasses import dataclass
import pandas as pd
import numpy as np

#######
@dataclass
class Dataset:
    name: str
    df: pd.DataFrame
    datetime_col: list

    def get_name(self):
        """
      Return filename of loaded dataset
      """
        return self.name

    def get_n_rows(self):
        """
        Return number of rows of loaded dataset
      """
        return self.df.shape[0]

    def get_n_cols(self):
        """
        Return number of columns of loaded dataset
      """
        return self.df.shape[1]

    def get_cols_list(self):
        """
        Return list column names of loaded dataset
      """
        return self.df.columns.values.tolist()

    def get_cols_dtype(self):
        """
        Return dictionary with column name as keys and data type as values
      """
        # get all column name as keys and data type as values
        keys_values = self.df.dtypes.to_dict().items()

        # convert data type value to string then return dictionary
        dict = {key: str(value) for key, value in keys_values}

        return dict

    def get_n_duplicates(self):
        """
        Return number of duplicated rows of loaded dataset
      """
        unique_df = self.df.drop_duplicates()  # get unique rows
        # duplicated row = total number of rows - total number of unique rows
        return self.df.shape[0] - unique_df.shape[0]

    def get_n_missing(self):
        """
        Return number of rows with missing values of loaded dataset
      """
        return self.df.isnull().sum().sum()

    def get_head(self, n=5):
        """
        Return Pandas Dataframe with top rows of loaded dataset
      """
        return self.df.head(n)

    def get_tail(self, n=5):
        """
        Return Pandas Dataframe with bottom rows of loaded dataset
      """
        return self.df.tail(n)

    def get_sample(self, n=5):
        """
        Return Pandas Dataframe with random sampled rows of loaded dataset
      """
        return self.df.sample(n)

    def get_numeric_columns(self):
      """
        Return list column names of numeric type from loaded dataset
      """
      df_types = pd.DataFrame(self.df.dtypes, columns=['Data Type'])
      df_types = df_types.astype(str)
      num_cols = df_types[df_types['Data Type'].isin(['int64' ,'float64'])].index.values
      numeric = self.df[num_cols]
      return numeric


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