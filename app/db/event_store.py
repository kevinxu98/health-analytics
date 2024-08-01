import azure.cosmos.cosmos_client as cosmos_client
from azure.cosmos import PartitionKey, exceptions
from app.events.events import ProfileCreatedEvent
from app.db import db_configs
from app.db.database import client, get_database, get_event_container

HOST = db_configs.settings['host']
MASTER_KEY = db_configs.settings['master_key']

class EventStore:
    def __init__(self):
        self.client = client
        self.database = get_database()
        self.container = get_event_container()

    async def save_event(self, event):
        try:
            self.container.create_item(event.dict())
        except exceptions.CosmosHttpResponseError as e:
            print(f'Error saving event: {e}')

    async def get_events(self, tenant_id: str):
        query = f"SELECT * FROM c WHERE c.tenant_id='{tenant_id}' ORDER BY c.version ASC"
        events = self.container.query_items(query=query, enable_cross_partition_query=True)
        return [self._deserialize_event(e) for e in events]

    def _deserialize_event(self, event_data):
        return ProfileCreatedEvent(**event_data)
