# test_preprocessing.py

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



# Test 1: Check train-test split worked


assert len(X_train) > 0
assert len(X_test) > 0

print("Train-test split test passed.")



# Test 2: Check missing values removed


assert X_train.isnull().sum().sum() == 0
assert X_test.isnull().sum().sum() == 0

print("Missing value handling test passed.")


# Test 3: Check scaling completed


assert X_train_scaled.shape[0] == X_train.shape[0]
assert X_test_scaled.shape[0] == X_test.shape[0]

print("Feature scaling test passed.")



# Test 4: Check target variable exists


assert y_train is not None
assert y_test is not None

print("Target variable test passed.")