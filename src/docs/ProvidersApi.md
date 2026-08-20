# wodby.ProvidersApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider_from_manifest**](ProvidersApi.md#create_provider_from_manifest) | **POST** /providers/actions/create-from-manifest | Create provider from manifest
[**create_variable_provider**](ProvidersApi.md#create_variable_provider) | **POST** /providers/actions/create-variable | Create variable provider
[**get_provider**](ProvidersApi.md#get_provider) | **GET** /providers/{id} | Get provider
[**get_provider_by_name**](ProvidersApi.md#get_provider_by_name) | **GET** /providers/by-name/{name} | Get provider by name
[**get_provider_revision**](ProvidersApi.md#get_provider_revision) | **GET** /provider-revisions/{id} | Get provider revision
[**import_providers**](ProvidersApi.md#import_providers) | **POST** /providers/actions/import | Import providers from Git
[**list_providers**](ProvidersApi.md#list_providers) | **GET** /providers | List providers
[**update_provider_from_git**](ProvidersApi.md#update_provider_from_git) | **POST** /providers/{id}/actions/update-from-git | Update provider from Git
[**update_provider_from_manifest**](ProvidersApi.md#update_provider_from_manifest) | **POST** /providers/{id}/actions/update-from-manifest | Update provider from manifest
[**update_provider_settings**](ProvidersApi.md#update_provider_settings) | **PUT** /providers/settings/{id} | Update provider settings


# **create_provider_from_manifest**
> Provider create_provider_from_manifest(provider_manifest_input)

Create provider from manifest

Creates a namespaced, versioned variable provider from manifest YAML.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.provider import Provider
from wodby.models.provider_manifest_input import ProviderManifestInput
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
    api_instance = wodby.ProvidersApi(api_client)
    provider_manifest_input = wodby.ProviderManifestInput() # ProviderManifestInput | 

    try:
        # Create provider from manifest
        api_response = api_instance.create_provider_from_manifest(provider_manifest_input)
        print("The response of ProvidersApi->create_provider_from_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->create_provider_from_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_manifest_input** | [**ProviderManifestInput**](ProviderManifestInput.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Provider created |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_variable_provider**
> Provider create_variable_provider(new_variable_provider_input)

Create variable provider

Creates a private provider whose integration fields are exposed as service environment variables.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_variable_provider_input import NewVariableProviderInput
from wodby.models.provider import Provider
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
    api_instance = wodby.ProvidersApi(api_client)
    new_variable_provider_input = wodby.NewVariableProviderInput() # NewVariableProviderInput | 

    try:
        # Create variable provider
        api_response = api_instance.create_variable_provider(new_variable_provider_input)
        print("The response of ProvidersApi->create_variable_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->create_variable_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_variable_provider_input** | [**NewVariableProviderInput**](NewVariableProviderInput.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Variable provider created |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider**
> Provider get_provider(id)

Get provider

Returns the provider identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.provider import Provider
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
    api_instance = wodby.ProvidersApi(api_client)
    id = 56 # int | 

    try:
        # Get provider
        api_response = api_instance.get_provider(id)
        print("The response of ProvidersApi->get_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_by_name**
> Provider get_provider_by_name(name)

Get provider by name

Returns the provider identified by name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.provider import Provider
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
    api_instance = wodby.ProvidersApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get provider by name
        api_response = api_instance.get_provider_by_name(name)
        print("The response of ProvidersApi->get_provider_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_provider_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_revision**
> ProviderRevision get_provider_revision(id)

Get provider revision

Returns the provider revision identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.provider_revision import ProviderRevision
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
    api_instance = wodby.ProvidersApi(api_client)
    id = 56 # int | 

    try:
        # Get provider revision
        api_response = api_instance.get_provider_revision(id)
        print("The response of ProvidersApi->get_provider_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_provider_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ProviderRevision**](ProviderRevision.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider revision |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_providers**
> OperationResult import_providers(import_catalog_from_git_input)

Import providers from Git

Starts a task that imports provider.yml or all providers listed by index.yml from a Git repository.

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
    api_instance = wodby.ProvidersApi(api_client)
    import_catalog_from_git_input = wodby.ImportCatalogFromGitInput() # ImportCatalogFromGitInput | 

    try:
        # Import providers from Git
        api_response = api_instance.import_providers(import_catalog_from_git_input)
        print("The response of ProvidersApi->import_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->import_providers: %s\n" % e)
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
**201** | Provider import task accepted |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ProvidersResponse list_providers(org_id=org_id, project_ids=project_ids, exclude_public=exclude_public, search=search, page=page, page_size=page_size)

List providers

Returns providers matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.providers_response import ProvidersResponse
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
    api_instance = wodby.ProvidersApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    exclude_public = True # bool |  (optional)
    search = 'search_example' # str |  (optional)
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List providers
        api_response = api_instance.list_providers(org_id=org_id, project_ids=project_ids, exclude_public=exclude_public, search=search, page=page, page_size=page_size)
        print("The response of ProvidersApi->list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->list_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **exclude_public** | **bool**|  | [optional] 
 **search** | **str**|  | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 30 | [optional] 

### Return type

[**ProvidersResponse**](ProvidersResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Providers response |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider_from_git**
> OperationResult update_provider_from_git(id, update_stack_from_git_request)

Update provider from Git

Starts an update from the selected ref. Changing a shared repository ref updates all repository usages.

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
    api_instance = wodby.ProvidersApi(api_client)
    id = 56 # int | 
    update_stack_from_git_request = wodby.UpdateStackFromGitRequest() # UpdateStackFromGitRequest | 

    try:
        # Update provider from Git
        api_response = api_instance.update_provider_from_git(id, update_stack_from_git_request)
        print("The response of ProvidersApi->update_provider_from_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->update_provider_from_git: %s\n" % e)
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
**201** | Provider update task accepted |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider_from_manifest**
> OperationResult update_provider_from_manifest(id, provider_manifest_update_input)

Update provider from manifest

Starts an update of a non-Git provider from versioned manifest YAML.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.provider_manifest_update_input import ProviderManifestUpdateInput
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
    api_instance = wodby.ProvidersApi(api_client)
    id = 56 # int | 
    provider_manifest_update_input = wodby.ProviderManifestUpdateInput() # ProviderManifestUpdateInput | 

    try:
        # Update provider from manifest
        api_response = api_instance.update_provider_from_manifest(id, provider_manifest_update_input)
        print("The response of ProvidersApi->update_provider_from_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->update_provider_from_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **provider_manifest_update_input** | [**ProviderManifestUpdateInput**](ProviderManifestUpdateInput.md)|  | 

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
**201** | Provider update task accepted |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider_settings**
> Provider update_provider_settings(id, provider_settings_input)

Update provider settings

Updates Git auto-update settings shared by the repository usages.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.provider import Provider
from wodby.models.provider_settings_input import ProviderSettingsInput
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
    api_instance = wodby.ProvidersApi(api_client)
    id = 56 # int | 
    provider_settings_input = wodby.ProviderSettingsInput() # ProviderSettingsInput | 

    try:
        # Update provider settings
        api_response = api_instance.update_provider_settings(id, provider_settings_input)
        print("The response of ProvidersApi->update_provider_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->update_provider_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **provider_settings_input** | [**ProviderSettingsInput**](ProviderSettingsInput.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated provider |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

