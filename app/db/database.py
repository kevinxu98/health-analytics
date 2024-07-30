import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})

if client.get_database_client(DATABASE_ID):
    db = client.get_database_client(DATABASE_ID)
    print('Database with id \'{0}\' was found'.format(DATABASE_ID))
else:
    db = client.create_database(id=DATABASE_ID)

if db.get_container_client(CONTAINER_ID):
    container = db.get_container_client(CONTAINER_ID)
    print('Container with id \'{0}\' was found'.format(CONTAINER_ID))
else:
    container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/partitionKey'))


class CosmosDBManager:

    def __init__(self, host, master_key):
        self.client = cosmos_client.CosmosClient(host, {'masterKey': master_key})

    def create_database(self, database_id, container_id):
        # setup database
        try:
            self.db = self.client.create_database(id=database_id)
            print('Database with id \'{0}\' created'.format(database_id))
        except exceptions.CosmosResourceExistsError:
            self.db = self.client.get_database_client(database_id)
            print('Database with id \'{0}\' was found'.format(database_id))

        # setup container
        try:
            self.container = self.db.create_container(id=container_id, partition_key=PartitionKey(path='/partitionKey'))
            print('Container with id \'{0}\' created'.format(container_id))
        except exceptions.CosmosResourceExistsError:
            self.container = self.db.get_container_client(container_id)
            print('Container with id \'{0}\' was found'.format(container_id))

    def scale_container(self):
        print('\nScaling Container\n')
        try:
            offer = self.container.read_offer()
            print('Found Offer and its throughput is \'{0}\''.format(offer.offer_throughput))

            offer.offer_throughput += 100
            self.container.replace_throughput(offer.offer_throughput)
            print('Replaced Offer. Offer Throughput is now \'{0}\''.format(offer.offer_throughput))
        except exceptions.CosmosHttpResponseError as e:
            if e.status_code == 400:
                print('Cannot read container throuthput.')
                print(e.http_error_message)
            else:
                raise e

    def profile_schema(self, id, name, age, params, risk):
        profile = {
            'id': id,
            'name': name,
            'age': age,
            'params': params,
            'risk': risk
        }
        return profile
    
    def create_profile(self):
        print('\nCreating Profile\n')
        profile_page = self.profile_schema('1', 'John Doe', 20, 'params', 'risk')
        self.container.create_item(body=profile_page)

    def update_profile(self, container, id):
        pass

if __name__ == "__main__":
    db_manager = CosmosDBManager(HOST, MASTER_KEY)
    db_manager.create_database(DATABASE_ID, CONTAINER_ID)
    db_manager.create_profile()

 