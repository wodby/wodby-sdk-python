# wodby.AppPortsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_port**](AppPortsApi.md#get_app_port) | **GET** /app-ports/{id} | Get app port
[**list_app_ports**](AppPortsApi.md#list_app_ports) | **GET** /app-ports | List app ports


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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App port |  -  |
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app ports |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

