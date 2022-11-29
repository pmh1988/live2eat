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
