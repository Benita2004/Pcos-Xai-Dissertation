# dashboard/app.py

import streamlit as st
from pathlib import Path

from components.header import render_header
from components.sidebar import render_sidebar
from components.prediction_card import render_prediction_card
from components.model_info_card import render_model_info_card

from utils.model_loader import load_model_and_scaler
from utils.input_processor import prepare_input
from utils.predictor import make_prediction


# Page configuration
st.set_page_config(
    page_title="HerVita AI",
    page_icon="🌸",
    layout="wide"
)


# Load custom CSS safely
css_path = Path(__file__).parent / "assets" / "styles.css"

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load trained model and scaler
model, scaler = load_model_and_scaler()


# Render dashboard header
render_header()


# Render sidebar inputs
user_inputs, predict_button = render_sidebar()


# Main dashboard layout
col1, col2 = st.columns(2)


with col1:
    if predict_button:
        # Convert sidebar inputs into the 41-feature model input
        input_df = prepare_input(user_inputs)

        # Make prediction
        prediction, probability, scaled_input = make_prediction(
            model,
            scaler,
            input_df
        )

        # Convert model output into readable label
        if prediction == 1:
            prediction_label = "PCOS Detected"
        else:
            prediction_label = "No PCOS Detected"

        # Display prediction result
        render_prediction_card(
            prediction_label=prediction_label,
            probability=round(probability * 100, 2)
        )

    else:
        render_prediction_card()


with col2:
    render_model_info_card()


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