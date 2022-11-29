from google.cloud import videointelligence as vi
import time
from typing import Optional, Sequence
from datetime import timedelta
from google.oauth2 import service_account

video_uri = 'gs://live2eat-bootcamp/Dish Videos/BakChorMee.mp4'

client = vi.VideoIntelligenceServiceClient()
job = client.annotate_video(
    input_uri=video_uri,
    features=['LABEL_DETECTION'],
)
result = job.result()
print(result)
