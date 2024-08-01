from typing import List
from app.commands.commands import UpdateHealthSummaryCommand
from app.dtos.dtos import HealthSummaryDTO
from app.events.events import HealthSummaryUpdatedEvent, ProfileCreatedEvent

class ProfileAggregate:
    def __init__(self, id: str, tenant_id: str, user_id: str, timestamp: str, version: int = 0):
        self.id = id
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.version = version
        self.health_summary = None  # Initialize health summary if needed

    def apply(self, event):
        if isinstance(event, ProfileCreatedEvent):
            self.id = event.id
            self.tenant_id = event.tenant_id
            self.user_id = event.user_id
            self.timestamp = event.timestamp
            self.version = event.version
        elif isinstance(event, HealthSummaryUpdatedEvent):
            self.timestamp = event.timestamp
            self.health_summary = event.health_summary
            self.version = event.version

    def create_profile(self):
        return ProfileCreatedEvent(
            id=self.id,
            tenant_id=self.tenant_id,
            user_id=self.user_id,
            timestamp=self.timestamp,
            version=self.version + 1
        )
    
    def update_health_summary(self, command: UpdateHealthSummaryCommand):
        return HealthSummaryUpdatedEvent(
            id=command.id,
            tenant_id=self.tenant_id,
            user_id=self.user_id,
            timestamp=command.timestamp,
            health_summary=command.health_summary,
            version=self.version + 1
        )

    @staticmethod
    def load_from_events(events: List):
        aggregate = ProfileAggregate(id="", tenant_id="", user_id="", timestamp="", version=0)
        for event in events:
            aggregate.apply(event)
        return aggregate
