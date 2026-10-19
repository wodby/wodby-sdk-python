# wodby.ServicesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_from_manifest**](ServicesApi.md#create_service_from_manifest) | **POST** /services/actions/create-from-manifest | Create service from manifest
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /services/{id} | Delete service
[**get_service**](ServicesApi.md#get_service) | **GET** /services/{id} | Get service
[**get_service_by_name**](ServicesApi.md#get_service_by_name) | **GET** /services/by-name/{name} | Get service by name
[**get_service_revision**](ServicesApi.md#get_service_revision) | **GET** /service-revisions/{id} | Get service revision
[**get_service_sharing**](ServicesApi.md#get_service_sharing) | **GET** /services/sharing/{id} | Get service sharing
[**import_services**](ServicesApi.md#import_services) | **POST** /services/actions/import | Import services from Git
[**list_inheriting_services**](ServicesApi.md#list_inheriting_services) | **GET** /services/by-name/{name}/inheriting-services | List inheriting services
[**list_resolved_service_configs**](ServicesApi.md#list_resolved_service_configs) | **GET** /service-revisions/{id}/configs | List resolved service configs
[**list_service_link_candidates**](ServicesApi.md#list_service_link_candidates) | **GET** /services/{name}/options/link-candidates | List service link candidates
[**list_services**](ServicesApi.md#list_services) | **GET** /services | List services
[**scaffold_service_from_helm_chart**](ServicesApi.md#scaffold_service_from_helm_chart) | **POST** /services/actions/scaffold-from-helm-chart | Scaffold service from Helm chart
[**update_service_from_git**](ServicesApi.md#update_service_from_git) | **POST** /services/{id}/actions/update-from-git | Update service from Git
[**update_service_from_manifest**](ServicesApi.md#update_service_from_manifest) | **POST** /services/{id}/actions/update-from-manifest | Update service from manifest
[**update_service_settings**](ServicesApi.md#update_service_settings) | **PUT** /services/settings/{id} | Update service settings
[**update_service_sharing**](ServicesApi.md#update_service_sharing) | **PUT** /services/sharing/{id} | Update service sharing
[**validate_service_manifest**](ServicesApi.md#validate_service_manifest) | **POST** /services/actions/validate-manifest | Validate service manifest


# **create_service_from_manifest**
> Service create_service_from_manifest(manifest_from_yaml_input)

Create service from manifest

Creates a non-Git Wodby service from a service manifest.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.manifest_from_yaml_input import ManifestFromYAMLInput
from wodby.models.service import Service
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
    api_instance = wodby.ServicesApi(api_client)
    manifest_from_yaml_input = wodby.ManifestFromYAMLInput() # ManifestFromYAMLInput | 

    try:
        # Create service from manifest
        api_response = api_instance.create_service_from_manifest(manifest_from_yaml_input)
        print("The response of ServicesApi->create_service_from_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->create_service_from_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_from_yaml_input** | [**ManifestFromYAMLInput**](ManifestFromYAMLInput.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**
> OperationResult delete_service(id)

Delete service

Deletes a service that no stack uses.

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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete service
        api_response = api_instance.delete_service(id)
        print("The response of ServicesApi->delete_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
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
**200** | Deletion result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> Service get_service(id)

Get service

Returns the service identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.service import Service
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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 

    try:
        # Get service
        api_response = api_instance.get_service(id)
        print("The response of ServicesApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Service**](Service.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_by_name**
> Service get_service_by_name(name, rev_number=rev_number)

Get service by name

Returns the service identified by name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.service import Service
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
    api_instance = wodby.ServicesApi(api_client)
    name = 'name_example' # str | 
    rev_number = 56 # int |  (optional)

    try:
        # Get service by name
        api_response = api_instance.get_service_by_name(name, rev_number=rev_number)
        print("The response of ServicesApi->get_service_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **rev_number** | **int**|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_revision**
> ServiceRevision get_service_revision(id)

Get service revision

Returns the service revision identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.service_revision import ServiceRevision
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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 

    try:
        # Get service revision
        api_response = api_instance.get_service_revision(id)
        print("The response of ServicesApi->get_service_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ServiceRevision**](ServiceRevision.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service revision |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_sharing**
> ResourceSharing get_service_sharing(id)

Get service sharing

Returns who owns the service and which projects can use it.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.resource_sharing import ResourceSharing
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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 

    try:
        # Get service sharing
        api_response = api_instance.get_service_sharing(id)
        print("The response of ServicesApi->get_service_sharing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_sharing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceSharing**](ResourceSharing.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service sharing |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_services**
> OperationResult import_services(import_services_from_git_input)

Import services from Git

Starts a task that imports services from a Git repository.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.import_services_from_git_input import ImportServicesFromGitInput
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
    api_instance = wodby.ServicesApi(api_client)
    import_services_from_git_input = wodby.ImportServicesFromGitInput() # ImportServicesFromGitInput | 

    try:
        # Import services from Git
        api_response = api_instance.import_services(import_services_from_git_input)
        print("The response of ServicesApi->import_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->import_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_services_from_git_input** | [**ImportServicesFromGitInput**](ImportServicesFromGitInput.md)|  | 

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

# **list_inheriting_services**
> List[Service] list_inheriting_services(name)

List inheriting services

Returns the services whose manifests inherit from the named service with from.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.service import Service
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
    api_instance = wodby.ServicesApi(api_client)
    name = 'name_example' # str | 

    try:
        # List inheriting services
        api_response = api_instance.list_inheriting_services(name)
        print("The response of ServicesApi->list_inheriting_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_inheriting_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**List[Service]**](Service.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inheriting services |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resolved_service_configs**
> List[ResolvedServiceConfig] list_resolved_service_configs(id, option_version, platform=platform)

List resolved service configs

Returns the configuration files of a service revision with the default content Wodby resolved for one option version and platform.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.resolved_service_config import ResolvedServiceConfig
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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 
    option_version = 'option_version_example' # str | Service option version.
    platform = 'platform_example' # str | Image platform. Defaults to linux/amd64. (optional)

    try:
        # List resolved service configs
        api_response = api_instance.list_resolved_service_configs(id, option_version, platform=platform)
        print("The response of ServicesApi->list_resolved_service_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_resolved_service_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **option_version** | **str**| Service option version. | 
 **platform** | **str**| Image platform. Defaults to linux/amd64. | [optional] 

### Return type

[**List[ResolvedServiceConfig]**](ResolvedServiceConfig.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resolved configuration files |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_link_candidates**
> List[Dict[str, object]] list_service_link_candidates(name)

List service link candidates

Returns service link candidates matching the request filters.

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
    api_instance = wodby.ServicesApi(api_client)
    name = 'name_example' # str | 

    try:
        # List service link candidates
        api_response = api_instance.list_service_link_candidates(name)
        print("The response of ServicesApi->list_service_link_candidates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_service_link_candidates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**List[Dict[str, object]]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service link candidates |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services**
> ServicesResponse list_services(org_id=org_id, project_ids=project_ids, search=search, page=page, page_size=page_size)

List services

Returns services matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.services_response import ServicesResponse
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
    api_instance = wodby.ServicesApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    search = 'search_example' # str |  (optional)
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List services
        api_response = api_instance.list_services(org_id=org_id, project_ids=project_ids, search=search, page=page, page_size=page_size)
        print("The response of ServicesApi->list_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_services: %s\n" % e)
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

[**ServicesResponse**](ServicesResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Services response |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scaffold_service_from_helm_chart**
> HelmChartServiceScaffoldResponse scaffold_service_from_helm_chart(helm_chart_service_scaffold_input)

Scaffold service from Helm chart

Renders a Helm chart and returns a best-effort Wodby service manifest for review and validation.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.helm_chart_service_scaffold_input import HelmChartServiceScaffoldInput
from wodby.models.helm_chart_service_scaffold_response import HelmChartServiceScaffoldResponse
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
    api_instance = wodby.ServicesApi(api_client)
    helm_chart_service_scaffold_input = wodby.HelmChartServiceScaffoldInput() # HelmChartServiceScaffoldInput | 

    try:
        # Scaffold service from Helm chart
        api_response = api_instance.scaffold_service_from_helm_chart(helm_chart_service_scaffold_input)
        print("The response of ServicesApi->scaffold_service_from_helm_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->scaffold_service_from_helm_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_chart_service_scaffold_input** | [**HelmChartServiceScaffoldInput**](HelmChartServiceScaffoldInput.md)|  | 

### Return type

[**HelmChartServiceScaffoldResponse**](HelmChartServiceScaffoldResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated service manifest |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_from_git**
> OperationResult update_service_from_git(id, update_stack_from_git_request)

Update service from Git

Starts a task that moves a Git-sourced service to another ref.

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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 
    update_stack_from_git_request = wodby.UpdateStackFromGitRequest() # UpdateStackFromGitRequest | 

    try:
        # Update service from Git
        api_response = api_instance.update_service_from_git(id, update_stack_from_git_request)
        print("The response of ServicesApi->update_service_from_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service_from_git: %s\n" % e)
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
**201** | Service update task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_from_manifest**
> OperationResult update_service_from_manifest(id, service_manifest_update_input)

Update service from manifest

Updates an existing non-Git Wodby service from a service manifest and starts a service update task.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.service_manifest_update_input import ServiceManifestUpdateInput
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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 
    service_manifest_update_input = wodby.ServiceManifestUpdateInput() # ServiceManifestUpdateInput | 

    try:
        # Update service from manifest
        api_response = api_instance.update_service_from_manifest(id, service_manifest_update_input)
        print("The response of ServicesApi->update_service_from_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service_from_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **service_manifest_update_input** | [**ServiceManifestUpdateInput**](ServiceManifestUpdateInput.md)|  | 

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
**201** | Service update task accepted |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_settings**
> Service update_service_settings(id, service_settings_input)

Update service settings

Updates service settings and returns the updated service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.service import Service
from wodby.models.service_settings_input import ServiceSettingsInput
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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 
    service_settings_input = wodby.ServiceSettingsInput() # ServiceSettingsInput | 

    try:
        # Update service settings
        api_response = api_instance.update_service_settings(id, service_settings_input)
        print("The response of ServicesApi->update_service_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **service_settings_input** | [**ServiceSettingsInput**](ServiceSettingsInput.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_sharing**
> ResourceSharing update_service_sharing(id, resource_sharing_input)

Update service sharing

Changes the service owner and replaces the projects it is shared with. It can also make an organization-owned service available to every project. Returns the resulting sharing.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.resource_sharing import ResourceSharing
from wodby.models.resource_sharing_input import ResourceSharingInput
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
    api_instance = wodby.ServicesApi(api_client)
    id = 56 # int | 
    resource_sharing_input = wodby.ResourceSharingInput() # ResourceSharingInput | 

    try:
        # Update service sharing
        api_response = api_instance.update_service_sharing(id, resource_sharing_input)
        print("The response of ServicesApi->update_service_sharing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service_sharing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **resource_sharing_input** | [**ResourceSharingInput**](ResourceSharingInput.md)|  | 

### Return type

[**ResourceSharing**](ResourceSharing.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated service sharing |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_service_manifest**
> ManifestValidationResponse validate_service_manifest(manifest_from_yaml_input)

Validate service manifest

Validates a Wodby service manifest without creating a service.

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
    api_instance = wodby.ServicesApi(api_client)
    manifest_from_yaml_input = wodby.ManifestFromYAMLInput() # ManifestFromYAMLInput | 

    try:
        # Validate service manifest
        api_response = api_instance.validate_service_manifest(manifest_from_yaml_input)
        print("The response of ServicesApi->validate_service_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->validate_service_manifest: %s\n" % e)
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
**200** | Service manifest validation result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

