from pydantic import BaseModel


class GetProfileQuery(BaseModel):
    tenant_id: str
    user_id: str