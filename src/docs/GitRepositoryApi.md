# wodby.GitRepositoryApi

All URIs are relative to *https://api.wodby.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_git_repo**](GitRepositoryApi.md#get_git_repo) | **GET** /git-repo/{id} | 
[**get_git_repos**](GitRepositoryApi.md#get_git_repos) | **GET** /git-repo | 


# **get_git_repo**
> GitRepo get_git_repo(id)



Retrieve git repository

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
api_instance = wodby.GitRepositoryApi(wodby.ApiClient(configuration))
id = 'id_example' # str | Git repository ID

try:
    api_response = api_instance.get_git_repo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitRepositoryApi->get_git_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Git repository ID | 

### Return type

[**GitRepo**](GitRepo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_repos**
> list[GitRepo] get_git_repos(org_id=org_id, name=name)



Retrieve git repositories

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
api_instance = wodby.GitRepositoryApi(wodby.ApiClient(configuration))
org_id = 'org_id_example' # str | Organization ID (optional)
name = 'name_example' # str | Git repository name (optional)

try:
    api_response = api_instance.get_git_repos(org_id=org_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitRepositoryApi->get_git_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | [**str**](.md)| Organization ID | [optional] 
 **name** | **str**| Git repository name | [optional] 

### Return type

[**list[GitRepo]**](GitRepo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

