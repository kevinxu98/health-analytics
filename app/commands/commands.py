from pydantic import BaseModel
from app.utils.utils import IDGenerator


class CreateProfileCommand(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    timestamp: str

class UpdateHealthSummaryCommand(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    timestamp: str
    health_summary: str

