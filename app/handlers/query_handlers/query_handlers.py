from app.db.event_store import EventStore
from app.aggregates.profile_aggregate import ProfileAggregate

class ProfileQueryHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    async def get_profile(self, tenant_id: str):
        events = await self.event_store.get_events(tenant_id)
        if not events:
            return None
        profile = ProfileAggregate(tenant_id, events[0].id)
        for event in events:
            profile.apply(event)
        return profile.to_dict()
