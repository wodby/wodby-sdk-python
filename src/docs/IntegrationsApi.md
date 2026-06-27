# wodby.IntegrationsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration**](IntegrationsApi.md#create_integration) | **POST** /integrations | Create integration
[**delete_integration**](IntegrationsApi.md#delete_integration) | **DELETE** /integrations/{id} | Delete integration
[**get_integration**](IntegrationsApi.md#get_integration) | **GET** /integrations/{id} | Get integration
[**get_integration_by_name**](IntegrationsApi.md#get_integration_by_name) | **GET** /integrations/by-name/{name} | Get integration by name
[**get_integration_kube_settings**](IntegrationsApi.md#get_integration_kube_settings) | **GET** /integrations/{id}/options/kube-settings | Get Kubernetes settings
[**list_integration_kube_machine_types**](IntegrationsApi.md#list_integration_kube_machine_types) | **GET** /integrations/{id}/options/kube-machine-types | List Kubernetes machine types
[**list_integration_kube_regions**](IntegrationsApi.md#list_integration_kube_regions) | **GET** /integrations/{id}/options/kube-regions | List Kubernetes regions
[**list_integration_kube_versions**](IntegrationsApi.md#list_integration_kube_versions) | **GET** /integrations/{id}/options/kube-versions | List Kubernetes versions
[**list_integration_kube_zones**](IntegrationsApi.md#list_integration_kube_zones) | **GET** /integrations/{id}/options/kube-zones | List Kubernetes zones
[**list_integration_remote_git_repo_branches**](IntegrationsApi.md#list_integration_remote_git_repo_branches) | **GET** /integrations/{id}/options/remote-git-repo-branches | List remote Git repository branches
[**list_integration_remote_git_repo_tags**](IntegrationsApi.md#list_integration_remote_git_repo_tags) | **GET** /integrations/{id}/options/remote-git-repo-tags | List remote Git repository tags
[**list_integration_remote_git_repos**](IntegrationsApi.md#list_integration_remote_git_repos) | **GET** /integrations/{id}/options/remote-git-repos | List remote Git repositories
[**list_integration_scopes**](IntegrationsApi.md#list_integration_scopes) | **GET** /integrations/{id}/options/scopes | List integration scopes
[**list_integration_storage_buckets**](IntegrationsApi.md#list_integration_storage_buckets) | **GET** /integrations/{id}/options/storage-buckets | List storage buckets
[**list_integration_storage_classes**](IntegrationsApi.md#list_integration_storage_classes) | **GET** /integrations/{id}/options/storage-classes | List storage classes
[**list_integrations**](IntegrationsApi.md#list_integrations) | **GET** /integrations | List integrations
[**update_integration**](IntegrationsApi.md#update_integration) | **PUT** /integrations/{id} | Update integration


# **create_integration**
> Integration create_integration(new_integration_input)

Create integration

Creates an integration and returns the created resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.integration import Integration
from wodby.models.new_integration_input import NewIntegrationInput
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
    api_instance = wodby.IntegrationsApi(api_client)
    new_integration_input = wodby.NewIntegrationInput() # NewIntegrationInput | 

    try:
        # Create integration
        api_response = api_instance.create_integration(new_integration_input)
        print("The response of IntegrationsApi->create_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_integration_input** | [**NewIntegrationInput**](NewIntegrationInput.md)|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created integration |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration**
> OperationResult delete_integration(id)

Delete integration

Deletes the integration and returns the operation result.

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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # Delete integration
        api_response = api_instance.delete_integration(id)
        print("The response of IntegrationsApi->delete_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->delete_integration: %s\n" % e)
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

# **get_integration**
> Integration get_integration(id)

Get integration

Returns the integration identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.integration import Integration
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # Get integration
        api_response = api_instance.get_integration(id)
        print("The response of IntegrationsApi->get_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_by_name**
> Integration get_integration_by_name(name, org_id=org_id)

Get integration by name

Returns the integration identified by name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.integration import Integration
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
    api_instance = wodby.IntegrationsApi(api_client)
    name = 'name_example' # str | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Get integration by name
        api_response = api_instance.get_integration_by_name(name, org_id=org_id)
        print("The response of IntegrationsApi->get_integration_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_integration_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_kube_settings**
> Dict[str, object] get_integration_kube_settings(id)

Get Kubernetes settings

Returns the Kubernetes settings identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # Get Kubernetes settings
        api_response = api_instance.get_integration_kube_settings(id)
        print("The response of IntegrationsApi->get_integration_kube_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_integration_kube_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**Dict[str, object]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kube_machine_types**
> List[Dict[str, object]] list_integration_kube_machine_types(id, location)

List Kubernetes machine types

Returns Kubernetes machine types matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 
    location = 'location_example' # str | 

    try:
        # List Kubernetes machine types
        api_response = api_instance.list_integration_kube_machine_types(id, location)
        print("The response of IntegrationsApi->list_integration_kube_machine_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_kube_machine_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **location** | **str**|  | 

### Return type

**List[Dict[str, object]]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes machine types |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kube_regions**
> List[Dict[str, object]] list_integration_kube_regions(id)

List Kubernetes regions

Returns Kubernetes regions matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # List Kubernetes regions
        api_response = api_instance.list_integration_kube_regions(id)
        print("The response of IntegrationsApi->list_integration_kube_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_kube_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[Dict[str, object]]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes regions |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kube_versions**
> List[KubeVersion] list_integration_kube_versions(id, location)

List Kubernetes versions

Returns Kubernetes versions matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.kube_version import KubeVersion
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 
    location = 'location_example' # str | 

    try:
        # List Kubernetes versions
        api_response = api_instance.list_integration_kube_versions(id, location)
        print("The response of IntegrationsApi->list_integration_kube_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_kube_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **location** | **str**|  | 

### Return type

[**List[KubeVersion]**](KubeVersion.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes versions |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_kube_zones**
> List[Dict[str, object]] list_integration_kube_zones(id)

List Kubernetes zones

Returns Kubernetes zones matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # List Kubernetes zones
        api_response = api_instance.list_integration_kube_zones(id)
        print("The response of IntegrationsApi->list_integration_kube_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_kube_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[Dict[str, object]]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes zones |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_remote_git_repo_branches**
> List[str] list_integration_remote_git_repo_branches(id, remote_git_repo_id)

List remote Git repository branches

Returns remote Git repository branches matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 
    remote_git_repo_id = 'remote_git_repo_id_example' # str | 

    try:
        # List remote Git repository branches
        api_response = api_instance.list_integration_remote_git_repo_branches(id, remote_git_repo_id)
        print("The response of IntegrationsApi->list_integration_remote_git_repo_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_remote_git_repo_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **remote_git_repo_id** | **str**|  | 

### Return type

**List[str]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Branch names |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_remote_git_repo_tags**
> List[str] list_integration_remote_git_repo_tags(id, remote_git_repo_id)

List remote Git repository tags

Returns remote Git repository tags matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 
    remote_git_repo_id = 'remote_git_repo_id_example' # str | 

    try:
        # List remote Git repository tags
        api_response = api_instance.list_integration_remote_git_repo_tags(id, remote_git_repo_id)
        print("The response of IntegrationsApi->list_integration_remote_git_repo_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_remote_git_repo_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **remote_git_repo_id** | **str**|  | 

### Return type

**List[str]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag names |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_remote_git_repos**
> List[RemoteGitRepo] list_integration_remote_git_repos(id)

List remote Git repositories

Returns remote Git repositories matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.remote_git_repo import RemoteGitRepo
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # List remote Git repositories
        api_response = api_instance.list_integration_remote_git_repos(id)
        print("The response of IntegrationsApi->list_integration_remote_git_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_remote_git_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[RemoteGitRepo]**](RemoteGitRepo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remote Git repositories |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_scopes**
> List[IntegrationScope] list_integration_scopes(id)

List integration scopes

Returns integration scopes matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.integration_scope import IntegrationScope
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # List integration scopes
        api_response = api_instance.list_integration_scopes(id)
        print("The response of IntegrationsApi->list_integration_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[IntegrationScope]**](IntegrationScope.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration scopes |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_storage_buckets**
> List[str] list_integration_storage_buckets(id)

List storage buckets

Returns storage buckets matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # List storage buckets
        api_response = api_instance.list_integration_storage_buckets(id)
        print("The response of IntegrationsApi->list_integration_storage_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_storage_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[str]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bucket names |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_storage_classes**
> List[str] list_integration_storage_classes(id)

List storage classes

Returns storage classes matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 

    try:
        # List storage classes
        api_response = api_instance.list_integration_storage_classes(id)
        print("The response of IntegrationsApi->list_integration_storage_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integration_storage_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[str]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage class names |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integrations**
> List[Integration] list_integrations(org_id=org_id, project_ids=project_ids, labels=labels)

List integrations

Returns integrations matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.integration import Integration
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
    api_instance = wodby.IntegrationsApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    labels = 'labels_example' # str | Comma-separated labels (optional)

    try:
        # List integrations
        api_response = api_instance.list_integrations(org_id=org_id, project_ids=project_ids, labels=labels)
        print("The response of IntegrationsApi->list_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **labels** | **str**| Comma-separated labels | [optional] 

### Return type

[**List[Integration]**](Integration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of integrations |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration**
> Integration update_integration(id, update_integration_input)

Update integration

Updates the integration and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.integration import Integration
from wodby.models.update_integration_input import UpdateIntegrationInput
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
    api_instance = wodby.IntegrationsApi(api_client)
    id = 56 # int | 
    update_integration_input = wodby.UpdateIntegrationInput() # UpdateIntegrationInput | 

    try:
        # Update integration
        api_response = api_instance.update_integration(id, update_integration_input)
        print("The response of IntegrationsApi->update_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->update_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_integration_input** | [**UpdateIntegrationInput**](UpdateIntegrationInput.md)|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated integration |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

