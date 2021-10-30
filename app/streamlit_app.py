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
except:
    st.error("Please upload a csv to begin")
    st.stop()

upload = Dataset("upload",df)

# Datetime

# This is wrong - while I can change the nominated columns to datetime, this needs to be in the data module.
# So still need to figure that out...
date_cols = st.multiselect("Which columns in the .csv are date/time format?", df.columns, None)
st.write(upload)
st.write("Preview:", df[df.columns.intersection(date_cols)])
dates = df[df.columns.intersection(date_cols)]
dates = dates.apply(pd.to_datetime)
st.write(dates)
upload.get_date_columns(date_cols)




