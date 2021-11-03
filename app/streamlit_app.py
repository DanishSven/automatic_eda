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

# Get Datetime columns - Needs to be split out first for other sections
date_cols = st.multiselect("Which columns in the .csv are date/time format?", df.columns, None)
dates = df[df.columns.intersection(date_cols)] 
# try inserting a try/except for pd.Datetime on the columns they select
st.write(dates)

# Init Class Dataset with 2 input:
upload = Dataset("upload", df, date_cols)
dates = upload.get_date_columns()
#st.write("Date-time column changed to Date-time data type:", dates)

######################################################
# Overall Section
######################################################


######################################################
# Numeric Section
######################################################

st.header('Information on numeric columns')
# provide an overview on the numeric columns
numeric = upload.get_numeric_columns()
st.write("Numeric columns are:", numeric.head())

# Numeric columns
part4_no = 0
for col in numeric.columns:
    part4_no = part4_no + 1
    numeric_stats = NumericColumn(col, df)
    numeric_col_stats_table = numeric_stats.construct_table()
    # Display name of column as subtitle
    st.subheader(str(4) + "." + str(part4_no) + " Field Name: " + numeric_stats.col_name)
    # Add numeric_col_stats_table
    st.write(numeric_col_stats_table)
    # bar chart showing the number of occurrence for each value
    st.subheader("Histogram")
    hist = numeric_stats.get_histogram
    st.hist_chart(hist)
    # frequencies and percentage for each value
    st.subheader("Most Frequent Values")
    frequency = numeric_stats.get_frequent()
    st.write(frequency)


######################################################
# Text Section
######################################################
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



######################################################
# DateTime Section
######################################################
# Datetime Columns

datetime = DateColumn(dates)

#some random change lol