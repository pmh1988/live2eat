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


def export_raw_data(food_times, cam):

    if cam.isOpened():

        while True:
            for time in food_times:

                # reading from frame
                ret, frame = cam.read()

                capture_time = time * 1000

                cam.set(cv2.CAP_PROP_POS_MSEC, capture_time)

                name = './raw_data/' + str(capture_time) + '.jpg'
                print('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)

                # Release all space and windows once done
                cam.release()
    cv2.destroyAllWindows()


def create_dish_list(sorted_dishes):
    dishes = []

    for dish in sorted_dishes:
        dish_image = cv2.imread(dish)
        dishes.append(dish_image)

    return dishes


def create_resized_dish_list(dishes):
    resized_dishes = []

    for dish_image in dishes:
        scale_percent = 25
        width = int(dish_image.shape[1] * scale_percent / 100)
        height = int(dish_image.shape[0] * scale_percent / 100)
        dsize = (width, height)
        # resize image
        resized_image = cv2.resize(dish_image, dsize)
        resized_dishes.append(resized_image)

    return resized_dishes


def create_reshaped_dish_list(resized_dishes):

    resized_dishes_2d = np.array(resized_dishes).reshape(330, 180 * 320 * 3)
    return resized_dishes_2d


def dish_clustering_dataframe(resized_dishes_2d, sorted_dishes):
    K = 4
    kmeans = KMeans(n_clusters=K, random_state=0)
    clusters = kmeans.fit(resized_dishes_2d.astype('uint8'))
    file_labels = pd.DataFrame({
        'files': sorted_dishes,
        'labels': clusters.labels_
    })
    file_labels['time'] = file_labels.files.str.split('/').str[-1].str.split(
        '.').str[0]

    return file_labels


def median_dish(file_labels, raw_data_dir, export_path):

    median_image_times = file_labels.groupby('labels')['time'].apply(
        statistics.median_low)

    for time in median_image_times:

        image = cv2.imread(f'{raw_data_dir}/{time}.0.jpg')
        cv2.imwrite(os.path.join(export_path, f'{time}.0.jpg'), image)
        cv2.waitKey(0)
    os.remove('/tmp/video.mp4')  # Delete tmp resources to free memory
