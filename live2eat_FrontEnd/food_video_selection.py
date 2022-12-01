import time
import statistics
import numpy as np
import pandas as pd
import cv2
import numpy as np
import pickle
import glob
import os

from typing import Optional, Sequence
from datetime import timedelta
from google.oauth2 import service_account
from sklearn.cluster import KMeans

from google.cloud import videointelligence as vi
from google.cloud import storage


def video_uri(option, credentials):
    video_client = vi.VideoIntelligenceServiceClient(credentials=credentials)
    if option == 'Bak Chor Mee':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Bak Chor Mee.mp4'
    if option == 'Hokkien Mee':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Hokkien Mee.mp4'
    if option == 'Kaya Toast':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Kaya Toast.mp4'
    if option == 'Chicken Rice':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Chicken Rice.mp4'
    elif option == 'Chilli Crab':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Chilli Crab.mp4'

    return video_uri


def download_video_opencv(video_uri, credentials):

    last_path = os.sep.join(os.path.normpath(video_uri).split(os.sep)[-2:])
    bucket = storage.Client(
        credentials=credentials).bucket('live2eat-bootcamp')
    blob = bucket.blob(last_path)
    blob.download_to_filename('/tmp/video.mp4')
