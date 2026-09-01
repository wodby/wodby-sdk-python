# wodby.TasksApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_task**](TasksApi.md#cancel_task) | **POST** /tasks/{id}/cancel | Cancel task
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{id} | Get task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /tasks | List tasks
[**repeat_task**](TasksApi.md#repeat_task) | **POST** /tasks/{id}/repeat | Repeat task


# **cancel_task**
> OperationResult cancel_task(id)

Cancel task

Requests cancellation for the task.

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
    api_instance = wodby.TasksApi(api_client)
    id = 56 # int | 

    try:
        # Cancel task
        api_response = api_instance.cancel_task(id)
        print("The response of TasksApi->cancel_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->cancel_task: %s\n" % e)
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
**200** | Cancel result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(id)

Get task

Returns the task identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.task import Task
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
    api_instance = wodby.TasksApi(api_client)
    id = 56 # int | 

    try:
        # Get task
        api_response = api_instance.get_task(id)
        print("The response of TasksApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> TasksResponse list_tasks(scope=scope, org_id=org_id, project_ids=project_ids, view=view, without_origin=without_origin, include_system=include_system, statuses=statuses, names=names, search=search, app_id=app_id, app_instance_id=app_instance_id, stack_id=stack_id, database_id=database_id, cluster_id=cluster_id, service_id=service_id, integration_id=integration_id, provider_id=provider_id, page=page, page_size=page_size)

List tasks

Returns tasks matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.tasks_response import TasksResponse
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
    api_instance = wodby.TasksApi(api_client)
    scope = 'scope_example' # str |  (optional)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    view = 'view_example' # str | Return matching tasks as a flat page or as filter-scoped task trees. Tree responses support user, organization, project, and resource filters, keep paginated roots in items, and include current-page tree nodes in treeItems. Root pages are capped at 100 tasks. Tree responses include up to 250 authorized tasks and set treeTruncated when additional visible descendants exist; exceeding the 10-level depth limit still returns 422. (optional)
    without_origin = True # bool | Deprecated compatibility alias for view=tree (optional)
    include_system = False # bool | Include operator-only system tasks when authorized (optional) (default to False)
    statuses = 'statuses_example' # str | Comma-separated task statuses (optional)
    names = 'names_example' # str | Comma-separated exact task names (optional)
    search = 'search_example' # str |  (optional)
    app_id = 56 # int |  (optional)
    app_instance_id = 56 # int |  (optional)
    stack_id = 56 # int |  (optional)
    database_id = 56 # int |  (optional)
    cluster_id = 56 # int |  (optional)
    service_id = 56 # int |  (optional)
    integration_id = 56 # int |  (optional)
    provider_id = 56 # int |  (optional)
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List tasks
        api_response = api_instance.list_tasks(scope=scope, org_id=org_id, project_ids=project_ids, view=view, without_origin=without_origin, include_system=include_system, statuses=statuses, names=names, search=search, app_id=app_id, app_instance_id=app_instance_id, stack_id=stack_id, database_id=database_id, cluster_id=cluster_id, service_id=service_id, integration_id=integration_id, provider_id=provider_id, page=page, page_size=page_size)
        print("The response of TasksApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | [optional] 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **view** | **str**| Return matching tasks as a flat page or as filter-scoped task trees. Tree responses support user, organization, project, and resource filters, keep paginated roots in items, and include current-page tree nodes in treeItems. Root pages are capped at 100 tasks. Tree responses include up to 250 authorized tasks and set treeTruncated when additional visible descendants exist; exceeding the 10-level depth limit still returns 422. | [optional] 
 **without_origin** | **bool**| Deprecated compatibility alias for view&#x3D;tree | [optional] 
 **include_system** | **bool**| Include operator-only system tasks when authorized | [optional] [default to False]
 **statuses** | **str**| Comma-separated task statuses | [optional] 
 **names** | **str**| Comma-separated exact task names | [optional] 
 **search** | **str**|  | [optional] 
 **app_id** | **int**|  | [optional] 
 **app_instance_id** | **int**|  | [optional] 
 **stack_id** | **int**|  | [optional] 
 **database_id** | **int**|  | [optional] 
 **cluster_id** | **int**|  | [optional] 
 **service_id** | **int**|  | [optional] 
 **integration_id** | **int**|  | [optional] 
 **provider_id** | **int**|  | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 30 | [optional] 

### Return type

[**TasksResponse**](TasksResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks response |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repeat_task**
> OperationResult repeat_task(id, repeat_task_request)

Repeat task

Creates a repeated run for the task.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.repeat_task_request import RepeatTaskRequest
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
    api_instance = wodby.TasksApi(api_client)
    id = 56 # int | 
    repeat_task_request = wodby.RepeatTaskRequest() # RepeatTaskRequest | 

    try:
        # Repeat task
        api_response = api_instance.repeat_task(id, repeat_task_request)
        print("The response of TasksApi->repeat_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->repeat_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **repeat_task_request** | [**RepeatTaskRequest**](RepeatTaskRequest.md)|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repeat task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

