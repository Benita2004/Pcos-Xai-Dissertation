# explainability.py

# Import libraries
import shap
import pandas as pd
import matplotlib.pyplot as plt

# Import LIME explainer
from lime.lime_tabular import LimeTabularExplainer


# Create SHAP Explainer
def create_shap_explainer(model):

    """
    Create a SHAP TreeExplainer for the trained model.
    """

    explainer = shap.TreeExplainer(model)

    print("SHAP explainer created successfully.")

    return explainer


# Generate SHAP Values

def generate_shap_values(explainer, X_test_scaled):

    """
    Generate SHAP values for the testing dataset.
    """

    shap_values = explainer.shap_values(X_test_scaled)

    print("SHAP values generated successfully.")

    return shap_values



# SHAP Summary Plot

def plot_shap_summary(shap_values, X_test, feature_names):

    """
    Display SHAP summary plot for feature importance analysis.
    """

    shap.summary_plot(
        shap_values[:, :, 1],
        X_test,
        feature_names=feature_names
    )



# SHAP Waterfall Plot

def plot_shap_waterfall(explainer, shap_values, X_test, feature_names):

    """
    Display SHAP waterfall plot for a single prediction.
    """

    shap.plots.waterfall(
        shap.Explanation(
            values=shap_values[:, :, 1][0],
            base_values=explainer.expected_value[1],
            data=X_test.iloc[0],
            feature_names=feature_names
        )
    )



# Create LIME Explainer

def create_lime_explainer(X_train_scaled, feature_names):

    """
    Create LIME explainer for local prediction explanations.
    """

    lime_explainer = LimeTabularExplainer(
        training_data=X_train_scaled,
        feature_names=feature_names,
        class_names=["No PCOS", "PCOS"],
        mode="classification"
    )

    print("LIME explainer created successfully.")

    return lime_explainer



# Generate LIME Explanation

def generate_lime_explanation(
    lime_explainer,
    X_test_scaled,
    model
):

    """
    Generate LIME explanation for a single prediction.
    """

    lime_exp = lime_explainer.explain_instance(
        X_test_scaled[0],
        model.predict_proba,
        num_features=10
    )

    print("LIME explanation generated successfully.")

    return lime_exp

# Plot LIME Bar Chart
def plot_lime_bar_chart(lime_exp):
    """
    Display LIME explanation as a horizontal bar chart.
    """

    # Convert LIME explanation into a DataFrame
    lime_df = pd.DataFrame(
        lime_exp.as_list(),
        columns=["Feature", "Contribution"]
    )

    # Sort values for cleaner visualisation
    lime_df = lime_df.sort_values(
        by="Contribution",
        ascending=True
    )

    # Create horizontal bar chart
    plt.figure(figsize=(10, 6))

    plt.barh(
        lime_df["Feature"],
        lime_df["Contribution"]
    )

    plt.xlabel("Feature Contribution")
    plt.ylabel("Feature")
    plt.title("LIME Explanation for Individual PCOS Prediction")

    plt.tight_layout()
    plt.show()