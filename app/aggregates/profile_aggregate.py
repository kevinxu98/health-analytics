from app.events.events import ProfileCreatedEvent
from app.db.event_store import EventStore

class ProfileAggregate:
    def __init__(self, tenant_id: str, id: str):
        self.tenant_id = tenant_id
        self.id = id
        self.version = 0
        # initialize other state as needed

    def apply(self, event):
        if isinstance(event, ProfileCreatedEvent):
            self.tenant_id = event.tenant_id
            self.id = event.id
            self.version = event.version

    def create_profile(self):
        # business logic for creating a profile
        return ProfileCreatedEvent(
            id=self.id,
            tenant_id=self.tenant_id,
            partitionKey=self.tenant_id,
            version=self.version + 1
        )