from fastapi import APIRouter
from pydantic import BaseModel
from app.database import supabase

router = APIRouter()


class Tenant(BaseModel):
    name: str
    mobile_number: str
    password: str
    room_number: str
    advance_amount: float
    monthly_rent: float
    joining_date: str


# ==========================================
# GET ALL TENANTS
# ==========================================

@router.get("/tenants")
def get_tenants():

    response = (
        supabase.table("tenants")
        .select("""
            id,
            advance_amount,
            monthly_rent,
            joining_date,
            users(name,mobile_number),
            rooms(room_number)
        """)
        .execute()
    )

    return response.data


# ==========================================
# ADD TENANT
# ==========================================

@router.post("/tenants")
def add_tenant(data: Tenant):

    # -------------------------
    # Check Mobile Already Exists
    # -------------------------

    existing = (
        supabase.table("users")
        .select("*")
        .eq("mobile_number", data.mobile_number)
        .execute()
    )

    if existing.data:
        return {
            "success": False,
            "message": "Mobile Number Already Exists"
        }

    # -------------------------
    # Find Room using Room Number
    # -------------------------

    room = (
        supabase.table("rooms")
        .select("*")
        .eq("room_number", data.room_number)
        .execute()
    )

    if not room.data:
        return {
            "success": False,
            "message": "Room Not Found"
        }

    room_data = room.data[0]

    room_id = room_data["id"]
    capacity = room_data["capacity"]

    # -------------------------
    # Check Room Capacity
    # -------------------------

    tenants = (
        supabase.table("tenants")
        .select("*")
        .eq("room_id", room_id)
        .execute()
    )

    if len(tenants.data) >= capacity:
        return {
            "success": False,
            "message": "Room is Full"
        }

    # -------------------------
    # Create Login User
    # -------------------------

    user = (
        supabase.table("users")
        .insert({
            "name": data.name,
            "mobile_number": data.mobile_number,
            "password": data.password,
            "role": "tenant"
        })
        .execute()
    )

    user_id = user.data[0]["id"]

    # -------------------------
    # Create Tenant
    # -------------------------

    supabase.table("tenants").insert({
        "user_id": user_id,
        "room_id": room_id,
        "advance_amount": data.advance_amount,
        "monthly_rent": data.monthly_rent,
        "joining_date": data.joining_date
    }).execute()

    return {
        "success": True,
        "message": "Tenant Created Successfully"
    }
class UpdateTenant(BaseModel):
    name: str
    mobile_number: str
    room_number: str
    advance_amount: float
    monthly_rent: float
    joining_date: str
# ==========================================
# UPDATE TENANT
# ==========================================

@router.put("/tenants/{tenant_id}")
def update_tenant(tenant_id: int, tenant: UpdateTenant):

    # Get room id using room number
    room = (
        supabase.table("rooms")
        .select("id")
        .eq("room_number", tenant.room_number)
        .execute()
    )

    if not room.data:
        return {
            "success": False,
            "message": "Room Not Found"
        }

    room_id = room.data[0]["id"]

    # Get tenant to find user id
    tenant_data = (
        supabase.table("tenants")
        .select("user_id")
        .eq("id", tenant_id)
        .execute()
    )

    if not tenant_data.data:
        return {
            "success": False,
            "message": "Tenant Not Found"
        }

    user_id = tenant_data.data[0]["user_id"]

    # Update user details
    (
        supabase.table("users")
        .update({
            "name": tenant.name,
            "mobile_number": tenant.mobile_number
        })
        .eq("id", user_id)
        .execute()
    )

    # Update tenant details
    (
        supabase.table("tenants")
        .update({
            "room_id": room_id,
            "advance_amount": tenant.advance_amount,
            "monthly_rent": tenant.monthly_rent,
            "joining_date": tenant.joining_date
        })
        .eq("id", tenant_id)
        .execute()
    )

    return {
        "success": True,
        "message": "Tenant Updated Successfully"
    }


# ==========================================
# DELETE TENANT
# ==========================================

@router.delete("/tenants/{tenant_id}")
def delete_tenant(tenant_id: int):

    tenant = (
        supabase.table("tenants")
        .select("*")
        .eq("id", tenant_id)
        .execute()
    )

    if not tenant.data:
        return {
            "success": False,
            "message": "Tenant Not Found"
        }

    user_id = tenant.data[0]["user_id"]

    supabase.table("tenants").delete().eq("id", tenant_id).execute()

    supabase.table("users").delete().eq("id", user_id).execute()

    return {
        "success": True,
        "message": "Tenant Deleted Successfully"
    }