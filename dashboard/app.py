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
    page_title="PCOS XAI Dashboard",
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


# Store prediction result so it does not disappear after Streamlit reruns
if "prediction_label" not in st.session_state:
    st.session_state.prediction_label = None

if "probability_percent" not in st.session_state:
    st.session_state.probability_percent = None

if "input_df" not in st.session_state:
    st.session_state.input_df = None

if "scaled_input" not in st.session_state:
    st.session_state.scaled_input = None


# Header
render_header()


# Sidebar inputs
user_inputs, predict_button = render_sidebar()


# Make prediction only when button is clicked
if predict_button:
    try:
        input_df = prepare_input(user_inputs)

        prediction, probability, scaled_input = make_prediction(
            model,
            scaler,
            input_df
        )

        if prediction == 1:
            st.session_state.prediction_label = "PCOS Detected"
        else:
            st.session_state.prediction_label = "No PCOS Detected"

        st.session_state.probability_percent = round(probability * 100, 2)

        # Store inputs for SHAP explanations
        st.session_state.input_df = input_df
        st.session_state.scaled_input = scaled_input

    except ValueError as error:
        # Clear previous result when invalid input is entered
        st.session_state.prediction_label = None
        st.session_state.probability_percent = None
        st.session_state.input_df = None
        st.session_state.scaled_input = None

        # Show validation message beside the inputs, not across the main dashboard
        st.sidebar.error(str(error))


# Prediction and probability cards
col1, col2 = st.columns(2)

with col1:
    render_prediction_card(
        prediction_label=st.session_state.prediction_label,
        probability=st.session_state.probability_percent
    )

with col2:
    render_probability_card(
        probability=st.session_state.probability_percent
    )


# SHAP explanation section
render_shap_section(
    model=model,
    input_df=st.session_state.input_df,
    scaled_input=st.session_state.scaled_input
)


# Model information section
render_model_info_card()


# Medical disclaimer
st.markdown(
    """
    <div class="disclaimer-card">
        <h4>Medical Disclaimer</h4>
        <p>
            This system is designed for educational and research purposes only and should not
            replace professional medical diagnosis, advice, or treatment. Always consult a
            qualified healthcare professional for medical concerns.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)