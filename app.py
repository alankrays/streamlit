import streamlit as st
import pandas as pd

st.title("My Dashboard")
df = pd.read_csv('data.csv',sep=',')

if st.checkbox("Affichier le jdd"):
  st.write(df)

pro = df.Profession.unique()

user_selection = st.selectbox('Selectionnez une profession', pro)
st.write(df[df.Profession==user_selection])

user_select1=st.slider("select your character", min_value=20,max_value=100,value=30,step=1)

st.write(df[df.Age==user_select1])


