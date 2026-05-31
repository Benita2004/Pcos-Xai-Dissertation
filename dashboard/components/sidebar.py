# dashboard/components/sidebar.py

import streamlit as st


def get_validation_error(value, field_name, min_value, max_value):
    """
    Return validation error message for sidebar text inputs.

    These limits are dataset-based validation ranges,
    not clinical diagnostic thresholds.
    """

    if value is None or str(value).strip() == "":
        return None

    try:
        value = float(value)
    except ValueError:
        return f"{field_name} must be a number."

    if value < min_value or value > max_value:
        return f"{field_name} must be between {min_value} and {max_value}."

    return None


def show_inline_error(message):
    """
    Show validation message directly under the related input.
    """

    if message:
        st.sidebar.markdown(
            f"""
            <div class="inline-validation-error">
                {message}
            </div>
            """,
            unsafe_allow_html=True
        )


def render_sidebar():
    """
    Render sidebar input fields for the PCOS prediction dashboard.
    """

    st.sidebar.markdown(
        """
        <div class="sidebar-title">
            <h2>💗 Patient Input</h2>
            <p>Enter patient clinical and lifestyle information below.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    has_validation_error = False

    age = st.sidebar.text_input(
        "Age (years)",
        placeholder="Enter age"
    )
    age_error = get_validation_error(age, "Age", 20, 48)
    show_inline_error(age_error)
    has_validation_error = age_error is not None or has_validation_error

    weight = st.sidebar.text_input(
        "Weight (kg)",
        placeholder="Enter weight"
    )
    weight_error = get_validation_error(weight, "Weight", 31, 108)
    show_inline_error(weight_error)
    has_validation_error = weight_error is not None or has_validation_error

    bmi = st.sidebar.text_input(
        "BMI (kg/m²)",
        placeholder="Enter BMI"
    )
    bmi_error = get_validation_error(bmi, "BMI", 12, 39)
    show_inline_error(bmi_error)
    has_validation_error = bmi_error is not None or has_validation_error

    cycle_pattern = st.sidebar.selectbox(
        "Cycle Pattern (last 3–6 months)",
        ["Regular", "Irregular"],
        index=None,
        placeholder="Select cycle pattern"
    )

    hair_growth = st.sidebar.selectbox(
        "Excess Hair Growth (Hirsutism)",
        ["No", "Yes"],
        index=None,
        placeholder="Select option"
    )

    skin_darkening = st.sidebar.selectbox(
        "Skin Darkening",
        ["No", "Yes"],
        index=None,
        placeholder="Select option"
    )

    follicle_count = st.sidebar.text_input(
        "Follicle Count (per ovary)",
        placeholder="Enter follicle count"
    )
    follicle_error = get_validation_error(
        follicle_count,
        "Follicle Count",
        0,
        22
    )
    show_inline_error(follicle_error)
    has_validation_error = follicle_error is not None or has_validation_error

    amh_level = st.sidebar.text_input(
        "AMH Level (ng/mL)",
        placeholder="Enter AMH level"
    )
    amh_error = get_validation_error(
        amh_level,
        "AMH Level",
        0,
        66
    )
    show_inline_error(amh_error)
    has_validation_error = amh_error is not None or has_validation_error

    weight_gain = st.sidebar.selectbox(
        "Weight Gain (recent)",
        ["No", "Yes"],
        index=None,
        placeholder="Select option"
    )

    acne = st.sidebar.selectbox(
        "Acne",
        ["No", "Yes"],
        index=None,
        placeholder="Select option"
    )

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    predict_button = st.sidebar.button(
        "Predict PCOS",
        disabled=has_validation_error
    )

    user_inputs = {
        "age": age,
        "weight": weight,
        "bmi": bmi,
        "cycle_pattern": cycle_pattern,
        "hair_growth": hair_growth,
        "skin_darkening": skin_darkening,
        "follicle_count": follicle_count,
        "amh_level": amh_level,
        "weight_gain": weight_gain,
        "acne": acne
    }

    st.sidebar.markdown(
        """
        <div class="sidebar-note">
            <p>
                Please enter the available patient details and click
                <strong>Predict PCOS</strong> to view the result.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    return user_inputs, predict_button