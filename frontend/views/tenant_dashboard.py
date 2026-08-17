import streamlit as st
from api import get_tenant_dashboard


def show_tenant_dashboard(user):

    data = get_tenant_dashboard(user["id"])

    if "success" in data and data["success"] is False:
        st.error(data["message"])
        return

    st.title(f"👋 Welcome, {data['users']['name']}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🏠 Room Number",
            data["rooms"]["room_number"]
        )

    with col2:
        st.metric(
            "💰 Monthly Rent",
            f"₹ {data['monthly_rent']}"
        )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "💵 Advance Paid",
            f"₹ {data['advance_amount']}"
        )

    with col4:
        st.metric(
            "📅 Joining Date",
            data["joining_date"]
        )