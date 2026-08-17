from fastapi import APIRouter
from pydantic import BaseModel
from database import supabase

router = APIRouter()


class Room(BaseModel):
    room_number: str
    capacity: int


# Get All Rooms
@router.get("/rooms")
def get_rooms():
    response = (
        supabase.table("rooms")
        .select("*")
        .order("room_number")
        .execute()
    )

    return response.data


# Add Room
@router.post("/rooms")
def add_room(room: Room):

    existing = (
        supabase.table("rooms")
        .select("*")
        .eq("room_number", room.room_number)
        .execute()
    )

    if existing.data:
        return {
            "success": False,
            "message": "Room already exists"
        }

    supabase.table("rooms").insert({
        "room_number": room.room_number,
        "capacity": room.capacity
    }).execute()

    return {
        "success": True,
        "message": "Room Added Successfully"
    }


# Update Room
@router.put("/rooms/{room_id}")
def update_room(room_id: int, room: Room):

    existing = (
        supabase.table("rooms")
        .select("*")
        .eq("id", room_id)
        .execute()
    )

    if not existing.data:
        return {
            "success": False,
            "message": "Room Not Found"
        }

    supabase.table("rooms").update({
        "room_number": room.room_number,
        "capacity": room.capacity
    }).eq("id", room_id).execute()

    return {
        "success": True,
        "message": "Room Updated Successfully"
    }


# Delete Room
@router.delete("/rooms/{room_id}")
def delete_room(room_id: int):

    supabase.table("rooms").delete().eq("id", room_id).execute()

    return {
        "success": True,
        "message": "Room Deleted Successfully"
    }