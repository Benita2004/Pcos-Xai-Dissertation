# dashboard/components/prediction_card.py

import streamlit as st


def render_prediction_card(prediction_label=None, probability=None):
    """
    Display the PCOS prediction result card.
    """

    if prediction_label is None:
        st.markdown(
            """
            <div class="prediction-card">
                <h3>Prediction Result</h3>
                <p class="prediction-placeholder">
                    Enter patient details in the sidebar and click
                    <strong>Predict PCOS</strong> to view the result.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        if prediction_label == "PCOS Detected":
            result_class = "prediction-positive"
            result_message = "The model predicts that the patient is likely to have PCOS."
        else:
            result_class = "prediction-negative"
            result_message = "The model predicts that the patient is unlikely to have PCOS."

        st.markdown(
            f"""
            <div class="prediction-card">
                <h3>Prediction Result</h3>
                <div class="{result_class}">
                    <h2>{prediction_label}</h2>
                    <p>{result_message}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )