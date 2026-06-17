import os
import wodby
from pprint import pprint

configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = os.environ['WODBY_API_KEY']

user_api = wodby.UserApi(wodby.ApiClient(configuration))
user_api.get_authenticated_user()

org_api = wodby.OrganizationApi(wodby.ApiClient(configuration))
org_api.get_orgs()

pprint('OK')
