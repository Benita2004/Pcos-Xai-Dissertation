# test_models.py

import sys
import os
import pandas as pd

# Allow access to project root directory
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.data_preprocessing import preprocess_data
from src.train_models import train_models


# Load cleaned dataset
df = pd.read_csv("data/processed/pcos_cleaned.csv")


# Run preprocessing
(
    X_train,
    X_test,
    y_train,
    y_test,
    X_train_scaled,
    X_test_scaled,
    scaler
) = preprocess_data(df)


# Train machine learning models
trained_models, predictions = train_models(
    X_train_scaled,
    y_train,
    X_test_scaled
)


# Test 1: Check models trained successfully

assert len(trained_models) > 0

print("Model training test passed.")


# Test 2: Check predictions generated

assert len(predictions) > 0

print("Prediction generation test passed.")


# Test 3: Check Random Forest predictions match test size

assert len(predictions["Random Forest"]) == len(y_test)

print("Random Forest prediction size test passed.")


# Test 4: Check Logistic Regression predictions match test size

assert len(predictions["Logistic Regression"]) == len(y_test)

print("Logistic Regression prediction size test passed.")