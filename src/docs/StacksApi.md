# wodby.StacksApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stack_from_manifest**](StacksApi.md#create_stack_from_manifest) | **POST** /stacks/actions/create-from-manifest | Create stack from manifest
[**duplicate_stack**](StacksApi.md#duplicate_stack) | **POST** /stacks/{id}/actions/duplicate | Duplicate stack
[**get_stack**](StacksApi.md#get_stack) | **GET** /stacks/{id} | Get stack
[**get_stack_by_name**](StacksApi.md#get_stack_by_name) | **GET** /stacks/by-name/{name} | Get stack by name
[**get_stack_origin_sync_changelog**](StacksApi.md#get_stack_origin_sync_changelog) | **GET** /stack-origin-sync-changelogs/{id} | Preview stack origin synchronization
[**get_stack_revision**](StacksApi.md#get_stack_revision) | **GET** /stack-revisions/{id} | Get stack revision
[**get_stack_service_update_changelog**](StacksApi.md#get_stack_service_update_changelog) | **GET** /stack-service-update-changelogs/{id} | Preview stack service revision updates
[**import_stacks**](StacksApi.md#import_stacks) | **POST** /stacks/actions/import | Import stacks from Git
[**list_public_stacks**](StacksApi.md#list_public_stacks) | **GET** /catalog/stacks | List public catalog stacks
[**list_stack_revision_services**](StacksApi.md#list_stack_revision_services) | **GET** /stack-revisions/{id}/services | List stack services
[**list_stacks**](StacksApi.md#list_stacks) | **GET** /stacks | List stacks
[**publish_stack_draft**](StacksApi.md#publish_stack_draft) | **POST** /stacks/{id}/actions/publish-draft | Publish stack draft
[**scaffold_stack_from_helm_chart**](StacksApi.md#scaffold_stack_from_helm_chart) | **POST** /stacks/actions/scaffold-from-helm-chart | Scaffold stack from Helm chart
[**sync_stack_with_origin**](StacksApi.md#sync_stack_with_origin) | **POST** /stacks/{id}/actions/sync-origin | Sync stack with origin
[**update_stack_from_git**](StacksApi.md#update_stack_from_git) | **POST** /stacks/{id}/actions/update-from-git | Update stack from git
[**update_stack_service_revisions**](StacksApi.md#update_stack_service_revisions) | **POST** /stacks/{id}/actions/update-service-revisions | Update stack service revisions
[**update_stack_settings**](StacksApi.md#update_stack_settings) | **PUT** /stacks/settings/{id} | Update stack settings
[**validate_stack_manifest**](StacksApi.md#validate_stack_manifest) | **POST** /stacks/actions/validate-manifest | Validate stack manifest


# **create_stack_from_manifest**
> Stack create_stack_from_manifest(manifest_from_yaml_input)

Create stack from manifest

Creates a non-Git Wodby stack from a stack manifest.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.manifest_from_yaml_input import ManifestFromYAMLInput
from wodby.models.stack import Stack
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
    api_instance = wodby.StacksApi(api_client)
    manifest_from_yaml_input = wodby.ManifestFromYAMLInput() # ManifestFromYAMLInput | 

    try:
        # Create stack from manifest
        api_response = api_instance.create_stack_from_manifest(manifest_from_yaml_input)
        print("The response of StacksApi->create_stack_from_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->create_stack_from_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_from_yaml_input** | [**ManifestFromYAMLInput**](ManifestFromYAMLInput.md)|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_stack**
> Stack duplicate_stack(id, duplicate_stack_request)

Duplicate stack

Duplicates the stack into the target organization or project.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.duplicate_stack_request import DuplicateStackRequest
from wodby.models.stack import Stack
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 
    duplicate_stack_request = wodby.DuplicateStackRequest() # DuplicateStackRequest | 

    try:
        # Duplicate stack
        api_response = api_instance.duplicate_stack(id, duplicate_stack_request)
        print("The response of StacksApi->duplicate_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->duplicate_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **duplicate_stack_request** | [**DuplicateStackRequest**](DuplicateStackRequest.md)|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Duplicated stack |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack**
> Stack get_stack(id)

Get stack

Returns the stack identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack import Stack
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 

    try:
        # Get stack
        api_response = api_instance.get_stack(id)
        print("The response of StacksApi->get_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->get_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_by_name**
> Stack get_stack_by_name(name, rev_number=rev_number)

Get stack by name

Returns the stack identified by name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack import Stack
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
    api_instance = wodby.StacksApi(api_client)
    name = 'name_example' # str | 
    rev_number = 56 # int |  (optional)

    try:
        # Get stack by name
        api_response = api_instance.get_stack_by_name(name, rev_number=rev_number)
        print("The response of StacksApi->get_stack_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->get_stack_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **rev_number** | **int**|  | [optional] 

### Return type

[**Stack**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_origin_sync_changelog**
> StackOriginSyncChangelog get_stack_origin_sync_changelog(id)

Preview stack origin synchronization

Returns the origin stack changes that would be synchronized into the stack.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_origin_sync_changelog import StackOriginSyncChangelog
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 

    try:
        # Preview stack origin synchronization
        api_response = api_instance.get_stack_origin_sync_changelog(id)
        print("The response of StacksApi->get_stack_origin_sync_changelog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->get_stack_origin_sync_changelog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**StackOriginSyncChangelog**](StackOriginSyncChangelog.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack origin synchronization changelog |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_revision**
> StackRevision get_stack_revision(id)

Get stack revision

Returns the stack revision identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_revision import StackRevision
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 

    try:
        # Get stack revision
        api_response = api_instance.get_stack_revision(id)
        print("The response of StacksApi->get_stack_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->get_stack_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**StackRevision**](StackRevision.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack revision |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_service_update_changelog**
> List[StackServiceUpdateChangelog] get_stack_service_update_changelog(id, stack_service_id=stack_service_id)

Preview stack service revision updates

Returns eligible service revision changes for a stack, optionally limited to one stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_update_changelog import StackServiceUpdateChangelog
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 
    stack_service_id = 56 # int |  (optional)

    try:
        # Preview stack service revision updates
        api_response = api_instance.get_stack_service_update_changelog(id, stack_service_id=stack_service_id)
        print("The response of StacksApi->get_stack_service_update_changelog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->get_stack_service_update_changelog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **stack_service_id** | **int**|  | [optional] 

### Return type

[**List[StackServiceUpdateChangelog]**](StackServiceUpdateChangelog.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack service update changelogs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_stacks**
> OperationResult import_stacks(import_catalog_from_git_input)

Import stacks from Git

Starts a task that imports stacks from a Git repository.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.import_catalog_from_git_input import ImportCatalogFromGitInput
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
    api_instance = wodby.StacksApi(api_client)
    import_catalog_from_git_input = wodby.ImportCatalogFromGitInput() # ImportCatalogFromGitInput | 

    try:
        # Import stacks from Git
        api_response = api_instance.import_stacks(import_catalog_from_git_input)
        print("The response of StacksApi->import_stacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->import_stacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_catalog_from_git_input** | [**ImportCatalogFromGitInput**](ImportCatalogFromGitInput.md)|  | 

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
**201** | Import task |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_stacks**
> List[Stack] list_public_stacks()

List public catalog stacks

Returns public stacks that can be duplicated into an organization or project.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack import Stack
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
    api_instance = wodby.StacksApi(api_client)

    try:
        # List public catalog stacks
        api_response = api_instance.list_public_stacks()
        print("The response of StacksApi->list_public_stacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->list_public_stacks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Stack]**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public catalog stacks |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_revision_services**
> List[StackService] list_stack_revision_services(id)

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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 

    try:
        # List stack services
        api_response = api_instance.list_stack_revision_services(id)
        print("The response of StacksApi->list_stack_revision_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->list_stack_revision_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackService]**](StackService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack services |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stacks**
> StacksResponse list_stacks(org_id=org_id, project_ids=project_ids, search=search, page=page, page_size=page_size)

List stacks

Returns stacks matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stacks_response import StacksResponse
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
    api_instance = wodby.StacksApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    search = 'search_example' # str |  (optional)
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List stacks
        api_response = api_instance.list_stacks(org_id=org_id, project_ids=project_ids, search=search, page=page, page_size=page_size)
        print("The response of StacksApi->list_stacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->list_stacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **search** | **str**|  | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 30 | [optional] 

### Return type

[**StacksResponse**](StacksResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stacks response |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_stack_draft**
> Stack publish_stack_draft(id)

Publish stack draft

Publishes the current stack draft as the active stack revision.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack import Stack
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 

    try:
        # Publish stack draft
        api_response = api_instance.publish_stack_draft(id)
        print("The response of StacksApi->publish_stack_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->publish_stack_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Published stack |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scaffold_stack_from_helm_chart**
> HelmChartStackScaffoldResponse scaffold_stack_from_helm_chart(helm_chart_stack_scaffold_input)

Scaffold stack from Helm chart

Renders a Helm chart and returns best-effort Wodby service and stack manifests for review and validation.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.helm_chart_stack_scaffold_input import HelmChartStackScaffoldInput
from wodby.models.helm_chart_stack_scaffold_response import HelmChartStackScaffoldResponse
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
    api_instance = wodby.StacksApi(api_client)
    helm_chart_stack_scaffold_input = wodby.HelmChartStackScaffoldInput() # HelmChartStackScaffoldInput | 

    try:
        # Scaffold stack from Helm chart
        api_response = api_instance.scaffold_stack_from_helm_chart(helm_chart_stack_scaffold_input)
        print("The response of StacksApi->scaffold_stack_from_helm_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->scaffold_stack_from_helm_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_chart_stack_scaffold_input** | [**HelmChartStackScaffoldInput**](HelmChartStackScaffoldInput.md)|  | 

### Return type

[**HelmChartStackScaffoldResponse**](HelmChartStackScaffoldResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated service and stack manifests |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_stack_with_origin**
> Stack sync_stack_with_origin(id, stack_sync_options_input=stack_sync_options_input)

Sync stack with origin

Syncs the stack with its origin stack revision.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack import Stack
from wodby.models.stack_sync_options_input import StackSyncOptionsInput
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 
    stack_sync_options_input = wodby.StackSyncOptionsInput() # StackSyncOptionsInput |  (optional)

    try:
        # Sync stack with origin
        api_response = api_instance.sync_stack_with_origin(id, stack_sync_options_input=stack_sync_options_input)
        print("The response of StacksApi->sync_stack_with_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->sync_stack_with_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **stack_sync_options_input** | [**StackSyncOptionsInput**](StackSyncOptionsInput.md)|  | [optional] 

### Return type

[**Stack**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synced stack |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_from_git**
> OperationResult update_stack_from_git(id, update_stack_from_git_request)

Update stack from git

Starts a task that updates the stack from its configured Git source.

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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 
    update_stack_from_git_request = wodby.UpdateStackFromGitRequest() # UpdateStackFromGitRequest | 

    try:
        # Update stack from git
        api_response = api_instance.update_stack_from_git(id, update_stack_from_git_request)
        print("The response of StacksApi->update_stack_from_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->update_stack_from_git: %s\n" % e)
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
**201** | Update task |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_service_revisions**
> OperationResult update_stack_service_revisions(id)

Update stack service revisions

Starts a task that advances unpinned stack services to their eligible revisions.

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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 

    try:
        # Update stack service revisions
        api_response = api_instance.update_stack_service_revisions(id)
        print("The response of StacksApi->update_stack_service_revisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->update_stack_service_revisions: %s\n" % e)
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
**200** | Stack update task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_settings**
> Stack update_stack_settings(id, stack_settings_input)

Update stack settings

Updates stack settings and returns the updated stack.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack import Stack
from wodby.models.stack_settings_input import StackSettingsInput
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
    api_instance = wodby.StacksApi(api_client)
    id = 56 # int | 
    stack_settings_input = wodby.StackSettingsInput() # StackSettingsInput | 

    try:
        # Update stack settings
        api_response = api_instance.update_stack_settings(id, stack_settings_input)
        print("The response of StacksApi->update_stack_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->update_stack_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **stack_settings_input** | [**StackSettingsInput**](StackSettingsInput.md)|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated stack |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_stack_manifest**
> ManifestValidationResponse validate_stack_manifest(manifest_from_yaml_input)

Validate stack manifest

Validates a Wodby stack manifest without creating a stack.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.manifest_from_yaml_input import ManifestFromYAMLInput
from wodby.models.manifest_validation_response import ManifestValidationResponse
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
    api_instance = wodby.StacksApi(api_client)
    manifest_from_yaml_input = wodby.ManifestFromYAMLInput() # ManifestFromYAMLInput | 

    try:
        # Validate stack manifest
        api_response = api_instance.validate_stack_manifest(manifest_from_yaml_input)
        print("The response of StacksApi->validate_stack_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->validate_stack_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_from_yaml_input** | [**ManifestFromYAMLInput**](ManifestFromYAMLInput.md)|  | 

### Return type

[**ManifestValidationResponse**](ManifestValidationResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stack manifest validation result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

