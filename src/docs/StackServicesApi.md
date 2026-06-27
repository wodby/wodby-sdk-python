# wodby.StackServicesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stack_service**](StackServicesApi.md#create_stack_service) | **POST** /stack-services | Create stack service
[**delete_stack_service**](StackServicesApi.md#delete_stack_service) | **DELETE** /stack-services/{id} | Delete stack service
[**list_stack_services**](StackServicesApi.md#list_stack_services) | **GET** /stack-services | List stack services
[**update_stack_service**](StackServicesApi.md#update_stack_service) | **PUT** /stack-services/{id} | Update stack service


# **create_stack_service**
> StackService create_stack_service(new_stack_service_input)

Create stack service

Creates a stack service and returns the created resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_stack_service_input import NewStackServiceInput
from wodby.models.stack_service import StackService
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
    api_instance = wodby.StackServicesApi(api_client)
    new_stack_service_input = wodby.NewStackServiceInput() # NewStackServiceInput | 

    try:
        # Create stack service
        api_response = api_instance.create_stack_service(new_stack_service_input)
        print("The response of StackServicesApi->create_stack_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_stack_service_input** | [**NewStackServiceInput**](NewStackServiceInput.md)|  | 

### Return type

[**StackService**](StackService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service**
> OperationResult delete_stack_service(id)

Delete stack service

Deletes the stack service and returns the operation result.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service
        api_response = api_instance.delete_stack_service(id)
        print("The response of StackServicesApi->delete_stack_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_services**
> List[StackService] list_stack_services(stack_rev_id)

List stack services

Returns stack services matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service import StackService
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
    api_instance = wodby.StackServicesApi(api_client)
    stack_rev_id = 56 # int | 

    try:
        # List stack services
        api_response = api_instance.list_stack_services(stack_rev_id)
        print("The response of StackServicesApi->list_stack_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_rev_id** | **int**|  | 

### Return type

[**List[StackService]**](StackService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack services |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_service**
> StackService update_stack_service(id, stack_service_input)

Update stack service

Updates the stack service and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service import StackService
from wodby.models.stack_service_input import StackServiceInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    stack_service_input = wodby.StackServiceInput() # StackServiceInput | 

    try:
        # Update stack service
        api_response = api_instance.update_stack_service(id, stack_service_input)
        print("The response of StackServicesApi->update_stack_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->update_stack_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **stack_service_input** | [**StackServiceInput**](StackServiceInput.md)|  | 

### Return type

[**StackService**](StackService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated stack service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

