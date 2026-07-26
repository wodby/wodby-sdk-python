# wodby.AppAuthsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_auth**](AppAuthsApi.md#create_app_auth) | **POST** /app-auths | Create app auth
[**delete_app_auth**](AppAuthsApi.md#delete_app_auth) | **DELETE** /app-auths/{id} | Delete app auth
[**list_app_auths**](AppAuthsApi.md#list_app_auths) | **GET** /app-auths | List app auths
[**update_app_auth**](AppAuthsApi.md#update_app_auth) | **PUT** /app-auths/{id} | Update app auth


# **create_app_auth**
> AppAuth create_app_auth(new_app_auth_input)

Create app auth

Creates an HTTP basic authentication entry at instance, service, or route scope and returns only non-secret metadata.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_auth import AppAuth
from wodby.models.new_app_auth_input import NewAppAuthInput
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
    api_instance = wodby.AppAuthsApi(api_client)
    new_app_auth_input = wodby.NewAppAuthInput() # NewAppAuthInput | 

    try:
        # Create app auth
        api_response = api_instance.create_app_auth(new_app_auth_input)
        print("The response of AppAuthsApi->create_app_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppAuthsApi->create_app_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_app_auth_input** | [**NewAppAuthInput**](NewAppAuthInput.md)|  | 

### Return type

[**AppAuth**](AppAuth.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app auth |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_auth**
> OperationResult delete_app_auth(id)

Delete app auth

Deletes an HTTP basic authentication entry and returns the operation result.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
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
    api_instance = wodby.AppAuthsApi(api_client)
    id = 56 # int | 

    try:
        # Delete app auth
        api_response = api_instance.delete_app_auth(id)
        print("The response of AppAuthsApi->delete_app_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppAuthsApi->delete_app_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_auths**
> List[AppAuth] list_app_auths(app_instance_id)

List app auths

Returns HTTP basic authentication entries for an app instance without exposing passwords or secret identifiers.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_auth import AppAuth
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
    api_instance = wodby.AppAuthsApi(api_client)
    app_instance_id = 56 # int | 

    try:
        # List app auths
        api_response = api_instance.list_app_auths(app_instance_id)
        print("The response of AppAuthsApi->list_app_auths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppAuthsApi->list_app_auths: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | 

### Return type

[**List[AppAuth]**](AppAuth.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app auths |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_auth**
> AppAuth update_app_auth(id, update_app_auth_input)

Update app auth

Updates an HTTP basic authentication entry. Omit both scope identifiers to preserve the current scope. Supplying appServiceId moves the entry to service scope and clears any route unless appRouteId is also supplied. Recreate the entry to move it back to instance scope. Omit password to retain the existing secret.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_auth import AppAuth
from wodby.models.update_app_auth_input import UpdateAppAuthInput
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
    api_instance = wodby.AppAuthsApi(api_client)
    id = 56 # int | 
    update_app_auth_input = wodby.UpdateAppAuthInput() # UpdateAppAuthInput | 

    try:
        # Update app auth
        api_response = api_instance.update_app_auth(id, update_app_auth_input)
        print("The response of AppAuthsApi->update_app_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppAuthsApi->update_app_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_auth_input** | [**UpdateAppAuthInput**](UpdateAppAuthInput.md)|  | 

### Return type

[**AppAuth**](AppAuth.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app auth |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

