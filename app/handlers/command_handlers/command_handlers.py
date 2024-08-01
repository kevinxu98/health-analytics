from app.commands.commands import CreateProfileCommand
from app.events.events import ProfileCreatedEvent
from app.db.event_store import EventStore
from app.aggregates.profile_aggregate import ProfileAggregate

class CreateProfileCommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    async def handle(self, command: CreateProfileCommand):
        # create the aggregate instance
        profile_aggregate = ProfileAggregate(
            id=command.id,
            tenant_id=command.tenant_id,
            user_id=command.user_id, 
            timestamp=command.timestamp
        )
        # apply business logic through the aggregate
        event = profile_aggregate.create_profile()
        
        # save the event to the event store
        await self.event_store.save_event(event)
        
        return event
