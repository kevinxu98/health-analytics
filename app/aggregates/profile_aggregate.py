from app.events.events import UserCreatedEvent

class ProfileAggregate:
    def __init__(self, user_id, name):
        self._id = user_id
        self._name = name
        self._uncommitted_events = []
        self._apply(UserCreatedEvent(user_id, name))

    def _apply(self, event):
        if isinstance(event, UserCreatedEvent):
            self._id = event.user_id
            self._name = event.name
        self._uncommitted_events.append(event)

    def get_uncommitted_events(self):
        return self._uncommitted_events