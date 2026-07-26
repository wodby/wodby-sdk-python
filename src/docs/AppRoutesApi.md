# wodby.AppRoutesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_route**](AppRoutesApi.md#create_app_route) | **POST** /app-routes | Create app route
[**delete_app_route**](AppRoutesApi.md#delete_app_route) | **DELETE** /app-routes/{id} | Delete app route
[**delete_app_route_setting**](AppRoutesApi.md#delete_app_route_setting) | **DELETE** /app-routes/{id}/settings/{name} | Delete app route setting
[**get_app_route**](AppRoutesApi.md#get_app_route) | **GET** /app-routes/{id} | Get app route
[**list_app_route_settings**](AppRoutesApi.md#list_app_route_settings) | **GET** /app-routes/{id}/settings | List app route settings
[**list_app_routes**](AppRoutesApi.md#list_app_routes) | **GET** /app-routes | List app routes
[**set_app_route_setting**](AppRoutesApi.md#set_app_route_setting) | **PUT** /app-routes/{id}/settings/{name} | Set app route setting
[**update_app_route**](AppRoutesApi.md#update_app_route) | **PUT** /app-routes/{id} | Update app route


# **create_app_route**
> AppRoute create_app_route(new_app_route_input)

Create app route

Creates an app route and returns the created resource.

### Example

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

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

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

Deletes the app route and returns the operation result.

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

# **delete_app_route_setting**
> OperationResult delete_app_route_setting(id, name)

Delete app route setting

Deletes a named app route setting and restores any applicable default.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_route_setting_name import AppRouteSettingName
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
    api_instance = wodby.AppRoutesApi(api_client)
    id = 56 # int | 
    name = wodby.AppRouteSettingName() # AppRouteSettingName | 

    try:
        # Delete app route setting
        api_response = api_instance.delete_app_route_setting(id, name)
        print("The response of AppRoutesApi->delete_app_route_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->delete_app_route_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | [**AppRouteSettingName**](.md)|  | 

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

# **get_app_route**
> AppRoute get_app_route(id)

Get app route

Returns the app route identified by the request path.

### Example

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

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App route |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_route_settings**
> List[AppRouteSetting] list_app_route_settings(id)

List app route settings

Returns route-specific setting overrides. Inherited app-instance defaults are not included.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_route_setting import AppRouteSetting
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
    api_instance = wodby.AppRoutesApi(api_client)
    id = 56 # int | 

    try:
        # List app route settings
        api_response = api_instance.list_app_route_settings(id)
        print("The response of AppRoutesApi->list_app_route_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->list_app_route_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppRouteSetting]**](AppRouteSetting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app route settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_routes**
> List[AppRoute] list_app_routes(app_instance_id)

List app routes

Returns app routes matching the request filters.

### Example

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

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app routes |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_app_route_setting**
> AppRouteSetting set_app_route_setting(id, name, set_string_value_input)

Set app route setting

Creates or updates a named app route setting.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_route_setting import AppRouteSetting
from wodby.models.app_route_setting_name import AppRouteSettingName
from wodby.models.set_string_value_input import SetStringValueInput
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
    api_instance = wodby.AppRoutesApi(api_client)
    id = 56 # int | 
    name = wodby.AppRouteSettingName() # AppRouteSettingName | 
    set_string_value_input = wodby.SetStringValueInput() # SetStringValueInput | 

    try:
        # Set app route setting
        api_response = api_instance.set_app_route_setting(id, name, set_string_value_input)
        print("The response of AppRoutesApi->set_app_route_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRoutesApi->set_app_route_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | [**AppRouteSettingName**](.md)|  | 
 **set_string_value_input** | [**SetStringValueInput**](SetStringValueInput.md)|  | 

### Return type

[**AppRouteSetting**](AppRouteSetting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app route setting |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_route**
> AppRoute update_app_route(id, update_app_route_input)

Update app route

Updates the app route and returns the updated resource.

### Example

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

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app route |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

