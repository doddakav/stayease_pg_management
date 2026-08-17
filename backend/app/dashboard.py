from fastapi import APIRouter
from app.database import supabase

router = APIRouter()


# ==========================================
# DASHBOARD
# ==========================================

@router.get("/dashboard")
def get_dashboard():

    # Total Rooms
    rooms = supabase.table("rooms").select("*").execute()

    # Total Tenants
    tenants = supabase.table("tenants").select("*").execute()

    # Total Payments
    payments = supabase.table("payments").select("*").execute()

    # Pending Complaints
    complaints = (
        supabase.table("complaints")
        .select("*")
        .eq("status", "Pending")
        .execute()
    )

    total_rooms = len(rooms.data)
    total_tenants = len(tenants.data)

    # Count distinct rooms that have at least one tenant,
    # instead of just counting tenants (a room can hold more than one tenant)
    occupied_room_ids = set()

    for tenant in tenants.data:
        occupied_room_ids.add(tenant["room_id"])

    occupied_rooms = len(occupied_room_ids)
    vacant_rooms = total_rooms - occupied_rooms
    total_payments = len(payments.data)
    pending_complaints = len(complaints.data)

    return {

        "total_rooms": total_rooms,

        "total_tenants": total_tenants,

        "occupied_rooms": occupied_rooms,

        "vacant_rooms": vacant_rooms,

        "total_payments": total_payments,

        "pending_complaints": pending_complaints

    }