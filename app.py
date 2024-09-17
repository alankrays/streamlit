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
   latitude  = st.text_input("latitude title", "Life of Brian")
   longitude  = st.text_input("Longitude title", "Life of Brian")
   housing_median_age  = st.text_input("housing_median_age title", "Life of Brian")
   total_rooms  = st.text_input("total_rooms title", "Life of Brian")
   population  = st.population("population title", "Life of Brian")
   total_bedrooms  = st.text_input("total_bedrooms title", "Life of Brian")
   households  = st.text_input("households title", "Life of Brian")
   median_income  = st.text_input("median_income title", "Life of Brian")
   st.form_submit_button('Submit my picks')

data = {"latitude" : latitude,
        "longitude" : longitude,
        "housing_median_age":housing_median_age,
        "total_rooms":total_rooms,
        "total_bedrooms":total_bedrooms,
        "population":population,
        "households":households,
        "median_income":median_income
      }
st.write(data)

response = requests.post('url',json=data)
st.write('response.text')

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
