import streamlit as st
import pandas as pd

st.title("My Dashboard")
df = pd.read_csv('data.csv',sep=',')

st.write(df)
