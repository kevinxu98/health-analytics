from typing import List
from app.commands.commands import UpdateHealthSummaryCommand
from app.dtos.dtos import HealthSummaryDTO
from app.events.events import HealthSummaryUpdatedEvent, ProfileCreatedEvent
from app.utils.utils import IDGenerator, TimestampGenerator

class ProfileAggregate:
    def __init__(self, tenant_id: str, user_id: str, version: int = 0):
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.version = version

    def apply(self, event):
        if isinstance(event, ProfileCreatedEvent):
            self.tenant_id = event.tenant_id
            self.user_id = event.user_id
            self.version = event.version
        elif isinstance(event, HealthSummaryUpdatedEvent):
            self.health_summary = event.health_summary
            self.version = event.version

    def create_profile(self):
        return ProfileCreatedEvent(
            id=f'{self.user_id}:{IDGenerator.generate_id()}',
            tenant_id=self.tenant_id,
            user_id=self.user_id,
            timestamp=TimestampGenerator.generate_timestamp(),
            version=self.version + 1
        )
    
    def update_health_summary(self, command: UpdateHealthSummaryCommand):
        return HealthSummaryUpdatedEvent(
            id=f'{self.user_id}:{IDGenerator.generate_id()}',
            tenant_id=self.tenant_id,
            user_id=self.user_id,
            timestamp=TimestampGenerator.generate_timestamp(),
            health_summary=command.health_summary,
            version=self.version + 1
        )

    @staticmethod
    def load_from_events(events: List):
        aggregate = ProfileAggregate(tenant_id="", user_id="", version=0)
        for event in events:
            aggregate.apply(event)
        return aggregate
