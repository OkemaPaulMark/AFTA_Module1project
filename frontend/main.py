import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Salary Loan Calculator", page_icon="💰", layout="centered")

# Title
st.title("💰 Salary Loan Calculator")
st.markdown("Estimate your monthly loan repayment based on your salary and loan terms.")

# Input form
with st.form("loan_form"):
    st.subheader("🔢 Enter Loan Details")

    col1, col2 = st.columns(2)
    with col1:
        salary = st.number_input("Monthly Salary (UGX)", min_value=100000, step=50000)
        loan_amount = st.number_input("Loan Amount (UGX)", min_value=100000, step=100000)
    with col2:
        interest_rate = st.slider("Annual Interest Rate (%)", 1.0, 30.0, 15.0)
        repayment_years = st.slider("Repayment Period (Years)", 1, 10, 2)

    submitted = st.form_submit_button("Calculate Monthly Payment")

if submitted:
    # Calculate monthly interest rate
    monthly_rate = (interest_rate / 100) / 12
    months = repayment_years * 12
    
    payload = {
    "salary": salary,
    "loan_amount": loan_amount,
    "interest_rate": interest_rate,
    "repayment_years": repayment_years
    }

    try:
        response = requests.post("http://backend:8000/calculate", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"📆 Monthly Payment: UGX {result['monthly_payment']:,.0f}")
            st.info(f"💵 Total Repayment: UGX {result['total_payment']:,.0f}")
        else:
            st.error("API Error: Could not calculate loan.")
    except requests.exceptions.RequestException as e:
        st.error(f"Connection Error: {e}")


# Footer
st.markdown("---")
st.caption("Made by khemical")
