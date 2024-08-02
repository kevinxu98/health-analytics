from azure.cosmos import exceptions
from app.db.projection_store import ProjectionStore
from app.events.events import HealthSummaryUpdatedEvent, ProfileCreatedEvent, RiskComputedEvent
from app.db.database import client, get_database, get_event_container, get_projection_container
from app.handlers.event_handlers.event_handler import ProfileEventHandler


class EventStore:
    def __init__(self):
        self.client = client
        self.database = get_database()
        self.event_container = get_event_container()
        self.projection_store = ProjectionStore()

    async def save_event(self, event):
        try:
            profile = event.dict()
            self.event_container.create_item(body=profile)
            await self._update_projections(event)
        except exceptions.CosmosHttpResponseError as e:
            print(e.http_error_message)

    async def get_events(self, user_id: str):
        query = f"SELECT * FROM c WHERE c.user_id='{user_id}' ORDER BY c.version ASC"
        try:
            items = list(self.event_container.query_items(query=query, enable_cross_partition_query=True))
            return [self._deserialize_event(e) for e in items]
        except exceptions.CosmosHttpResponseError as e:
            print(e.http_error_message)
            return []

    def _deserialize_event(self, event_data):
        event_type = event_data.get("event_type")
        if event_type == "ProfileCreatedEvent":
            return ProfileCreatedEvent(**event_data)
        elif event_type == "HealthSummaryUpdatedEvent":
            return HealthSummaryUpdatedEvent(**event_data)
        elif event_type == "RiskComputedEvent":
            return RiskComputedEvent(**event_data)
        else:
            raise ValueError(f"Unknown event type: {event_type}")
        
    async def _update_projections(self, event):
        handler = ProfileEventHandler(self.projection_store)
        await handler.handle(event)