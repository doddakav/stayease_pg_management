import streamlit as st
from api import (
    get_tenants,
    get_payments,
    add_payment,
    delete_payment
)


def show_payments():

    st.title("💰 Payment Management")

    # ====================================
    # ADD PAYMENT
    # ====================================

    st.subheader("➕ Add Payment")

    tenants = get_tenants()

    if len(tenants) == 0:
        st.warning("No tenants available.")
        return

    tenant_dict = {}

    for tenant in tenants:
        tenant_name = tenant["users"]["name"]
        tenant_id = tenant["id"]
        tenant_dict[tenant_name] = tenant_id

    with st.form("payment_form"):

        selected_tenant = st.selectbox(
            "Select Tenant",
            list(tenant_dict.keys())
        )

        rent_month = st.text_input(
            "Rent Month",
            placeholder="2026-08"
        )

        amount = st.number_input(
            "Amount",
            min_value=0.0
        )

        status = st.selectbox(
            "Payment Status",
            ["Pending", "Paid"]
        )

        submit = st.form_submit_button("Add Payment")

        if submit:

            tenant_id = tenant_dict[selected_tenant]

            result = add_payment(
                tenant_id,
                rent_month,
                amount,
                status
            )

            if result["success"]:
                st.success(result["message"])
                st.rerun()
            else:
                st.error(result["message"])

    st.divider()

    # ====================================
    # PAYMENT HISTORY
    # ====================================

    st.subheader("📋 Payment History")

    payments = get_payments()

    if len(payments) == 0:
        st.info("No Payments Found")
        return

    for payment in payments:

        tenant = payment["tenants"]["users"]

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(f"### 👤 {tenant['name']}")

            st.write(f"📱 {tenant['mobile_number']}")

            st.write(f"📅 Month : {payment['rent_month']}")

            st.write(f"💰 Amount : ₹{payment['amount']}")

            st.write(f"📌 Status : {payment['status']}")

        with col2:

            if st.button(
                "🗑 Delete",
                key=f"payment_{payment['id']}"
            ):

                delete_payment(payment["id"])

                st.success("Payment Deleted")

                st.rerun()

        st.divider()