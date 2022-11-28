from google.cloud import videointelligence_v1 as vi
import time
from typing import Optional, Sequence
from datetime import timedelta


def gcs_uri(option, credentials):

    if option == 'Bak Chor Mee':
        gcs_uri = 'https://storage.cloud.google.com/live2eat-project-url/Dish%20Videos/Bak%20Chor%20Mee.mp4?authuser=0'
    if option == 'Hokkien Mee':
        gcs_uri = 'https://storage.cloud.google.com/live2eat-project-url/Dish%20Videos/Hokkien%20Mee.mp4?authuser=0'
    if option == 'Kaya Toast':
        gcs_uri = 'http://storage.cloud.google.com/live2eat-project-url/Dish%20Videos/Kaya%20Toast.mp4?authuser=0'
    if option == 'Laksa':
        gcs_uri = 'https://storage.cloud.google.com/live2eat-project-url/Dish%20Videos/Laksa.mp4?authuser=0'
    if option == 'Mee Rubus':
        gcs_uri = 'https://storage.cloud.google.com/live2eat-project-url/Dish%20Videos/Mee%20Rebus.mp4?authuser=0'
    elif option == 'Mee Siam':
        gcs_uri = 'https://storage.cloud.google.com/live2eat-project-url/Dish%20Videos/Mee%20Siam.mp4?authuser=0'

    video_client = vi.VideoIntelligenceServiceClient(credentials=credentials)

    return gcs_uri


def segments():
    segment = vi.VideoSegment(
        start_time_offset=timedelta(seconds=1),
        end_time_offset=timedelta(seconds=240),
    )
    return segment


def track_objects(
    gcs_uri: str,
    segments: Optional[Sequence[vi.VideoSegment]] = None
) -> vi.VideoAnnotationResults:

    video_client = vi.VideoIntelligenceServiceClient()
    features = [vi.Feature.OBJECT_TRACKING]
    context = vi.VideoContext(segments=segments)
    request = vi.AnnotateVideoRequest(
        input_uri=gcs_uri,
        features=features,
        video_context=context,
    )
    print(f'Processing video "{gcs_uri}"...')

    operation = video_client.annotate_video(request)
    results = operation.result().annotation_results[0]

    return results


def print_object_frames(results: vi.VideoAnnotationResults,
                        entity_id: str,
                        min_confidence: float = 0.7):

    def keep_annotation(annotation: vi.ObjectTrackingAnnotation) -> bool:
        return all([
            annotation.entity.entity_id == entity_id,
            min_confidence <= annotation.confidence,
        ])

    annotations = results.object_annotations
    annotations = [a for a in annotations if keep_annotation(a)]
    for annotation in annotations:
        description = annotation.entity.description
        confidence = annotation.confidence
        print(f" {description},"
              f" confidence: {confidence:.0%},"
              f" frames: {len(annotation.frames)} ".center(80, "-"))
        for frame in annotation.frames:
            t = frame.time_offset.total_seconds()
            box = frame.normalized_bounding_box
            print(
                f"{t:>7.3f}",
                f"({box.left:.5f}, {box.top:.5f})",
                f"({box.right:.5f}, {box.bottom:.5f})",
                sep=" | ",
            )

    return annotations
