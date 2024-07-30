from fastapi import APIRouter, HTTPException, Query
from app.dtos.dtos import ProfileDTO
from db.database import create_profile

router = APIRouter()

@router.get("/test_command_endpoint")
async def test_command_endpoint():
    return {"message": "Hello from test_command_endpoint!"}

@router.post("/add_profile")
async def add_profile(user_profile: ProfileDTO, name: str = Query()):
    try:
        profile_page = create_profile(name, user_profile.dict())
        return {"message": "profile added successfully!"}
    except Exception as e:
        return {"error": str(e)}