import os
from keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def predict(export_path):
    print(f'{export_path = }')

    model = load_model('my_model.h5')
    test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
    predict_data = test_datagen.flow_from_directory(os.path.join(
        os.getcwd(), 'data'),
                                                    batch_size=470,
                                                    shuffle=False,
                                                    class_mode='categorical')

    result = model.predict(predict_data)
    return result
