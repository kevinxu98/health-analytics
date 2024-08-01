from pydantic import BaseModel


class CreateProfileCommand(BaseModel):
    id: str
    tenant_id: str


class UpdateProfileCommand(BaseModel):
    tenant_id: str
    id: str
    profile: dict

