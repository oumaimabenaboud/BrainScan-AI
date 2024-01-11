# BrainScan-AI

BrainScan AI is a web application providing an innovative solution for the detection of brain tumors using artificial intelligence (AI). This repository contains the code and resources for the BrainScan AI project.

- [Overview](#overview)
- [Usage](#usage)
- [DataSet Description](#dataset-description)
- [AI Model Development](#ai-model-development)
  - [Model Architecture](#model-architecture)
  - [Key Model Steps](#key-model-steps)
- [Deployment](#deployment)
- [User Interface](#user-interface)

## Overview

BrainScan AI provides a fast, efficient, and accessible solution for detecting brain tumors. It offers a non-invasive alternative to current detection methods and can enhance the accuracy of brain tumor detection. Our platform plays a crucial role in improving the prevention and treatment of brain-related diseases.

## Usage

Users can upload a brain MRI image to the website, which will then be analyzed using a pre-trained AI model to detect tumors. The output includes the detection result (whether a tumor is present or not) and its classification.

## DataSet Description

The dataset used in this project comprises images of brain tumors categorized into four classes:
1. Glioma Tumor
2. Meningioma Tumor
3. Pituitary Tumor
4. No Tumor Detected

There are approximately 500 images in each class, totaling 2000 images in the dataset. The images, sourced from an open repository, have a resolution of 150x150 pixels.

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

To integrate the brain tumor detection CNN model into our website, the following general steps were followed:

1. **Model Saving:**
   - Utilize Keras' `model.save()` function to save the trained model as an .h5 file.

2. **Model Loading:**
   - Load the .h5 file on your web server using Keras' `keras.models.load_model()` function, which loads a previously saved model from a file.

## User Interface
1. Landing Page![1](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/cdd81187-7128-456f-9f4b-b288ea4e107c)

2. About Us Section![2](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/8d0d473b-2a9e-47c6-b03a-7a555144f91a)

3. Team Section![3](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/05fd5d27-d3da-4b31-ae0a-5a53a6115fd9)

4. Contact Us Section![4](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/63fa017e-55f0-4af0-896a-0f09e1b63aff)

5. MRI Image Upload Interface![5](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/5e62c640-d718-4394-a94c-b751fffa0512)

6. Tumor Detection Result Display![6](https://github.com/oumaimabenaboud/BrainScan-AI/assets/120368654/36dde5dd-33bc-42b5-8744-9b49da2d782b)

