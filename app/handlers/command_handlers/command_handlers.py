import uuid
from app.commands.commands import CreateUserCommand
from app.aggregates.profile_aggregate import ProfileAggregate
from app.db.event_store import EventStore

class UserCommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def handle_create_user(self, command: CreateUserCommand):
        user_id = str(uuid.uuid4())
        user = ProfileAggregate(user_id, command.name)
        events = user.get_uncommitted_events()
        self.event_store.save(events)
        return user_id