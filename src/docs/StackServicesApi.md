# wodby.StackServicesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stack_service**](StackServicesApi.md#create_stack_service) | **POST** /stack-services | Create stack service
[**create_stack_service_annotation**](StackServicesApi.md#create_stack_service_annotation) | **POST** /stack-services/{id}/annotations | Create stack service annotation
[**create_stack_service_cron_schedule**](StackServicesApi.md#create_stack_service_cron_schedule) | **POST** /stack-services/{id}/cron-schedules | Create stack service cron schedule
[**create_stack_service_env_var**](StackServicesApi.md#create_stack_service_env_var) | **POST** /stack-services/{id}/env-vars | Create stack service env var
[**create_stack_service_helm_value**](StackServicesApi.md#create_stack_service_helm_value) | **POST** /stack-services/{id}/helm-values | Create stack service Helm value
[**create_stack_service_integration**](StackServicesApi.md#create_stack_service_integration) | **POST** /stack-services/{id}/integrations | Create stack service integration
[**create_stack_service_token**](StackServicesApi.md#create_stack_service_token) | **POST** /stack-services/{id}/tokens | Create stack service token
[**delete_stack_service**](StackServicesApi.md#delete_stack_service) | **DELETE** /stack-services/{id} | Delete stack service
[**delete_stack_service_annotation**](StackServicesApi.md#delete_stack_service_annotation) | **DELETE** /stack-service-annotations/{id} | Delete stack service annotation
[**delete_stack_service_cron_schedule**](StackServicesApi.md#delete_stack_service_cron_schedule) | **DELETE** /stack-service-cron-schedules/{id} | Delete stack service cron schedule
[**delete_stack_service_env_var**](StackServicesApi.md#delete_stack_service_env_var) | **DELETE** /stack-service-env-vars/{id} | Delete stack service env var
[**delete_stack_service_helm_value**](StackServicesApi.md#delete_stack_service_helm_value) | **DELETE** /stack-service-helm-values/{id} | Delete stack service Helm value
[**delete_stack_service_integration**](StackServicesApi.md#delete_stack_service_integration) | **DELETE** /stack-service-integrations/{id} | Delete stack service integration
[**delete_stack_service_token**](StackServicesApi.md#delete_stack_service_token) | **DELETE** /stack-service-tokens/{id} | Delete stack service token
[**list_stack_service_annotations**](StackServicesApi.md#list_stack_service_annotations) | **GET** /stack-services/{id}/annotations | List stack service annotations
[**list_stack_service_configs**](StackServicesApi.md#list_stack_service_configs) | **GET** /stack-services/{id}/configs | List stack service configs
[**list_stack_service_cron_schedules**](StackServicesApi.md#list_stack_service_cron_schedules) | **GET** /stack-services/{id}/cron-schedules | List stack service cron schedules
[**list_stack_service_env_vars**](StackServicesApi.md#list_stack_service_env_vars) | **GET** /stack-services/{id}/env-vars | List stack service env vars
[**list_stack_service_helm_values**](StackServicesApi.md#list_stack_service_helm_values) | **GET** /stack-services/{id}/helm-values | List stack service Helm values
[**list_stack_service_integrations**](StackServicesApi.md#list_stack_service_integrations) | **GET** /stack-services/{id}/integrations | List stack service integrations
[**list_stack_service_links**](StackServicesApi.md#list_stack_service_links) | **GET** /stack-services/{id}/links | List stack service links
[**list_stack_service_tokens**](StackServicesApi.md#list_stack_service_tokens) | **GET** /stack-services/{id}/tokens | List stack service tokens
[**list_stack_service_volumes**](StackServicesApi.md#list_stack_service_volumes) | **GET** /stack-services/{id}/volumes | List stack service volumes
[**list_stack_services**](StackServicesApi.md#list_stack_services) | **GET** /stack-services | List stack services
[**set_stack_service_config**](StackServicesApi.md#set_stack_service_config) | **PUT** /stack-services/{id}/configs/{name} | Set stack service config
[**set_stack_service_link**](StackServicesApi.md#set_stack_service_link) | **PUT** /stack-services/{id}/links/{name} | Set stack service link
[**set_stack_service_options**](StackServicesApi.md#set_stack_service_options) | **PUT** /stack-services/{id}/options | Update stack service options
[**set_stack_service_resources**](StackServicesApi.md#set_stack_service_resources) | **PUT** /stack-services/{id}/resources | Set stack service resources
[**set_stack_service_setting**](StackServicesApi.md#set_stack_service_setting) | **PUT** /stack-services/{id}/settings/{name} | Set stack service setting
[**set_stack_service_volume**](StackServicesApi.md#set_stack_service_volume) | **PUT** /stack-services/{id}/volumes/{name} | Set stack service volume
[**update_stack_service**](StackServicesApi.md#update_stack_service) | **PUT** /stack-services/{id} | Update stack service
[**update_stack_service_cron_schedule**](StackServicesApi.md#update_stack_service_cron_schedule) | **PUT** /stack-service-cron-schedules/{id} | Update stack service cron schedule
[**update_stack_service_env_var**](StackServicesApi.md#update_stack_service_env_var) | **PUT** /stack-service-env-vars/{id} | Update stack service env var
[**update_stack_service_helm_value**](StackServicesApi.md#update_stack_service_helm_value) | **PUT** /stack-service-helm-values/{id} | Update stack service Helm value
[**update_stack_service_token**](StackServicesApi.md#update_stack_service_token) | **PUT** /stack-service-tokens/{id} | Update stack service token


# **create_stack_service**
> StackService create_stack_service(new_stack_service_input)

Create stack service

Creates a stack service and returns the created resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_stack_service_input import NewStackServiceInput
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
    api_instance = wodby.StackServicesApi(api_client)
    new_stack_service_input = wodby.NewStackServiceInput() # NewStackServiceInput | 

    try:
        # Create stack service
        api_response = api_instance.create_stack_service(new_stack_service_input)
        print("The response of StackServicesApi->create_stack_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_stack_service_input** | [**NewStackServiceInput**](NewStackServiceInput.md)|  | 

### Return type

[**StackService**](StackService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_service_annotation**
> StackServiceAnnotation create_stack_service_annotation(id, new_stack_service_annotation_input)

Create stack service annotation

Creates an annotation for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_stack_service_annotation_input import NewStackServiceAnnotationInput
from wodby.models.stack_service_annotation import StackServiceAnnotation
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    new_stack_service_annotation_input = wodby.NewStackServiceAnnotationInput() # NewStackServiceAnnotationInput | 

    try:
        # Create stack service annotation
        api_response = api_instance.create_stack_service_annotation(id, new_stack_service_annotation_input)
        print("The response of StackServicesApi->create_stack_service_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_stack_service_annotation_input** | [**NewStackServiceAnnotationInput**](NewStackServiceAnnotationInput.md)|  | 

### Return type

[**StackServiceAnnotation**](StackServiceAnnotation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service annotation |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_service_cron_schedule**
> StackServiceCronSchedule create_stack_service_cron_schedule(id, new_stack_service_cron_schedule_input)

Create stack service cron schedule

Creates a cron schedule for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_stack_service_cron_schedule_input import NewStackServiceCronScheduleInput
from wodby.models.stack_service_cron_schedule import StackServiceCronSchedule
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    new_stack_service_cron_schedule_input = wodby.NewStackServiceCronScheduleInput() # NewStackServiceCronScheduleInput | 

    try:
        # Create stack service cron schedule
        api_response = api_instance.create_stack_service_cron_schedule(id, new_stack_service_cron_schedule_input)
        print("The response of StackServicesApi->create_stack_service_cron_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service_cron_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_stack_service_cron_schedule_input** | [**NewStackServiceCronScheduleInput**](NewStackServiceCronScheduleInput.md)|  | 

### Return type

[**StackServiceCronSchedule**](StackServiceCronSchedule.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service cron schedule |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_service_env_var**
> StackServiceEnvVar create_stack_service_env_var(id, new_stack_service_env_var_input)

Create stack service env var

Creates an environment variable for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_stack_service_env_var_input import NewStackServiceEnvVarInput
from wodby.models.stack_service_env_var import StackServiceEnvVar
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    new_stack_service_env_var_input = wodby.NewStackServiceEnvVarInput() # NewStackServiceEnvVarInput | 

    try:
        # Create stack service env var
        api_response = api_instance.create_stack_service_env_var(id, new_stack_service_env_var_input)
        print("The response of StackServicesApi->create_stack_service_env_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service_env_var: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_stack_service_env_var_input** | [**NewStackServiceEnvVarInput**](NewStackServiceEnvVarInput.md)|  | 

### Return type

[**StackServiceEnvVar**](StackServiceEnvVar.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service env var |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_service_helm_value**
> StackServiceHelmValue create_stack_service_helm_value(id, new_stack_service_scoped_value_input)

Create stack service Helm value

Creates a Helm value override for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_stack_service_scoped_value_input import NewStackServiceScopedValueInput
from wodby.models.stack_service_helm_value import StackServiceHelmValue
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    new_stack_service_scoped_value_input = wodby.NewStackServiceScopedValueInput() # NewStackServiceScopedValueInput | 

    try:
        # Create stack service Helm value
        api_response = api_instance.create_stack_service_helm_value(id, new_stack_service_scoped_value_input)
        print("The response of StackServicesApi->create_stack_service_helm_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service_helm_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_stack_service_scoped_value_input** | [**NewStackServiceScopedValueInput**](NewStackServiceScopedValueInput.md)|  | 

### Return type

[**StackServiceHelmValue**](StackServiceHelmValue.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service Helm value |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_service_integration**
> StackServiceIntegration create_stack_service_integration(id, integration_link_input)

Create stack service integration

Links an integration to a stack service integration slot.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.integration_link_input import IntegrationLinkInput
from wodby.models.stack_service_integration import StackServiceIntegration
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    integration_link_input = wodby.IntegrationLinkInput() # IntegrationLinkInput | 

    try:
        # Create stack service integration
        api_response = api_instance.create_stack_service_integration(id, integration_link_input)
        print("The response of StackServicesApi->create_stack_service_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **integration_link_input** | [**IntegrationLinkInput**](IntegrationLinkInput.md)|  | 

### Return type

[**StackServiceIntegration**](StackServiceIntegration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service integration |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_service_token**
> StackServiceToken create_stack_service_token(id, new_stack_service_token_input)

Create stack service token

Creates a token for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.new_stack_service_token_input import NewStackServiceTokenInput
from wodby.models.stack_service_token import StackServiceToken
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    new_stack_service_token_input = wodby.NewStackServiceTokenInput() # NewStackServiceTokenInput | 

    try:
        # Create stack service token
        api_response = api_instance.create_stack_service_token(id, new_stack_service_token_input)
        print("The response of StackServicesApi->create_stack_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->create_stack_service_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_stack_service_token_input** | [**NewStackServiceTokenInput**](NewStackServiceTokenInput.md)|  | 

### Return type

[**StackServiceToken**](StackServiceToken.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created stack service token |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service**
> OperationResult delete_stack_service(id)

Delete stack service

Deletes the stack service and returns the operation result.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service
        api_response = api_instance.delete_stack_service(id)
        print("The response of StackServicesApi->delete_stack_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service: %s\n" % e)
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
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service_annotation**
> OperationResult delete_stack_service_annotation(id)

Delete stack service annotation

Deletes a stack service annotation.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service annotation
        api_response = api_instance.delete_stack_service_annotation(id)
        print("The response of StackServicesApi->delete_stack_service_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service_annotation: %s\n" % e)
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
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service_cron_schedule**
> OperationResult delete_stack_service_cron_schedule(id)

Delete stack service cron schedule

Deletes a stack service cron schedule.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service cron schedule
        api_response = api_instance.delete_stack_service_cron_schedule(id)
        print("The response of StackServicesApi->delete_stack_service_cron_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service_cron_schedule: %s\n" % e)
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
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service_env_var**
> OperationResult delete_stack_service_env_var(id)

Delete stack service env var

Deletes a stack service environment variable.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service env var
        api_response = api_instance.delete_stack_service_env_var(id)
        print("The response of StackServicesApi->delete_stack_service_env_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service_env_var: %s\n" % e)
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
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service_helm_value**
> OperationResult delete_stack_service_helm_value(id)

Delete stack service Helm value

Deletes a stack service Helm value override.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service Helm value
        api_response = api_instance.delete_stack_service_helm_value(id)
        print("The response of StackServicesApi->delete_stack_service_helm_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service_helm_value: %s\n" % e)
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
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service_integration**
> OperationResult delete_stack_service_integration(id)

Delete stack service integration

Removes an integration link from a stack service.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service integration
        api_response = api_instance.delete_stack_service_integration(id)
        print("The response of StackServicesApi->delete_stack_service_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service_integration: %s\n" % e)
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
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_service_token**
> OperationResult delete_stack_service_token(id)

Delete stack service token

Deletes a stack service token.

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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete stack service token
        api_response = api_instance.delete_stack_service_token(id)
        print("The response of StackServicesApi->delete_stack_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->delete_stack_service_token: %s\n" % e)
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
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_annotations**
> List[StackServiceAnnotation] list_stack_service_annotations(id)

List stack service annotations

Returns annotations configured for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_annotation import StackServiceAnnotation
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service annotations
        api_response = api_instance.list_stack_service_annotations(id)
        print("The response of StackServicesApi->list_stack_service_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceAnnotation]**](StackServiceAnnotation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service annotations |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_configs**
> List[StackServiceConfig] list_stack_service_configs(id)

List stack service configs

Returns config overrides for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_config import StackServiceConfig
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service configs
        api_response = api_instance.list_stack_service_configs(id)
        print("The response of StackServicesApi->list_stack_service_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceConfig]**](StackServiceConfig.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service configs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_cron_schedules**
> List[StackServiceCronSchedule] list_stack_service_cron_schedules(id)

List stack service cron schedules

Returns cron schedules configured for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_cron_schedule import StackServiceCronSchedule
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service cron schedules
        api_response = api_instance.list_stack_service_cron_schedules(id)
        print("The response of StackServicesApi->list_stack_service_cron_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_cron_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceCronSchedule]**](StackServiceCronSchedule.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service cron schedules |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_env_vars**
> List[StackServiceEnvVar] list_stack_service_env_vars(id)

List stack service env vars

Returns environment variables configured for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_env_var import StackServiceEnvVar
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service env vars
        api_response = api_instance.list_stack_service_env_vars(id)
        print("The response of StackServicesApi->list_stack_service_env_vars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_env_vars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceEnvVar]**](StackServiceEnvVar.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service env vars |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_helm_values**
> List[StackServiceHelmValue] list_stack_service_helm_values(id)

List stack service Helm values

Returns Helm values configured for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_helm_value import StackServiceHelmValue
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service Helm values
        api_response = api_instance.list_stack_service_helm_values(id)
        print("The response of StackServicesApi->list_stack_service_helm_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_helm_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceHelmValue]**](StackServiceHelmValue.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service Helm values |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_integrations**
> List[StackServiceIntegration] list_stack_service_integrations(id)

List stack service integrations

Returns integration links configured for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_integration import StackServiceIntegration
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service integrations
        api_response = api_instance.list_stack_service_integrations(id)
        print("The response of StackServicesApi->list_stack_service_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceIntegration]**](StackServiceIntegration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service integrations |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_links**
> List[StackServiceLink] list_stack_service_links(id)

List stack service links

Returns service links configured for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_link import StackServiceLink
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service links
        api_response = api_instance.list_stack_service_links(id)
        print("The response of StackServicesApi->list_stack_service_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceLink]**](StackServiceLink.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service links |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_tokens**
> List[StackServiceToken] list_stack_service_tokens(id)

List stack service tokens

Returns tokens configured for a stack service without revealing secret values.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_token import StackServiceToken
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service tokens
        api_response = api_instance.list_stack_service_tokens(id)
        print("The response of StackServicesApi->list_stack_service_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceToken]**](StackServiceToken.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service tokens |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_service_volumes**
> List[StackServiceVolume] list_stack_service_volumes(id)

List stack service volumes

Returns volumes configured for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_volume import StackServiceVolume
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 

    try:
        # List stack service volumes
        api_response = api_instance.list_stack_service_volumes(id)
        print("The response of StackServicesApi->list_stack_service_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_service_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[StackServiceVolume]**](StackServiceVolume.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stack service volumes |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_services**
> List[StackService] list_stack_services(stack_rev_id)

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
    api_instance = wodby.StackServicesApi(api_client)
    stack_rev_id = 56 # int | 

    try:
        # List stack services
        api_response = api_instance.list_stack_services(stack_rev_id)
        print("The response of StackServicesApi->list_stack_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->list_stack_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_rev_id** | **int**|  | 

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

# **set_stack_service_config**
> OperationResult set_stack_service_config(id, name, stack_service_config_input)

Set stack service config

Sets a named config override for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.stack_service_config_input import StackServiceConfigInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    stack_service_config_input = wodby.StackServiceConfigInput() # StackServiceConfigInput | 

    try:
        # Set stack service config
        api_response = api_instance.set_stack_service_config(id, name, stack_service_config_input)
        print("The response of StackServicesApi->set_stack_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->set_stack_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **stack_service_config_input** | [**StackServiceConfigInput**](StackServiceConfigInput.md)|  | 

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
**200** | Update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_stack_service_link**
> OperationResult set_stack_service_link(id, name, stack_service_link_input)

Set stack service link

Links or unlinks another stack service for a named link slot.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.stack_service_link_input import StackServiceLinkInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    stack_service_link_input = wodby.StackServiceLinkInput() # StackServiceLinkInput | 

    try:
        # Set stack service link
        api_response = api_instance.set_stack_service_link(id, name, stack_service_link_input)
        print("The response of StackServicesApi->set_stack_service_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->set_stack_service_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **stack_service_link_input** | [**StackServiceLinkInput**](StackServiceLinkInput.md)|  | 

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
**200** | Update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_stack_service_options**
> OperationResult set_stack_service_options(id, stack_service_options_input)

Update stack service options

Replaces stack service option settings.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.stack_service_options_input import StackServiceOptionsInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    stack_service_options_input = wodby.StackServiceOptionsInput() # StackServiceOptionsInput | 

    try:
        # Update stack service options
        api_response = api_instance.set_stack_service_options(id, stack_service_options_input)
        print("The response of StackServicesApi->set_stack_service_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->set_stack_service_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **stack_service_options_input** | [**StackServiceOptionsInput**](StackServiceOptionsInput.md)|  | 

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
**200** | Update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_stack_service_resources**
> OperationResult set_stack_service_resources(id, resources_input)

Set stack service resources

Sets CPU and memory requests or limits for a stack service container.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.resources_input import ResourcesInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    resources_input = wodby.ResourcesInput() # ResourcesInput | 

    try:
        # Set stack service resources
        api_response = api_instance.set_stack_service_resources(id, resources_input)
        print("The response of StackServicesApi->set_stack_service_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->set_stack_service_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **resources_input** | [**ResourcesInput**](ResourcesInput.md)|  | 

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
**200** | Update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_stack_service_setting**
> OperationResult set_stack_service_setting(id, name, set_nullable_string_value_input)

Set stack service setting

Sets or clears a named setting value for a stack service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.set_nullable_string_value_input import SetNullableStringValueInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    set_nullable_string_value_input = wodby.SetNullableStringValueInput() # SetNullableStringValueInput | 

    try:
        # Set stack service setting
        api_response = api_instance.set_stack_service_setting(id, name, set_nullable_string_value_input)
        print("The response of StackServicesApi->set_stack_service_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->set_stack_service_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **set_nullable_string_value_input** | [**SetNullableStringValueInput**](SetNullableStringValueInput.md)|  | 

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
**200** | Update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_stack_service_volume**
> OperationResult set_stack_service_volume(id, name, stack_service_volume_input)

Set stack service volume

Sets or clears a stack service volume size.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.stack_service_volume_input import StackServiceVolumeInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    stack_service_volume_input = wodby.StackServiceVolumeInput() # StackServiceVolumeInput | 

    try:
        # Set stack service volume
        api_response = api_instance.set_stack_service_volume(id, name, stack_service_volume_input)
        print("The response of StackServicesApi->set_stack_service_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->set_stack_service_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **stack_service_volume_input** | [**StackServiceVolumeInput**](StackServiceVolumeInput.md)|  | 

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
**200** | Update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_service**
> StackService update_stack_service(id, stack_service_input)

Update stack service

Updates the stack service and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service import StackService
from wodby.models.stack_service_input import StackServiceInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    stack_service_input = wodby.StackServiceInput() # StackServiceInput | 

    try:
        # Update stack service
        api_response = api_instance.update_stack_service(id, stack_service_input)
        print("The response of StackServicesApi->update_stack_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->update_stack_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **stack_service_input** | [**StackServiceInput**](StackServiceInput.md)|  | 

### Return type

[**StackService**](StackService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated stack service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_service_cron_schedule**
> StackServiceCronSchedule update_stack_service_cron_schedule(id, update_stack_service_cron_schedule_input)

Update stack service cron schedule

Updates a stack service cron schedule.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_cron_schedule import StackServiceCronSchedule
from wodby.models.update_stack_service_cron_schedule_input import UpdateStackServiceCronScheduleInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    update_stack_service_cron_schedule_input = wodby.UpdateStackServiceCronScheduleInput() # UpdateStackServiceCronScheduleInput | 

    try:
        # Update stack service cron schedule
        api_response = api_instance.update_stack_service_cron_schedule(id, update_stack_service_cron_schedule_input)
        print("The response of StackServicesApi->update_stack_service_cron_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->update_stack_service_cron_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_stack_service_cron_schedule_input** | [**UpdateStackServiceCronScheduleInput**](UpdateStackServiceCronScheduleInput.md)|  | 

### Return type

[**StackServiceCronSchedule**](StackServiceCronSchedule.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated stack service cron schedule |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_service_env_var**
> StackServiceEnvVar update_stack_service_env_var(id, update_stack_service_env_var_input)

Update stack service env var

Updates a stack service environment variable.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_env_var import StackServiceEnvVar
from wodby.models.update_stack_service_env_var_input import UpdateStackServiceEnvVarInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    update_stack_service_env_var_input = wodby.UpdateStackServiceEnvVarInput() # UpdateStackServiceEnvVarInput | 

    try:
        # Update stack service env var
        api_response = api_instance.update_stack_service_env_var(id, update_stack_service_env_var_input)
        print("The response of StackServicesApi->update_stack_service_env_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->update_stack_service_env_var: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_stack_service_env_var_input** | [**UpdateStackServiceEnvVarInput**](UpdateStackServiceEnvVarInput.md)|  | 

### Return type

[**StackServiceEnvVar**](StackServiceEnvVar.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated stack service env var |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_service_helm_value**
> StackServiceHelmValue update_stack_service_helm_value(id, update_secret_value_input)

Update stack service Helm value

Updates a stack service Helm value override.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_helm_value import StackServiceHelmValue
from wodby.models.update_secret_value_input import UpdateSecretValueInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    update_secret_value_input = wodby.UpdateSecretValueInput() # UpdateSecretValueInput | 

    try:
        # Update stack service Helm value
        api_response = api_instance.update_stack_service_helm_value(id, update_secret_value_input)
        print("The response of StackServicesApi->update_stack_service_helm_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->update_stack_service_helm_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_secret_value_input** | [**UpdateSecretValueInput**](UpdateSecretValueInput.md)|  | 

### Return type

[**StackServiceHelmValue**](StackServiceHelmValue.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated stack service Helm value |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_service_token**
> StackServiceToken update_stack_service_token(id, update_stack_service_token_input)

Update stack service token

Updates a stack service token value, secret flag, or regex.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.stack_service_token import StackServiceToken
from wodby.models.update_stack_service_token_input import UpdateStackServiceTokenInput
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
    api_instance = wodby.StackServicesApi(api_client)
    id = 56 # int | 
    update_stack_service_token_input = wodby.UpdateStackServiceTokenInput() # UpdateStackServiceTokenInput | 

    try:
        # Update stack service token
        api_response = api_instance.update_stack_service_token(id, update_stack_service_token_input)
        print("The response of StackServicesApi->update_stack_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StackServicesApi->update_stack_service_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_stack_service_token_input** | [**UpdateStackServiceTokenInput**](UpdateStackServiceTokenInput.md)|  | 

### Return type

[**StackServiceToken**](StackServiceToken.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated stack service token |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

