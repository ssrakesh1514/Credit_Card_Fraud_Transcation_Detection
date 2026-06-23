# Credit Card Fraud Detection API

A simple machine learning project that detects potentially fraudulent credit card transactions and exposes the prediction through a REST API built with Flask.

The project uses a Logistic Regression model trained on transaction data and provides a prediction endpoint that can be consumed by external applications or tested using Postman.

## Features

* Fraud prediction using a trained Logistic Regression model
* REST API built with Flask
* Input validation for incoming requests
* Request and prediction logging
* Unit testing using Pytest
* Model persistence using Pickle

## Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Pytest

## Project Structure


credit-card-fraud-api/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
├── app.log
│
├── tests/
│   └── test_api.py
│
└── CreditCard Fraud Detection.ipynb


## Running the Application

Clone the repository and install the required packages.


pip install -r requirements.txt

Start the Flask server:


python app.py

The application will be available at:


http://127.0.0.1:5000


## API Endpoint

### Predict Fraud

**POST** 

#### Sample Request


{
  "Unnamed_0": 1,
  "cc_num": 123456,
  "amt": 500,
  "zip": 10001,
  "lat": 40,
  "long": -80,
  "city_pop": 100000,
  "unix_time": 1371816865,
  "merch_lat": 40.5,
  "merch_long": -80.2,
  "hour": 14,
  "day": 23,
  "month": 6
}


#### Sample Response


{
  "fraud_prediction": 0
}


Where:

* `0` = Legitimate Transaction
* `1` = Fraudulent Transaction

## Validation

The API validates incoming requests and returns an error message if any required field is missing.

Example:


{
  "error": "amt is missing"
}


## Logging

Prediction requests are logged to `app.log`  for basic audit tracking and troubleshooting.

Example log entry:


2026-06-23 17:30:15 - Prediction=0, Amount=500


## Testing

Run the unit tests using:


python -m pytest


## Future Improvements

* Support batch transaction scoring
* Add model performance monitoring
* Containerize the application using Docker
* Deploy to a cloud platform
* Experiment with advanced fraud detection models such as Random Forest and XGBoost



Rakesh

Built as a hands-on machine learning and backend development project to understand model deployment, API development, validation, testing, and logging workflows.
