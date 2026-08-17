import streamlit as st
from api import login, get_dashboard
from views.rooms import show_rooms
from views.tenants import show_tenants
from views.payments import show_payments
from views.complaints import show_complaints
from views.tenant_dashboard import show_tenant_dashboard
from views.tenant_payments import show_tenant_payments
from views.tenant_complaints import show_tenant_complaints
from views.tenant_profile import show_tenant_profile

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="StayEase",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ===========================================================
# LOGIN SCREEN
# ===========================================================

if not st.session_state.logged_in:

    st.title("🏠 StayEase")
    st.subheader("PG & Hostel Management System")

    st.write("Please login to continue.")

    mobile = st.text_input("📱 Mobile Number")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        result = login(mobile, password)

        if result["success"]:

            st.session_state.logged_in = True
            st.session_state.user = result["user"]
            if result["user"]["role"] == "owner":
                st.session_state.page = "Dashboard"
            else:
                st.session_state.page = "Tenant Dashboard"
            st.rerun()

        else:

            st.error(result["message"])

# ===========================================================
# DASHBOARD
# ===========================================================

else:

    user = st.session_state.user
    role = user["role"]

    # -----------------------------
# Sidebar
# -----------------------------

    st.sidebar.title("🏠 StayEase")

    st.sidebar.write(f"👤 {user['name']}")
    st.sidebar.write(f"Role : {role}")

    st.sidebar.divider()

# ==========================================
# OWNER MENU
# ==========================================

    if role == "owner":

        if st.sidebar.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = "Dashboard"

        if st.sidebar.button("🛏️ Rooms", use_container_width=True):
            st.session_state.page = "Rooms"

        if st.sidebar.button("👥 Tenants", use_container_width=True):
            st.session_state.page = "Tenants"

        if st.sidebar.button("💰 Payments", use_container_width=True):
            st.session_state.page = "Payments"

        if st.sidebar.button("🛠️ Complaints", use_container_width=True):
            st.session_state.page = "Complaints"

        if st.sidebar.button("👤 Profile", use_container_width=True):
            st.session_state.page = "Profile"

# ==========================================
# TENANT MENU
# ==========================================

    else:

        if st.sidebar.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = "Tenant Dashboard"

        if st.sidebar.button("💰 My Payments", use_container_width=True):
            st.session_state.page = "My Payments"

        if st.sidebar.button("🛠️ My Complaints", use_container_width=True):
            st.session_state.page = "My Complaints"

        if st.sidebar.button("👤 My Profile", use_container_width=True):
            st.session_state.page = "My Profile"

    st.sidebar.divider()

    if st.sidebar.button("🚪 Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.page = "Dashboard"

        st.rerun()
    # -----------------------------
    # Main Content
    # -----------------------------

    page = st.session_state.page

    # =======================================================
    # Dashboard
    # =======================================================


    if page == "Dashboard":

        dashboard = get_dashboard()

        st.title("🏠 Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🏠 Total Rooms",
                dashboard["total_rooms"]
            )

        with col2:
            st.metric(
                "👥 Total Tenants",
                dashboard["total_tenants"]
            )

        with col3:
            st.metric(
                "💰 Total Payments",
                dashboard["total_payments"]
            )

        st.divider()

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric(
                "🛏 Occupied Rooms",
                dashboard["occupied_rooms"]
            )

        with col5:
            st.metric(
                "🟢 Vacant Rooms",
                dashboard["vacant_rooms"]
            )

        with col6:
            st.metric(
                "🛠 Pending Complaints",
                dashboard["pending_complaints"]
            )

    # =======================================================
    # Rooms
    # =======================================================

    elif page == "Rooms":

        show_rooms()

    # =======================================================
    # Tenants
    # =======================================================

    elif page == "Tenants":
        show_tenants()

    # =======================================================
    # Payments
    # =======================================================

    elif page == "Payments":

        show_payments()

    # =======================================================
    # Complaints
    # =======================================================

    elif page == "Complaints":

        show_complaints()

    # =======================================================
    # Profile
    # =======================================================

    elif page == "Profile":

        st.title("👤 Profile")

        st.write("### User Information")

        st.write(f"**Name:** {user['name']}")
        st.write(f"**Role:** {user['role']}")

    # =======================================================
    # TENANT DASHBOARD
    # =======================================================

    elif page == "Tenant Dashboard":

        show_tenant_dashboard(user)

    # =======================================================
    # TENANT PAYMENTS
    # =======================================================

    elif page == "My Payments":

        show_tenant_payments(user)

    # =======================================================
    # TENANT COMPLAINTS
    # =======================================================

    elif page == "My Complaints":

        show_tenant_complaints(user)

    # =======================================================
    # TENANT PROFILE
    # =======================================================

    elif page == "My Profile":

        show_tenant_profile(user)