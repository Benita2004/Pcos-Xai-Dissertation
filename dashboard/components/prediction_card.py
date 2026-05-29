import streamlit as st


def render_prediction_card(
        prediction_label="Waiting for input",
        probability=None):

    st.markdown("### Prediction Result")

    col1, col2 = st.columns([2, 1])

    with col1:

        if probability is None:
            st.info(
                "Enter patient details and click Predict PCOS "
                "to see the result."
            )

        else:

            if prediction_label == "PCOS Detected":
                st.error(prediction_label)
            else:
                st.success(prediction_label)

            st.metric(
                "Prediction Probability",
                f"{probability:.0f}%"
            )

    with col2:
        st.image(
            "dashboard/assets/images/uterus.png", width=90,
            width=180
        )