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
    Create a polished top contributing features bar plot using only dashboard-visible inputs.
    """

    top_indices = np.argsort(np.abs(display_values))[::-1][:top_n]

    top_features = [display_names[i] for i in top_indices]
    top_values = [display_values[i] for i in top_indices]

    fig, ax = plt.subplots(figsize=(7.5, 4.8))

    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    y_positions = np.arange(len(top_features))

    bar_colours = [
        "#EC4899" if value >= 0 else "#F9A8D4"
        for value in top_values
    ]

    ax.barh(
        y_positions,
        top_values,
        color=bar_colours,
        edgecolor="#C2185B",
        linewidth=0.6
    )

    ax.set_yticks(y_positions)
    ax.set_yticklabels(top_features, fontsize=10, color="#2F2F3A")
    ax.invert_yaxis()

    ax.set_xlabel(
        "SHAP value impact on PCOS prediction",
        fontsize=10,
        color="#4A4A4A"
    )

    ax.set_title(
        "Top Contributing Dashboard Features",
        fontsize=12,
        fontweight="bold",
        color="#2F2F3A",
        pad=12
    )

    ax.axvline(0, color="#4A4A4A", linewidth=0.9)

    # Soft graph grid lines
    ax.grid(
        axis="x",
        linestyle="--",
        linewidth=0.7,
        alpha=0.35,
        color="#C9C9C9"
    )

    ax.set_axisbelow(True)

    # Soft border around the graph
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor("#F8BBD0")
        spine.set_linewidth(1.2)

    # Value labels
    for i, value in enumerate(top_values):
        label_position = value + 0.005 if value >= 0 else value - 0.005
        alignment = "left" if value >= 0 else "right"

        ax.text(
            label_position,
            i,
            f"{value:+.2f}",
            va="center",
            ha=alignment,
            fontsize=9,
            color="#4A4A4A"
        )

    ax.tick_params(axis="x", colors="#4A4A4A", labelsize=9)
    ax.tick_params(axis="y", colors="#2F2F3A", labelsize=10)

    plt.tight_layout()

    return fig


def plot_waterfall(display_names, display_values, display_data, expected_value, shap_values, used_indices):
    """
    Create a polished SHAP waterfall plot using only dashboard-visible inputs.

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
    fig.patch.set_facecolor("#FFFFFF")

    shap.plots.waterfall(
        explanation,
        max_display=10,
        show=False
    )

    ax = plt.gca()
    ax.set_facecolor("#FFFFFF")

    positive_pink = "#EC4899"
    negative_pink = "#F9A8D4"
    text_dark = "#4A4A4A"
    heading_dark = "#2F2F3A"
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

    # Soft graph grid lines
    ax.grid(
        axis="x",
        linestyle="--",
        linewidth=0.7,
        alpha=0.35,
        color="#C9C9C9"
    )

    ax.set_axisbelow(True)

    # Soft border around the graph
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor("#F8BBD0")
        spine.set_linewidth(1.2)

    ax.tick_params(axis="x", colors=text_dark, labelsize=10)
    ax.tick_params(axis="y", colors=heading_dark, labelsize=10)

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