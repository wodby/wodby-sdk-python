import os
import wodby_sdk
from pprint import pprint

configuration = wodby_sdk.Configuration()
configuration.api_key['X-API-KEY'] = os.environ['WODBY_API_KEY']

user_api = wodby_sdk.UserApi(wodby_sdk.ApiClient(configuration))
user_api.get_authenticated_user()

org_api = wodby_sdk.OrganizationApi(wodby_sdk.ApiClient(configuration))
org_api.get_orgs()

pprint('OK')
