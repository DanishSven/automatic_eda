
<<<<<<< HEAD

# from src.data import Dataset
=======
import streamlit as st
import pandas as pd
import sys
import os 

relative_path = 'src'
sys.path.insert(1, relative_path)

lol = sys.path
print(lol)

from src.data import Dataset
>>>>>>> datetime
# from src.datetime_part import DateColumn
# from src.numeric import NumericColumn
# from src.text import TextColum

sys.path.remove(relative_path) 
st.title("Automatic Exploratory Data Analysis")
st.write("Simply upload a csv and watch the data unfold..")

try:
    uploaded = st.file_uploader("Upload your .csv here:", ['csv'])
    dataframe = pd.read_csv(uploaded)
except:
    st.error("Please upload a csv to begin")
    st.stop()

