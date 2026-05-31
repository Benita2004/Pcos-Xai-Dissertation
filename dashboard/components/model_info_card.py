import streamlit as st


def render_model_info_card():

    st.markdown("### Model Information")

    st.write("**Model used:** Random Forest")
    st.write("**Purpose:** PCOS risk prediction")
    st.write("**Explainability method:** SHAP and LIME")
    st.write("**Input type:** Clinical and lifestyle features")