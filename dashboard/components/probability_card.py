# dashboard/components/probability_card.py

import streamlit as st


def render_probability_card(probability=None):
    """
    Display the prediction probability card.
    """

    if probability is None:
        html = (
            '<div class="probability-card">'
            '<h3>Prediction Probability</h3>'
            '<div class="probability-ring">'
            '<div class="probability-value">--</div>'
            '</div>'
            '<p class="probability-status">Waiting for prediction</p>'
            '<p class="probability-description">'
            'Enter patient details and click <strong>Predict PCOS</strong> to view the probability.'
            '</p>'
            '</div>'
        )

    else:
        if probability >= 70:
            confidence_label = "High Confidence"
        elif probability >= 40:
            confidence_label = "Moderate Confidence"
        else:
            confidence_label = "Low Confidence"

        html = (
            '<div class="probability-card">'
            '<h3>Prediction Probability</h3>'
            '<div class="probability-ring">'
            f'<div class="probability-value">{probability}%</div>'
            '</div>'
            f'<p class="probability-status">{confidence_label}</p>'
            '<p class="probability-description">'
            f'There is a <strong>{probability}%</strong> probability that the patient has PCOS.'
            '</p>'
            '</div>'
        )

    st.markdown(html, unsafe_allow_html=True)