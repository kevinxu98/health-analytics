from azure.cosmos import CosmosClient, exceptions
from app.models.types import ProfileView
from app.db.database import client, get_database, get_projection_container

class ProjectionStore:
    def __init__(self):
        self.client = client
        self.database = get_database()
        self.projection_container = get_projection_container()

    async def save(self, profile_view: ProfileView):
        try:
            profile_dict = profile_view.dict()
            self.projection_container.upsert_item(body=profile_dict)
        except exceptions.CosmosHttpResponseError as e:
            print(e.http_error_message)

    async def get(self, user_id: str) -> ProfileView:
        query = f"SELECT * FROM c WHERE c.id='{user_id}'"
        try:
            items = list(self.projection_container.query_items(query=query, enable_cross_partition_query=True))
            if items:
                return ProfileView(**items[0])
        except exceptions.CosmosHttpResponseError as e:
            print(e.http_error_message)
            return None
