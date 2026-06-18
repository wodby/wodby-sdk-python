# wodby.ProvidersApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provider**](ProvidersApi.md#get_provider) | **GET** /providers/{id} | Get provider
[**get_provider_by_name**](ProvidersApi.md#get_provider_by_name) | **GET** /providers/by-name/{name} | Get provider by name
[**get_provider_revision**](ProvidersApi.md#get_provider_revision) | **GET** /provider-revisions/{id} | Get provider revision
[**list_providers**](ProvidersApi.md#list_providers) | **GET** /providers | List providers


# **get_provider**
> Provider get_provider(id)

Get provider

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

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

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider revision |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ProvidersResponse list_providers(org_id, project_ids=project_ids, exclude_public=exclude_public, search=search, page=page, page_size=page_size)

List providers

### Example

* Api Key Authentication (accessTokenHeader):
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

# Configure API key authorization: accessTokenHeader
configuration.api_key['accessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenHeader'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ProvidersApi(api_client)
    org_id = 56 # int | 
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    exclude_public = True # bool |  (optional)
    search = 'search_example' # str |  (optional)
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List providers
        api_response = api_instance.list_providers(org_id, project_ids=project_ids, exclude_public=exclude_public, search=search, page=page, page_size=page_size)
        print("The response of ProvidersApi->list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->list_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **exclude_public** | **bool**|  | [optional] 
 **search** | **str**|  | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 30 | [optional] 

### Return type

[**ProvidersResponse**](ProvidersResponse.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Providers response |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

