# dashboard/components/shap_section.py

import streamlit as st


def render_shap_section():
    """
    Display the SHAP explainability section.
    Placeholder version until real SHAP plots are connected.
    """

    st.markdown(
        """
        <div class="shap-section">
            <h3>Top Contributing Features (SHAP)</h3>
            <p>
                SHAP explanations will be displayed here after a prediction is made.
                This section will show which clinical and lifestyle features had the
                strongest influence on the model output.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )