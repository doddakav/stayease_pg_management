import streamlit as st
from api import (
    get_rooms,
    add_tenant,
    get_tenants,
    update_tenant,
    delete_tenant
)


def show_tenants():
    if "edit_tenant" not in st.session_state:
        st.session_state.edit_tenant = None

    st.title("👥 Tenant Management")

    # ====================================
    # ADD TENANT
    # ====================================

    if st.session_state.edit_tenant is None:
        st.subheader("➕ Add Tenant")
    else:
        st.subheader("✏ Edit Tenant")

    rooms = get_rooms()

    room_numbers = []

    for room in rooms:
        room_numbers.append(room["room_number"])
    edit = st.session_state.edit_tenant
    with st.form("tenant_form"):

        name = st.text_input(
        "Tenant Name",
        value=edit["users"]["name"] if edit else ""
        )

        mobile = st.text_input(
            "Mobile Number",
            value=edit["users"]["mobile_number"] if edit else ""
        )

        room = st.selectbox(
            "Select Room",
            room_numbers,
            index=room_numbers.index(edit["rooms"]["room_number"]) if edit else 0
        )

        advance = st.number_input(
            "Advance Amount",
            min_value=0.0,
            value=float(edit["advance_amount"]) if edit else 0.0
        )

        monthly_rent = st.number_input(
            "Monthly Rent",
            min_value=0.0,
            value=float(edit["monthly_rent"]) if edit else 0.0
        )

        joining_date = st.date_input(
            "Joining Date",
            value=edit["joining_date"] if edit else None
        )
        submit = st.form_submit_button(

        "Update Tenant"

        if edit

        else "Create Tenant"

)

        if submit:

            if edit:

                result = update_tenant(

                    edit["id"],

                    name,

                    mobile,

                    room,

                    advance,

                    monthly_rent,

                    str(joining_date)

                )

            else:

                result = add_tenant(

                    name,

                    mobile,

                    room,

                    advance,

                    monthly_rent,

                    str(joining_date)

                )

            if result["success"]:

                st.success(result["message"])

                st.session_state.edit_tenant = None

                st.rerun()

            else:

                st.error(result["message"])

    if edit:

        if st.button("❌ Cancel Edit"):

            st.session_state.edit_tenant = None

            st.rerun()

    st.divider()

    # ====================================
    # TENANT LIST
    # ====================================

    st.subheader("📋 Existing Tenants")

    tenants = get_tenants()

    if len(tenants) == 0:

        st.info("No Tenants Found")

        return

    for tenant in tenants:

        user = tenant["users"]
        room = tenant["rooms"]

        col1, col2, col3 = st.columns([5,1,1])

        with col1:

            st.markdown(f"### 👤 {user['name']}")

            st.write(f"📱 {user['mobile_number']}")

            st.write(f"🏠 Room : {room['room_number']}")

            st.write(f"💰 Monthly Rent : ₹{tenant['monthly_rent']}")

            st.write(f"💵 Advance : ₹{tenant['advance_amount']}")

            st.write(f"📅 Joined : {tenant['joining_date']}")
        with col2:

            if st.button(
                "✏ Edit",
                key=f"edit_{tenant['id']}"
            ):

                st.session_state.edit_tenant = tenant

                st.rerun()
        with col3:

            if st.button(
                "🗑 Delete",
                key=f"delete_{tenant['id']}"
            ):

                delete_tenant(
                    tenant["id"]
                )

                st.success("Tenant Deleted")

                st.rerun()

        st.divider()