import streamlit as st
from api import (
    get_tenant_dashboard,
    change_password
)


def show_tenant_profile(user):

    st.title("👤 My Profile")

    data = get_tenant_dashboard(user["id"])

    if "success" in data and data["success"] is False:
        st.error(data["message"])
        return

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Personal Details")

        st.write(f"**Name:** {data['users']['name']}")
        st.write(f"**Mobile:** {data['users']['mobile_number']}")

    with col2:

        st.subheader("Stay Details")

        st.write(f"**Room Number:** {data['rooms']['room_number']}")
        st.write(f"**Joining Date:** {data['joining_date']}")
        st.write(f"**Monthly Rent:** ₹{data['monthly_rent']}")
        st.write(f"**Advance Paid:** ₹{data['advance_amount']}")

    st.divider()

    st.subheader("🔒 Change Password")

    with st.form("change_password_form"):

        current_password = st.text_input(
            "Current Password",
            type="password"
        )

        new_password = st.text_input(
            "New Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        submit = st.form_submit_button(
            "Change Password"
        )

        if submit:

            if new_password != confirm_password:

                st.error("Passwords do not match.")

            else:

                result = change_password(

                    user["id"],

                    current_password,

                    new_password

                )

                if result["success"]:

                    st.success(result["message"])

                else:

                    st.error(result["message"])