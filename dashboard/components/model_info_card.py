# dashboard/components/model_info_card.py

import streamlit as st


def render_model_info_card():
    """
    Display information about the trained machine learning model.
    """

    html = (
        '<div class="model-card">'
        '<h3>Model Information</h3>'

        '<p><strong>Model used:</strong> Random Forest</p>'

        '<p><strong>Purpose:</strong> PCOS risk prediction</p>'

        '<p><strong>Explainability method:</strong> SHAP and LIME</p>'

        '<p><strong>Input type:</strong> Clinical and lifestyle features</p>'

        '<p><strong>Input limits:</strong> The input ranges used in this dashboard '
        'are based on the minimum and maximum values found in the training dataset. '
        'These limits were added to prevent unrealistic values from being entered '
        'into the academic prototype. They should not be interpreted as medical '
        'or diagnostic thresholds.</p>'

        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)