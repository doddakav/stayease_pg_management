from fastapi import APIRouter
from pydantic import BaseModel
from app.database import supabase

router = APIRouter()


# ==========================================
# LOGIN MODEL
# ==========================================

class Login(BaseModel):
    mobile_number: str
    password: str


# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login(data: Login):

    response = (
        supabase.table("users")
        .select("*")
        .eq("mobile_number", data.mobile_number)
        .eq("password", data.password)
        .execute()
    )

    if not response.data:

        return {
            "success": False,
            "message": "Invalid Mobile Number or Password"
        }

    user = response.data[0]

    # --------------------------------------
    # If Tenant, Get tenant_id
    # --------------------------------------

    if user["role"] == "tenant":

        tenant = (
            supabase.table("tenants")
            .select("id")
            .eq("user_id", user["id"])
            .execute()
        )

        if tenant.data:

            user["tenant_id"] = tenant.data[0]["id"]

    return {

        "success": True,

        "message": "Login Successful",

        "user": user

    }