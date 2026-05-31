# dashboard/utils/model_loader.py

import joblib
from pathlib import Path


def load_model_and_scaler():
    """
    Load the trained Random Forest model and fitted StandardScaler
    used by the PCOS dashboard.
    """

    # Get project root:
    # dashboard/utils/model_loader.py -> dashboard/utils -> dashboard -> project root
    project_root = Path(__file__).resolve().parents[2]

    model_path = project_root / "models" / "random_forest_model.pkl"
    scaler_path = project_root / "models" / "scaler.pkl"

    # Check files exist before loading
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    if not scaler_path.exists():
        raise FileNotFoundError(f"Scaler file not found at: {scaler_path}")

    # Load saved model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    return model, scaler
