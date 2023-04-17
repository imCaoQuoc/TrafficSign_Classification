import tensorflow as tf
import numpy as np
import streamlit as st
from tensorflow import keras
from PIL import Image

classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)',
            2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)',
            4:'Speed limit (70km/h)',
            5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection',
            12:'Priority road',
            13:'Yield',
            14:'Stop',
            15:'No vehicles',
            16:'Vehicle > 3.5 tons prohibited',
            17:'No entry',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road',
            23:'Slippery road',
            24:'Road narrows on the right',
            25:'Road work',
            26:'Traffic signals',
            27:'Pedestrians',
            28:'Children crossing',
            29:'Bicycles crossing',
            30:'Beware of ice/snow',
            31:'Wild animals crossing',
            32:'End speed + passing limits',
            33:'Turn right ahead',
            34:'Turn left ahead',
            35:'Ahead only',
            36:'Go straight or right',
            37:'Go straight or left',
            38:'Keep right',
            39:'Keep left',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing vehicle > 3.5 tons' }

model = tf.keras.models.load_model("D:\predict_traffic_sign\model.h5", compile=False)

img = st.sidebar.file_uploader("Upload your image")
if img is not None:
    image = Image.open(img)
    st.sidebar.image(image, caption='Your image')

    # Show original image size
    st.sidebar.write("Original image size:", image.size[0], "x", image.size[1])

    # Resize and display image
    resized_image = image.resize([300, 300])
    img_placeholder = st.sidebar.empty()
    img_placeholder.image(resized_image, caption='Resized image')

    # Add slider for zooming
    zoom = st.sidebar.slider("Zoom", 0.5, 2.0, 1.0, 0.1)
    new_width = int(resized_image.width * zoom)
    new_height = int(resized_image.height * zoom)

    # Add slider for horizontal and vertical translation
    h_translate = st.sidebar.slider("Horizontal Translation", -new_width // 2, new_width // 2, 0, 1)
    v_translate = st.sidebar.slider("Vertical Translation", -new_height // 2, new_height // 2, 0, 1)

    # Crop and display image
    left = (new_width - 300) // 2 - h_translate
    top = (new_height - 300) // 2 - v_translate
    right = left + 300
    bottom = top + 300
    cropped_image = resized_image.crop((left, top, right, bottom))
    img_array = np.array(cropped_image)
    img_placeholder.image(cropped_image, caption='Cropped image')

    predict = np.argmax(model.predict(np.expand_dims(img_array, axis=0)), axis=-1)
    st.write("Your image is " + str(predict[0]))
else:
    st.write("Please upload an image to get a prediction.")
