import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# retrieve environment variables
account_host = os.environ.get('ACCOUNT_HOST')
account_key = os.environ.get('ACCOUNT_KEY')
database_id = os.environ.get('DATABASE_ID')
event_container_id = os.environ.get('EVENT_CONTAINER_ID')
projection_container_id = os.environ.get('PROJECTION_CONTAINER_ID')


# settings dictionary with environment variables
settings = {
    'host': account_host, 
    'master_key': account_key,
    'database_id': database_id,
    'event_container_id': event_container_id,
    'projection_container_id': projection_container_id
}