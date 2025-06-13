import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Salary Loan Calculator", page_icon="💰", layout="centered")

st.title("💰 Salary Loan Calculator")
st.markdown("Estimate your monthly loan repayment based on your salary and loan terms.")

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

            # Convert schedule to DataFrame for display and plotting
            schedule_df = pd.DataFrame(result['schedule'])

            st.subheader("📊 Amortization Schedule")
            st.dataframe(schedule_df)

            # Plotting the principal vs interest payments over time
            fig, ax = plt.subplots()
            ax.plot(schedule_df['Month'], schedule_df['Principal'], label='Principal')
            ax.plot(schedule_df['Month'], schedule_df['Interest'], label='Interest')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount (UGX)')
            ax.set_title('Monthly Principal and Interest Payments')
            ax.legend()
            st.pyplot(fig)

            # Plot remaining balance over time
            fig2, ax2 = plt.subplots()
            ax2.plot(schedule_df['Month'], schedule_df['Remaining Balance'], color='red')
            ax2.set_xlabel('Month')
            ax2.set_ylabel('Remaining Balance (UGX)')
            ax2.set_title('Loan Balance Over Time')
            st.pyplot(fig2)

        else:
            st.error("API Error: Could not calculate loan.")
    except requests.exceptions.RequestException as e:
        st.error(f"Connection Error: {e}")

st.markdown("---")
st.caption("Made by khemical")
