import streamlit as st
import pandas as pd

st.title("My Dashboard")
#df = pd.read_csv('data.csv',sep=',')



#pro = df.Profession.unique()

#user_selection = st.selectbox('Selectionnez une profession', pro)
#st.write(df[df.Profession==user_selection])

#user_select1=st.slider("select your character", min_value=20,max_value=100,value=30,step=1)

#st.write(df[(df.Age==user_select1) & (df.Profession==user_selection)])

#if st.checkbox("Affichier le jdd"):
 # st.write(df[(df.Age==user_select1) & (df.Profession==user_selection)])
with st.form("my_form"):
   st.write("Inside the form")
   my_number = st.slider('Pick a number', 1, 10)
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   longitude  = st.text_input("Longitude title", "Life of Brian")
   st.form_submit_button('Submit my picks')
st.write(longitude)
#curl -X 'POST' \
#  'https://0c73-34-32-169-73.ngrok-free.app/predict' \
 # -H 'accept: application/json' \
 # -H 'Content-Type: application/json' \
 # -d '{
 # "longitude": 0,
 # "latitude": 0,
 # "housing_median_age": 0,
 # "total_rooms": 0,
 # "total_bedrooms": 0,
 # "population": 0,
 # "households": 0,
 # "median_income": 0
#}'
