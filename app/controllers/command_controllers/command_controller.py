from fastapi import APIRouter, HTTPException, Query
from app.dtos.dtos import ProfileDTO
from app.commands.commands import CreateProfileCommand
from app.handlers.command_handlers.command_handlers import CreateProfileCommandHandler
from app.db.event_store import EventStore

router = APIRouter()

@router.get("/test_command_endpoint")
async def test_command_endpoint():
    return {"message": "Hello from test_command_endpoint!"}

@router.post("/create_profile")
async def create_profile(tenant_id: str=Query(...), id: str=Query(...)):
    try:
        return await CreateProfileCommandHandler(EventStore()).handle(CreateProfileCommand(tenant_id=tenant_id, id=id))
    except Exception as e:
        return {"error": str(e)}
    
