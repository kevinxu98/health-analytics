from azure.cosmos import exceptions
from app.events.events import HealthSummaryUpdatedEvent, ProfileCreatedEvent
from app.db.database import client, get_database, get_event_container


class EventStore:
    def __init__(self):
        self.client = client
        self.database = get_database()
        self.container = get_event_container()

    async def save_event(self, event):
        try:
            profile = event.dict()
            self.container.create_item(body=profile)
        except exceptions.CosmosHttpResponseError as e:
            print(e.http_error_message)

    async def get_events(self, user_id: str):
        query = f"SELECT * FROM c WHERE c.user_id='{user_id}' ORDER BY c.version ASC"
        try:
            items = list(self.container.query_items(query=query, enable_cross_partition_query=True))
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
        else:
            raise ValueError(f"Unknown event type: {event_type}")