from fastapi import APIRouter, Query
from app.commands.commands import CreateProfileCommand, UpdateHealthSummaryCommand
from app.dtos.dtos import HealthSummaryDTO
from app.handlers.command_handlers.command_handlers import CreateProfileCommandHandler, UpdateHealthSummaryCommandHandler
from app.db.event_store import EventStore
from app.utils.utils import IDGenerator, TimestampGenerator

router = APIRouter()

@router.get("/test_command_endpoint")
async def test_command_endpoint():
    return {"message": "Hello from test_command_endpoint!"}

@router.post("/create_profile")
async def create_profile(tenant_id: str=Query(...), user_id: str=Query(...)):
    try:
        return await CreateProfileCommandHandler(EventStore()).handle(
            CreateProfileCommand(
                id=f'{user_id}:{IDGenerator.generate_id()}', 
                tenant_id=tenant_id,
                user_id=user_id,
                timestamp=TimestampGenerator.generate_timestamp()
                )
            )
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/update_health_summary")
async def update_profile(health_summary: HealthSummaryDTO, tenant_id: str=Query(...), user_id: str=Query(...)):
    try:
        return await UpdateHealthSummaryCommandHandler(EventStore()).handle(
            UpdateHealthSummaryCommand(
                id=f'{user_id}:{IDGenerator.generate_id()}', 
                tenant_id=tenant_id,
                user_id=user_id,
                timestamp=TimestampGenerator.generate_timestamp(),
                health_summary=health_summary
                )
            )
    except Exception as e:
        return {"error": str(e)}
