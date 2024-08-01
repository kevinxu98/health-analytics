from pydantic import BaseModel


class GetProfileQuery(BaseModel):
    tenant_id: str
    id: str