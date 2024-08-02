from pydantic import BaseModel
from app.dtos.dtos import HealthSummaryDTO
from app.utils.utils import IDGenerator, TimestampGenerator

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

class RiskComputedEvent(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    timestamp: str
    event_type: str = "RiskComputedEvent"
    risk_score: float
    version: int