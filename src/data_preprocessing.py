# data_preprocessing.py

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def cap_outliers(df, column):
    """
    Cap extreme outliers using the IQR method.
    """

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    df[column] = np.where(
        df[column] > upper_bound,
        upper_bound,
        np.where(df[column] < lower_bound, lower_bound, df[column])
    )

    return df


def preprocess_data(df):
    """
    Apply preprocessing steps used in the PCOS dissertation project.
    """

    # Clean column names
    df.columns = df.columns.str.strip()

    # Remove unnecessary column
    if "Unnamed: 44" in df.columns:
        df.drop(columns=["Unnamed: 44"], inplace=True)

    # Fill missing values using median imputation
    if "Marriage Status (Yrs)" in df.columns:
        df["Marriage Status (Yrs)"] = df["Marriage Status (Yrs)"].fillna(
            df["Marriage Status (Yrs)"].median()
        )

    if "Fast food (Y/N)" in df.columns:
        df["Fast food (Y/N)"] = df["Fast food (Y/N)"].fillna(
            df["Fast food (Y/N)"].median()
        )

    # Hormone-related features used for outlier handling
    hormone_features = ["FSH(mIU/mL)", "LH(mIU/mL)", "FSH/LH"]

    # Apply controlled IQR capping to hormone-related features
    for feature in hormone_features:
        if feature in df.columns:
            df = cap_outliers(df, feature)

    # Remove identifier-related columns
    identifier_columns = ["Sl. No", "Patient File No."]

    for column in identifier_columns:
        if column in df.columns:
            df.drop(columns=[column], inplace=True)

    # Separate features and target variable
    X = df.drop(columns=["PCOS (Y/N)"])
    y = df["PCOS (Y/N)"]

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Convert object columns to numeric
    object_columns = X_train.select_dtypes(include=["object"]).columns

    for column in object_columns:
        X_train[column] = pd.to_numeric(X_train[column], errors="coerce")
        X_test[column] = pd.to_numeric(X_test[column], errors="coerce")

    # Fill any remaining missing values after conversion
    train_medians = X_train.median()

    X_train = X_train.fillna(train_medians)
    X_test = X_test.fillna(train_medians)

    # Scale features
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Preprocessing completed successfully.")

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        X_train_scaled,
        X_test_scaled,
        scaler
    )