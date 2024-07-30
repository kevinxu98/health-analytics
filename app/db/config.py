import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# retrieve environment variables
account_host = os.environ.get('ACCOUNT_HOST')
account_key = os.environ.get('ACCOUNT_KEY')
database_id = os.environ.get('COSMOS_DATABASE')
container_id = os.environ.get('COSMOS_CONTAINER')

# Create a settings dictionary with environment variables
settings = {
    'host': account_host, 
    'master_key': account_key,
    'database_id': database_id,
    'container_id': container_id,
}