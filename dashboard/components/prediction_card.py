import streamlit as st


def render_prediction_card(prediction_label="Waiting for input", probability=None):

    st.markdown("###  Prediction Result")

    if probability is None:
        st.info("Enter patient details and click **Predict PCOS** to see the result.")
        return

    if prediction_label == "PCOS Detected":
        st.error(f"### {prediction_label}")
    else:
        st.success(f"### {prediction_label}")

    st.metric(
        label="Prediction Probability",
        value=f"{probability:.0f}%"
    )