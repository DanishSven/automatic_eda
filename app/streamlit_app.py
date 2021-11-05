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
from src.datetime import DateColumn
from src.numeric import NumericColumn
from src.text import TextColumn

######################################################
# Streamlit App
######################################################
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
st.write(df)

# Get Datetime columns - Needs to be split out first for other sections
date_cols = st.multiselect("Which columns in the .csv are date/time format?", df.columns, None)

name = uploaded.name
# Init Class Dataset with 3 input:
upload = Dataset(name, df, date_cols)
try:
    dates = upload.get_date_columns()
except:
    st.error("A column you have chosen can't be converted to datetime. Please check which columns you are adding and try again.")
    st.stop()


######################################################
# Overall Section
######################################################
st.header('1. Overall Information')
# Display Name of Table
st.subheader(f'Name of Table: {upload.get_name()}')
# Display Number of Rows value
st.subheader(f'Number of Rows: {upload.get_n_rows()}')
# Display Number of Columns value
st.subheader(f'Number of Columns: {upload.get_n_cols()}')
# Display Number of Duplicated Rows values
st.subheader(f'Number of Duplicated Rows: {upload.get_n_duplicates()}')
# Display Number of Rows with Missing Values
st.subheader(f'Number of Rows with Missing Values: {upload.get_n_missing()}')
# get all column of file
columns = upload.get_cols_list()
# Format list of columns in to string with delimiter
columns_text = ', '.join(map(str, columns))
# Display List of Columns
st.subheader('List of Columns:')
st.write(columns_text)
# Display Type of Columns table
st.subheader('Type of Columns:')
# Convert dictionary to dataframe then display
st.write(pd.DataFrame.from_dict(upload.get_cols_dtype(), orient='index'))

if upload.get_n_rows() > 50:
    row_num_filter = st.slider('Select number of rows to display', 5, 50, key='filter_num')
else:
    row_num_filter = st.slider('Select number of rows to display', 5, upload.get_n_rows(), key='filter_num')

# Display sort order option. Default is display top rows of table
display_option = ['Top Rows of Table', 'Bottom Rows of Table', 'Random Sample Rows of Table']
selected_option = st.selectbox('What is the sort order for displaying',(display_option),key='display_options')
if selected_option == 'Top Rows of Table':
    # Display 'Top Rows of Table:'
    st.subheader('Top Rows of Table:')
    # Format date columns and write
    st.write(upload.get_head(row_num_filter))
if selected_option == 'Bottom Rows of Table':
    # Display 'Bottom Rows of Table:'
    st.subheader('Bottom Rows of Table:')
    # Format date columns and write
    st.write(upload.get_tail(row_num_filter))
if selected_option == 'Random Sample Rows of Table':
    # Display 'Random Sample Rows of Table:'
    st.subheader('Random Sample Rows of Table:')
    # Format date columns and write
    st.write(upload.get_sample(row_num_filter))

######################################################
# Numeric Section
######################################################

st.header('2. Information on numeric columns')
# provide an overview on the numeric columns
numeric = upload.get_numeric_columns()
st.write("Numeric columns are:", numeric.head())

# Numeric columns
part2_no = -1
for col in numeric.columns:
    part2_no = part2_no + 1
    numeric_stats = NumericColumn(col, df)
    numeric_col_stats_table = numeric_stats.construct_table()
    # Display name of column as subtitle
    st.subheader(str(2) + "." + str(part2_no) + " Field Name: " + numeric_stats.col_name)
    # Add numeric_col_stats_table
    st.write(numeric_col_stats_table)
    # histogram showing the number of occurrence for each value
    st.subheader("Histogram")
    num_hist = numeric_stats.get_histogram()
    st.pyplot(num_hist)
    # frequencies and percentage for each value
    st.subheader("Most Frequent Values")
    frequency = numeric_stats.get_frequent()
    st.write(frequency)



######################################################
# Text Section
######################################################
st.header('3. Information on text columns')
# provide an overview on the text columns
texts = upload.get_text_columns()
st.write("Text columns are:", texts.head())

# Text Part - for each column
part3_no = -1
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



######################################################
# DateTime Section
######################################################
st.header('4. Information on datetime columns')
part4_no = -1
dates_cols = dates.columns
for col in dates_cols:
    part4_no = part4_no + 1
    datetime = DateColumn(col,dates[col])
    st.subheader(str(4) + "." + str(part4_no) + " Field Name: " + col)
    #Data table
    date_col_stats_table = datetime.construct_table()
    st.write(date_col_stats_table)
    #Bar chart
    st.subheader('Barchart')
    barchart_data = datetime.get_barchart()
    st.bar_chart(barchart_data)
    #Most Frequent
    st.subheader('Most Frequent Values')
    frequent = datetime.get_frequent()
    st.write(frequent)
    