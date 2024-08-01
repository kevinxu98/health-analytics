from pydantic import BaseModel


class CreateProfileCommand(BaseModel):
    tenant_id: str
    id: str


class UpdateProfileCommand(BaseModel):
    tenant_id: str
    id: str
    profile: dict

