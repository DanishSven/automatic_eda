# from src.data import Dataset
# from src.datetime_part import DateColumn
# from src.numeric import NumericColumn
# from src.text import TextColum
import streamlit as st
import pandas as pd
 
st.title("Automatic Exploratory Data Analysis")
st.write("Simply upload a csv and watch the data unfold..")

try:
    uploaded = st.file_uploader("Upload your .csv here:", ['csv'])
    dataframe = pd.read_csv(uploaded)
except:
    st.error("Please upload a csv to begin")
    st.stop()