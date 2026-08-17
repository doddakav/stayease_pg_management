from fastapi import APIRouter
from app.database import supabase
from pydantic import BaseModel

router = APIRouter()


# ==========================================
# TENANT DASHBOARD
# ==========================================

@router.get("/tenant/dashboard/{user_id}")
def tenant_dashboard(user_id: int):

    response = (
        supabase.table("tenants")
        .select("""
            joining_date,
            advance_amount,
            monthly_rent,
            rooms(
                room_number
            ),
            users(
                name,
                mobile_number
            )
        """)
        .eq("user_id", user_id)
        .execute()
    )

    if not response.data:
        return {
            "success": False,
            "message": "Tenant Not Found"
        }

    return response.data[0]


# ==========================================
# MY PAYMENTS
# ==========================================

@router.get("/tenant/payments/{user_id}")
def tenant_payments(user_id: int):

    tenant = (
        supabase.table("tenants")
        .select("id")
        .eq("user_id", user_id)
        .execute()
    )

    if not tenant.data:
        return []

    tenant_id = tenant.data[0]["id"]

    payments = (
        supabase.table("payments")
        .select("*")
        .eq("tenant_id", tenant_id)
        .execute()
    )

    return payments.data


# ==========================================
# MY COMPLAINTS
# ==========================================

@router.get("/tenant/complaints/{user_id}")
def tenant_complaints(user_id: int):

    tenant = (
        supabase.table("tenants")
        .select("id")
        .eq("user_id", user_id)
        .execute()
    )

    if not tenant.data:
        return []

    tenant_id = tenant.data[0]["id"]

    complaints = (
        supabase.table("complaints")
        .select("*")
        .eq("tenant_id", tenant_id)
        .execute()
    )

    return complaints.data




# ==========================================
# CHANGE PASSWORD MODEL
# ==========================================

class ChangePassword(BaseModel):
    user_id: int
    current_password: str
    new_password: str


# ==========================================
# CHANGE PASSWORD
# ==========================================

@router.put("/tenant/change-password")
def change_password(data: ChangePassword):

    # Check current password
    user = (
        supabase.table("users")
        .select("*")
        .eq("id", data.user_id)
        .eq("password", data.current_password)
        .execute()
    )

    if not user.data:
        return {
            "success": False,
            "message": "Current Password is Incorrect"
        }

    # Update password
    (
        supabase.table("users")
        .update({
            "password": data.new_password
        })
        .eq("id", data.user_id)
        .execute()
    )

    return {
        "success": True,
        "message": "Password Changed Successfully"
    }