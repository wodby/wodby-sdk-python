# wodby.TaskStepsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_step_log_url**](TaskStepsApi.md#get_task_step_log_url) | **GET** /task-steps/{id}/log-url | Get task step log URL
[**get_task_step_logs**](TaskStepsApi.md#get_task_step_logs) | **GET** /task-steps/{id}/logs | Get task step logs


# **get_task_step_log_url**
> URLResponse get_task_step_log_url(id)

Get task step log URL

Returns a temporary log URL for the task step.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.url_response import URLResponse
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
    api_instance = wodby.TaskStepsApi(api_client)
    id = 56 # int | 

    try:
        # Get task step log URL
        api_response = api_instance.get_task_step_log_url(id)
        print("The response of TaskStepsApi->get_task_step_log_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskStepsApi->get_task_step_log_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**URLResponse**](URLResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task step log URL |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_step_logs**
> TaskStepLogs get_task_step_logs(id)

Get task step logs

Returns logs captured for the task step.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.task_step_logs import TaskStepLogs
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
    api_instance = wodby.TaskStepsApi(api_client)
    id = 56 # int | 

    try:
        # Get task step logs
        api_response = api_instance.get_task_step_logs(id)
        print("The response of TaskStepsApi->get_task_step_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskStepsApi->get_task_step_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TaskStepLogs**](TaskStepLogs.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task step logs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

