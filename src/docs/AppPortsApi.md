# wodby.AppPortsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_app_port_setting**](AppPortsApi.md#delete_app_port_setting) | **DELETE** /app-ports/{id}/settings/{name} | Delete app port setting
[**get_app_endpoint**](AppPortsApi.md#get_app_endpoint) | **GET** /app-endpoints/{id} | Get app endpoint
[**get_app_port**](AppPortsApi.md#get_app_port) | **GET** /app-ports/{id} | Get app port
[**list_app_endpoints**](AppPortsApi.md#list_app_endpoints) | **GET** /app-endpoints | List app endpoints
[**list_app_port_settings**](AppPortsApi.md#list_app_port_settings) | **GET** /app-ports/{id}/settings | List app port settings
[**list_app_ports**](AppPortsApi.md#list_app_ports) | **GET** /app-ports | List app ports
[**publish_app_port**](AppPortsApi.md#publish_app_port) | **POST** /app-ports/{id}/actions/publish | Publish app port
[**replace_app_port_settings**](AppPortsApi.md#replace_app_port_settings) | **PUT** /app-ports/{id}/settings | Replace app port settings
[**set_app_port_setting**](AppPortsApi.md#set_app_port_setting) | **PUT** /app-ports/{id}/settings/{name} | Set app port setting
[**unpublish_app_port**](AppPortsApi.md#unpublish_app_port) | **POST** /app-ports/{id}/actions/unpublish | Unpublish app port
[**update_app_port**](AppPortsApi.md#update_app_port) | **PUT** /app-ports/{id} | Update app port


# **delete_app_port_setting**
> OperationResult delete_app_port_setting(id, name)

Delete app port setting

Removes a named app port setting.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port_setting_name import AppPortSettingName
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 
    name = wodby.AppPortSettingName() # AppPortSettingName | 

    try:
        # Delete app port setting
        api_response = api_instance.delete_app_port_setting(id, name)
        print("The response of AppPortsApi->delete_app_port_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->delete_app_port_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | [**AppPortSettingName**](.md)|  | 

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
**200** | Deletion result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_endpoint**
> AppEndpoint get_app_endpoint(id)

Get app endpoint

Returns one app endpoint with its route and port IDs.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_endpoint import AppEndpoint
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 

    try:
        # Get app endpoint
        api_response = api_instance.get_app_endpoint(id)
        print("The response of AppPortsApi->get_app_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->get_app_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppEndpoint**](AppEndpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App endpoint |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_port**
> AppPort get_app_port(id)

Get app port

Returns the app port identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port import AppPort
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 

    try:
        # Get app port
        api_response = api_instance.get_app_port(id)
        print("The response of AppPortsApi->get_app_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->get_app_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppPort**](AppPort.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App port |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_endpoints**
> List[AppEndpoint] list_app_endpoints(app_environment_id)

List app endpoints

Returns the endpoints of an app environment. An endpoint groups the routes and ports of one app service endpoint.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_endpoint import AppEndpoint
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
    api_instance = wodby.AppPortsApi(api_client)
    app_environment_id = 56 # int | 

    try:
        # List app endpoints
        api_response = api_instance.list_app_endpoints(app_environment_id)
        print("The response of AppPortsApi->list_app_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->list_app_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_environment_id** | **int**|  | 

### Return type

[**List[AppEndpoint]**](AppEndpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App endpoints |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_port_settings**
> List[AppPortSetting] list_app_port_settings(id)

List app port settings

Returns the settings of an app port.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port_setting import AppPortSetting
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 

    try:
        # List app port settings
        api_response = api_instance.list_app_port_settings(id)
        print("The response of AppPortsApi->list_app_port_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->list_app_port_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppPortSetting]**](AppPortSetting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App port settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_ports**
> List[AppPort] list_app_ports(app_instance_id)

List app ports

Returns app ports matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port import AppPort
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
    api_instance = wodby.AppPortsApi(api_client)
    app_instance_id = 56 # int | 

    try:
        # List app ports
        api_response = api_instance.list_app_ports(app_instance_id)
        print("The response of AppPortsApi->list_app_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->list_app_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | 

### Return type

[**List[AppPort]**](AppPort.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app ports |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_app_port**
> AppPort publish_app_port(id, update_app_port_input=update_app_port_input)

Publish app port

Exposes the app port on the cluster's public address. Leave publicPort out to pick a free port. Returns the port.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port import AppPort
from wodby.models.update_app_port_input import UpdateAppPortInput
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 
    update_app_port_input = wodby.UpdateAppPortInput() # UpdateAppPortInput |  (optional)

    try:
        # Publish app port
        api_response = api_instance.publish_app_port(id, update_app_port_input=update_app_port_input)
        print("The response of AppPortsApi->publish_app_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->publish_app_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_port_input** | [**UpdateAppPortInput**](UpdateAppPortInput.md)|  | [optional] 

### Return type

[**AppPort**](AppPort.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Published app port |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_app_port_settings**
> List[AppPortSetting] replace_app_port_settings(id, app_port_settings_input)

Replace app port settings

Replaces all settings of an app port. A setting left out is removed. Returns the stored settings.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port_setting import AppPortSetting
from wodby.models.app_port_settings_input import AppPortSettingsInput
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 
    app_port_settings_input = wodby.AppPortSettingsInput() # AppPortSettingsInput | 

    try:
        # Replace app port settings
        api_response = api_instance.replace_app_port_settings(id, app_port_settings_input)
        print("The response of AppPortsApi->replace_app_port_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->replace_app_port_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_port_settings_input** | [**AppPortSettingsInput**](AppPortSettingsInput.md)|  | 

### Return type

[**List[AppPortSetting]**](AppPortSetting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored app port settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_app_port_setting**
> AppPortSetting set_app_port_setting(id, name, set_string_value_input)

Set app port setting

Creates or updates a named app port setting.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port_setting import AppPortSetting
from wodby.models.app_port_setting_name import AppPortSettingName
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 
    name = wodby.AppPortSettingName() # AppPortSettingName | 
    set_string_value_input = wodby.SetStringValueInput() # SetStringValueInput | 

    try:
        # Set app port setting
        api_response = api_instance.set_app_port_setting(id, name, set_string_value_input)
        print("The response of AppPortsApi->set_app_port_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->set_app_port_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | [**AppPortSettingName**](.md)|  | 
 **set_string_value_input** | [**SetStringValueInput**](SetStringValueInput.md)|  | 

### Return type

[**AppPortSetting**](AppPortSetting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App port setting |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_app_port**
> AppPort unpublish_app_port(id)

Unpublish app port

Stops exposing the app port on the cluster's public address and returns the port.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port import AppPort
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 

    try:
        # Unpublish app port
        api_response = api_instance.unpublish_app_port(id)
        print("The response of AppPortsApi->unpublish_app_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->unpublish_app_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppPort**](AppPort.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unpublished app port |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_port**
> AppPort update_app_port(id, update_app_port_input)

Update app port

Changes the public port of an app port and returns it.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_port import AppPort
from wodby.models.update_app_port_input import UpdateAppPortInput
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
    api_instance = wodby.AppPortsApi(api_client)
    id = 56 # int | 
    update_app_port_input = wodby.UpdateAppPortInput() # UpdateAppPortInput | 

    try:
        # Update app port
        api_response = api_instance.update_app_port(id, update_app_port_input)
        print("The response of AppPortsApi->update_app_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPortsApi->update_app_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_port_input** | [**UpdateAppPortInput**](UpdateAppPortInput.md)|  | 

### Return type

[**AppPort**](AppPort.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app port |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

