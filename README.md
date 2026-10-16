# 💳 Credit Loan Risk Prediction System

<p><a href="https://credit-loan-risk-predictor.streamlit.app"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit App"></a></p>


> 🔗 **Live Demo:** [Launch Credit Loan Risk Predictor](https://credit-loan-risk-predictor.streamlit.app)


An interactive Machine Learning web application built using **Streamlit** and **Scikit-Learn** that evaluates loan applicant profiles and predicts whether an applicant presents a **Low Risk (Likely Approved)** or **High Risk (Likely Rejected)** credit profile.

---

## 📌 Project Overview

Credit risk evaluation is essential for lending institutions to reduce default rates while accelerating approval workflows. This project takes demographic, socioeconomic, and marketing/interaction features of an applicant, processes one-hot encoded variables dynamically, and outputs real-time risk predictions using a trained **Random Forest** classifier.

---

## 🚀 Key Features

- **Interactive User Interface:** Clean, dual-column input layout built with Streamlit.
- **Dynamic Feature Preprocessing:** Automatically aligns user input selections to the one-hot encoded features expected by the trained model.
- **Instant Risk Assessment:** Clear visual feedback indicating whether an applicant is likely low-risk or high-risk.
- **Robust Model Core:** Backed by a Random Forest Classifier trained on applicant credit and contact behavior histories.
- **Production-Ready Artifact:** Compressed model serialized with `joblib` for rapid cloud inference.

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python 3.9+
- **Frontend / Framework:** [Streamlit](https://streamlit.io/)
- **Machine Learning:** [Scikit-learn](https://scikit-learn.org/), [XGBoost](https://xgboost.readthedocs.io/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Model Serialization:** [Joblib](https://joblib.readthedocs.io/)
- **Exploration & Training:** Jupyter Notebook

---

## 📂 Project Structure

```text
├── app.py                         # Streamlit web application
├── Random_Forest_credit_model.pkl # Trained & compressed Random Forest model
├── loan_detection.csv             # Processed dataset used for modeling
├── Major project.ipynb            # Model exploration, tuning, and training notebook
├── requirements.txt               # Dependencies list for local setup & deployment
├── LICENSE                        # Open-source MIT license
└── README.md                      # Project documentation


