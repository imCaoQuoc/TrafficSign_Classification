# **TRAFFIC SIGN CLASSIFIER**

---

### **INTRODUCTION**
This project is a traffic sign classifier built using Convolutional Neurol Networks (CNNs). The model is trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which consists of over 50,000 labeled images of 43 different classes of traffic signs. The model is able to classify traffic signs and the demo application allows users to upload an image of a traffic sign and receive a prediction of its class. In the future, I want to improve the project so that it can classify traffic sign in real-time.

Technologies I used:
  - [Pillow](https://pypi.org/project/Pillow/) to load an image.
  - [Numpy](https://numpy.org/) to handle array.
  - [Tensorflow](https://www.tensorflow.org/) to build a deep learning model.
  - [Sci-kit learn](https://www.tensorflow.org/) to processing data.
  - [Streamlit](https://streamlit.io/) to build a simple demo web.
  - [Streamlit documentation](https://www.youtube.com/playlist?list=PLtqF5YXg7GLmCvTswG32NqQypOuYkPRUE) to learn the basic of streamlit.

---

### **INSTALLATION**
I highly recommend you using Google Colab to run the TrafficSign.ipynb file because it already has backages and libraries I use. But if you want to run on your local machine, following the instruction below.
  - Install essential libraries and packages:
  
  ```
  pip install -r requirements.txt
  ```
  
  - Run demo:
  
  ```
  streamlit run TrafficApp.py
  ```

---

### **DATA INFORMATION** 

The source of our data is referred from Kaggle: [CLICK HERE](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign?ref=morioh.com&utm_source=morioh.com)

This data 43 classes, which stays for 43 types of traffic sign: 
- `0`: Speed limit (20km/h)
- `1`: Speed limit (30km/h)
- `2`: Speed limit (50km/h)
- `3`: Speed limit (60km/h)
- `4`: Speed limit (70km/h)
- `5`: Speed limit (80km/h)
- `6`: End of speed limit (80km/h)
- `7`: Speed limit (100km/h)
- `8`: Speed limit (120km/h)
- `9`: No passing
- `10`: No passing veh over 3.5 tons
- `11`: Right-of-way at intersection
- `12`: Priority road
- `13`: Yield
- `14`: Stop
- `15`: No vehicles
- `16`: Vehicle > 3.5 tons prohibited
- `17`: No entry
- `18`: General caution
- `19`: Dangerous curve left
- `20`: Dangerous curve right
- `21`: Double curve
- `22`: Bumpy road
- `23`: Slippery road
- `24`: Road narrows on the right
- `25`: Road work
- `26`: Traffic signals
- `27`: Pedestrians
- `28`: Children crossing
- `29`: Bicycles crossing
- `30`: Beware of ice/snow
- `31`: Wild animals crossing
- `32`: End speed + passing limits
- `33`: Turn right ahead
- `34`: Turn left ahead
- `35`: Ahead only
- `36`: Go straight or right
- `37`: Go straight or left
- `38`: Keep right
- `39`: Keep left
- `40`: Roundabout mandatory
- `41`: End of no passing
- `42`: End no passing vehicle > 3.5 tons

Data has 51869 labeled images, which splitted into 39239 images for training and 12630 images for testing.

---

### **CONVOLUTIONAL NEURAL NETWORK**

Convolutional Neural Networks (CNNs) are a type of deep learning algorithm that have proven to be highly effective in image recognition, classification, and other computer vision tasks. They are inspired by the structure and function of the human visual system, and use a series of convolutional layers to automatically learn and extract features from input images. These features are then processed through a series of fully connected layers, which make predictions about the class of the input image. CNNs have achieved state-of-the-art results in a wide range of applications, including object recognition, facial recognition, and self-driving cars.

In this repository, I provide an example of how to build a CNNs model using TensorFlow library in Python. The model is training on an [image dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign?ref=morioh.com&utm_source=morioh.com) and using to classify traffic signs.

---

### **DEMO**

#### 1. Uploading image

You need to upload your image, it should be in PNG format. 

---

### **RESULT**

A deom will return a traffic sign's class.

![alt text](https://github.com/imCaoQuoc/Healthcare_stroke_prediction/blob/main/DATA/Screenshot%202023-03-31%20202705.png)
