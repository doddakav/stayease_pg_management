import streamlit as st
from api import (
    get_tenant_complaints,
    add_complaint
)


def show_tenant_complaints(user):

    st.title("🛠 My Complaints")

    st.subheader("➕ Raise Complaint")

    with st.form("tenant_complaint_form"):

        title = st.text_input(
            "Complaint Title"
        )

        description = st.text_area(
            "Description"
        )

        submit = st.form_submit_button(
            "Raise Complaint"
        )

        if submit:

            result = add_complaint(

                user["tenant_id"],

                title,

                description,

                "Pending"

            )

            if result["success"]:

                st.success(result["message"])

                st.rerun()

            else:

                st.error(result["message"])

    st.divider()

    st.subheader("📋 Complaint History")

    complaints = get_tenant_complaints(
        user["id"]
    )

    if len(complaints) == 0:

        st.info("No Complaints Found")

        return

    for complaint in complaints:

        st.markdown(
            f"### 🛠 {complaint['title']}"
        )

        st.write(
            complaint["description"]
        )

        st.write(
            f"📌 Status : {complaint['status']}"
        )

        st.divider()