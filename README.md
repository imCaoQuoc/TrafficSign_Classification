# **TRAFFIC SIGN CLASSIFIER**

---

### **INTRODUCTION**
This project is a traffic sign classifier built using Convolutional Neurol Network (CNN). The model is trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which consists of over 50,000 labeled images of 43 different classes of traffic signs. The model is able to classify traffic signs and the demo application allows users to upload an image of a traffic sign and receive a prediction of its class. In the future, I want to improve the model so that it can classify traffic sign in real-time.

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

The source of our data is referred from Kaggle: [CLICK HERE](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

This data has 12 columns, which stayed for 12 factors may cause stroke. These factors include: 
  - `id`: unique identifier
  - `gender`: "Male", "Female" or "Other"
  - `age`: age of the patient
  - `hypertension`: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
  - `heart_disease`: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
  - `ever_married`: "No" or "Yes"
  - `work_type`: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
  - `Residence_type`: "Rural" or "Urban"
  - `avg_glucose_level`: average glucose level in blood
  - `bmi`: body mass index
  - `smoking_status`: "formerly smoked", "never smoked", "smokes" or "Unknown"
  - `stroke`: 1 if the patient had a stroke or 0 if not

Data has 5110 samples, where it has 201 missing values in column `bmi`.

---

### **NEURAL NETWORK**

The Sequential Model is a type of neural network architecture in which the layers of the network are arranged sequentially, with the output of one layer being the input to the next layer. This type of architecture is commonly used for deep learning tasks such as image and speech recognition, natural language processing, and more.

In this repository, I provide an example of how to build a sequential model using the TensorFlow library in Python. The model is trained on a [stroke dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) and used to classify whether someone could be stroke or not.

---

### **DEMO**

#### 1. Selecting features

You need to select features such as your gender, your age,... 

#### 2. Click `Start`

---

### **RESULT**

A model will return a number between 0 and 1, that would be a percentage of stroke you may get.

![alt text](https://github.com/imCaoQuoc/Healthcare_stroke_prediction/blob/main/DATA/Screenshot%202023-03-31%20202705.png)
