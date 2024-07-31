

class ProjectionStore:

    def __init__(self, db_client):
        self.db_client = db_client

    def save_user_projection(self, user_id, name):
        self.db_client.create_item({"id": user_id, "name": name}, partition_key=user_id)