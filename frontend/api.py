import requests

BASE_URL = " https://stayease-pg-backend.onrender.com"


# ==========================================
# LOGIN
# ==========================================

def login(mobile_number, password):

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "mobile_number": mobile_number,
            "password": password
        }
    )

    return response.json()


# ==========================================
# ROOMS
# ==========================================

def get_rooms():

    response = requests.get(f"{BASE_URL}/rooms")

    return response.json()


def add_room(room_number, capacity):

    response = requests.post(
        f"{BASE_URL}/rooms",
        json={
            "room_number": room_number,
            "capacity": capacity
        }
    )

    return response.json()


def update_room(room_id, room_number, capacity):

    response = requests.put(
        f"{BASE_URL}/rooms/{room_id}",
        json={
            "room_number": room_number,
            "capacity": capacity
        }
    )

    return response.json()


def delete_room(room_id):

    response = requests.delete(
        f"{BASE_URL}/rooms/{room_id}"
    )

    return response.json()


# ==========================================
# TENANTS
# ==========================================

def get_tenants():

    response = requests.get(
        f"{BASE_URL}/tenants"
    )

    return response.json()


def add_tenant(
    name,
    mobile_number,
    room_number,
    advance_amount,
    monthly_rent,
    joining_date
):

    response = requests.post(

        f"{BASE_URL}/tenants",

        json={

            "name": name,

            "mobile_number": mobile_number,

            "password": mobile_number,

            "room_number": room_number,

            "advance_amount": advance_amount,

            "monthly_rent": monthly_rent,

            "joining_date": joining_date

        }

    )

    return response.json()


def delete_tenant(tenant_id):

    response = requests.delete(
        f"{BASE_URL}/tenants/{tenant_id}"
    )

    return response.json()
# ==========================================
# PAYMENTS
# ==========================================

def get_payments():

    response = requests.get(
        f"{BASE_URL}/payments"
    )

    return response.json()


def add_payment(
    tenant_id,
    rent_month,
    amount,
    status
):

    response = requests.post(

        f"{BASE_URL}/payments",

        json={

            "tenant_id": tenant_id,

            "rent_month": rent_month,

            "amount": amount,

            "status": status

        }

    )

    return response.json()


def delete_payment(payment_id):

    response = requests.delete(
        f"{BASE_URL}/payments/{payment_id}"
    )

    return response.json()
# ==========================================
# COMPLAINTS
# ==========================================

def get_complaints():

    response = requests.get(
        f"{BASE_URL}/complaints"
    )

    return response.json()


def add_complaint(
    tenant_id,
    title,
    description,
    status
):

    response = requests.post(

        f"{BASE_URL}/complaints",

        json={

            "tenant_id": tenant_id,

            "title": title,

            "description": description,

            "status": status

        }

    )

    return response.json()


def update_complaint(
    complaint_id,
    status
):

    response = requests.put(

        f"{BASE_URL}/complaints/{complaint_id}",

        json={
            "status": status
        }

    )

    return response.json()


def delete_complaint(
    complaint_id
):

    response = requests.delete(
        f"{BASE_URL}/complaints/{complaint_id}"
    )

    return response.json()
# ==========================================
# DASHBOARD
# ==========================================

def get_dashboard():

    response = requests.get(
        f"{BASE_URL}/dashboard"
    )

    return response.json()
# ==========================================
# TENANT
# ==========================================

def get_tenant_dashboard(user_id):

    response = requests.get(
        f"{BASE_URL}/tenant/dashboard/{user_id}"
    )

    return response.json()


def get_tenant_payments(user_id):

    response = requests.get(
        f"{BASE_URL}/tenant/payments/{user_id}"
    )

    return response.json()


def get_tenant_complaints(user_id):

    response = requests.get(
        f"{BASE_URL}/tenant/complaints/{user_id}"
    )

    return response.json()
# ==========================================
# CHANGE PASSWORD
# ==========================================

def change_password(
    user_id,
    current_password,
    new_password
):

    response = requests.put(

        f"{BASE_URL}/tenant/change-password",

        json={

            "user_id": user_id,

            "current_password": current_password,

            "new_password": new_password

        }

    )

    return response.json()
# ==========================================
# UPDATE ROOM
# ==========================================

def update_room(
    room_id,
    room_number,
    capacity
):

    response = requests.put(

        f"{BASE_URL}/rooms/{room_id}",

        json={

            "room_number": room_number,
            "capacity": capacity

        }

    )

    return response.json()
# ==========================================
# UPDATE TENANT
# ==========================================

def update_tenant(
    tenant_id,
    name,
    mobile_number,
    room_number,
    advance_amount,
    monthly_rent,
    joining_date
):

    response = requests.put(

        f"{BASE_URL}/tenants/{tenant_id}",

        json={

            "name": name,
            "mobile_number": mobile_number,
            "room_number": room_number,
            "advance_amount": advance_amount,
            "monthly_rent": monthly_rent,
            "joining_date": joining_date

        }

    )

    return response.json()