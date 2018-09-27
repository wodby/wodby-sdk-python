# wodby.StackApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stack**](StackApi.md#get_stack) | **GET** /stacks/{id} | 
[**get_stacks**](StackApi.md#get_stacks) | **GET** /stacks | 
[**update_stack_from_upstream**](StackApi.md#update_stack_from_upstream) | **POST** /stacks/{id}/update | 
[**update_stacks_from_upstream**](StackApi.md#update_stacks_from_upstream) | **POST** /stacks/update | 


# **get_stack**
> Stack get_stack(id)



Retrieve stack

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
api_instance = wodby.StackApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Stack ID

try:
    api_response = api_instance.get_stack(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->get_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Stack ID | 

### Return type

[**Stack**](Stack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stacks**
> list[Stack] get_stacks(org_id=org_id)



Retrieve stacks

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
api_instance = wodby.StackApi(wodby.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)

try:
    api_response = api_instance.get_stacks(org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->get_stacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 

### Return type

[**list[Stack]**](Stack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_from_upstream**
> ResponseTask update_stack_from_upstream(id)



Update official stack from upstream

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
api_instance = wodby.StackApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Stack ID

try:
    api_response = api_instance.update_stack_from_upstream(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->update_stack_from_upstream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Stack ID | 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stacks_from_upstream**
> ResponseTask update_stacks_from_upstream(data)



Update official stacks from upstream

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
api_instance = wodby.StackApi(wodby.ApiClient(configuration))
data = wodby.RequestStacksUpdate() # RequestStacksUpdate | 

try:
    api_response = api_instance.update_stacks_from_upstream(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->update_stacks_from_upstream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RequestStacksUpdate**](RequestStacksUpdate.md)|  | 

### Return type

[**ResponseTask**](ResponseTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

