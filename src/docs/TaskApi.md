# wodby.TaskApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TaskApi.md#get_task) | **GET** /tasks/{id} | 
[**get_tasks**](TaskApi.md#get_tasks) | **GET** /tasks | 


# **get_task**
> Task get_task(id)



Retrieve task

### Example
```python
from __future__ import print_function
import time
import wodby
from wodby.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby.TaskApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Task ID

try:
    api_response = api_instance.get_task(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Task ID | 

### Return type

[**Task**](Task.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> list[Task] get_tasks(org_id=org_id, user_id=user_id, status=status)



Retrieve tasks

### Example
```python
from __future__ import print_function
import time
import wodby
from wodby.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = wodby.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = wodby.TaskApi(wodby.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
user_id = 'user_id_example' # str | User ID (optional)
status = 'status_example' # str | Task status (optional)

try:
    api_response = api_instance.get_tasks(org_id=org_id, user_id=user_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 
 **user_id** | [**str**](.md)| User ID | [optional] 
 **status** | **str**| Task status | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

