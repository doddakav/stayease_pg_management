from fastapi import APIRouter
from pydantic import BaseModel
from database import supabase

router = APIRouter()


# ==========================================
# Pydantic Models
# ==========================================

class Complaint(BaseModel):
    tenant_id: int
    title: str
    description: str
    status: str


class ComplaintStatus(BaseModel):
    status: str


# ==========================================
# GET ALL COMPLAINTS
# ==========================================

@router.get("/complaints")
def get_complaints():

    response = (
        supabase.table("complaints")
        .select("""
            id,
            title,
            description,
            status,
            created_at,
            tenants(
                id,
                rooms(
                    room_number
                ),
                users(
                    name,
                    mobile_number
                )
            )
        """)
        .execute()
    )

    return response.data

# ==========================================
# ADD COMPLAINT
# ==========================================

@router.post("/complaints")
def add_complaint(data: Complaint):

    response = (
        supabase.table("complaints")
        .insert({
            "tenant_id": data.tenant_id,
            "title": data.title,
            "description": data.description,
            "status": data.status
        })
        .execute()
    )

    return {
        "success": True,
        "message": "Complaint Added Successfully"
    }


# ==========================================
# UPDATE COMPLAINT STATUS
# ==========================================

@router.put("/complaints/{complaint_id}")
def update_complaint(complaint_id: int, data: ComplaintStatus):

    complaint = (
        supabase.table("complaints")
        .select("*")
        .eq("id", complaint_id)
        .execute()
    )

    if not complaint.data:
        return {
            "success": False,
            "message": "Complaint Not Found"
        }

    (
        supabase.table("complaints")
        .update({
            "status": data.status
        })
        .eq("id", complaint_id)
        .execute()
    )

    return {
        "success": True,
        "message": "Complaint Status Updated Successfully"
    }


# ==========================================
# DELETE COMPLAINT
# ==========================================

@router.delete("/complaints/{complaint_id}")
def delete_complaint(complaint_id: int):

    complaint = (
        supabase.table("complaints")
        .select("*")
        .eq("id", complaint_id)
        .execute()
    )

    if not complaint.data:
        return {
            "success": False,
            "message": "Complaint Not Found"
        }

    (
        supabase.table("complaints")
        .delete()
        .eq("id", complaint_id)
        .execute()
    )

    return {
        "success": True,
        "message": "Complaint Deleted Successfully"
    }

# NOTE: "Get complaints for one tenant" already exists in tenant.py
# as GET /tenant/complaints/{user_id}, so it is not duplicated here.