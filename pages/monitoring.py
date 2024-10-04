import streamlit as st

st.title("monitoring")

option = st.selectbox(
    "How would you like to be contacted?",
    ("gpt-3.5-turbo", "gpt-3", "gpt-4"),
)

st.write("You selected:", option)
