import tensorflow as tf
import numpy as np
import streamlit as st
from tensorflow import keras
from PIL import Image

model = tf.keras.models.load_model("D:\predict_traffic_sign\model.h5", compile=False)

img = st.file_uploader("Upload your image")
image = Image.open(img)
st.image(image, caption='test')

resize_image = image.resize([30, 30])
array_image = np.array(resize_image)
img_array = array_image.reshape((1,) + array_image.shape)

predict = np.argmax(model.predict(resize_image), axis=-1)
st.write(predict)