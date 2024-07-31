
from dataclasses import dataclass

@dataclass
class UserCreatedEvent:
    user_id: str
    name: str