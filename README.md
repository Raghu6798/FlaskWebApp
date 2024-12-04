# Stellar Classification Model WebApp

This project is a **Stellar Classification Web Application** built using **Flask**. The app allows users to input data about stellar objects and get predictions on the classification of the stars based on a machine learning model.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [What is Flask?](#what-is-flask)
- [How Flask Works](#how-flask-works)
- [Application Structure](#application-structure)
- [Running the Application](#running-the-application)
---

## Introduction

This is a simple **Stellar Classification WebApp** that uses a machine learning model to predict the class of a star based on its features. Users can enter values for various attributes of a star like `alpha`, `delta`, `u`, `g`, `r`, etc., and the app will output the predicted class. The web application is built using **Flask**, a lightweight Python framework used for building web applications.

---

## Technologies Used

- **Flask**: A micro web framework for Python that is used to build the web application.
- **HTML/CSS**: For creating and styling the user interface.
- **Python**: For the back-end, where we handle the machine learning model prediction.
- **Machine Learning Model (saved as `model.pkl`)**: A pre-trained model for stellar classification.
- **MinMaxScaler**: For scaling the input features before feeding them into the model.
- **LabelEncoder**: To transform the prediction output back into its original label format.

---

## What is Flask?

**Flask** is a micro web framework written in Python. It is considered "micro" because it is lightweight and minimal, providing the essential tools to get a web application up and running, while leaving developers the freedom to choose the other components they need (like databases or authentication mechanisms). Flask makes it easy to create web servers, handle requests, and render HTML templates. It is well-suited for small to medium-sized applications, including those that involve machine learning models.

Flask is used here because it provides a simple way to:

- Handle HTTP requests.
- Render HTML templates.
- Serve static files (like CSS or JavaScript files).
- Integrate with back-end Python code (for handling machine learning predictions).

---

## How Flask Works

Flask works on the **request-response cycle**. Here’s how it works in this application:

1. **User Request**: When a user accesses the application (via a browser), Flask listens for incoming HTTP requests.
2. **Route Handling**: Flask maps the incoming request (like GET or POST) to a specific function using **routes** (URLs). Each route is linked to a Python function (called a **view function**) that processes the request.
3. **Rendering Templates**: Flask renders HTML templates and returns the HTML response to the user's browser.
4. **Predicting with Machine Learning**: When the user submits the form with input data, the data is sent to Flask, which uses the machine learning model to make a prediction and then renders the result back to the user.

---

## Application Structure

Here's the folder structure of the application:

FlaskWebApp├
|───archive
│       star_classification.csv
│
├───models
│       label_encoder.pkl
│       model.pkl
│       scaler.pkl
│
├───ModelTraining
│       Training.py
│
├───static
│       styles.css
│
└───templates
        form.html
        result.html



- **archive/**: Contains the dataset (in this case, `star_classification.csv`) used for training the model.
- **ModelTraining/**: Contains the Python file for training the machine learning model.
- **templates/**: This folder holds the HTML files used to render the web pages (`form.html` for user input and `result.html` for showing predictions).
- **models/**: Contains the saved machine learning models (`model.pkl` for the classifier, `scaler.pkl` for feature scaling, and `label_encoder.pkl` for decoding predictions).

---

## Running the Application

To run the application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FlaskWebApp.git
   cd FlaskWebApp
2. ``` Install the required dependencies
   pip install -r requirements.txt

3. ``` Run the flask application
   python MLWeb.py
4. By default, the app will run on http://127.0.0.1:5000/.

Open the application in a web browser and start interacting with the form!
