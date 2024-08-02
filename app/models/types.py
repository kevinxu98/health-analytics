from pydantic import BaseModel
from typing import Optional
from app.dtos.dtos import HealthSummaryDTO

class ProfileView(BaseModel):
    tenant_id: str
    id: str
    timestamp: str
    health_summary: Optional[HealthSummaryDTO] = None