

class EventStore:
    def __init__(self, db_client):
        self.db_client = db_client

    def save(self, events):
        for event in events:
            self.db_client.create_item(event.__dict__, partition_key=event.user_id)