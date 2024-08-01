

class ProjectionStore:

    def __init__(self, db_client):
        self.db_client = db_client

    def save_user_projection(self, id, name):
        self.db_client.create_item({"id": id, "name": name}, partitionKey=id)