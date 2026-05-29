import streamlit as st


def render_sidebar():

    st.sidebar.title("💗 Patient Input")

    st.sidebar.write(
        "Enter patient clinical and lifestyle information below."
    )

    age = st.sidebar.number_input(
        "Age (years)",
        min_value=10,
        max_value=60,
        value=26
    )

    weight = st.sidebar.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=150.0,
        value=68.0
    )

    bmi = st.sidebar.number_input(
        "BMI (kg/m²)",
        min_value=10.0,
        max_value=60.0,
        value=26.3
    )

    cycle_pattern = st.sidebar.selectbox(
        "Cycle Pattern (last 3–6 months)",
        [
            "Regular",
            "Irregular for less than 3 months",
            "Irregular for 3 months or more",
            "Missed periods for 3 months or more"
        ]
    )

    hair_growth = st.sidebar.selectbox(
        "Excess Hair Growth (Hirsutism)",
        ["No", "Yes"]
    )

    skin_darkening = st.sidebar.selectbox(
        "Skin Darkening",
        ["No", "Yes"]
    )

    follicle_count = st.sidebar.number_input(
        "Follicle Count (per ovary)",
        min_value=0,
        max_value=40,
        value=18
    )

    amh_level = st.sidebar.number_input(
        "AMH Level (ng/mL)",
        min_value=0.0,
        max_value=25.0,
        value=5.2
    )

    weight_gain = st.sidebar.selectbox(
        "Weight Gain (recent)",
        ["No", "Yes"]
    )

    acne = st.sidebar.selectbox(
        "Acne",
        ["No", "Yes"]
    )

    predict_button = st.sidebar.button("✨ Predict PCOS")

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

    return user_inputs, predict_button