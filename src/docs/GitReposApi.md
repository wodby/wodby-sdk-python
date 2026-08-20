# wodby.GitReposApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_git_repo_usages**](GitReposApi.md#get_git_repo_usages) | **GET** /git-repos/{id}/usages | Get Git repository usages
[**update_git_repo_from_git**](GitReposApi.md#update_git_repo_from_git) | **POST** /git-repos/{id}/actions/update-from-git | Update all Git repository usages


# **get_git_repo_usages**
> GitRepoUsages get_git_repo_usages(id)

Get Git repository usages

Returns every service, stack, and provider that shares the Git repository.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.git_repo_usages import GitRepoUsages
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
    api_instance = wodby.GitReposApi(api_client)
    id = 56 # int | 

    try:
        # Get Git repository usages
        api_response = api_instance.get_git_repo_usages(id)
        print("The response of GitReposApi->get_git_repo_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitReposApi->get_git_repo_usages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GitRepoUsages**](GitRepoUsages.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Git repository usages |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_repo_from_git**
> OperationResult update_git_repo_from_git(id, update_stack_from_git_request)

Update all Git repository usages

Starts one parent task that updates every service, stack, and provider sharing the selected repository to the requested ref.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.update_stack_from_git_request import UpdateStackFromGitRequest
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
    api_instance = wodby.GitReposApi(api_client)
    id = 56 # int | 
    update_stack_from_git_request = wodby.UpdateStackFromGitRequest() # UpdateStackFromGitRequest | 

    try:
        # Update all Git repository usages
        api_response = api_instance.update_git_repo_from_git(id, update_stack_from_git_request)
        print("The response of GitReposApi->update_git_repo_from_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitReposApi->update_git_repo_from_git: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_stack_from_git_request** | [**UpdateStackFromGitRequest**](UpdateStackFromGitRequest.md)|  | 

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
**201** | Repository update task accepted |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

