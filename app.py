import streamlit as st
import requests

# TaxiFareModel front


'''
## Hi! Welcome to taxi fare predictor!

Please complete the following data in order get information about your taxi fare.'''

user_input_date = st.text_input("Date and time (Please enter it as YYYY-MM-DD HH:MM:SS UTC):", value='')
user_input_plon = st.text_input("Pickup longitude:", value='')
user_input_plat = st.text_input("Pickup latitude:", value='')
user_input_dlon = st.text_input("Dropoff longitude:", value='')
user_input_dlat = st.text_input("Dropoff latitude:", value='')
user_input_numpass = st.text_input("Number of passengers:", value='')


url = 'http://taxifare.lewagon.ai/predict_fare/'
params = {  'key': 1,
                "pickup_datetime": user_input_date,
                "pickup_longitude": user_input_plon,
                "pickup_latitude": user_input_plat,
                "dropoff_longitude": user_input_dlon,
                "dropoff_latitude": user_input_dlat,
                "passenger_count": user_input_numpass
                }

response = requests.get(url, params=params)


if st.button("Let's get my taxi fare!"):
    if user_input_date == '' or user_input_plon == '' or user_input_plat == '' or user_input_dlon == '' or user_input_dlat=='' or user_input_numpass=='':
        'You are missing some values :('
    else:
        'You will be paying:'
        response.json()['prediction']

else:
    pass

