from app.events.events import ProfileCreatedEvent
from app.db.event_store import EventStore

class ProfileAggregate:
    def __init__(self, tenant_id: str, user_id: str):
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.version = 0
        # initialize other state as needed

    def apply(self, event):
        if isinstance(event, ProfileCreatedEvent):
            self.tenant_id = event.tenant_id
            self.user_id = event.user_id
            self.version = event.version

    def create_profile(self):
        # business logic for creating a profile
        return ProfileCreatedEvent(
            tenant_id=self.tenant_id,
            user_id=self.user_id,
            version=self.version + 1
        )