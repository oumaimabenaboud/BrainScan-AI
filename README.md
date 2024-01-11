# BrainScan-AI

BrainScan AI is a web application providing an innovative solution for the detection of brain tumors using artificial intelligence (AI).

- [Overview](#overview)
- [Usage](#usage)
- [Dataset](#dataset)
- [AI Model Development](#ai-model-development)
  - [Model Architecture](#model-architecture)
  - [Key Model Steps](#key-model-steps)
- [Deployment](#deployment)
- [User Interface](#user-interface)
- [Setup Instructions](#setup-instructions)

## Overview

BrainScan AI provides a fast, efficient, and accessible solution for detecting brain tumors. It offers a non-invasive alternative to current detection methods and can enhance the accuracy of brain tumor detection. Our platform plays a crucial role in improving the prevention and treatment of brain-related diseases.

## Usage

Users can upload a brain MRI image to the website, which will then be analyzed using a pre-trained AI model to detect tumors. The output includes the detection result (whether a tumor is present or not) and its classification.

## Dataset
The dataset used in this project can be accessed via the following link: [Brain Tumor Classification DataSet](https://github.com/SartajBhuvaji/Brain-Tumor-Classification-DataSet).

This dataset includes images of brain tumors categorized into four classes:

1. Glioma Tumor
2. Meningioma Tumor
3. Pituitary Tumor
4. No Tumor Detected

Approximately 500 images are available for each class, resulting in a total of 2000 images in the dataset. The images have a resolution of 150x150 pixels and were obtained from an open repository.

## AI Model Development

### Model Architecture

The trained model is a CNN Model. Convolutional Neural Networks (CNNs) are employed to detect brain tumors from MRI images through machine learning.
- Convolutional layers, pooling layers, and normalization layers.
- Global average pooling layer.
- Dropout layer.
- Dense layer for final classification.

The training process incorporates validation data and employs decay reduction methods to fine-tune parameters.

### Key Model Steps

1. **Data Preparation:**
   - Brain tumor images are read from training and testing data folders, resized to 150x150 pixels, and randomly shuffled.
   - Labels for these images (glioma tumor, no tumor, meningioma tumor, pituitary tumor) are stored in separate arrays.

2. **Transfer Learning:**
   - The model utilizes a pre-trained neural network, EfficientNetB0, to extract features from images. This model was pre-trained on ImageNet for recognizing various objects.

3. **Model Training:**
   - The model is trained on the training data to learn how to classify images based on corresponding labels.
   - Metrics such as loss and accuracy are used to monitor training progress.

4. **Prediction:**
   - The model is used to predict labels for test images. Predictions are compared with actual labels to evaluate model accuracy.

5. **Evaluation:**
   - A confusion matrix is utilized to assess the classification model's performance, summarizing classification results by comparing true and predicted class labels.

## Deployment

### Model Saving:
1. Use Keras' `model.save()` in the notebook to save the trained model as an .h5 file.
2. Transfer the saved .h5 file to a folder in your web app.

### Model Loading:
1. In your web app's `views.py`, use `keras.models.load_model()` to load the saved model.
2. Ensure the path to the saved model file in the code matches the actual location in the web app.

## User Interface

| Landing Page | About Us Section | Team Section |
| --- | --- | --- |
| ![Landing Page](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/cdd81187-7128-456f-9f4b-b288ea4e107c) | ![About Us](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/8d0d473b-2a9e-47c6-b03a-7a555144f91a) | ![Team](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/05fd5d27-d3da-4b31-ae0a-5a53a6115fd9) |

| Contact Us Section | MRI Image Upload Interface | Tumor Detection Result Display |
| --- | --- | --- |
| ![Contact Us](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/63fa017e-55f0-4af0-896a-0f09e1b63aff) | ![MRI Image Upload](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/5e62c640-d718-4394-a94c-b751fffa0512) | ![Tumor Detection Result](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/36dde5dd-33bc-42b5-8744-9b49da2d782b) |

## Setup Instructions

Follow the steps below to set up the project environment and install the required dependencies.

### Step 1: Install Virtual Environment Wrapper (Windows)

```bash
py -m pip install virtualenvwrapper-win
```

### Step 2: Create Virtual Environment

```bash
py -m venv myvenv
```

### Step 3: Activate Virtual Environment

```bash
myvenv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
py -m pip install -r requirements.txt
```

These commands create a virtual environment named "myvenv" and activate it. Then, it installs the project dependencies listed in the "requirements.txt" file.

Now, your environment is set up, and you are ready to work on the project.
