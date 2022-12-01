import datetime
import glob
import os
import pickle
import statistics
import time
from datetime import timedelta
from typing import Optional, Sequence

import cv2
import numpy as np
import pandas as pd
import requests
import streamlit as st
from food_frame_export import *
from food_frame_extract import *
from food_prediction import *
from food_video_selection import *
from google.cloud import storage
from google.cloud import videointelligence as vi
from google.oauth2 import service_account
from sklearn.cluster import KMeans

st.set_page_config(
    page_title="Live2Eat",
    page_icon="🐍",
    layout="centered",  # wide
    initial_sidebar_state="auto")  # collapsed
'''
# Live2Eat Food Tracking
Take the hard work out of tracking your food

'''
st.markdown('#')

option = st.selectbox('Please select a video',
                      ('Bak Chor Mee', 'Hokkien Mee', 'Kaya Toast', 'Laksa',
                       'Mee Rubus', 'Mee Siam'))

if option == 'Bak Chor Mee':
    video_URL = 'https://www.youtube.com/watch?v=V4GR-TcqYkk'
if option == 'Kaya Toast':
    video_URL = 'https://www.youtube.com/watch?v=7R-iTYFaS6A'
if option == 'Hokkien Mee':
    video_URL = 'https://www.youtube.com/watch?v=3zH2Hw4EE_U'
if option == 'Laksa':
    video_URL = 'https://www.youtube.com/watch?v=ksBTwhiEVJw'
if option == 'Mee Rubus':
    video_URL = 'https://www.youtube.com/watch?v=kOfofLXBB-E'
elif option == 'Mee Siam':
    video_URL = 'https://www.youtube.com/watch?v=1O6HwbTa1ok'

st.video(video_URL, format="video/mp4", start_time=0)

st.markdown('#')
st.markdown('#')

credentials = service_account.Credentials.from_service_account_info(
    st.secrets['gcp_service_account'])

#---------------------------------------------------------------

# specify local folder locations
dir = os.getcwd()
raw_data_dir = f'{dir}/raw_data'
export_path = f'{dir}/data'

try:
    # creating a folder named data
    if not os.path.exists('raw_data'):
        os.makedirs('raw_data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

#---------------------------------------------------------------

# select the video and download it
video_uri = video_uri(option, credentials)
download_video_opencv(video_uri, credentials)
cam = cv2.VideoCapture('/tmp/video.mp4')

#---------------------------------------------------------------

# googleVideointelligence API video frames extract
results = track_objects(video_uri, credentials)

with open("results.p", "wb") as f:
    pickle.dump(results, f)

with open("results.p", "rb") as f:
    results = pickle.load(f)

food_entity_id = '/m/02wbm'
food_times = print_object_frames(results, food_entity_id)
food_times = sorted(set(food_times))[::5]

# with open('food_times.csv', 'w') as f:
#     for timing in food_times:
#         f.write(str(timing) + '\n')
#     f.close()

#---------------------------------------------------------------

# video frames export
sorted_dishes = sorted(glob.glob(raw_data_dir + "/*.jpg"),
                       key=lambda s: int(s.split('/')[-1].split('.')[0]))
export_raw_data(food_times, cam)
dishes = create_dish_list(sorted_dishes)
resized_dishes = create_resized_dish_list(dishes)
resized_dishes_2d = create_reshaped_dish_list(resized_dishes)
file_labels = dish_clustering_dataframe(resized_dishes_2d, sorted_dishes)
median_dish(file_labels, raw_data_dir, export_path)

#---------------------------------------------------------------

# model predict dishes

prediction = predict(export_path)

#---------------------------------------------------------------
st.markdown('#')
st.markdown('#')

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.title('**Bak Chor Mee**')
        st.image("https://static.streamlit.io/examples/cat.jpg")
        st.header('Calorie: 50')
        st.button('Register your calorie')

    with col2:
        st.title('**Kaya Toast**')
        st.image("https://static.streamlit.io/examples/dog.jpg")
        st.header('Calorie: 50')
        st.button('Register your calorie')

    with col3:
        st.title('**Chicken Rice**')
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.header('Calorie: 50')
        st.button('Register your calorie')

    with col4:
        st.title('**Hokkien Mee**')
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.header('Calorie: 50')
        st.cbutton('Register your calorie')

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text("Bak Chor Mee")
        st.image("https://static.streamlit.io/examples/cat.jpg")
        st.checkbox('Select')

    with col2:
        st.text("Kaya Toast")
        st.image("https://static.streamlit.io/examples/dog.jpg")
        st.checkbox('Select')

    with col3:
        st.text("Mee Siam")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.checkbox('Select')

    with col4:
        st.text("Hokkien Mee")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.checkbox('Select')

st.markdown('#')
st.markdown('#')

st.header("Total Calories : ")
st.success("Your choice has been submitted!")
