import streamlit as st
from api import (
    get_tenants,
    get_complaints,
    add_complaint,
    update_complaint,
    delete_complaint
)


def show_complaints():

    st.title("🛠 Complaint Management")

    # =====================================
    # ADD COMPLAINT
    # =====================================

    st.subheader("➕ Add Complaint")

    tenants = get_tenants()

    if len(tenants) == 0:
        st.warning("No tenants found.")
        return

    tenant_dict = {}

    for tenant in tenants:
        label = f"{tenant['users']['name']} ({tenant['users']['mobile_number']})"
        tenant_dict[label] = tenant["id"]

    with st.form("complaint_form"):

        tenant_name = st.selectbox(
            "Select Tenant",
            list(tenant_dict.keys())
        )

        title = st.text_input(
            "Complaint Title"
        )

        description = st.text_area(
            "Description"
        )

        status = st.selectbox(
            "Status",
            [
                "Pending",
                "Resolved"
            ]
        )

        submit = st.form_submit_button(
            "Add Complaint"
        )

        if submit:

            result = add_complaint(

                tenant_dict[tenant_name],

                title,

                description,

                status

            )

            if result["success"]:

                st.success(result["message"])

                st.rerun()

            else:

                st.error(result["message"])

    st.divider()

    # =====================================
    # COMPLAINT HISTORY
    # =====================================

    st.subheader("📋 Complaint History")

    complaints = get_complaints()

    if len(complaints) == 0:

        st.info("No Complaints Found")

        return

    for complaint in complaints:

        tenant = complaint["tenants"]["users"]

        room = complaint["tenants"]["rooms"]

        col1, col2, col3 = st.columns([6, 1, 1])

        with col1:

            st.markdown(f"### 🏠 Room {room['room_number']}")

            st.write(f"👤 Tenant : {tenant['name']}")

            st.write(f"🛠 Title : {complaint['title']}")

            st.write(f"📝 Description : {complaint['description']}")

            st.write(f"📌 Status : {complaint['status']}")

        with col2:

            if complaint["status"] == "Pending":

                if st.button(
                    "✅ Resolve",
                    key=f"resolve_{complaint['id']}"
                ):

                    update_complaint(
                        complaint["id"],
                        "Resolved"
                    )

                    st.success(
                        "Complaint Resolved"
                    )

                    st.rerun()

        with col3:

            if st.button(
                "🗑 Delete",
                key=f"delete_{complaint['id']}"
            ):

                delete_complaint(
                    complaint["id"]
                )

                st.success(
                    "Complaint Deleted"
                )

                st.rerun()

        st.divider()