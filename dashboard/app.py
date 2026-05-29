import streamlit as st

from components.header import render_header
from components.sidebar import render_sidebar
from components.prediction_card import render_prediction_card

st.set_page_config(
    page_title="HerVita AI",
    page_icon="🌸",
    layout="wide"
)

render_header()

user_inputs, predict_button = render_sidebar()

if predict_button:
    render_prediction_card(
        prediction_label="PCOS Detected",
        probability=84
    )
else:
    render_prediction_card()