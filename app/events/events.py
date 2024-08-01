from pydantic import BaseModel

class ProfileCreatedEvent(BaseModel):
    tenant_id: str
    user_id: str
    version: int