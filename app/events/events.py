from pydantic import BaseModel

class ProfileCreatedEvent(BaseModel):
    id: str
    tenant_id: str
    partitionKey: str
    version: int