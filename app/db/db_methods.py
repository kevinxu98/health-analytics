# import azure.cosmos.exceptions as exceptions
# import app.utils.utils as utils
# from app.db.database import container

# def profile_schema(id, name, age, params, risk):
#     profile = {
#         'id': id,
#         'name': name,
#         'age': age,
#         'params': params,
#         'risk': risk
#     }
#     return profile

# def create_profile(name, user_profile):
#     print('\nCreating Profile\n')
#     try:
#         profile = {
#             'id': utils.IDGenerator.generate_id(),
#             'name': name, 
#             'profile': user_profile
#         }
#         container.create_item(body=profile)
#     except exceptions.CosmosHttpResponseError as e:
#         print(e.http_error_message)


