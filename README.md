# 💳 Credit Loan Risk Prediction System

An interactive, end-to-end Machine Learning web application built using **Streamlit** and **Scikit-Learn** that evaluates loan applicant profiles and predicts whether an applicant presents a **Low Risk (Likely Approved)** or **High Risk (Likely Rejected)** credit profile.

---

## 📌 Project Overview

Evaluating credit risk accurately is crucial for lending institutions to minimize default rates while ensuring fair, expedited loan approvals. This project leverages an applicant's demographic, socioeconomic, and prior interaction attributes to predict credit risk in real time using a trained **Random Forest** classification model.

---

## 🚀 Key Highlights & Features

- **Interactive User Interface:** Clean, user-friendly frontend built with Streamlit.
- **Dynamic Feature Preprocessing:** Automatically aligns user input selections to the one-hot encoded features expected by the trained model.
- **Instant Risk Assessment:** Real-time inference showing whether an applicant is low-risk or high-risk.
- **Optimized Model Delivery:** Random Forest classifier compressed via `joblib` for efficient storage and fast deployment.

---

## 🛠️ Tech Stack & Tools

- **Language:** Python 3.9+
- **Web Framework:** [Streamlit](https://streamlit.io/)
- **Machine Learning:** [Scikit-learn](https://scikit-learn.org/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Model Serialization:** [Joblib](https://joblib.readthedocs.io/)
- **Exploratory Data Analysis:** Jupyter Notebook

---

## 📂 Repository Structure

```text
├── app.py                         # Streamlit web application
├── Random_Forest_credit_model.pkl # Trained & compressed Random Forest model
├── loan_detection.csv             # Processed dataset used for modeling
├── Major project.ipynb            # Jupyter notebook with EDA & model training
├── LICENSE                        # Open-source license
└── README.md                      # Project documentation

