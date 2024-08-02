from fastapi import APIRouter, Query
from app.commands.commands import ComputeRiskCommand, CreateProfileCommand, UpdateHealthSummaryCommand
from app.dtos.dtos import HealthSummaryDTO
from app.handlers.command_handlers.command_handlers import ComputeRiskCommandHandler, CreateProfileCommandHandler, UpdateHealthSummaryCommandHandler
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
                tenant_id=tenant_id,
                user_id=user_id,
                )
            )
    except Exception as e:
        return {"error": str(e)}
    
@router.put("/update_health_summary")
async def update_profile(health_summary: HealthSummaryDTO, tenant_id: str=Query(...), user_id: str=Query(...)):
    try:
        return await UpdateHealthSummaryCommandHandler(EventStore()).handle(
            UpdateHealthSummaryCommand(
                tenant_id=tenant_id,
                user_id=user_id,
                health_summary=health_summary
                )
            )
    except Exception as e:
        return {"error": str(e)}

@router.put("/compute_risk")
async def compute_risk(tenant_id: str=Query(...), user_id: str=Query(...)):
    try:
        return await ComputeRiskCommandHandler(EventStore()).handle(
            ComputeRiskCommand(
                tenant_id=tenant_id,
                user_id=user_id
                )
            )
    except Exception as e:
        return {"error": str(e)}