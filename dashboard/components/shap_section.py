import streamlit as st


def render_shap_section():

    st.markdown("### SHAP Explainability")

    st.info(
        """
        SHAP explanations will be displayed here to show which
        features contributed most to the model prediction.
        """
    )