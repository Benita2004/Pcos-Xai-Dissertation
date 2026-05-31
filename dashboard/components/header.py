# dashboard/components/header.py

import streamlit as st
from pathlib import Path


def render_header():
    """
    Render the dashboard header section with an optional logo image.
    """

    # Get the path to the image safely
    BASE_DIR = Path(__file__).resolve().parent.parent
    logo_path = BASE_DIR / "assets" / "images" / "Benita.png"

    # If the image exists, show it. If not, use the butterfly emoji.
    if logo_path.exists():
        header_icon = f'<img src="data:image/png;base64,{get_image_base64(logo_path)}" class="header-logo">'
    else:
        header_icon = "🦋"

    st.markdown(
        f"""
        <div class="main-header">
            <div class="header-icon">{header_icon}</div>
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


def get_image_base64(image_path):
    """
    Convert image to base64 so it can be displayed inside HTML.
    """
    import base64

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()