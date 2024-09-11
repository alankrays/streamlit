import streamlit as st
import pandas as pd
from io import StringIO
from vega_datasets import data
import numpy as np

uploaded_file = st.file_uploader("Choose a file",type="csv")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
   # st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file,sep=',')
    st.write(dataframe)

    user_selection = st.selectbox('Selectionnez une profession', dataframe.columns)
    
    source = dataframe['user_selection']
    
    st.bar_chart(source, x="year", y="yield", color="site", stack=False)
