from app.events.events import ProfileCreatedEvent
from app.db.event_store import EventStore

class ProfileAggregate:
    def __init__(self, id: str, tenant_id: str, user_id: str, timestamp: str):
        self.id = id
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.version = 0

    def apply(self, event):
        if isinstance(event, ProfileCreatedEvent):
            self.id = event.id,
            self.tenant_id = event.tenant_id,
            self.user_id = event.user_id
            self.timestamp = event.timestamp
            self.version = event.version

    def create_profile(self):
        # business logic for creating a profile
        return ProfileCreatedEvent(
            id=self.id,
            tenant_id=self.tenant_id,
            user_id=self.user_id,
            timestamp=self.timestamp,
            version=self.version + 1
        )