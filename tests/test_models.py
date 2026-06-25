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


def test_models_trained_successfully():
    assert len(trained_models) > 0


def test_predictions_generated():
    assert len(predictions) > 0


def test_random_forest_predictions_match_test_size():
    assert len(predictions["Random Forest"]) == len(y_test)


def test_logistic_regression_predictions_match_test_size():
    assert len(predictions["Logistic Regression"]) == len(y_test)