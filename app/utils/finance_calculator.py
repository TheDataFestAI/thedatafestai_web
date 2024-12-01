def emi_calculator(loan_amount, yearly_interest_rate, months, rounding = 1):
    """emi_calculator doc
    EMI = (Principal x Monthly Interest Rate x (1 + Monthly Interest Rate)^Loan Term) / ((1 + Monthly Interest Rate)^Loan Term - 1)
    """
    p = loan_amount
    r = yearly_interest_rate / (12 * 100)
    n = int(months)
    out = dict()
    
    if (loan_amount != 0 or yearly_interest_rate != 0 or months != 0):
        out["emi_monthly"] = round(p * r * (((1+r) ** n) / (((1+r) ** n) - 1)), rounding)
        # print(f"Loan amount: {p}, tenure is {n} months or {n/12} years, rate of interest is {yearly_interest_rate}")
        # print(f'monthly EMI will be, {out["emi_monthly"]}')    
        out["amortization_details"] = list()
        
        principle_balance = p
        for i in range(0, n):
            interest_part = principle_balance * r
            principle_part = out["emi_monthly"] - interest_part
            principle_balance -= principle_part
            
            amortization_details = {}
            amortization_details["emi_month_sequence"] = str(i+1) + " - Month"
            amortization_details["interest_part"] = round(interest_part, rounding)
            amortization_details["principle_part"] = round(principle_part, rounding)
            amortization_details["principle_balance"] = round(principle_balance, rounding)
            out["amortization_details"].append(amortization_details)
            # print(f'{i+1}-months: emi: {out["emi_monthly"]}, interest: {interest_part}, principle: {principle_part}, balance: {principle_balance}')
    return out

def loan_eligibility(monthly_income):
    out = {}
    out["eligible_monthly_emi"] = monthly_income * 0.6
    out["interest"] = 9
    out["months"] = 25*12
    out["principle"] = 3500000
    out["monthly_emi"] = emi_calculator(out["principle"], out["interest"], out["months"]).get("emi_monthly", 0)
    
    if out["eligible_monthly_emi"] >= out["monthly_emi"]:
        while out["eligible_monthly_emi"] >= out["monthly_emi"]:
            out["principle"] += 100000 
            out["monthly_emi"] =  emi_calculator(out["principle"], out["interest"], out["months"]).get("emi_monthly", 0)
            # print(out["principle"], out["monthly_emi"])
    elif out["eligible_monthly_emi"] <= out["monthly_emi"]:
        while out["eligible_monthly_emi"] <= out["monthly_emi"]:
            out["principle"] -= 100000 
            out["monthly_emi"] =  emi_calculator(out["principle"], out["interest"], out["months"]).get("emi_monthly", 0)
            # print(out["principle"], out["monthly_emi"])
    return out       
        
        
        
    
    
    
if __name__ == "__main__":
    out = emi_calculator(1800000, 12, 12)
    print(out)