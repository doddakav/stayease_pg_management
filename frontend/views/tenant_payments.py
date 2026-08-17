import streamlit as st
from api import get_tenant_payments


def show_tenant_payments(user):

    st.title("💰 My Payments")

    payments = get_tenant_payments(user["id"])

    if len(payments) == 0:
        st.info("No Payments Found")
        return

    for payment in payments:

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(f"### 📅 {payment['rent_month']}")

            st.write(f"💰 Amount : ₹{payment['amount']}")

            st.write(f"📌 Status : {payment['status']}")

            if payment["paid_on"]:
                st.write(f"✅ Paid On : {payment['paid_on']}")

        st.divider()