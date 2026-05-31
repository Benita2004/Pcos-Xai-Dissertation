# dashboard/components/header.py

import streamlit as st


def render_header():
    """
    Render the dashboard header section.
    """

    st.markdown(
        """
        <div class="main-header">
            <div class="header-icon">🦋</div>
            <div>
                <h1>PCOS Prediction and Explainable AI Dashboard</h1>
                <p>
                    This system predicts the likelihood of Polycystic Ovary Syndrome (PCOS)
                    using a Random Forest machine learning model with SHAP explainability.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    