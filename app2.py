from openai import OpenAI
import streamlit as st
import requests


st.title("FAQ")
url = 'https://8e11-35-231-28-0.ngrok-free.app/model'
x = requests.get(url)
openai_model=x.text.replace('"','')
st.write("You selected:", openai_model)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"] )

if "openai_model" not in st.session_state:
    
    st.write("You selected:", str(x.text))
    #st.session_state["openai_model"] = "gpt-3.5-turbo"
    st.session_state["openai_model"] = openai_model

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            #model=openai_model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
