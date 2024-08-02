from pydantic import BaseModel
from app.dtos.dtos import HealthSummaryDTO


class CreateProfileCommand(BaseModel):
    tenant_id: str
    user_id: str

class UpdateHealthSummaryCommand(BaseModel):
    tenant_id: str
    user_id: str
    health_summary: HealthSummaryDTO

class ComputeRiskCommand(BaseModel):
    tenant_id: str
    user_id: str

