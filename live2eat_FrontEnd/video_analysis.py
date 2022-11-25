from google.cloud import videointelligence_v1 as videointelligence
import time


def video_analysis_googleapi(option, credentials):

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

    # video_client = videointelligence.VideoIntelligenceServiceClient.from_service_account_file(
    #     credentials)

    features = [
        videointelligence.Feature.OBJECT_TRACKING,
        videointelligence.Feature.SPEECH_TRANSCRIPTION
        # videointelligence.Feature.LABEL_DETECTION,
        # videointelligence.Feature.SHOT_CHANGE_DETECTION,s
        # videointelligence.Feature.LOGO_RECOGNITION,
        # videointelligence.Feature.EXPLICIT_CONTENT_DETECTION,
        # videointelligence.Feature.TEXT_DETECTION,
        # videointelligence.Feature.FACE_DETECTION,
        # videointelligence.Feature.PERSON_DETECTION
    ]

    transcript_config = videointelligence.SpeechTranscriptionConfig(
        language_code="en-US", enable_automatic_punctuation=True)

    # person_config = videointelligence.PersonDetectionConfig(
    #     include_bounding_boxes=True,
    #     include_attributes=False,
    #     include_pose_landmarks=True,
    # )

    # face_config = videointelligence.FaceDetectionConfig(
    #     include_bounding_boxes=True, include_attributes=True
    # )

    video_context = videointelligence.VideoContext(
        speech_transcription_config=transcript_config)
    # person_detection_config=person_config,
    # face_detection_config=face_config)

    operation = credentials.annotate_video(
        request={
            "features": features,
            "input_uri": gcs_uri,
            "output_uri": output_uri,
            "video_context": video_context
        })

    print("\nProcessing video.", operation)

    result = operation.result(timeout=300)

    print("\n finnished processing.")

    output_uri = "gs://videozzz/output - {}.json".format(time.time())

    return output_uri
