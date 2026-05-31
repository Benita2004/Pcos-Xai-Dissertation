# dashboard/components/shap_section.py

import streamlit as st
import shap
import numpy as np
import matplotlib.pyplot as plt


USER_FACING_FEATURES = {
    "Age": ["Age (yrs)"],
    "Weight": ["Weight (Kg)"],
    "BMI": ["BMI"],
    "Cycle": ["Cycle(R/I)"],
    "Hair Growth": ["hair growth(Y/N)"],
    "Skin Darkening": ["Skin darkening (Y/N)"],
    "Follicle Count": ["Follicle No. (L)", "Follicle No. (R)"],
    "AMH": ["AMH(ng/mL)"],
    "Weight Gain": ["Weight gain(Y/N)"],
    "Acne": ["Pimples(Y/N)"]
}


def get_pcos_shap_values(model, scaled_input):
    """
    Generate SHAP values for the PCOS class.

    This matches the notebook approach:
    explainer = shap.TreeExplainer(rf_model)
    shap_values = explainer.shap_values(X_test_scaled)
    shap_values[:, :, 1] is used for the PCOS class.
    """

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(scaled_input)

    if isinstance(shap_values, np.ndarray) and shap_values.ndim == 3:
        pcos_shap_values = shap_values[0, :, 1]
        expected_value = explainer.expected_value[1]

    elif isinstance(shap_values, list):
        pcos_shap_values = shap_values[1][0]
        expected_value = explainer.expected_value[1]

    else:
        raise ValueError("Unexpected SHAP output format.")

    return pcos_shap_values, expected_value


def get_user_facing_shap_values(shap_values, input_df):
    """
    Keep only the dashboard-visible features.

    Some dashboard fields map to more than one training feature.
    For example, Follicle Count is used for both left and right follicle count,
    so their SHAP values are combined.
    """

    feature_names = input_df.columns.tolist()

    display_names = []
    display_values = []
    display_data = []
    used_indices = []

    for display_name, training_columns in USER_FACING_FEATURES.items():
        combined_shap_value = 0
        shown_value = None

        for column in training_columns:
            if column in feature_names:
                index = feature_names.index(column)
                combined_shap_value += shap_values[index]
                used_indices.append(index)

                if shown_value is None:
                    shown_value = input_df.iloc[0][column]

        display_names.append(display_name)
        display_values.append(combined_shap_value)
        display_data.append(shown_value)

    return display_names, np.array(display_values), np.array(display_data), used_indices


def plot_top_contributing_features(display_names, display_values, top_n=8):
    """
    Create a top contributing features bar plot using only dashboard-visible inputs.
    """

    top_indices = np.argsort(np.abs(display_values))[::-1][:top_n]

    top_features = [display_names[i] for i in top_indices]
    top_values = [display_values[i] for i in top_indices]

    fig, ax = plt.subplots(figsize=(7.5, 4.8))

    y_positions = np.arange(len(top_features))

    ax.barh(y_positions, top_values, color="#EC4899")
    ax.set_yticks(y_positions)
    ax.set_yticklabels(top_features, fontsize=9)
    ax.invert_yaxis()

    ax.set_xlabel("SHAP value impact on PCOS prediction", fontsize=9)
    ax.set_title("Top Contributing Dashboard Features", fontsize=11, fontweight="bold")

    ax.axvline(0, color="#444444", linewidth=0.8)

    for i, value in enumerate(top_values):
        ax.text(
            value,
            i,
            f" {value:+.2f}",
            va="center",
            fontsize=8
        )

    plt.tight_layout()

    return fig


def plot_waterfall(display_names, display_values, display_data, expected_value, shap_values, used_indices):
    """
    Create a SHAP waterfall plot using only dashboard-visible inputs.

    Hidden/defaulted model features are absorbed into the adjusted base value,
    so the simplified waterfall still explains the visible dashboard inputs clearly.
    """

    all_indices = set(range(len(shap_values)))
    used_indices = set(used_indices)
    hidden_indices = list(all_indices - used_indices)

    hidden_contribution = np.sum(shap_values[hidden_indices])
    adjusted_base_value = expected_value + hidden_contribution

    explanation = shap.Explanation(
        values=display_values,
        base_values=adjusted_base_value,
        data=display_data,
        feature_names=display_names
    )

    fig = plt.figure(figsize=(7.5, 4.8))

    shap.plots.waterfall(
        explanation,
        max_display=10,
        show=False
    )

    ax = plt.gca()

    # Pink styling
    positive_pink = "#EC4899"
    negative_pink = "#F9A8D4"
    text_dark = "#4A4A4A"
    accent = "#C2185B"

    # Recolour waterfall bars/arrows
    for patch in ax.patches:
        try:
            width = patch.get_width()
        except Exception:
            width = 0

        if width >= 0:
            patch.set_facecolor(positive_pink)
            patch.set_edgecolor(positive_pink)
        else:
            patch.set_facecolor(negative_pink)
            patch.set_edgecolor(negative_pink)

    # Recolour text
    for text in ax.texts:
        text.set_color(accent)
        text.set_fontsize(10)

    # Axis styling
    ax.set_facecolor("#FFFFFF")
    ax.tick_params(axis="x", colors=text_dark, labelsize=10)
    ax.tick_params(axis="y", colors=text_dark, labelsize=10)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    ax.spines["bottom"].set_color("#D1D5DB")

    plt.tight_layout()

    return fig


def render_shap_section(model=None, input_df=None, scaled_input=None):
    """
    Display SHAP explainability section.

    Before prediction, a placeholder is shown.
    After prediction, local SHAP explanations are generated using the
    same TreeExplainer approach used in the XAI notebook.
    """

    if model is None or input_df is None or scaled_input is None:
        st.markdown(
            """
            <div class="shap-section">
                <h3>Top Contributing Features (SHAP)</h3>
                <p>
                    SHAP explanations will be displayed here after a prediction is made.
                    This section will show which dashboard inputs had the strongest influence
                    on the model output.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    try:
        pcos_shap_values, expected_value = get_pcos_shap_values(
            model,
            scaled_input
        )

        display_names, display_values, display_data, used_indices = get_user_facing_shap_values(
            pcos_shap_values,
            input_df
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                """
                <div class="shap-section">
                    <h3>Top Contributing Features (SHAP)</h3>
                    <p>
                        This chart shows the dashboard inputs that had the strongest effect
                        on the PCOS prediction.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            top_features_fig = plot_top_contributing_features(
                display_names,
                display_values
            )

            st.pyplot(top_features_fig)

        with col2:
            st.markdown(
                """
                <div class="shap-section">
                    <h3>SHAP Waterfall Explanation</h3>
                    <p>
                        This plot shows how the visible dashboard inputs push the prediction
                        higher or lower for this patient.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            waterfall_fig = plot_waterfall(
                display_names,
                display_values,
                display_data,
                expected_value,
                pcos_shap_values,
                used_indices
            )

            st.pyplot(waterfall_fig)

    except Exception as error:
        st.error(f"Unable to generate SHAP explanation: {error}")