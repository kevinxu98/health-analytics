import uuid
from datetime import datetime

class IDGenerator:
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

class TimestampGenerator:
    @staticmethod
    def generate_timestamp():
        return datetime.now().isoformat()