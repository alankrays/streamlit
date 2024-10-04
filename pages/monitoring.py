import streamlit as st
import requests

st.title("monitoring")

option = st.selectbox(
    "How would you like to be contacted?",
    ("gpt-3.5-turbo", "gpt-3", "gpt-4"),
)

st.write(option)
url = ' https://8e11-35-231-28-0.ngrok-free.app/updtmodel'
myobj = {'model': option.text}
x = requests.post(url, json = myobj)

#openai_model=x.text.replace('"','')
url = 'https://8e11-35-231-28-0.ngrok-free.app/model'
x = requests.get(url)
openai_model=x.text.replace('"','')
st.session_state["openai_model"] = openai_model
