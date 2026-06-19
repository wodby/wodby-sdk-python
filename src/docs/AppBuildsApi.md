# wodby.AppBuildsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_build**](AppBuildsApi.md#create_app_build) | **POST** /app-builds | Create build
[**create_app_build_from_ci**](AppBuildsApi.md#create_app_build_from_ci) | **POST** /app-builds/from-ci | Create build from CI
[**deploy_app_build**](AppBuildsApi.md#deploy_app_build) | **POST** /app-builds/{id}/deploy | Deploy build
[**get_app_build**](AppBuildsApi.md#get_app_build) | **GET** /app-builds/{id} | Get build
[**get_app_build_config**](AppBuildsApi.md#get_app_build_config) | **GET** /app-builds/{id}/config | Get build config
[**get_app_build_docker_registry_credentials**](AppBuildsApi.md#get_app_build_docker_registry_credentials) | **GET** /app-builds/{id}/docker-registry-credentials | Get Docker registry credentials for build
[**list_app_builds**](AppBuildsApi.md#list_app_builds) | **GET** /app-builds | List app builds
[**void_app_build**](AppBuildsApi.md#void_app_build) | **POST** /app-builds/{id}/void | Void build images


# **create_app_build**
> List[AppBuild] create_app_build(create_build_request)

Create build

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_build import AppBuild
from wodby.models.create_build_request import CreateBuildRequest
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
    api_instance = wodby.AppBuildsApi(api_client)
    create_build_request = wodby.CreateBuildRequest() # CreateBuildRequest | 

    try:
        # Create build
        api_response = api_instance.create_app_build(create_build_request)
        print("The response of AppBuildsApi->create_app_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->create_app_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_build_request** | [**CreateBuildRequest**](CreateBuildRequest.md)|  | 

### Return type

[**List[AppBuild]**](AppBuild.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created build list |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_build_from_ci**
> AppBuild create_app_build_from_ci(new_build_from_ci_input)

Create build from CI

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_build import AppBuild
from wodby.models.new_build_from_ci_input import NewBuildFromCIInput
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
    api_instance = wodby.AppBuildsApi(api_client)
    new_build_from_ci_input = wodby.NewBuildFromCIInput() # NewBuildFromCIInput | 

    try:
        # Create build from CI
        api_response = api_instance.create_app_build_from_ci(new_build_from_ci_input)
        print("The response of AppBuildsApi->create_app_build_from_ci:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->create_app_build_from_ci: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_build_from_ci_input** | [**NewBuildFromCIInput**](NewBuildFromCIInput.md)|  | 

### Return type

[**AppBuild**](AppBuild.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created build |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_app_build**
> AppDeployment deploy_app_build(id)

Deploy build

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_deployment import AppDeployment
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
    api_instance = wodby.AppBuildsApi(api_client)
    id = 56 # int | 

    try:
        # Deploy build
        api_response = api_instance.deploy_app_build(id)
        print("The response of AppBuildsApi->deploy_app_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->deploy_app_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppDeployment**](AppDeployment.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created deployment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_build**
> AppBuild get_app_build(id)

Get build

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (ciAccessTokenHeader):

```python
import wodby
from wodby.models.app_build import AppBuild
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

# Configure API key authorization: ciAccessTokenHeader
configuration.api_key['ciAccessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ciAccessTokenHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppBuildsApi(api_client)
    id = 56 # int | 

    try:
        # Get build
        api_response = api_instance.get_app_build(id)
        print("The response of AppBuildsApi->get_app_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->get_app_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppBuild**](AppBuild.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [ciAccessTokenHeader](../README.md#ciAccessTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Build |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_build_config**
> AppBuildConfig get_app_build_config(id)

Get build config

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (ciAccessTokenHeader):

```python
import wodby
from wodby.models.app_build_config import AppBuildConfig
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

# Configure API key authorization: ciAccessTokenHeader
configuration.api_key['ciAccessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ciAccessTokenHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppBuildsApi(api_client)
    id = 56 # int | 

    try:
        # Get build config
        api_response = api_instance.get_app_build_config(id)
        print("The response of AppBuildsApi->get_app_build_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->get_app_build_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppBuildConfig**](AppBuildConfig.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [ciAccessTokenHeader](../README.md#ciAccessTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Build config |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_build_docker_registry_credentials**
> DockerRegistryCredentials get_app_build_docker_registry_credentials(id)

Get Docker registry credentials for build

### Example

* Api Key Authentication (apiKeyHeader):
* Api Key Authentication (ciAccessTokenHeader):

```python
import wodby
from wodby.models.docker_registry_credentials import DockerRegistryCredentials
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

# Configure API key authorization: ciAccessTokenHeader
configuration.api_key['ciAccessTokenHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ciAccessTokenHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.AppBuildsApi(api_client)
    id = 56 # int | 

    try:
        # Get Docker registry credentials for build
        api_response = api_instance.get_app_build_docker_registry_credentials(id)
        print("The response of AppBuildsApi->get_app_build_docker_registry_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->get_app_build_docker_registry_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DockerRegistryCredentials**](DockerRegistryCredentials.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [ciAccessTokenHeader](../README.md#ciAccessTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Docker registry credentials |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_builds**
> AppBuildsResponse list_app_builds(app_instance_id, page=page, page_size=page_size)

List app builds

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_builds_response import AppBuildsResponse
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
    api_instance = wodby.AppBuildsApi(api_client)
    app_instance_id = 56 # int | 
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List app builds
        api_response = api_instance.list_app_builds(app_instance_id, page=page, page_size=page_size)
        print("The response of AppBuildsApi->list_app_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->list_app_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 30 | [optional] 

### Return type

[**AppBuildsResponse**](AppBuildsResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of builds |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_app_build**
> AppBuild void_app_build(id)

Void build images

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_build import AppBuild
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
    api_instance = wodby.AppBuildsApi(api_client)
    id = 56 # int | 

    try:
        # Void build images
        api_response = api_instance.void_app_build(id)
        print("The response of AppBuildsApi->void_app_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppBuildsApi->void_app_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppBuild**](AppBuild.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated build |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

