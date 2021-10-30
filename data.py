import pandas as pd
def fnc_get_row_num(df):
        return  df.shape[0]   # shape[0] is number of rows of dataframe


def fnc_get_column_num(df):
    return  df.shape[1]       # shape[1] is number of columns of dataframe

def fnc_get_dup_num(df):
    unique_df = df.drop_duplicates()        # total of unique rows
    return  df.shape[0]-unique_df.shape[0]  # duplicated row = total number of rows - total number of unique rows

def fnc_get_missing_num(df):           # get total number of missing data
    return  df.isnull().sum().sum()

def fnc_get_columns_name(df):             # function get the list of columns name
    list_columns = df.columns.values.tolist()
    return  list_columns

def fnc_get_columns_type(df):     # get the list datatype of columns
    rows = []
    for i in df.columns.values.tolist():     # loop through list of column name
        rows.append([i,df[i].dtype.name])    # get column name and data type name
    df_type = pd.DataFrame(rows, columns=["Name","Type"]).set_index('Name')     # convert the list data types to a dataframe
    return  df_type