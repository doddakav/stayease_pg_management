from fastapi import APIRouter
from pydantic import BaseModel
from database import supabase
from datetime import date

router = APIRouter()


class Payment(BaseModel):
    tenant_id: int
    rent_month: str
    amount: float
    status: str


# ==========================================
# GET ALL PAYMENTS
# ==========================================

@router.get("/payments")
def get_payments():

    response = (
        supabase.table("payments")
        .select("""
            id,
            rent_month,
            amount,
            status,
            paid_on,
            tenants(
                id,
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
# ADD PAYMENT
# ==========================================

@router.post("/payments")
def add_payment(data: Payment):
    tenant_id = data.tenant_id

    # Check Duplicate Payment
    existing = (
        supabase.table("payments")
        .select("*")
        .eq("tenant_id", tenant_id)
        .eq("rent_month", data.rent_month)
        .execute()
    )

    if existing.data:
        return {
            "success": False,
            "message": "Payment already exists for this month"
        }

    # Insert Payment
    supabase.table("payments").insert({

        "tenant_id": tenant_id,

        "rent_month": data.rent_month,

        "amount": data.amount,

        "status": data.status,

        "paid_on": str(date.today()) if data.status == "Paid" else None

    }).execute()

    return {
        "success": True,
        "message": "Payment Added Successfully"
    }


# ==========================================
# DELETE PAYMENT
# ==========================================

@router.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):

    supabase.table("payments").delete().eq("id", payment_id).execute()

    return {
        "success": True,
        "message": "Payment Deleted Successfully"
    }