# dashboard/components/header.py

import streamlit as st


def render_header():
    """
    Render the HerVita AI dashboard header.
    """

    st.title("HerVita AI")

    st.subheader(
        "PCOS Prediction & Explainable AI Dashboard"
    )

    st.write(
        """
        This dashboard was developed as part of a final-year Computer Science
        dissertation exploring the use of Explainable Artificial Intelligence
        for Polycystic Ovary Syndrome (PCOS) prediction.
        """
    )

    st.info(
        "Users can enter patient information, receive a PCOS prediction, "
        "view model confidence, and understand the prediction through SHAP explanations."
    )
    