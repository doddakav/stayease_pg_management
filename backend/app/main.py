from fastapi import FastAPI

from app.database import supabase
from app.login import router as login_router
from app.rooms import router as rooms_router
from app.tenants import router as tenants_router
from app.payments import router as payments_router
from app.complaints import router as complaints_router
from app.dashboard import router as dashboard_router
from app.tenant import router as tenant_router

app = FastAPI(
    title="StayEase API",
    version="1.0"
)

app.include_router(login_router)
app.include_router(rooms_router)
app.include_router(tenants_router)
app.include_router(payments_router)
app.include_router(complaints_router)
app.include_router(dashboard_router)
app.include_router(tenant_router)


@app.get("/")
def home():
    return {
        "message": "StayEase API Running 🚀"
    }


@app.get("/users")
def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data