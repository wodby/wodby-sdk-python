# wodby.UserApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user**](UserApi.md#get_current_user) | **GET** /user | Get current user
[**update_current_user**](UserApi.md#update_current_user) | **PUT** /user | Update current user


# **get_current_user**
> CurrentUser get_current_user()

Get current user

Returns the authenticated user account.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.current_user import CurrentUser
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.UserApi(api_client)

    try:
        # Get current user
        api_response = api_instance.get_current_user()
        print("The response of UserApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current user |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user**
> CurrentUser update_current_user(update_current_user_request)

Update current user

Updates the authenticated user's basic profile and returns the updated account.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.current_user import CurrentUser
from wodby.models.update_current_user_request import UpdateCurrentUserRequest
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.UserApi(api_client)
    update_current_user_request = wodby.UpdateCurrentUserRequest() # UpdateCurrentUserRequest | 

    try:
        # Update current user
        api_response = api_instance.update_current_user(update_current_user_request)
        print("The response of UserApi->update_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_current_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_current_user_request** | [**UpdateCurrentUserRequest**](UpdateCurrentUserRequest.md)|  | 

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated current user |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

