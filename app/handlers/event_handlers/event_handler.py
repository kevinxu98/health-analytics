from app.events.events import ProfileCreatedEvent, HealthSummaryUpdatedEvent
from app.db.projection_store import ProjectionStore
from app.models.types import ProfileView

class ProfileEventHandler:
    def __init__(self, projection_store: ProjectionStore):
        self.projection_store = projection_store

    async def handle(self, event):
        if isinstance(event, ProfileCreatedEvent):
            await self.handle_profile_created(event)
        elif isinstance(event, HealthSummaryUpdatedEvent):
            await self.handle_health_summary_updated(event)

    async def handle_profile_created(self, event: ProfileCreatedEvent):
        profile_view = ProfileView(
            tenant_id=event.tenant_id,
            id=event.user_id,
            version=event.version,
            timestamp=event.timestamp
        )
        await self.projection_store.save(profile_view)

    async def handle_health_summary_updated(self, event: HealthSummaryUpdatedEvent):
        existing_profile = await self.projection_store.get(event.user_id)
        if existing_profile:
            existing_profile.health_summary = event.health_summary
            existing_profile.timestamp = event.timestamp
            existing_profile.version = event.version
            await self.projection_store.save(existing_profile)
