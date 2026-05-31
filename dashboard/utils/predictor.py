# dashboard/utils/predictor.py


def make_prediction(model, scaler, input_df):
    """
    Scale the 41-feature input and generate a PCOS prediction.
    """

    # Scale input using the fitted scaler
    scaled_input = scaler.transform(input_df)

    # Generate class prediction
    prediction = model.predict(scaled_input)[0]

    # Generate PCOS probability
    prediction_probability = model.predict_proba(scaled_input)[0][1]

    return prediction, prediction_probability, scaled_input