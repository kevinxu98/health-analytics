from app.commands.commands import ComputeRiskCommand, CreateProfileCommand, UpdateHealthSummaryCommand
from app.db.event_store import EventStore
from app.aggregates.profile_aggregate import ProfileAggregate

class CreateProfileCommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    async def handle(self, command: CreateProfileCommand):
        # create aggregate instance
        profile_aggregate = ProfileAggregate(
            tenant_id=command.tenant_id,
            user_id=command.user_id, 
        )
        # apply business logic through the aggregate
        event = profile_aggregate.create_profile()
        
        # save the event to the event store
        await self.event_store.save_event(event)
        
        return event

class UpdateHealthSummaryCommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    async def handle(self, command: UpdateHealthSummaryCommand):
        # retrieve existing events
        events = await self.event_store.get_events(command.user_id)

        # load aggregate from the retrieved events
        profile_aggregate = ProfileAggregate.load_from_events(events)

        # apply new business logic through the aggregate
        event = profile_aggregate.update_health_summary(command)

        # save event
        await self.event_store.save_event(event)
        
        return event

class ComputeRiskCommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    async def handle(self, command: ComputeRiskCommand):
  
        events = await self.event_store.get_events(command.user_id)
        profile_aggregate = ProfileAggregate.load_from_events(events)

        event = profile_aggregate.compute_risk()
        await self.event_store.save_event(event)
        
        return event
        