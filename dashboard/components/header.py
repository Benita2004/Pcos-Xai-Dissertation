import streamlit as st

def render_header():
    
    st.title("🌸 HerVita AI")

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
        "Users will be able to enter patient information, receive a PCOS prediction, "
        "view the model confidence, and understand the prediction through SHAP explanations."
    )