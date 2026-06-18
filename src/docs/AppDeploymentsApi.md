# wodby.AppDeploymentsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_deployment**](AppDeploymentsApi.md#create_app_deployment) | **POST** /app-deployments | Create deployment
[**create_app_deployment_from_ci**](AppDeploymentsApi.md#create_app_deployment_from_ci) | **POST** /app-deployments/from-ci | Create deployment from CI
[**get_app_deployment**](AppDeploymentsApi.md#get_app_deployment) | **GET** /app-deployments/{id} | Get deployment
[**list_app_deployments**](AppDeploymentsApi.md#list_app_deployments) | **GET** /app-deployments | List app deployments
[**redeploy_app_deployment**](AppDeploymentsApi.md#redeploy_app_deployment) | **POST** /app-deployments/{id}/redeploy | Redeploy deployment


# **create_app_deployment**
> AppDeployment create_app_deployment(create_deployment_request)

Create deployment

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_deployment import AppDeployment
from wodby.models.create_deployment_request import CreateDeploymentRequest
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
    api_instance = wodby.AppDeploymentsApi(api_client)
    create_deployment_request = wodby.CreateDeploymentRequest() # CreateDeploymentRequest | 

    try:
        # Create deployment
        api_response = api_instance.create_app_deployment(create_deployment_request)
        print("The response of AppDeploymentsApi->create_app_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppDeploymentsApi->create_app_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_deployment_request** | [**CreateDeploymentRequest**](CreateDeploymentRequest.md)|  | 

### Return type

[**AppDeployment**](AppDeployment.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created deployment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_deployment_from_ci**
> AppDeployment create_app_deployment_from_ci(deployment_from_ci_input)

Create deployment from CI

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_deployment import AppDeployment
from wodby.models.deployment_from_ci_input import DeploymentFromCIInput
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
    api_instance = wodby.AppDeploymentsApi(api_client)
    deployment_from_ci_input = wodby.DeploymentFromCIInput() # DeploymentFromCIInput | 

    try:
        # Create deployment from CI
        api_response = api_instance.create_app_deployment_from_ci(deployment_from_ci_input)
        print("The response of AppDeploymentsApi->create_app_deployment_from_ci:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppDeploymentsApi->create_app_deployment_from_ci: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_from_ci_input** | [**DeploymentFromCIInput**](DeploymentFromCIInput.md)|  | 

### Return type

[**AppDeployment**](AppDeployment.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created deployment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_deployment**
> AppDeployment get_app_deployment(id)

Get deployment

### Example

* Api Key Authentication (accessTokenHeader):
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
    api_instance = wodby.AppDeploymentsApi(api_client)
    id = 56 # int | 

    try:
        # Get deployment
        api_response = api_instance.get_app_deployment(id)
        print("The response of AppDeploymentsApi->get_app_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppDeploymentsApi->get_app_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppDeployment**](AppDeployment.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_deployments**
> AppDeploymentsResponse list_app_deployments(app_instance_id, page=page, page_size=page_size)

List app deployments

### Example

* Api Key Authentication (accessTokenHeader):
* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_deployments_response import AppDeploymentsResponse
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
    api_instance = wodby.AppDeploymentsApi(api_client)
    app_instance_id = 56 # int | 
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List app deployments
        api_response = api_instance.list_app_deployments(app_instance_id, page=page, page_size=page_size)
        print("The response of AppDeploymentsApi->list_app_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppDeploymentsApi->list_app_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 30 | [optional] 

### Return type

[**AppDeploymentsResponse**](AppDeploymentsResponse.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of deployments |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_app_deployment**
> AppDeployment redeploy_app_deployment(id)

Redeploy deployment

### Example

* Api Key Authentication (accessTokenHeader):
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
    api_instance = wodby.AppDeploymentsApi(api_client)
    id = 56 # int | 

    try:
        # Redeploy deployment
        api_response = api_instance.redeploy_app_deployment(id)
        print("The response of AppDeploymentsApi->redeploy_app_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppDeploymentsApi->redeploy_app_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppDeployment**](AppDeployment.md)

### Authorization

[accessTokenHeader](../README.md#accessTokenHeader), [apiKeyHeader](../README.md#apiKeyHeader)

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

