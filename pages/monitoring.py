import streamlit as st
import requests

st.title("monitoring")

option = st.selectbox(
    "How would you like to be contacted?",
    ("gpt-3.5-turbo", "gpt-3", "gpt-4"),
)

url = ' https://e6fb-35-231-28-0.ngrok-free.app/model'
x = requests.get(url)
st.write("You selected:", x.text)
