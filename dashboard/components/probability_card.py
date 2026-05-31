# dashboard/components/probability_card.py

import streamlit as st


def render_probability_card(probability=None):
    """
    Display the prediction probability/confidence card.
    """

    if probability is None:
        probability_text = "--"
        confidence_label = "Waiting for prediction"
    else:
        probability_text = f"{probability}%"

        if probability >= 75:
            confidence_label = "High Confidence"
        elif probability >= 50:
            confidence_label = "Moderate Confidence"
        else:
            confidence_label = "Low Confidence"

    st.markdown(
        f"""
        <div class="dashboard-card probability-card">
            <h3>Prediction Probability</h3>
            <div class="probability-circle">
                <span>{probability_text}</span>
            </div>
            <p>{confidence_label}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

 