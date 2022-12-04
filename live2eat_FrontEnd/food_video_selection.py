import time
import statistics
import numpy as np
import pandas as pd
import cv2
import numpy as np
import pickle
import glob
import os
import streamlit as st

from typing import Optional, Sequence
from datetime import timedelta
from google.oauth2 import service_account
from sklearn.cluster import KMeans

from google.cloud import videointelligence as vi
from google.cloud import storage



def video_uri(option, credentials):
    video_client = vi.VideoIntelligenceServiceClient(credentials=credentials)
    if option == 'Video 1':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Bak Chor Mee.mp4'
    if option == 'Video 2':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Hokkien Mee.mp4'
    if option == 'Video 3':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Kaya Toast.mp4'
    if option == 'Video 5':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Chicken Rice.mp4'
    elif option == 'Video 4':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Chilli Crab.mp4'

    return video_uri



def download_video_opencv(video_uri, credentials):

    last_path = os.sep.join(os.path.normpath(video_uri).split(os.sep)[-2:])
    bucket = storage.Client(
        credentials=credentials).bucket('live2eat-bootcamp')
    blob = bucket.blob(last_path)
    download_path = os.path.join(os.getcwd(), 'video.mp4')
    print('Video downloaded to: ', download_path)
    blob.download_to_filename(download_path)
