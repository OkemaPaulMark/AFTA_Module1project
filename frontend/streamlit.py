import streamlit as st

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

    try:
        # Monthly payment formula: P * r * (1+r)^n / ((1+r)^n - 1)
        monthly_payment = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
        total_payment = monthly_payment * months

        st.success(f"📆 Monthly Payment: UGX {monthly_payment:,.0f}")
        st.info(f"💵 Total Repayment Over {repayment_years} years: UGX {total_payment:,.0f}")
    except ZeroDivisionError:
        st.error("Error: Cannot divide by zero. Please check your interest rate and period.")

# Footer
st.markdown("---")
st.caption("Made with by khemical")
