# Packages
import sys, os
import streamlit as st
import pandas as pd
import numpy as np

# Set up relative paths
if os.path.abspath(".") not in sys.path:
    sys.path.append(os.path.abspath("."))

# Import custom module
from src.data import Dataset
from src.datetime_part import DateColumn
from src.numeric import NumericColumn
from src.text import TextColumn

# Title
st.title("Automatic Exploratory Data Analysis")
st.write("Simply upload a csv and watch the data unfold..")

# File upload
try:
    uploaded = st.file_uploader("Upload your .csv here:", ['csv'])
    df = pd.read_csv(uploaded)
    df = pd.DataFrame(df)
except:
    st.error("Please upload a csv to begin")
    st.stop()

# upload = Dataset("upload",df)

# Datetime

# This is wrong - while I can change the nominated columns to datetime, this needs to be in the data module.
# So still need to figure that out...
date_cols = st.multiselect("Which columns in the .csv are date/time format?", df.columns, None)
#st.write(type(df))
st.dataframe(df)
st.write("Preview:", df[df.columns.intersection(date_cols)])

# dates = df[df.columns.intersection(date_cols)] # TODO Comment the 3 lines as they are already in upload.get_date_columns()
# dates = dates.apply(pd.to_datetime)
# st.write(dates)


# Init Class Dataset with 2 input:
upload = Dataset("upload", df, date_cols)
dates = upload.get_date_columns()
st.write("Date-time column changed to Date-time data type:", dates)


# Text Part - Overview TODO added text part
st.header('Information on text columns')
# provide an overview on the text columns
texts = upload.get_text_columns()
st.write("Text columns are:", texts.head())

# Text Part - for each column
part3_no = 0
for col in texts.columns:
    part3_no = part3_no + 1
    Text_stats = TextColumn(col, df)
    text_col_stats_table = Text_stats.construct_table()
    # Display name of column as subtitle
    st.subheader(str(3) + "." + str(part3_no) + " Field Name: " + Text_stats.col_name)
    # Add text_col_stats_table
    st.write(text_col_stats_table)
    # bar chart showing the number of occurrence for each value
    st.subheader("Barchart")
    chart_data = Text_stats.get_barchart()
    st.bar_chart(chart_data)
    # frequencies and percentage for each value
    st.subheader("Most Frequent Values")
    frequency = Text_stats.get_frequent()
    st.write(frequency)

# Overal Information
from data import fnc_get_row_num, fnc_get_column_num, fnc_get_dup_num, \
    fnc_get_missing_num, fnc_get_columns_name, fnc_get_columns_type

if 'filter_num' not in st.session_state:     # Set default value of "filter_num" session variable and used for filter number of rows
    st.session_state.filter_num = 5

if 'options' not in st.session_state:        # Set default value of "options" session variable and used for selection box
    st.session_state.options = None

if 'display_options' not in st.session_state:   # Set default value of "display_options" session variable and used for selection box
    st.session_state.display_options = 'Top Rows of Table'


def fnc_read_file(uploaded_file):      # Read the data of file uploaded and return a pandas dataframe
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    else:
        return None



def styler_data(options,df):      # format date columns of df dataframe, and Return a formated dataframe
    if options is not None:
        for o in options:
            try:
                df[o] = pd.to_datetime(df[o])
                fmt = '%b/%d/%Y'
                df = df.style.format(
                    {
                        o: lambda t: t.strftime(fmt)
                    }
                )
            except Exception as e:
                pass
        return df
    return df

def main():
    st.title('Data explorer tool')    # Display: 'Data explorer tool'

    uploaded_file = st.file_uploader("Choose a file")    # Get the data of file uploaded into uploaded_file variable

    data = fnc_read_file(uploaded_file)    # Assign all rows of file to a dataframe


    if data is not None:
        row_num = fnc_get_row_num(data)
        st.header('1. Overall Information')   # Display Overall Information

        st.subheader(f'Name of Table: {uploaded_file.name}')   # Display Name of Table

        st.subheader(f'Number of Rows: {row_num}')    # Display Number of Rows value

        st.subheader(f'Number of Columns: {fnc_get_column_num(data)}')   # Display Number of Columns value

        st.subheader(f'Number of Duplicated Rows: {fnc_get_dup_num(data)}')   # Display Number of Duplicated Rows values

        st.subheader(f'Number of Rows with Missing Values: {fnc_get_missing_num(data)}')  # Display Number of Rows with Missing Values


        columns = fnc_get_columns_name(data)  # Get all columns of file

        columns_text = ', '.join(map(str, columns))    # Format list of columns in to string with delimiter

        st.subheader('List of Columns:')   # Display List of Columns
        st.write(columns_text)

        st.subheader('Type of Columns:')   # Display Type of Columns table
        st.write(fnc_get_columns_type(data))

        row_num_filter = st.slider('Select number of rows to display', 5, 50,key='filter_num')   # Display slider with min and max value of rows

        display_option = ['Top Rows of Table', 'Bottom Rows of Table', 'Random Sample Rows of Table']   # Display sort order option. Default is display top rows of table
        selected_option = st.selectbox('What is the sort order for displaying',(display_option),key='display_options')

        if selected_option == 'Top Rows of Table':
            st.subheader('Top Rows of Table:')   # Display 'Top Rows of Table:'

            st.write(styler_data(st.session_state.options,data.head(row_num_filter)))   # Format date columns and write

        if selected_option == 'Bottom Rows of Table':
            st.subheader('Bottom Rows of Table:')    # Display 'Bottom Rows of Table:'
            st.write(styler_data(st.session_state.options,data.tail(row_num_filter)))   # Format date columns and write

        if selected_option == 'Random Sample Rows of Table':
            st.subheader('Random Sample Rows of Table:')   # Display 'Random Sample Rows of Table:'
            st.write(styler_data(st.session_state.options,data.sample(row_num_filter)))   # Format date columns and write

        option_list = columns.copy()   # Create option with the values are list of column names of file
                                       # Add "Chose an option" to the first element of the options list. The app will display "Chose an option" in the selection box
        option_list.insert(0, 'Chose an option')

        options = st.multiselect('Which columns do you want to convert to dates?',    # Display selection box
                                 (option_list),key='options')


if __name__ == "__main__":    #run the main function
    
    main()
 
 # end of Overal Information