# dashboard/app.py

import streamlit as st
from pathlib import Path

from components.header import render_header
from components.sidebar import render_sidebar
from components.prediction_card import render_prediction_card
from components.probability_card import render_probability_card
from components.model_info_card import render_model_info_card
from components.shap_section import render_shap_section

from utils.model_loader import load_model_and_scaler
from utils.input_processor import prepare_input
from utils.predictor import make_prediction


# Page configuration
st.set_page_config(
    page_title="HerVita AI",
    page_icon="🌸",
    layout="wide"
)


# Load custom CSS
css_path = Path(__file__).parent / "assets" / "styles.css"

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load trained model and scaler
model, scaler = load_model_and_scaler()


# Header
render_header()


# Sidebar inputs
user_inputs, predict_button = render_sidebar()


# Default values before prediction
prediction_label = None
probability_percent = None


# Make prediction only when button is clicked
if predict_button:
    input_df = prepare_input(user_inputs)

    prediction, probability, scaled_input = make_prediction(
        model,
        scaler,
        input_df
    )

    if prediction == 1:
        prediction_label = "PCOS Detected"
    else:
        prediction_label = "No PCOS Detected"

    probability_percent = round(probability * 100, 2)


# Prediction and probability cards
col1, col2 = st.columns(2)

with col1:
    render_prediction_card(
        prediction_label=prediction_label,
        probability=probability_percent
    )

with col2:
    render_probability_card(
        probability=probability_percent
    )


# SHAP placeholder section
render_shap_section()


# Model information section
render_model_info_card()


# Medical disclaimer
# Medical disclaimer
st.markdown(
    """
    <div class="disclaimer-card">
        <h4>Medical Disclaimer</h4>
        <p>
            HerVita AI is an academic prototype developed for a final-year dissertation project.
            It is not a medical diagnostic tool and should not replace advice from a qualified
            healthcare professional.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)