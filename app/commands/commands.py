from pydantic import BaseModel


class CreateProfileCommand(BaseModel):
    tenant_id: str
    user_id: str


class UpdateProfileCommand(BaseModel):
    tenant_id: str
    user_id: str
    profile: dict

