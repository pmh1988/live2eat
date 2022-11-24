import streamlit as st

import datetime
import requests

st.set_page_config(
    page_title="Live2Eat",
    page_icon="🐍",
    layout="centered",  # wide
    initial_sidebar_state="auto")  # collapsed
'''
# Live2Eat Food Tracking
Take the hard work out of tracking your food

'''
option = st.selectbox('Please select a video',
                      ('https://youtu.be/YaHtE96uc2c',
                       'https://www.youtube.com/watch?v=42_j8Mk_haw',
                       'https://www.youtube.com/watch?v=OdSGnEXMbTQ'))

st.video(option, format="video/mp4", start_time=0)

st.markdown('#')
st.markdown('#')

if picture:
    st.image(picture)

st.markdown('#')
st.markdown('#')

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text("Bak Chor Mee")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.text("Kaya Toast")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.text("Mee Siam")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    with col4:
        st.text("Hokkien Mee")
        st.image("https://static.streamlit.io/examples/owl.jpg")

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text("Bak Chor Mee")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.text("Kaya Toast")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.text("Mee Siam")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    with col4:
        st.text("Hokkien Mee")
        st.image("https://static.streamlit.io/examples/owl.jpg")

st.markdown('#')
st.markdown('#')

# with st.form(key='params_for_api'):

#     pickup_date = st.date_input('pickup datetime',
#                                 value=datetime.datetime(
#                                     2012, 10, 6, 12, 10, 20))
#     pickup_time = st.time_input('pickup datetime',
#                                 value=datetime.datetime(
#                                     2012, 10, 6, 12, 10, 20))
#     pickup_datetime = f'{pickup_date} {pickup_time}'
#     pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
#     pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
#     dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
#     dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
#     passenger_count = st.number_input('passenger_count',
#                                       min_value=1,
#                                       max_value=8,
#                                       step=1,
#                                       value=1)

#     st.form_submit_button('Make prediction')

# params = dict(pickup_datetime=pickup_datetime,
#               pickup_longitude=pickup_longitude,
#               pickup_latitude=pickup_latitude,
#               dropoff_longitude=dropoff_longitude,
#               dropoff_latitude=dropoff_latitude,
#               passenger_count=passenger_count)

# wagon_cab_api_url = 'https://taxifare.lewagon.ai/predict'
# response = requests.get(wagon_cab_api_url, params=params)

# prediction = response.json()

# pred = prediction['fare']

# st.header(f'Total Calories: ${round(pred, 2)}')

st.header("Total Calories : ")
