import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import app.db.db_configs as db_configs

HOST = db_configs.settings['host']
MASTER_KEY = db_configs.settings['master_key']
DATABASE_ID = db_configs.settings['database_id']
EVENT_CONTAINER_ID = db_configs.settings['event_container_id']
PROJECTION_CONTAINER_ID = db_configs.settings['projection_container_id']

client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})

# database
def create_database():
    try:
        db = client.create_database(id=DATABASE_ID)
        print('Database with id \'{0}\' created'.format(DATABASE_ID))
        return db
    except exceptions.CosmosResourceExistsError:
        db = client.get_database_client(DATABASE_ID)
        print('Database with id \'{0}\' was found'.format(DATABASE_ID))
        return db

# events container
def create_events_container(db):
    try:
        db.create_container(id=EVENT_CONTAINER_ID, partition_key=PartitionKey(path='/tenant_id'))
        print('Container with id \'{0}\' created'.format(EVENT_CONTAINER_ID))
    except exceptions.CosmosResourceExistsError:
        db.get_container_client(EVENT_CONTAINER_ID)
        print('Container with id \'{0}\' was found'.format(EVENT_CONTAINER_ID))

# projection container
def create_projections_container(db):
    try:
        db.create_container(id=PROJECTION_CONTAINER_ID , partition_key=PartitionKey(path='/tenant_id'))
        print('Container with id \'{0}\' created'.format(PROJECTION_CONTAINER_ID ))
    except exceptions.CosmosResourceExistsError:
        db.get_container_client(PROJECTION_CONTAINER_ID )
        print('Container with id \'{0}\' was found'.format(PROJECTION_CONTAINER_ID ))

# create containers
def create_containers():
    db = create_database()
    create_events_container(db)
    create_projections_container(db)

# throughput scaling
def scale_container(container):
    print('\nScaling Container\n')
    try:
        offer = container.read_offer()
        print('Found Offer and its throughput is \'{0}\''.format(offer.offer_throughput))

        offer.offer_throughput += 100
        container.replace_throughput(offer.offer_throughput)
        print('Replaced Offer. Offer Throughput is now \'{0}\''.format(offer.offer_throughput))
    except exceptions.CosmosHttpResponseError as e:
        if e.status_code == 400:
            print('Cannot read container throuthput.')
            print(e.http_error_message)
        else:
            raise e
        
def get_database():
    return client.get_database_client(DATABASE_ID)

def get_event_container():
    return get_database().get_container_client(EVENT_CONTAINER_ID)

def get_projection_container():
    return get_database().get_container_client(PROJECTION_CONTAINER_ID)

