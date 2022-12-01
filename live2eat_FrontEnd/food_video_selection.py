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

    if option == 'Bak Chor Mee':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Bak Chor Mee.mp4'
    if option == 'Hokkien Mee':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Hokkien Mee.mp4'
    if option == 'Kaya Toast':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Kaya Toast.mp4'
    if option == 'Laksa':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Laksa.mp4'
    if option == 'Mee Rubus':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Mee Rebus.mp4'
    elif option == 'Mee Siam':
        video_uri = 'gs://live2eat-bootcamp/Dish Videos/Mee Siam.mp4'

    return video_uri


def download_video_opencv(video_uri):
    last_path = os.sep.join(os.path.normpath(video_uri).split(os.sep)[-2:])
    bucket = storage.Client().bucket('live2eat-bootcamp')
    blob = bucket.blob(last_path)
    blob.download_to_filename('/tmp/video.mp4')
