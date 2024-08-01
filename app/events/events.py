from pydantic import BaseModel

class ProfileCreatedEvent(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    timestamp: str
    version: int