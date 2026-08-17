import streamlit as st

from api import (
    add_room,
    get_rooms,
    update_room,
    delete_room
)


def show_rooms():

    st.title("🛏️ Room Management")

    # --------------------------
    # Session State
    # --------------------------

    if "editing_room" not in st.session_state:
        st.session_state.editing_room = None

    # --------------------------
    # Add Room
    # --------------------------

    st.subheader("➕ Add New Room")

    with st.form("add_room_form"):

        room_number = st.text_input("Room Number")

        capacity = st.number_input(
            "Capacity",
            min_value=1,
            step=1
        )

        submit = st.form_submit_button("Add Room")

        if submit:

            result = add_room(room_number, capacity)

            if result["success"]:

                st.success(result["message"])
                st.rerun()

            else:

                st.error(result["message"])

    st.divider()

    # --------------------------
    # Edit Room
    # --------------------------

    if st.session_state.editing_room is not None:

        room = st.session_state.editing_room

        st.subheader("✏ Edit Room")

        with st.form("update_room_form"):

            new_room = st.text_input(
                "Room Number",
                value=room["room_number"]
            )

            new_capacity = st.number_input(
                "Capacity",
                min_value=1,
                value=int(room["capacity"]),
                step=1
            )

            col1, col2 = st.columns(2)

            with col1:
                update = st.form_submit_button("Update")

            with col2:
                cancel = st.form_submit_button("Cancel")

            if update:

                result = update_room(
                    room["id"],
                    new_room,
                    new_capacity
                )

                st.success(result["message"])

                st.session_state.editing_room = None

                st.rerun()

            if cancel:

                st.session_state.editing_room = None

                st.rerun()

        st.divider()

    # --------------------------
    # Existing Rooms
    # --------------------------

    st.subheader("📋 Existing Rooms")

    rooms = get_rooms()

    if len(rooms) == 0:

        st.info("No Rooms Available")

        return

    for room in rooms:

        col1, col2, col3 = st.columns([5, 1, 1])

        with col1:

            st.markdown(f"### 🏠 Room {room['room_number']}")
            st.write(f"Capacity : {room['capacity']}")

        with col2:

            if st.button("✏", key=f"edit_btn_{room['id']}"):

                st.session_state.editing_room = room

                st.rerun()

        with col3:

            if st.button("🗑", key=f"delete_btn_{room['id']}"):

                delete_room(room["id"])

                st.success("Room Deleted Successfully")

                st.rerun()

        st.divider()