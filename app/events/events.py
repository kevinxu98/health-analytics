from pydantic import BaseModel

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
    health_summary: str
    version: int