import streamlit as st
import pickle
import numpy as np


model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Approval Prediction")


gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
income = st.number_input("Income", 10000, 100000, 40000)
loan = st.number_input("Loan Amount", 50, 500000, 250000)
credit = st.slider("Credit Score", 300, 850, 700)
dependents = st.slider("Dependents", 0, 5, 1)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])


gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0


if st.button("Check Loan Status"):
    data = np.array([[gender, married, income, loan, credit, dependents, education]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")