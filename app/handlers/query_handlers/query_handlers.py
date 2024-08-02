from app.db.event_store import ProjectionStore
from app.aggregates.profile_aggregate import ProfileAggregate
from app.queries.queries import GetProfileQuery

class GetProfileQueryHandler:

    def __init__(self, projection_store: ProjectionStore):
        self.projection_store = projection_store

    async def handle(self, query: GetProfileQuery):
        profile_view = await self.projection_store.get(query.id)
        return profile_view.dict()