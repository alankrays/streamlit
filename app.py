import streamlit as st
import pandas as pd

st.title("My Dashboard")
df = pd.read_csv('data.csv',sep=',')

if st.checkbox("Affichier le jdd"):
  st.write(df)

pro = df.Profession.unique()

st.selectbox('Selectionnez une profession', pro)
