from database import db, container
import azure.cosmos.exceptions as exceptions

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

def profile_schema(id, name, age, params, risk):
    profile = {
        'id': id,
        'name': name,
        'age': age,
        'params': params,
        'risk': risk
    }
    return profile

def create_profile():
    print('\nCreating Profile\n')
    profile_id = '1'  # The ID for the profile you want to create
    query = f"SELECT * FROM c WHERE c.id = '{profile_id}'"

    try:
        # Query for existing profile
        existing_profiles = list(container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))

        if existing_profiles:
            print(f'Profile with id \'{profile_id}\' already exists.')
        else:
            # Create the profile
            profile_page = profile_schema(profile_id, 'John Doe', 20, 'params', 'risk')
            container.create_item(body=profile_page)
            print(f'Profile with id \'{profile_id}\' created successfully.')

    except exceptions.CosmosHttpResponseError as e:
        print('An error occurred while querying or creating the profile.')
        print(e.http_error_message)
