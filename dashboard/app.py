import streamlit as st
import os

st.write(os.getcwd())

from components.header import render_header
from components.sidebar import render_sidebar
from components.prediction_card import render_prediction_card
from components.model_info_card import render_model_info_card
from components.disclaimer import render_disclaimer
from components.shap_section import render_shap_section

st.set_page_config(
    page_title="HerVita AI",
    page_icon="🌸",
    layout="wide"
)


# Load custom CSS
with open("dashboard/assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


render_header()

user_inputs, predict_button = render_sidebar()

col1, col2 = st.columns(2)

with col1:
    if predict_button:
        render_prediction_card(
            prediction_label="PCOS Detected",
            probability=84
        )
    else:
        render_prediction_card()

with col2:
    render_model_info_card()

render_shap_section()

render_disclaimer()

