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


def test_train_test_split_worked():
    assert len(X_train) > 0
    assert len(X_test) > 0


def test_missing_values_removed():
    assert X_train.isnull().sum().sum() == 0
    assert X_test.isnull().sum().sum() == 0


def test_feature_scaling_completed():
    assert X_train_scaled.shape[0] == X_train.shape[0]
    assert X_test_scaled.shape[0] == X_test.shape[0]


def test_target_variables_exist():
    assert y_train is not None
    assert y_test is not None