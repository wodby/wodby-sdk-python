# wodby.UserApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authenticated_user**](UserApi.md#get_authenticated_user) | **GET** /user | 


# **get_authenticated_user**
> User get_authenticated_user()



Retrieve authenticated user

### Example
```python
from __future__ import print_function
import time
import wodby
from wodby.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby.UserApi(wodby.ApiClient(configuration))

try:
    api_response = api_instance.get_authenticated_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_authenticated_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

