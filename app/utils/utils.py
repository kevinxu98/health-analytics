import uuid

class IDGenerator:
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

