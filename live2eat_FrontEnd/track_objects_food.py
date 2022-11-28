from google.cloud import videointelligence as vi
import time
from typing import Optional, Sequence
from datetime import timedelta


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

    video_client = vi.VideoIntelligenceServiceClient(credentials=credentials)

    return video_uri


def track_objects(
    video_uri: str,
    segments: Optional[Sequence[vi.VideoSegment]] = None
) -> vi.VideoAnnotationResults:

    video_client = vi.VideoIntelligenceServiceClient()
    features = [vi.Feature.OBJECT_TRACKING]
    context = vi.VideoContext(segments=segments)
    request = vi.AnnotateVideoRequest(
        input_uri=video_uri,
        features=features,
        video_context=context,
    )
    print(f'Processing video "{video_uri}"...')

    operation = video_client.annotate_video(request)
    return operation.result().annotation_results[0]


segment = vi.VideoSegment(
    start_time_offset=timedelta(seconds=1),
    end_time_offset=timedelta(seconds=240),
    )
results = track_objects(video_uri, [segment])

def print_object_frames(
    results: vi.VideoAnnotationResults, entity_id: str, min_confidence: float = 0.7
):
    def keep_annotation(annotation: vi.ObjectTrackingAnnotation) -> bool:
        return all(
            [
                annotation.entity.entity_id == entity_id,
                min_confidence <= annotation.confidence,
            ]
        )

    annotations = results.object_annotations
    annotations = [a for a in annotations if keep_annotation(a)]
    for annotation in annotations:
        description = annotation.entity.description
        confidence = annotation.confidence
        print(
            f" {description},"
            f" confidence: {confidence:.0%},"
            f" frames: {len(annotation.frames)} ".center(80, "-")
        )
        for frame in annotation.frames:
            t = frame.time_offset.total_seconds()
            box = frame.normalized_bounding_box
            print(
                f"{t:>7.3f}",
                f"({box.left:.5f}, {box.top:.5f})",
                f"({box.right:.5f}, {box.bottom:.5f})",
                sep=" | ",
            )

food_entity_id = '/m/02wbm'
print_object_frames(results, food_entity_id)
