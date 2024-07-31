from fastapi import APIRouter, HTTPException, Query
from app.dtos.dtos import ProfileDTO
from app.commands.commands import CreateUserCommand
from app.handlers.command_handlers.command_handlers import UserCommandHandler

router = APIRouter()

@router.get("/test_command_endpoint")
async def test_command_endpoint():
    return {"message": "Hello from test_command_endpoint!"}

@router.get("/create_user")
async def create_user(name: str=Query(...)):
    try:
        command = CreateUserCommand(name)
        UserCommandHandler().handle_create_user(command)
        return {"message": "user created successfully!"}
    except Exception as e:
        return {"error": str(e)}
    

# @router.post("/add_profile")
# async def add_profile(user_profile: ProfileDTO, name: str = Query()):
#     try:
#         create_profile(name, user_profile.dict())
#         return {"message": "profile added successfully!"}
#     except Exception as e:
#         return {"error": str(e)}
    