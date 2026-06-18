# wodby.AppInstancesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_instance**](AppInstancesApi.md#create_app_instance) | **POST** /app-instances | Create app instance
[**delete_app_instance**](AppInstancesApi.md#delete_app_instance) | **DELETE** /app-instances/{id} | Delete app instance
[**get_app_instance**](AppInstancesApi.md#get_app_instance) | **GET** /app-instances/{id} | Get app instance
[**get_app_instance_by_name**](AppInstancesApi.md#get_app_instance_by_name) | **GET** /app-instances/by-name/{appName}/{instanceName} | Get app instance by app and instance name
[**list_app_instances**](AppInstancesApi.md#list_app_instances) | **GET** /app-instances | List app instances
[**update_app_instance**](AppInstancesApi.md#update_app_instance) | **PUT** /app-instances/{id} | Update app instance


# **create_app_instance**
> AppInstance create_app_instance(new_app_instance_input)

Create app instance

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
from wodby.models.new_app_instance_input import NewAppInstanceInput
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
    api_instance = wodby.AppInstancesApi(api_client)
    new_app_instance_input = wodby.NewAppInstanceInput() # NewAppInstanceInput | 

    try:
        # Create app instance
        api_response = api_instance.create_app_instance(new_app_instance_input)
        print("The response of AppInstancesApi->create_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->create_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_app_instance_input** | [**NewAppInstanceInput**](NewAppInstanceInput.md)|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_instance**
> OperationResult delete_app_instance(id, force=force)

Delete app instance

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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    force = False # bool |  (optional) (default to False)

    try:
        # Delete app instance
        api_response = api_instance.delete_app_instance(id, force=force)
        print("The response of AppInstancesApi->delete_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->delete_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **force** | **bool**|  | [optional] [default to False]

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

# **get_app_instance**
> AppInstance get_app_instance(id)

Get app instance

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 

    try:
        # Get app instance
        api_response = api_instance.get_app_instance(id)
        print("The response of AppInstancesApi->get_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->get_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_instance_by_name**
> AppInstance get_app_instance_by_name(app_name, instance_name, org_id)

Get app instance by app and instance name

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
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
    api_instance = wodby.AppInstancesApi(api_client)
    app_name = 'app_name_example' # str | 
    instance_name = 'instance_name_example' # str | 
    org_id = 56 # int | 

    try:
        # Get app instance by app and instance name
        api_response = api_instance.get_app_instance_by_name(app_name, instance_name, org_id)
        print("The response of AppInstancesApi->get_app_instance_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->get_app_instance_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | 
 **instance_name** | **str**|  | 
 **org_id** | **int**|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_instances**
> List[AppInstance] list_app_instances(org_id, project_ids=project_ids, app_id=app_id, cluster_id=cluster_id, cluster_app=cluster_app)

List app instances

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
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
    api_instance = wodby.AppInstancesApi(api_client)
    org_id = 56 # int | 
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    app_id = 56 # int |  (optional)
    cluster_id = 56 # int |  (optional)
    cluster_app = True # bool |  (optional)

    try:
        # List app instances
        api_response = api_instance.list_app_instances(org_id, project_ids=project_ids, app_id=app_id, cluster_id=cluster_id, cluster_app=cluster_app)
        print("The response of AppInstancesApi->list_app_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->list_app_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **app_id** | **int**|  | [optional] 
 **cluster_id** | **int**|  | [optional] 
 **cluster_app** | **bool**|  | [optional] 

### Return type

[**List[AppInstance]**](AppInstance.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app instances |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_instance**
> AppInstance update_app_instance(id, update_title_request)

Update app instance

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_instance import AppInstance
from wodby.models.update_title_request import UpdateTitleRequest
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
    api_instance = wodby.AppInstancesApi(api_client)
    id = 56 # int | 
    update_title_request = wodby.UpdateTitleRequest() # UpdateTitleRequest | 

    try:
        # Update app instance
        api_response = api_instance.update_app_instance(id, update_title_request)
        print("The response of AppInstancesApi->update_app_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppInstancesApi->update_app_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_title_request** | [**UpdateTitleRequest**](UpdateTitleRequest.md)|  | 

### Return type

[**AppInstance**](AppInstance.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app instance |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

