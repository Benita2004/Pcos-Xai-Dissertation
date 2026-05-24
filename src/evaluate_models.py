# evaluate_models.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    roc_auc_score
)


def create_comparison_table(y_test, model_predictions):
    results = []

    for model_name, predictions in model_predictions.items():

        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        results.append({
            "Model": model_name,
            "Accuracy": round(accuracy * 100, 2),
            "Precision": round(precision * 100, 2),
            "Recall": round(recall * 100, 2),
            "F1-Score": round(f1 * 100, 2)
        })

    results_df = pd.DataFrame(results)

    return results_df


def plot_confusion_matrices(y_test, model_predictions):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    for ax, (model_name, predictions) in zip(axes.flatten(), model_predictions.items()):

        cm = confusion_matrix(y_test, predictions)

        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            ax=ax
        )

        ax.set_title(model_name)
        ax.set_xlabel("Predicted Label")
        ax.set_ylabel("True Label")

    plt.tight_layout()
    plt.show()


def plot_roc_curves(y_test, trained_models, X_test_scaled):
    plt.figure(figsize=(8, 6))

    auc_scores = {}

    for model_name, model in trained_models.items():

        probs = model.predict_proba(X_test_scaled)[:, 1]

        fpr, tpr, _ = roc_curve(y_test, probs)

        auc_score = roc_auc_score(y_test, probs)

        auc_scores[model_name] = auc_score

        plt.plot(
            fpr,
            tpr,
            label=f"{model_name} (AUC = {auc_score:.2f})"
        )

    plt.plot([0, 1], [0, 1], linestyle="--")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison")
    plt.legend()

    plt.show()

    return auc_scores


def create_auc_table(auc_scores):
    auc_results = pd.DataFrame({
        "Model": list(auc_scores.keys()),
        "AUC Score": [round(score, 2) for score in auc_scores.values()]
    })

    return auc_results