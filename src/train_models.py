# train_models.py

# Import Machine Learning Models

# Logistic Regression:
# A simple and interpretable linear model commonly used in healthcare research
from sklearn.linear_model import LogisticRegression

# Decision Tree:
# A tree-based algorithm that learns using feature-based decision splits
from sklearn.tree import DecisionTreeClassifier

# Random Forest:
# An ensemble learning model that combines multiple decision trees
from sklearn.ensemble import RandomForestClassifier

# Support Vector Machine (SVM):
# A model that separates classes using optimal decision boundaries
from sklearn.svm import SVC

# XGBoost:
# A gradient boosting algorithm designed for strong predictive performance
from xgboost import XGBClassifier


def train_models(X_train_scaled, y_train, X_test_scaled):

    """
    Train all machine learning models used in the PCOS dissertation project.
    """

    # Store trained models and predictions
    trained_models = {}
    predictions = {}


    # Logistic Regression Model
    
    log_model = LogisticRegression(random_state=42)

    log_model.fit(X_train_scaled, y_train)

    y_pred_log = log_model.predict(X_test_scaled)

    trained_models["Logistic Regression"] = log_model
    predictions["Logistic Regression"] = y_pred_log

    print("Logistic Regression model trained successfully.")

  

    # Decision Tree Model
   
    dt_model = DecisionTreeClassifier(random_state=42)

    dt_model.fit(X_train_scaled, y_train)

    y_pred_dt = dt_model.predict(X_test_scaled)

    trained_models["Decision Tree"] = dt_model
    predictions["Decision Tree"] = y_pred_dt

    print("Decision Tree model trained successfully.")


    # Random Forest Model
    
    rf_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    rf_model.fit(X_train_scaled, y_train)

    y_pred_rf = rf_model.predict(X_test_scaled)

    trained_models["Random Forest"] = rf_model
    predictions["Random Forest"] = y_pred_rf

    print("Random Forest model trained successfully.")

    # Support Vector Machine Model
  

    svm_model = SVC(
        kernel='rbf',
        probability=True,
        random_state=42
    )

    svm_model.fit(X_train_scaled, y_train)

    y_pred_svm = svm_model.predict(X_test_scaled)

    trained_models["SVM"] = svm_model
    predictions["SVM"] = y_pred_svm

    print("SVM model trained successfully.")

    
    # XGBoost Model
   

    xgb_model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        eval_metric='logloss'
    )

    xgb_model.fit(X_train_scaled, y_train)

    y_pred_xgb = xgb_model.predict(X_test_scaled)

    trained_models["XGBoost"] = xgb_model
    predictions["XGBoost"] = y_pred_xgb

    print("XGBoost model trained successfully.")

    # Return all trained models and predictions
    return trained_models, predictions
