from pydantic import BaseModel
from app.dtos.dtos import HealthSummaryDTO

class ProfileCreatedEvent(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    timestamp: str
    event_type: str = "ProfileCreatedEvent"
    version: int

class HealthSummaryUpdatedEvent(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    timestamp: str
    event_type: str = "HealthSummaryUpdatedEvent"
    health_summary: HealthSummaryDTO
    version: int