# LEGO Character Classifier

A web application that identifies LEGO characters from Marvel or Star Wars using a ResNet model built with TensorFlow. Users can upload an image, and the app will predict the character displayed in the image.

## Features
- **Character Classification**: Upload an image of a LEGO character, and the app will predict whether it belongs to Marvel or Star Wars and identify the character.
- **Deep Learning Model**: Utilizes a ResNet model trained with TensorFlow for high accuracy.
- **Flask Backend**: Manages the server-side operations and prediction logic.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript (for file upload and user interface)
- **Backend**: Flask (Python)
- **Machine Learning**: TensorFlow (ResNet model)

## Getting Started
Download the file fully in you computer as the backend saves image at the same time and puts it into the model. If you run it by just cloning then it might show an error as even after saving the imaage in the static file the backend might not able to access the image as it had not been commited.
### Prerequisites
- Python 3.7+
- Virtual environment (recommended)
- TensorFlow
- Flask
- Any additional dependencies listed in `requirements.txt`


