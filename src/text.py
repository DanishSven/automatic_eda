# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class TextColumn:
    col_name: str
    # series: pd.Series
    df: pd.DataFrame

    # def get_name(self):
    #     """
    #     Return name of selected column
    #     """
    #     return None

    def get_unique(self):
        """
        Return number of unique values for selected column
        """
        no_unique_values = len(self.df[self.col_name].unique())

        return no_unique_values

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        no_missing_values = self.df[self.col_name].isnull().sum()
        return no_missing_values

    def get_empty(self):
        """
        Return number of rows with empty string for selected column #
        """
        no_empty = sum(map(lambda x: str(x) == '', self.df[self.col_name]))

        return no_empty

    def get_whitespace(self):
        """
        Return number of rows with only whitespaces for selected column
        """
        no_whitespace = sum(map(lambda x: str(x).isspace(), self.df[self.col_name]))

        return no_whitespace

    def get_lowercase(self):
        """
        Return number of rows with only lower case characters for selected column
        """
        no_lowercase = sum(map(lambda x: str(x).islower(), self.df[self.col_name]))
        return no_lowercase

    def get_uppercase(self):
        """
        Return number of rows with only upper case characters for selected column
        """
        no_uppercase = sum(map(lambda x: str(x).isupper(), self.df[self.col_name]))
        return no_uppercase

    def get_alphabet(self):
        """
        Return number of rows with only alphabet characters for selected column
        """
        no_alphabet = sum(map(lambda x: str(x).isalpha(), self.df[self.col_name]))
        return no_alphabet

    def get_digit(self):
        """
        Return number of rows with only numbers as characters for selected column
        """
        # target_df = self.df
        # target_df[self.col_name] = target_df[self.col_name].str.replace(".", "")
        no_digit = sum(map(lambda x: str(x).isdigit(), self.df[self.col_name]))
        return no_digit

    def get_mode(self):
        """
        Return the mode value for selected column
        """
        str_mode = self.df[self.col_name].mode().values[0]

        return str_mode

    def get_barchart(self):
        """
        Return the generated bar chart for selected column
        """
        chart_data = self.df[self.col_name].value_counts().T

        return chart_data

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
        no_unique_values = self.get_unique()
        no_missing_values = self.get_missing()
        no_empty = self.get_empty()
        no_whitespace = self.get_whitespace()
        no_lowercase = self.get_lowercase()
        no_uppercase = self.get_uppercase()
        no_alphabet = self.get_alphabet()
        no_digit = self.get_digit()
        str_mode = self.get_mode()

        table = {
            'number of unique values': [no_unique_values],
            'number of missing values': [no_missing_values],
            'number of rows with empty string': [no_empty],
            'number of rows with only whitespaces': [no_whitespace],
            'number of rows with only lower case characters': [no_lowercase],
            'number of rows with only upper case characters': [no_uppercase],
            'number of rows with only alphabet characters': [no_alphabet],
            'number of rows with only numbers as characters': [no_digit],
            'the mode value': [str_mode]
        }
        table = pd.DataFrame.from_dict(table).T
        table.columns = ['value']
        return table.astype(str)

