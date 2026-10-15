import streamlit as st
import pandas as pd 
import joblib

model= joblib.load("Random_Forest_credit_model.pkl")   

st.set_page_config(page_title="Credit Loan Risk Predictor", page_icon=":money_with_wings:", layout="centered")  
st.title("Credit Loan Risk Predictor")
st.write("Enter the details of the loan applicant to predict the credit loan risk.")    

st.divider()
# Input fields for user to enter loan applicant details
col1, col2= st.columns(2)
with col1:
    age= st.number_input("Age", min_value=17, max_value=100, value=30)
    campaign= st.number_input("Contacts during this campaign", min_value=0, value=1)
    previous= st.number_input("Contacts made before thisCampaign", min_value=0, value=0)
    pdays= st.number_input("Days since last contact(999 if never contacted)", min_value=0, value=999)
    no_previous_contact= st.number_input("Is this the first contact?(0=No, 1=Yes)", min_value=0, max_value=1, value=1)

with col2:
    job= st.selectbox("Job Type", ["admin", "blue-collar", "entrepreneur", "housemaid", "management", "retired", 
                                   "self-employed", "services", "student", "technician", "unemployed", "unknown"])
    marital= st.selectbox("Marital Status", ["single", "married", "divorced", "unknown"])
    education= st.selectbox("Education Level", ["basic.4y","basic.6y","basic.9y","high.school", "illiterate", 
                                                "professional.course","university.degree","unknown"])
    default= st.selectbox("Has credit in default?", ["yes", "no", "unknown"])
    housing= st.selectbox("Has housing loan?", ["yes", "no", "unknown"])
    loan= st.selectbox("Has personal loan?", ["yes", "no", "unknown"])

    col3, col4= st.columns(2)
    with col3:
        contact= st.selectbox("Contact communication type", ["cellular", "telephone"])
        month= st.selectbox("Last contact month", ["sep", "aug", "dec", "feb", "jan", "jul", 
                                                   "jun", "mar", "may", "nov", "oct", "apr"])
        
    with col4:
        day_of_week= st.selectbox("Last contact day of the week", ["fri", "mon", "thu", "tue", "wed"])
        poutcome= st.selectbox("Outcome of previous marketing campaign", ["success", "nonexistent", "failure"])

    st.divider()

    if st.button("Predict Credit Loan Risk"):

        input_dict = {}
        # Numerical
        input_dict ['age'] = age
        input_dict['campaign'] = campaign
        input_dict ['pdays'] = pdays
        input_dict['previous'] = previous
        input_dict ['no_previous_contact'] = 1 if no_previous_contact == "Yes" else 0

        for col in model.feature_names_in_:
            if col not in input_dict:
                input_dict[col] = 0

        # activate user selections
        def set_col(col_name):
            if col_name in input_dict:
                input_dict[col_name] = 1

        set_col(f'job_{job}')
        set_col(f'marital_{marital}')
        set_col(f'education_{education}')
        set_col(f'default_{default}')
        set_col(f'housing_{housing}')
        set_col(f'loan_{loan}')
        set_col(f'contact_{contact}')
        set_col(f"month_{month}")
        set_col(f"day_of_week_{day_of_week}")
        set_col(f"poutcome_{poutcome}")
        # Convert to DataFrame
        df = pd.DataFrame([[input_dict[col] for col in model.feature_names_in_]], 
                        columns=model.feature_names_in_)

        # Make prediction
        prediction = model.predict(df)[0]

        # Result
        st.subheader('Result Prediction:')
        if prediction == 1:
            st.error ("Loan likely to be **rejected (High Risk Applicant)**")
        else:
            st.success ("Loan likely to be **approved (Low Risk Applicant)**")