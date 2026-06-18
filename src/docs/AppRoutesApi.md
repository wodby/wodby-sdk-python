# wodby.AppRoutesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_route**](AppRoutesApi.md#create_app_route) | **POST** /app-routes | Create app route
[**delete_app_route**](AppRoutesApi.md#delete_app_route) | **DELETE** /app-routes/{id} | Delete app route
[**get_app_route**](AppRoutesApi.md#get_app_route) | **GET** /app-routes/{id} | Get app route
[**list_app_routes**](AppRoutesApi.md#list_app_routes) | **GET** /app-routes | List app routes
[**update_app_route**](AppRoutesApi.md#update_app_route) | **PUT** /app-routes/{id} | Update app route


# **create_app_route**
> AppRoute create_app_route(new_app_route_input)

Create app route

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_route import AppRoute
from wodby.models.new_app_route_input import NewAppRouteInput
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppRoutesApi(api_client)
    new_app_route_input = wodby.NewAppRouteInput() # NewAppRouteInput | 

    try:
        # Create app route
        api_response = api_instance.create_app_route(new_app_route_input)
        print("The response of AppRoutesApi->create_app_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->create_app_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_app_route_input** | [**NewAppRouteInput**](NewAppRouteInput.md)|  | 

### Return type

[**AppRoute**](AppRoute.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app route |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_route**
> OperationResult delete_app_route(id)

Delete app route

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppRoutesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app route
        api_response = api_instance.delete_app_route(id)
        print("The response of AppRoutesApi->delete_app_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->delete_app_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_route**
> AppRoute get_app_route(id)

Get app route

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_route import AppRoute
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppRoutesApi(api_client)
    id = 56 # int | 

    try:
        # Get app route
        api_response = api_instance.get_app_route(id)
        print("The response of AppRoutesApi->get_app_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->get_app_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppRoute**](AppRoute.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App route |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_routes**
> List[AppRoute] list_app_routes(app_instance_id)

List app routes

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_route import AppRoute
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppRoutesApi(api_client)
    app_instance_id = 56 # int | 

    try:
        # List app routes
        api_response = api_instance.list_app_routes(app_instance_id)
        print("The response of AppRoutesApi->list_app_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->list_app_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | 

### Return type

[**List[AppRoute]**](AppRoute.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app routes |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_route**
> AppRoute update_app_route(id, update_app_route_input)

Update app route

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_route import AppRoute
from wodby.models.update_app_route_input import UpdateAppRouteInput
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppRoutesApi(api_client)
    id = 56 # int | 
    update_app_route_input = wodby.UpdateAppRouteInput() # UpdateAppRouteInput | 

    try:
        # Update app route
        api_response = api_instance.update_app_route(id, update_app_route_input)
        print("The response of AppRoutesApi->update_app_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->update_app_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_route_input** | [**UpdateAppRouteInput**](UpdateAppRouteInput.md)|  | 

### Return type

[**AppRoute**](AppRoute.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app route |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

