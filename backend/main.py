from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Updated model to match frontend
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

        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "duration_months": months
        }
    except ZeroDivisionError:
        return {"error": "Invalid interest rate or duration."}
