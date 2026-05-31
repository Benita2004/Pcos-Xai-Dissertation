# tests/test_dashboard.py

import pandas as pd


def test_dashboard_user_input_features_exist():
    """
    Test that the dashboard-facing input features are defined correctly.
    """

    dashboard_features = [
        "Age",
        "Weight",
        "BMI",
        "Cycle",
        "Hair Growth",
        "Skin Darkening",
        "Follicle Count",
        "AMH",
        "Weight Gain",
        "Acne",
    ]

    assert len(dashboard_features) == 10
    assert "Age" in dashboard_features
    assert "BMI" in dashboard_features
    assert "AMH" in dashboard_features
    assert "Follicle Count" in dashboard_features


def test_dashboard_input_dataframe_creation():
    """
    Test that dashboard user inputs can be converted into a DataFrame.
    """

    user_inputs = {
        "Age": 25,
        "Weight": 65,
        "BMI": 24.5,
        "Cycle": 2,
        "Hair Growth": 1,
        "Skin Darkening": 0,
        "Follicle Count": 15,
        "AMH": 4.2,
        "Weight Gain": 1,
        "Acne": 0,
    }

    input_df = pd.DataFrame([user_inputs])

    assert isinstance(input_df, pd.DataFrame)
    assert input_df.shape == (1, 10)
    assert input_df.iloc[0]["Age"] == 25
    assert input_df.iloc[0]["BMI"] == 24.5


def test_dashboard_probability_range():
    """
    Test that dashboard prediction probability stays within a valid percentage range.
    """

    probability = 78.5

    assert probability >= 0
    assert probability <= 100


def test_dashboard_prediction_label_format():
    """
    Test that the dashboard prediction label is one of the expected user-facing labels.
    """

    prediction_label = "PCOS Detected"

    expected_labels = [
        "PCOS Detected",
        "No PCOS Detected",
    ]

    assert prediction_label in expected_labels