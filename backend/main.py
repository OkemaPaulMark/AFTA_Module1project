from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class LoanRequest(BaseModel):
    salary: float
    loan_amount: float
    interest_rate: float  # Annual in %
    repayment_years: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Calculator API"}

@app.post("/calculate")
def calculate_loan(data: LoanRequest):
    monthly_rate = (data.interest_rate / 100) / 12
    months = data.repayment_years * 12

    try:
        monthly_payment = (
            data.loan_amount *
            monthly_rate *
            (1 + monthly_rate) ** months /
            ((1 + monthly_rate) ** months - 1)
        )
        total_payment = monthly_payment * months

        # Build amortization schedule using pandas
        schedule = []
        balance = data.loan_amount

        for month in range(1, months + 1):
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            if balance < 0:
                balance = 0

            schedule.append({
                "Month": month,
                "Monthly Payment": round(monthly_payment, 2),
                "Principal": round(principal_payment, 2),
                "Interest": round(interest_payment, 2),
                "Remaining Balance": round(balance, 2),
            })

        df_schedule = pd.DataFrame(schedule)

        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "duration_months": months,
            "schedule": df_schedule.to_dict(orient="records")  # Send schedule as list of dicts
        }
    except ZeroDivisionError:
        return {"error": "Invalid interest rate or duration."}
