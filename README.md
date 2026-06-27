# PCOS XAI Dissertation

## Overview
This project investigates the use of machine learning and explainable artificial intelligence (XAI) techniques for predicting Polycystic Ovary Syndrome (PCOS). The system integrates SHAP and LIME explainability methods to improve model transparency and interpretation within healthcare-focused machine learning applications.

An interactive Streamlit dashboard is also being developed to allow users to input clinical and lifestyle-related features, generate PCOS predictions, and visualise explainability outputs in real time.

The project explores the importance of interpretable AI in healthcare environments where prediction transparency, trust, and ethical considerations are critical.

---

## Research Aim
To develop and evaluate an explainable machine learning system capable of predicting the likelihood of PCOS while improving prediction transparency through explainable AI techniques.

---

## Objectives
- Predict the likelihood of PCOS using machine learning classification models
- Compare and evaluate multiple machine learning algorithms
- Apply explainable AI techniques using SHAP and LIME
- Develop an interactive Streamlit dashboard for prediction and visual analytics
- Analyse feature importance and model interpretability
- Explore ethical considerations surrounding AI in healthcare systems

---

## Technologies Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SHAP
- LIME
- Streamlit
- Jupyter Notebook
- Pytest

---

## Project Structure

```text
pcos-xai-dissertation/
│
├── dashboard/
│   ├── assets/
│   │   ├── images/
│   │   │   ├── Benita.png
│   │   │   ├── Butterfly.png
│   │   │   └── Uterus.png
│   │   └── styles.css
│   │
│   ├── components/
│   │   ├── disclaimer.py
│   │   ├── header.py
│   │   ├── model_info_card.py
│   │   ├── prediction_card.py
│   │   ├── probability_card.py
│   │   ├── shap_section.py
│   │   └── sidebar.py
│   │
│   ├── utils/
│   │   ├── image_helper.py
│   │   ├── input_processor.py
│   │   ├── model_loader.py
│   │   └── predictor.py
│   │
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── PCOS_data.csv
│   └── processed/
│
├── models/
│   ├── random_forest_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_xai_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── evaluate_models.py
│   ├── explainability.py
│   └── train_models.py
│
├── tests/
│   ├── test_dashboard.py
│   ├── test_models.py
│   └── test_preprocessing.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Machine Learning Models
The project will compare multiple machine learning classification algorithms, including:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

Model performance will be evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

---

## Explainable AI Features
The project integrates:
- SHAP (SHapley Additive exPlanations)
- LIME (Local Interpretable Model-Agnostic Explanations)

These techniques will be used to:
- Analyse feature importance
- Improve prediction transparency
- Support interpretability within healthcare AI systems
- Visualise global and local model explanations

---

## Dashboard Features
The Streamlit dashboard will include:
- Patient input form
- Real-time PCOS prediction
- Prediction confidence score
- SHAP explanation visualisations
- LIME local prediction explanations
- Model performance metrics
- Interactive visual analytics

---

## Ethical Considerations
This project acknowledges the ethical considerations associated with AI-driven healthcare systems, including:
- Prediction transparency
- Dataset bias
- Fairness and interpretability
- Responsible AI usage
- Limitations of automated medical predictions

The system is intended for educational and research purposes only and should not be considered a replacement for professional medical diagnosis.

---

## Current Status
Project Finalised

Planned stages include:
- Data preprocessing and exploratory analysis
- Machine learning model training and evaluation
- Explainable AI integration
- Dashboard implementation
- Dissertation write-up and evaluation

---

## Future Improvements
Potential future enhancements include:
- Clinical dataset expansion
- Deep learning integration
- Real-time cloud deployment
- Improved dashboard usability
- Additional explainability techniques
- Clinical validation and testing

---

## Author
Baridule Benita Aalo

Final Year BSc Computer Science Dissertation Project  
Leeds Beckett University



