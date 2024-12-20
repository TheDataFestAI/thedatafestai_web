import streamlit as st
import pandas as pd
from utils.finance_calculator import emi_calculator, monthly_emi_loan_eligibility

    
st.title("Finance Module", anchor=False)
st.html("<hr>")

with st.expander("Check Monthly EMI Affordibility:"):
    st.html("<h5>Please use below Monthly EMI Eligibility Calculator </h5>")
    with st.form("loan_eligibility_calculator"):
        age = st.number_input("Your Age -", value=25)
        salaried_or_not = st.radio("Are you Salaried Or Self-Employed -", ["Salaried", "Self Employed", "Others"], horizontal=True)
        credit_score = st.slider("Your Credit Score -", value=750, min_value=300, max_value=900)
        monthly_net_salary = st.number_input("Your Monthly In-Hand Salary -", value=80000)
        loan_eligibility_calculator_submitted = st.form_submit_button("Submit")

    if loan_eligibility_calculator_submitted:
        # out_df = pd.DataFrame(loan_eligibility(monthly_net_salary))
        if age < 18 or age > 55:
            st.error("You are not eligible for taking any loan as 18 <= age <= 55")
            
        if credit_score < 700:
            st.error("You should have credit score more than 699")
            
        if salaried_or_not == "Salaried" and monthly_net_salary < 24999:
            st.error("For Salaried people, Your Salary Should Be Greater Than 24999")
        elif salaried_or_not == "Self Employed" and monthly_net_salary < 124999:
            st.error("For Self Employed people, Your salary Should Be Greater Than 124999")
        elif salaried_or_not != "Salaried" and salaried_or_not != "Self Employed":
            st.error("You need to be salaried or self-employed")
            
        loan_tenure = (60 - age)
        current_interest = 9
        if loan_tenure < 7 or credit_score < 600:
            current_interest += 3
        elif (loan_tenure >= 7 and loan_tenure < 11) or credit_score < 700:
            current_interest += 1.5
                                
        out = monthly_emi_loan_eligibility(monthly_net_salary, loan_tenure, current_interest)
        st.html(f'<p>You are eligible for monthly EMI: <u><b>{out.get("eligible_monthly_emi", 0)}</b></u></p>')
        col1, col2, col3, col4 = st.columns([2,2,2,2])
        col1.text("Principle Amount")
        col2.text("Rate of Interest")
        col3.text("Tenure in Months")
        col4.text("Monthly EMI")
        
        col1, col2, col3, col4 = st.columns([2,2,2,2])
        col1.text("Rs. " + str(out.get("principle", 0)))
        col2.text(str(out.get("interest", 0)) + " %")
        col3.text(str(out.get("months", 0)) + " months (" + str(int(out.get("months", 0)/12)) + " years)")
        col4.text("Rs. " + str(out.get("monthly_emi", 0)))
        

with st.expander("Monthly EMI Calculator: (**Home/Car/Personal Loan)"):
    st.html("<h5>Please use below EMI Calculator for any kind of loan <br><br>**Home loan, Car loan, Personal loan </h5>")
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
        