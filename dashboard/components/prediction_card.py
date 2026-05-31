# dashboard/components/prediction_card.py

import streamlit as st


def render_prediction_card(prediction_label=None, probability=None):
    """
    Display the PCOS prediction result card.
    """

    st.markdown(
        """
        <div class="prediction-card">
            <h3>Prediction Result</h3>
        """,
        unsafe_allow_html=True
    )

    if prediction_label is None:
        st.markdown(
            """
            <p class="prediction-placeholder">
                Enter patient details in the sidebar and click Predict PCOS to view the result.
            </p>
            """,
            unsafe_allow_html=True
        )

    else:
        if prediction_label == "PCOS Detected":
            result_class = "prediction-positive"
        else:
            result_class = "prediction-negative"

        st.markdown(
            f"""
            <div class="{result_class}">
                <h2>{prediction_label}</h2>
                <p>Prediction confidence: <strong>{probability}%</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True
    )