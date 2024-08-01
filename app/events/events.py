from pydantic import BaseModel

class ProfileCreatedEvent(BaseModel):
    tenant_id: str
    id: str
    version: int