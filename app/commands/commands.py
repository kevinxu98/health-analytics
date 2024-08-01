from pydantic import BaseModel
from app.utils.utils import IDGenerator


class CreateProfileCommand(BaseModel):
    id: str
    tenant_id: str
    user_id: str
    timestamp: str

class UpdateProfileCommand(BaseModel):
    tenant_id: str
    id: str
    profile: dict

