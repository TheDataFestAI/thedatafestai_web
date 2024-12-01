import streamlit as st
import pandas as pd
from utils.finance_calculator import emi_calculator, loan_eligibility

    
st.title("Finance Module", anchor=False)
st.html("<hr>")

with st.expander("Loan Eligibility:", expanded=True):
    st.html("<h3>Please use below Loan Eligibility Calculator </h3>")
    with st.form("loan_eligibility_calculator"):
        monthly_net_salary = st.number_input("Your Monthly Net Salary", value=80000)
        loan_eligibility_calculator_submitted = st.form_submit_button("Submit")

    if loan_eligibility_calculator_submitted:
        # out_df = pd.DataFrame(loan_eligibility(monthly_net_salary))
        out = loan_eligibility(monthly_net_salary)
        st.html(f'<p>You are eligible for monthly EMI: <u><b>{out.get("eligible_monthly_emi", 0)}</b></u></p>')
        col1, col2, col3, col4 = st.columns([2,2,2,2])
        col1.text("Principle Amount")
        col2.text("Rate of Interest")
        col3.text("Tenure in Months")
        col4.text("Monthly EMI")
        
        col1, col2, col3, col4 = st.columns([2,2,2,2])
        col1.text("Rs. " + str(out.get("principle", 0)))
        col2.text(str(out.get("interest", 0)) + " %")
        col3.text(str(out.get("months", 0)) + " months")
        col4.text("Rs. " + str(out.get("monthly_emi", 0)))
        

with st.expander("EMI Calculator:"):
    st.html("<h3>Please use below EMI Calculator for any kind of loan <br><br>**Home loan, Car loan, Personal loan </h3>")
    with st.form("emi_calculator"):
        # st.write("EMI Calculator:")
        principle_amount = st.number_input("Principle Amount for Loan", value=3000000)
        rate_of_interest = st.number_input("Rate Of Interest", value=9)
        months_of_tenure = st.number_input("Loan Tenure in Months", value=12*25)
        
        emi_calculator_submitted = st.form_submit_button("Submit")
    if emi_calculator_submitted:
        if principle_amount != 0 or rate_of_interest != 0 or months_of_tenure != 0:
            emi_out = emi_calculator(principle_amount, rate_of_interest, months_of_tenure)
            
            st.html(f'<p>Your monthly EMI will be <u><b>{emi_out.get("emi_monthly", 0)}</b></u></p>')        
            st.write("Loan Amortization Details")
            amortization_df = pd.DataFrame(emi_out["amortization_details"])
            st.table(amortization_df)
        else:
            st.error("Please provide correct data")
    
        # col1, col2, col3, col4 = st.columns([2,2,2,2])
        # col1.text("Months")
        # col2.text("Interest Part")
        # col3.text("Principle Part")
        # col4.text("Principle Balance")
        
        # for i in emi_out["amortization_details"]:
        #     st.table(i)
        #     col1, col2, col3, col4 = st.columns([2,2,2,2])
        #     col1.text(i["emi_month_sequence"])
        #     col2.text(i["interest_part"])
        #     col3.text(i["principle_part"])
        #     col4.text(i["principle_balance"])
        