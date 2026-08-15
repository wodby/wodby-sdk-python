# wodby.AppServicesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_app_service_volume**](AppServicesApi.md#add_app_service_volume) | **POST** /app-services/{id}/volumes | Add an optional app service volume
[**create_app_service_annotation**](AppServicesApi.md#create_app_service_annotation) | **POST** /app-services/{id}/annotations | Create app service annotation
[**create_app_service_cron_schedule**](AppServicesApi.md#create_app_service_cron_schedule) | **POST** /app-services/{id}/cron-schedules | Create app service cron schedule
[**create_app_service_env_var**](AppServicesApi.md#create_app_service_env_var) | **POST** /app-services/{id}/env-vars | Create app service env var
[**create_app_service_helm_value**](AppServicesApi.md#create_app_service_helm_value) | **POST** /app-services/{id}/helm-values | Create app service Helm value
[**create_app_service_integration**](AppServicesApi.md#create_app_service_integration) | **POST** /app-services/{id}/integrations | Create app service integration
[**create_app_service_log_stream**](AppServicesApi.md#create_app_service_log_stream) | **POST** /app-services/{id}/log-streams | Create app service log stream
[**create_app_service_token**](AppServicesApi.md#create_app_service_token) | **POST** /app-services/{id}/tokens | Create app service token
[**delete_app_service_annotation**](AppServicesApi.md#delete_app_service_annotation) | **DELETE** /app-service-annotations/{id} | Delete app service annotation
[**delete_app_service_cron_schedule**](AppServicesApi.md#delete_app_service_cron_schedule) | **DELETE** /app-service-cron-schedules/{id} | Delete app service cron schedule
[**delete_app_service_env_var**](AppServicesApi.md#delete_app_service_env_var) | **DELETE** /app-service-env-vars/{id} | Delete app service env var
[**delete_app_service_helm_value**](AppServicesApi.md#delete_app_service_helm_value) | **DELETE** /app-service-helm-values/{id} | Delete app service Helm value
[**delete_app_service_integration**](AppServicesApi.md#delete_app_service_integration) | **DELETE** /app-service-integrations/{id} | Delete app service integration
[**delete_app_service_token**](AppServicesApi.md#delete_app_service_token) | **DELETE** /app-service-tokens/{id} | Delete app service token
[**get_app_service**](AppServicesApi.md#get_app_service) | **GET** /app-services/{id} | Get app service
[**get_app_service_cron_job**](AppServicesApi.md#get_app_service_cron_job) | **GET** /app-service-cron-jobs/{id} | Get app service cron job
[**keep_log_stream_alive**](AppServicesApi.md#keep_log_stream_alive) | **POST** /log-streams/{id}/keep-alive | Keep log stream alive
[**list_app_service_annotations**](AppServicesApi.md#list_app_service_annotations) | **GET** /app-services/{id}/annotations | List app service annotations
[**list_app_service_configs**](AppServicesApi.md#list_app_service_configs) | **GET** /app-services/{id}/configs | List app service configs
[**list_app_service_containers**](AppServicesApi.md#list_app_service_containers) | **GET** /app-services/{id}/containers | List app service containers
[**list_app_service_cron_jobs**](AppServicesApi.md#list_app_service_cron_jobs) | **GET** /app-service-cron-jobs | List app service cron jobs
[**list_app_service_cron_schedules**](AppServicesApi.md#list_app_service_cron_schedules) | **GET** /app-services/{id}/cron-schedules | List app service cron schedules
[**list_app_service_env_vars**](AppServicesApi.md#list_app_service_env_vars) | **GET** /app-services/{id}/env-vars | List app service env vars
[**list_app_service_helm_values**](AppServicesApi.md#list_app_service_helm_values) | **GET** /app-services/{id}/helm-values | List app service Helm values
[**list_app_service_integrations**](AppServicesApi.md#list_app_service_integrations) | **GET** /app-services/{id}/integrations | List app service integrations
[**list_app_service_links**](AppServicesApi.md#list_app_service_links) | **GET** /app-services/{id}/links | List app service links
[**list_app_service_settings**](AppServicesApi.md#list_app_service_settings) | **GET** /app-services/{id}/settings | List app service settings
[**list_app_service_tokens**](AppServicesApi.md#list_app_service_tokens) | **GET** /app-services/{id}/tokens | List app service tokens
[**list_app_service_volume_storage_classes**](AppServicesApi.md#list_app_service_volume_storage_classes) | **GET** /app-services/{id}/options/volume-storage-classes | List app service volume storage-class state
[**list_app_service_volumes**](AppServicesApi.md#list_app_service_volumes) | **GET** /app-services/{id}/volumes | List app service volumes
[**list_app_services**](AppServicesApi.md#list_app_services) | **GET** /app-services | List app services
[**run_app_service_action**](AppServicesApi.md#run_app_service_action) | **POST** /app-services/{id}/actions/{name} | Run app service action
[**run_app_service_cron_schedule**](AppServicesApi.md#run_app_service_cron_schedule) | **POST** /app-service-cron-schedules/{id}/run | Run app service cron schedule
[**set_app_service_config**](AppServicesApi.md#set_app_service_config) | **PUT** /app-services/{id}/configs/{name} | Set app service config
[**set_app_service_link**](AppServicesApi.md#set_app_service_link) | **PUT** /app-services/{id}/links/{name} | Set app service link
[**set_app_service_resources**](AppServicesApi.md#set_app_service_resources) | **PUT** /app-services/{id}/resources | Set app service resources
[**set_app_service_setting**](AppServicesApi.md#set_app_service_setting) | **PUT** /app-services/{id}/settings/{name} | Set app service setting
[**start_log_stream**](AppServicesApi.md#start_log_stream) | **POST** /log-streams/{id}/start | Start log stream
[**stop_log_stream**](AppServicesApi.md#stop_log_stream) | **POST** /log-streams/{id}/stop | Stop log stream
[**update_app_service**](AppServicesApi.md#update_app_service) | **PUT** /app-services/{id} | Update app service
[**update_app_service_cron_schedule**](AppServicesApi.md#update_app_service_cron_schedule) | **PUT** /app-service-cron-schedules/{id} | Update app service cron schedule
[**update_app_service_database**](AppServicesApi.md#update_app_service_database) | **PUT** /app-services/{id}/database | Update app service database references
[**update_app_service_env_var**](AppServicesApi.md#update_app_service_env_var) | **PUT** /app-service-env-vars/{id} | Update app service env var
[**update_app_service_helm_value**](AppServicesApi.md#update_app_service_helm_value) | **PUT** /app-service-helm-values/{id} | Update app service Helm value
[**update_app_service_token**](AppServicesApi.md#update_app_service_token) | **PUT** /app-service-tokens/{id} | Update app service token


# **add_app_service_volume**
> OperationResult add_app_service_volume(id, add_app_service_volume_input)

Add an optional app service volume

Adds a volume that is optional in the service manifest and returns the reconciliation task identifier.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.add_app_service_volume_input import AddAppServiceVolumeInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    add_app_service_volume_input = wodby.AddAppServiceVolumeInput() # AddAppServiceVolumeInput | 

    try:
        # Add an optional app service volume
        api_response = api_instance.add_app_service_volume(id, add_app_service_volume_input)
        print("The response of AppServicesApi->add_app_service_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->add_app_service_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **add_app_service_volume_input** | [**AddAppServiceVolumeInput**](AddAppServiceVolumeInput.md)|  | 

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
**201** | Volume reconciliation task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_service_annotation**
> AppServiceAnnotation create_app_service_annotation(id, new_annotation_input)

Create app service annotation

Creates an annotation for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_annotation import AppServiceAnnotation
from wodby.models.new_annotation_input import NewAnnotationInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    new_annotation_input = wodby.NewAnnotationInput() # NewAnnotationInput | 

    try:
        # Create app service annotation
        api_response = api_instance.create_app_service_annotation(id, new_annotation_input)
        print("The response of AppServicesApi->create_app_service_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->create_app_service_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_annotation_input** | [**NewAnnotationInput**](NewAnnotationInput.md)|  | 

### Return type

[**AppServiceAnnotation**](AppServiceAnnotation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app service annotation |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_service_cron_schedule**
> AppServiceCronSchedule create_app_service_cron_schedule(id, new_app_service_cron_schedule_input)

Create app service cron schedule

Creates a cron schedule for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_cron_schedule import AppServiceCronSchedule
from wodby.models.new_app_service_cron_schedule_input import NewAppServiceCronScheduleInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    new_app_service_cron_schedule_input = wodby.NewAppServiceCronScheduleInput() # NewAppServiceCronScheduleInput | 

    try:
        # Create app service cron schedule
        api_response = api_instance.create_app_service_cron_schedule(id, new_app_service_cron_schedule_input)
        print("The response of AppServicesApi->create_app_service_cron_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->create_app_service_cron_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_app_service_cron_schedule_input** | [**NewAppServiceCronScheduleInput**](NewAppServiceCronScheduleInput.md)|  | 

### Return type

[**AppServiceCronSchedule**](AppServiceCronSchedule.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app service cron schedule |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_service_env_var**
> AppServiceEnvVar create_app_service_env_var(id, new_app_service_env_var_input)

Create app service env var

Creates an environment variable for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_env_var import AppServiceEnvVar
from wodby.models.new_app_service_env_var_input import NewAppServiceEnvVarInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    new_app_service_env_var_input = wodby.NewAppServiceEnvVarInput() # NewAppServiceEnvVarInput | 

    try:
        # Create app service env var
        api_response = api_instance.create_app_service_env_var(id, new_app_service_env_var_input)
        print("The response of AppServicesApi->create_app_service_env_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->create_app_service_env_var: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_app_service_env_var_input** | [**NewAppServiceEnvVarInput**](NewAppServiceEnvVarInput.md)|  | 

### Return type

[**AppServiceEnvVar**](AppServiceEnvVar.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app service env var |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_service_helm_value**
> AppServiceHelmValue create_app_service_helm_value(id, named_secret_value_input)

Create app service Helm value

Creates a Helm value override for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_helm_value import AppServiceHelmValue
from wodby.models.named_secret_value_input import NamedSecretValueInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    named_secret_value_input = wodby.NamedSecretValueInput() # NamedSecretValueInput | 

    try:
        # Create app service Helm value
        api_response = api_instance.create_app_service_helm_value(id, named_secret_value_input)
        print("The response of AppServicesApi->create_app_service_helm_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->create_app_service_helm_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **named_secret_value_input** | [**NamedSecretValueInput**](NamedSecretValueInput.md)|  | 

### Return type

[**AppServiceHelmValue**](AppServiceHelmValue.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app service Helm value |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_service_integration**
> AppServiceIntegration create_app_service_integration(id, integration_link_input)

Create app service integration

Links an integration to an app service integration slot.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_integration import AppServiceIntegration
from wodby.models.integration_link_input import IntegrationLinkInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    integration_link_input = wodby.IntegrationLinkInput() # IntegrationLinkInput | 

    try:
        # Create app service integration
        api_response = api_instance.create_app_service_integration(id, integration_link_input)
        print("The response of AppServicesApi->create_app_service_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->create_app_service_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **integration_link_input** | [**IntegrationLinkInput**](IntegrationLinkInput.md)|  | 

### Return type

[**AppServiceIntegration**](AppServiceIntegration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app service integration |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_service_log_stream**
> LogStream create_app_service_log_stream(id, new_app_service_log_stream_input=new_app_service_log_stream_input)

Create app service log stream

Creates a log stream for an app service container across all replicas or for one selected pod and returns the stream id. Log streams are available while the app instance status is ok or deploying.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.log_stream import LogStream
from wodby.models.new_app_service_log_stream_input import NewAppServiceLogStreamInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    new_app_service_log_stream_input = wodby.NewAppServiceLogStreamInput() # NewAppServiceLogStreamInput |  (optional)

    try:
        # Create app service log stream
        api_response = api_instance.create_app_service_log_stream(id, new_app_service_log_stream_input=new_app_service_log_stream_input)
        print("The response of AppServicesApi->create_app_service_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->create_app_service_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_app_service_log_stream_input** | [**NewAppServiceLogStreamInput**](NewAppServiceLogStreamInput.md)|  | [optional] 

### Return type

[**LogStream**](LogStream.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created log stream |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_service_token**
> AppServiceToken create_app_service_token(id, named_secret_value_input)

Create app service token

Creates a token for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_token import AppServiceToken
from wodby.models.named_secret_value_input import NamedSecretValueInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    named_secret_value_input = wodby.NamedSecretValueInput() # NamedSecretValueInput | 

    try:
        # Create app service token
        api_response = api_instance.create_app_service_token(id, named_secret_value_input)
        print("The response of AppServicesApi->create_app_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->create_app_service_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **named_secret_value_input** | [**NamedSecretValueInput**](NamedSecretValueInput.md)|  | 

### Return type

[**AppServiceToken**](AppServiceToken.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app service token |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_service_annotation**
> OperationResult delete_app_service_annotation(id)

Delete app service annotation

Deletes an app service annotation.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app service annotation
        api_response = api_instance.delete_app_service_annotation(id)
        print("The response of AppServicesApi->delete_app_service_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->delete_app_service_annotation: %s\n" % e)
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

# **delete_app_service_cron_schedule**
> OperationResult delete_app_service_cron_schedule(id)

Delete app service cron schedule

Deletes an app service cron schedule.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app service cron schedule
        api_response = api_instance.delete_app_service_cron_schedule(id)
        print("The response of AppServicesApi->delete_app_service_cron_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->delete_app_service_cron_schedule: %s\n" % e)
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

# **delete_app_service_env_var**
> OperationResult delete_app_service_env_var(id)

Delete app service env var

Deletes an app service environment variable.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app service env var
        api_response = api_instance.delete_app_service_env_var(id)
        print("The response of AppServicesApi->delete_app_service_env_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->delete_app_service_env_var: %s\n" % e)
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

# **delete_app_service_helm_value**
> OperationResult delete_app_service_helm_value(id)

Delete app service Helm value

Deletes an app service Helm value override.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app service Helm value
        api_response = api_instance.delete_app_service_helm_value(id)
        print("The response of AppServicesApi->delete_app_service_helm_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->delete_app_service_helm_value: %s\n" % e)
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

# **delete_app_service_integration**
> OperationResult delete_app_service_integration(id)

Delete app service integration

Removes an integration link from an app service.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app service integration
        api_response = api_instance.delete_app_service_integration(id)
        print("The response of AppServicesApi->delete_app_service_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->delete_app_service_integration: %s\n" % e)
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

# **delete_app_service_token**
> OperationResult delete_app_service_token(id)

Delete app service token

Deletes an app service token.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Delete app service token
        api_response = api_instance.delete_app_service_token(id)
        print("The response of AppServicesApi->delete_app_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->delete_app_service_token: %s\n" % e)
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

# **get_app_service**
> AppService get_app_service(id)

Get app service

Returns the app service identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service import AppService
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Get app service
        api_response = api_instance.get_app_service(id)
        print("The response of AppServicesApi->get_app_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->get_app_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppService**](AppService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_service_cron_job**
> AppServiceCronJob get_app_service_cron_job(id)

Get app service cron job

Returns the app service cron job identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_cron_job import AppServiceCronJob
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Get app service cron job
        api_response = api_instance.get_app_service_cron_job(id)
        print("The response of AppServicesApi->get_app_service_cron_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->get_app_service_cron_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppServiceCronJob**](AppServiceCronJob.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App service cron job |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keep_log_stream_alive**
> OperationResult keep_log_stream_alive(id)

Keep log stream alive

Extends an existing log stream lease.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Keep log stream alive
        api_response = api_instance.keep_log_stream_alive(id)
        print("The response of AppServicesApi->keep_log_stream_alive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->keep_log_stream_alive: %s\n" % e)
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
**200** | Keep-alive result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_annotations**
> List[AppServiceAnnotation] list_app_service_annotations(id)

List app service annotations

Returns annotations configured for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_annotation import AppServiceAnnotation
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service annotations
        api_response = api_instance.list_app_service_annotations(id)
        print("The response of AppServicesApi->list_app_service_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceAnnotation]**](AppServiceAnnotation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service annotations |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_configs**
> List[AppServiceConfig] list_app_service_configs(id)

List app service configs

Returns config overrides for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_config import AppServiceConfig
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service configs
        api_response = api_instance.list_app_service_configs(id)
        print("The response of AppServicesApi->list_app_service_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceConfig]**](AppServiceConfig.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service configs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_containers**
> List[AppServiceContainer] list_app_service_containers(id)

List app service containers

Returns container resource settings for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_container import AppServiceContainer
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service containers
        api_response = api_instance.list_app_service_containers(id)
        print("The response of AppServicesApi->list_app_service_containers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_containers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceContainer]**](AppServiceContainer.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service containers |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_cron_jobs**
> AppServiceCronJobsResponse list_app_service_cron_jobs(app_instance_id=app_instance_id, app_service_id=app_service_id, schedule_id=schedule_id, page=page, page_size=page_size)

List app service cron jobs

Returns app service cron jobs matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_cron_jobs_response import AppServiceCronJobsResponse
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
    api_instance = wodby.AppServicesApi(api_client)
    app_instance_id = 56 # int |  (optional)
    app_service_id = 56 # int |  (optional)
    schedule_id = 56 # int |  (optional)
    page = 56 # int | Page number, defaults to 1 (optional)
    page_size = 56 # int | Page size, defaults to 30 (optional)

    try:
        # List app service cron jobs
        api_response = api_instance.list_app_service_cron_jobs(app_instance_id=app_instance_id, app_service_id=app_service_id, schedule_id=schedule_id, page=page, page_size=page_size)
        print("The response of AppServicesApi->list_app_service_cron_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_cron_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | [optional] 
 **app_service_id** | **int**|  | [optional] 
 **schedule_id** | **int**|  | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 30 | [optional] 

### Return type

[**AppServiceCronJobsResponse**](AppServiceCronJobsResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App service cron jobs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_cron_schedules**
> List[AppServiceCronSchedule] list_app_service_cron_schedules(id)

List app service cron schedules

Returns cron schedules configured for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_cron_schedule import AppServiceCronSchedule
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service cron schedules
        api_response = api_instance.list_app_service_cron_schedules(id)
        print("The response of AppServicesApi->list_app_service_cron_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_cron_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceCronSchedule]**](AppServiceCronSchedule.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service cron schedules |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_env_vars**
> List[AppServiceEnvVar] list_app_service_env_vars(id)

List app service env vars

Returns environment variables configured for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_env_var import AppServiceEnvVar
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service env vars
        api_response = api_instance.list_app_service_env_vars(id)
        print("The response of AppServicesApi->list_app_service_env_vars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_env_vars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceEnvVar]**](AppServiceEnvVar.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service env vars |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_helm_values**
> List[AppServiceHelmValue] list_app_service_helm_values(id)

List app service Helm values

Returns Helm values configured for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_helm_value import AppServiceHelmValue
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service Helm values
        api_response = api_instance.list_app_service_helm_values(id)
        print("The response of AppServicesApi->list_app_service_helm_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_helm_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceHelmValue]**](AppServiceHelmValue.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service Helm values |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_integrations**
> List[AppServiceIntegration] list_app_service_integrations(id)

List app service integrations

Returns integration links configured for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_integration import AppServiceIntegration
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service integrations
        api_response = api_instance.list_app_service_integrations(id)
        print("The response of AppServicesApi->list_app_service_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceIntegration]**](AppServiceIntegration.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service integrations |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_links**
> List[AppServiceLink] list_app_service_links(id)

List app service links

Returns service links configured for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_link import AppServiceLink
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service links
        api_response = api_instance.list_app_service_links(id)
        print("The response of AppServicesApi->list_app_service_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceLink]**](AppServiceLink.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service links |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_settings**
> List[AppServiceSetting] list_app_service_settings(id)

List app service settings

Returns settings configured for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_setting import AppServiceSetting
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service settings
        api_response = api_instance.list_app_service_settings(id)
        print("The response of AppServicesApi->list_app_service_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceSetting]**](AppServiceSetting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_tokens**
> List[AppServiceToken] list_app_service_tokens(id)

List app service tokens

Returns tokens configured for an app service without revealing secret values.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_token import AppServiceToken
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service tokens
        api_response = api_instance.list_app_service_tokens(id)
        print("The response of AppServicesApi->list_app_service_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceToken]**](AppServiceToken.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service tokens |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_volume_storage_classes**
> List[AppServiceVolumeStorageClassState] list_app_service_volume_storage_classes(id)

List app service volume storage-class state

Returns configured and effective storage-class choices for each app service volume.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_volume_storage_class_state import AppServiceVolumeStorageClassState
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service volume storage-class state
        api_response = api_instance.list_app_service_volume_storage_classes(id)
        print("The response of AppServicesApi->list_app_service_volume_storage_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_volume_storage_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceVolumeStorageClassState]**](AppServiceVolumeStorageClassState.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volume storage-class state |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_service_volumes**
> List[AppServiceVolume] list_app_service_volumes(id)

List app service volumes

Returns configured volume metadata together with effective Kubernetes storage-class state.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_volume import AppServiceVolume
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # List app service volumes
        api_response = api_instance.list_app_service_volumes(id)
        print("The response of AppServicesApi->list_app_service_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_service_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[AppServiceVolume]**](AppServiceVolume.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app service volumes |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_services**
> List[AppService] list_app_services(app_instance_id)

List app services

Returns app services matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service import AppService
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
    api_instance = wodby.AppServicesApi(api_client)
    app_instance_id = 56 # int | 

    try:
        # List app services
        api_response = api_instance.list_app_services(app_instance_id)
        print("The response of AppServicesApi->list_app_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->list_app_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **int**|  | 

### Return type

[**List[AppService]**](AppService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app services |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_app_service_action**
> OperationResult run_app_service_action(id, name)

Run app service action

Runs the named action for an app service.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 

    try:
        # Run app service action
        api_response = api_instance.run_app_service_action(id, name)
        print("The response of AppServicesApi->run_app_service_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->run_app_service_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 

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
**201** | Action task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_app_service_cron_schedule**
> Task run_app_service_cron_schedule(id)

Run app service cron schedule

Runs an app service cron schedule immediately and returns the created task.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.task import Task
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Run app service cron schedule
        api_response = api_instance.run_app_service_cron_schedule(id)
        print("The response of AppServicesApi->run_app_service_cron_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->run_app_service_cron_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cron run task |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_app_service_config**
> OperationResult set_app_service_config(id, name, config_override_input)

Set app service config

Sets or disables a named config override for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.config_override_input import ConfigOverrideInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    config_override_input = wodby.ConfigOverrideInput() # ConfigOverrideInput | 

    try:
        # Set app service config
        api_response = api_instance.set_app_service_config(id, name, config_override_input)
        print("The response of AppServicesApi->set_app_service_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->set_app_service_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **config_override_input** | [**ConfigOverrideInput**](ConfigOverrideInput.md)|  | 

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

# **set_app_service_link**
> OperationResult set_app_service_link(id, name, app_service_link_input)

Set app service link

Links or unlinks another app service for a named link slot.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_link_input import AppServiceLinkInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    app_service_link_input = wodby.AppServiceLinkInput() # AppServiceLinkInput | 

    try:
        # Set app service link
        api_response = api_instance.set_app_service_link(id, name, app_service_link_input)
        print("The response of AppServicesApi->set_app_service_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->set_app_service_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **app_service_link_input** | [**AppServiceLinkInput**](AppServiceLinkInput.md)|  | 

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

# **set_app_service_resources**
> OperationResult set_app_service_resources(id, resources_input)

Set app service resources

Sets CPU and memory requests or limits for an app service container.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    resources_input = wodby.ResourcesInput() # ResourcesInput | 

    try:
        # Set app service resources
        api_response = api_instance.set_app_service_resources(id, resources_input)
        print("The response of AppServicesApi->set_app_service_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->set_app_service_resources: %s\n" % e)
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

# **set_app_service_setting**
> AppServiceSetting set_app_service_setting(id, name, set_string_value_input)

Set app service setting

Sets a named setting value for an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_setting import AppServiceSetting
from wodby.models.set_string_value_input import SetStringValueInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    name = 'name_example' # str | 
    set_string_value_input = wodby.SetStringValueInput() # SetStringValueInput | 

    try:
        # Set app service setting
        api_response = api_instance.set_app_service_setting(id, name, set_string_value_input)
        print("The response of AppServicesApi->set_app_service_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->set_app_service_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **set_string_value_input** | [**SetStringValueInput**](SetStringValueInput.md)|  | 

### Return type

[**AppServiceSetting**](AppServiceSetting.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app service setting |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_log_stream**
> OperationResult start_log_stream(id)

Start log stream

Starts an existing log stream.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Start log stream
        api_response = api_instance.start_log_stream(id)
        print("The response of AppServicesApi->start_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->start_log_stream: %s\n" % e)
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
**200** | Start result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_log_stream**
> OperationResult stop_log_stream(id)

Stop log stream

Stops an existing log stream.

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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 

    try:
        # Stop log stream
        api_response = api_instance.stop_log_stream(id)
        print("The response of AppServicesApi->stop_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->stop_log_stream: %s\n" % e)
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
**200** | Stop result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_service**
> AppService update_app_service(id, app_service_input)

Update app service

Updates the app service and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service import AppService
from wodby.models.app_service_input import AppServiceInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    app_service_input = wodby.AppServiceInput() # AppServiceInput | 

    try:
        # Update app service
        api_response = api_instance.update_app_service(id, app_service_input)
        print("The response of AppServicesApi->update_app_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->update_app_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_service_input** | [**AppServiceInput**](AppServiceInput.md)|  | 

### Return type

[**AppService**](AppService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_service_cron_schedule**
> AppServiceCronSchedule update_app_service_cron_schedule(id, update_app_service_cron_schedule_input)

Update app service cron schedule

Updates an app service cron schedule.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_cron_schedule import AppServiceCronSchedule
from wodby.models.update_app_service_cron_schedule_input import UpdateAppServiceCronScheduleInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    update_app_service_cron_schedule_input = wodby.UpdateAppServiceCronScheduleInput() # UpdateAppServiceCronScheduleInput | 

    try:
        # Update app service cron schedule
        api_response = api_instance.update_app_service_cron_schedule(id, update_app_service_cron_schedule_input)
        print("The response of AppServicesApi->update_app_service_cron_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->update_app_service_cron_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_service_cron_schedule_input** | [**UpdateAppServiceCronScheduleInput**](UpdateAppServiceCronScheduleInput.md)|  | 

### Return type

[**AppServiceCronSchedule**](AppServiceCronSchedule.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app service cron schedule |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_service_database**
> AppService update_app_service_database(id, update_app_service_database_input)

Update app service database references

Updates the database DB and user references used by an app service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service import AppService
from wodby.models.update_app_service_database_input import UpdateAppServiceDatabaseInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    update_app_service_database_input = wodby.UpdateAppServiceDatabaseInput() # UpdateAppServiceDatabaseInput | 

    try:
        # Update app service database references
        api_response = api_instance.update_app_service_database(id, update_app_service_database_input)
        print("The response of AppServicesApi->update_app_service_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->update_app_service_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_service_database_input** | [**UpdateAppServiceDatabaseInput**](UpdateAppServiceDatabaseInput.md)|  | 

### Return type

[**AppService**](AppService.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app service |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_service_env_var**
> AppServiceEnvVar update_app_service_env_var(id, update_app_service_env_var_input)

Update app service env var

Updates an app service environment variable.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_env_var import AppServiceEnvVar
from wodby.models.update_app_service_env_var_input import UpdateAppServiceEnvVarInput
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    update_app_service_env_var_input = wodby.UpdateAppServiceEnvVarInput() # UpdateAppServiceEnvVarInput | 

    try:
        # Update app service env var
        api_response = api_instance.update_app_service_env_var(id, update_app_service_env_var_input)
        print("The response of AppServicesApi->update_app_service_env_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->update_app_service_env_var: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_app_service_env_var_input** | [**UpdateAppServiceEnvVarInput**](UpdateAppServiceEnvVarInput.md)|  | 

### Return type

[**AppServiceEnvVar**](AppServiceEnvVar.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app service env var |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_service_helm_value**
> AppServiceHelmValue update_app_service_helm_value(id, update_secret_value_input)

Update app service Helm value

Updates an app service Helm value override.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_helm_value import AppServiceHelmValue
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    update_secret_value_input = wodby.UpdateSecretValueInput() # UpdateSecretValueInput | 

    try:
        # Update app service Helm value
        api_response = api_instance.update_app_service_helm_value(id, update_secret_value_input)
        print("The response of AppServicesApi->update_app_service_helm_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->update_app_service_helm_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_secret_value_input** | [**UpdateSecretValueInput**](UpdateSecretValueInput.md)|  | 

### Return type

[**AppServiceHelmValue**](AppServiceHelmValue.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app service Helm value |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_service_token**
> AppServiceToken update_app_service_token(id, update_secret_value_input)

Update app service token

Updates an app service token value or secret flag.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_service_token import AppServiceToken
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
    api_instance = wodby.AppServicesApi(api_client)
    id = 56 # int | 
    update_secret_value_input = wodby.UpdateSecretValueInput() # UpdateSecretValueInput | 

    try:
        # Update app service token
        api_response = api_instance.update_app_service_token(id, update_secret_value_input)
        print("The response of AppServicesApi->update_app_service_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppServicesApi->update_app_service_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_secret_value_input** | [**UpdateSecretValueInput**](UpdateSecretValueInput.md)|  | 

### Return type

[**AppServiceToken**](AppServiceToken.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app service token |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

