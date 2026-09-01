# wodby.AppEnvironmentsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_environment**](AppEnvironmentsApi.md#create_app_environment) | **POST** /app-environments | Create app environment
[**delete_app_environment**](AppEnvironmentsApi.md#delete_app_environment) | **DELETE** /app-environments/{id} | Delete app environment
[**get_app_environment**](AppEnvironmentsApi.md#get_app_environment) | **GET** /app-environments/{id} | Get app environment
[**get_app_environment_by_name**](AppEnvironmentsApi.md#get_app_environment_by_name) | **GET** /app-environments/by-name/{appName}/{environmentName} | Get app environment by name
[**get_app_environment_cicd_settings**](AppEnvironmentsApi.md#get_app_environment_cicd_settings) | **GET** /app-environments/cicd-settings/{id} | Get app environment CI/CD settings
[**list_app_environments**](AppEnvironmentsApi.md#list_app_environments) | **GET** /app-environments | List app environments
[**reconcile_app_environment_stack**](AppEnvironmentsApi.md#reconcile_app_environment_stack) | **POST** /app-environments/{id}/actions/reconcile-stack | Reconcile app environment stack
[**update_app_environment**](AppEnvironmentsApi.md#update_app_environment) | **PUT** /app-environments/{id} | Update app environment
[**update_app_environment_cicd_settings**](AppEnvironmentsApi.md#update_app_environment_cicd_settings) | **PUT** /app-environments/cicd-settings/{id} | Update app environment CI/CD settings
[**update_app_environment_maintenance_mode**](AppEnvironmentsApi.md#update_app_environment_maintenance_mode) | **PUT** /app-environments/{id}/actions/maintenance-mode | Update app environment maintenance mode
[**update_app_environment_settings**](AppEnvironmentsApi.md#update_app_environment_settings) | **PUT** /app-environments/settings/{id} | Update app environment settings
[**upgrade_app_environment_stack**](AppEnvironmentsApi.md#upgrade_app_environment_stack) | **POST** /app-environments/{id}/actions/upgrade-stack | Upgrade app environment stack


# **create_app_environment**
> AppEnvironment create_app_environment(new_app_environment_input)

Create app environment

Creates an app environment and returns the created resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment import AppEnvironment
from wodby.models.new_app_environment_input import NewAppEnvironmentInput
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    new_app_environment_input = wodby.NewAppEnvironmentInput() # NewAppEnvironmentInput | 

    try:
        # Create app environment
        api_response = api_instance.create_app_environment(new_app_environment_input)
        print("The response of AppEnvironmentsApi->create_app_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->create_app_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_app_environment_input** | [**NewAppEnvironmentInput**](NewAppEnvironmentInput.md)|  | 

### Return type

[**AppEnvironment**](AppEnvironment.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created app environment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_environment**
> OperationResult delete_app_environment(id, force=force)

Delete app environment

Deletes the app environment and returns the operation result.

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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 
    force = False # bool |  (optional) (default to False)

    try:
        # Delete app environment
        api_response = api_instance.delete_app_environment(id, force=force)
        print("The response of AppEnvironmentsApi->delete_app_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->delete_app_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **force** | **bool**|  | [optional] [default to False]

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

# **get_app_environment**
> AppEnvironment get_app_environment(id)

Get app environment

Returns the app environment identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment import AppEnvironment
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 

    try:
        # Get app environment
        api_response = api_instance.get_app_environment(id)
        print("The response of AppEnvironmentsApi->get_app_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->get_app_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppEnvironment**](AppEnvironment.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App environment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_environment_by_name**
> AppEnvironment get_app_environment_by_name(app_name, environment_name, org_id=org_id)

Get app environment by name

Returns the app environment identified by app and environment name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment import AppEnvironment
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    app_name = 'app_name_example' # str | 
    environment_name = 'environment_name_example' # str | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Get app environment by name
        api_response = api_instance.get_app_environment_by_name(app_name, environment_name, org_id=org_id)
        print("The response of AppEnvironmentsApi->get_app_environment_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->get_app_environment_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | 
 **environment_name** | **str**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**AppEnvironment**](AppEnvironment.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App environment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_environment_cicd_settings**
> AppEnvironmentCICDSettings get_app_environment_cicd_settings(id)

Get app environment CI/CD settings

Returns the CI and registry integrations used by future app environment builds. Integration ID 0 identifies the built-in Wodby service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment_cicd_settings import AppEnvironmentCICDSettings
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 

    try:
        # Get app environment CI/CD settings
        api_response = api_instance.get_app_environment_cicd_settings(id)
        print("The response of AppEnvironmentsApi->get_app_environment_cicd_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->get_app_environment_cicd_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppEnvironmentCICDSettings**](AppEnvironmentCICDSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App environment CI/CD settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_environments**
> List[AppEnvironment] list_app_environments(org_id=org_id, project_ids=project_ids, app_id=app_id, cluster_id=cluster_id, cluster_app=cluster_app)

List app environments

Returns app environments matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment import AppEnvironment
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    app_id = 56 # int |  (optional)
    cluster_id = 56 # int |  (optional)
    cluster_app = True # bool |  (optional)

    try:
        # List app environments
        api_response = api_instance.list_app_environments(org_id=org_id, project_ids=project_ids, app_id=app_id, cluster_id=cluster_id, cluster_app=cluster_app)
        print("The response of AppEnvironmentsApi->list_app_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->list_app_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **app_id** | **int**|  | [optional] 
 **cluster_id** | **int**|  | [optional] 
 **cluster_app** | **bool**|  | [optional] 

### Return type

[**List[AppEnvironment]**](AppEnvironment.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of app environments |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_app_environment_stack**
> OperationResult reconcile_app_environment_stack(id, app_environment_stack_reconciliation_input)

Reconcile app environment stack

Reapplies the app environment's assigned stack revision using the selected override sections without changing its stack revision.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment_stack_reconciliation_input import AppEnvironmentStackReconciliationInput
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 
    app_environment_stack_reconciliation_input = wodby.AppEnvironmentStackReconciliationInput() # AppEnvironmentStackReconciliationInput | 

    try:
        # Reconcile app environment stack
        api_response = api_instance.reconcile_app_environment_stack(id, app_environment_stack_reconciliation_input)
        print("The response of AppEnvironmentsApi->reconcile_app_environment_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->reconcile_app_environment_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_environment_stack_reconciliation_input** | [**AppEnvironmentStackReconciliationInput**](AppEnvironmentStackReconciliationInput.md)|  | 

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
**200** | Reconciliation result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_environment**
> AppEnvironment update_app_environment(id, update_title_request)

Update app environment

Updates the app environment and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment import AppEnvironment
from wodby.models.update_title_request import UpdateTitleRequest
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 
    update_title_request = wodby.UpdateTitleRequest() # UpdateTitleRequest | 

    try:
        # Update app environment
        api_response = api_instance.update_app_environment(id, update_title_request)
        print("The response of AppEnvironmentsApi->update_app_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->update_app_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_title_request** | [**UpdateTitleRequest**](UpdateTitleRequest.md)|  | 

### Return type

[**AppEnvironment**](AppEnvironment.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app environment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_environment_cicd_settings**
> AppEnvironmentCICDSettings update_app_environment_cicd_settings(id, app_environment_cicd_settings_input)

Update app environment CI/CD settings

Updates the CI and registry integrations used by future app environment builds. Integration ID 0 selects the built-in Wodby service.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment_cicd_settings import AppEnvironmentCICDSettings
from wodby.models.app_environment_cicd_settings_input import AppEnvironmentCICDSettingsInput
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 
    app_environment_cicd_settings_input = wodby.AppEnvironmentCICDSettingsInput() # AppEnvironmentCICDSettingsInput | 

    try:
        # Update app environment CI/CD settings
        api_response = api_instance.update_app_environment_cicd_settings(id, app_environment_cicd_settings_input)
        print("The response of AppEnvironmentsApi->update_app_environment_cicd_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->update_app_environment_cicd_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_environment_cicd_settings_input** | [**AppEnvironmentCICDSettingsInput**](AppEnvironmentCICDSettingsInput.md)|  | 

### Return type

[**AppEnvironmentCICDSettings**](AppEnvironmentCICDSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app environment CI/CD settings |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_environment_maintenance_mode**
> OperationResult update_app_environment_maintenance_mode(id, app_environment_maintenance_mode_input)

Update app environment maintenance mode

Enables or disables the fixed maintenance response on all public HTTP routes while application workloads continue running.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment_maintenance_mode_input import AppEnvironmentMaintenanceModeInput
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 
    app_environment_maintenance_mode_input = wodby.AppEnvironmentMaintenanceModeInput() # AppEnvironmentMaintenanceModeInput | 

    try:
        # Update app environment maintenance mode
        api_response = api_instance.update_app_environment_maintenance_mode(id, app_environment_maintenance_mode_input)
        print("The response of AppEnvironmentsApi->update_app_environment_maintenance_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->update_app_environment_maintenance_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_environment_maintenance_mode_input** | [**AppEnvironmentMaintenanceModeInput**](AppEnvironmentMaintenanceModeInput.md)|  | 

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
**200** | Maintenance mode update result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_environment_settings**
> AppEnvironment update_app_environment_settings(id, app_environment_settings_input)

Update app environment settings

Updates app environment settings and returns the updated app environment.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment import AppEnvironment
from wodby.models.app_environment_settings_input import AppEnvironmentSettingsInput
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 
    app_environment_settings_input = wodby.AppEnvironmentSettingsInput() # AppEnvironmentSettingsInput | 

    try:
        # Update app environment settings
        api_response = api_instance.update_app_environment_settings(id, app_environment_settings_input)
        print("The response of AppEnvironmentsApi->update_app_environment_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->update_app_environment_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_environment_settings_input** | [**AppEnvironmentSettingsInput**](AppEnvironmentSettingsInput.md)|  | 

### Return type

[**AppEnvironment**](AppEnvironment.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated app environment |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_app_environment_stack**
> OperationResult upgrade_app_environment_stack(id, app_environment_stack_upgrade_input)

Upgrade app environment stack

Upgrades an app environment stack using the selected upgrade sections.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.app_environment_stack_upgrade_input import AppEnvironmentStackUpgradeInput
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
    api_instance = wodby.AppEnvironmentsApi(api_client)
    id = 56 # int | 
    app_environment_stack_upgrade_input = wodby.AppEnvironmentStackUpgradeInput() # AppEnvironmentStackUpgradeInput | 

    try:
        # Upgrade app environment stack
        api_response = api_instance.upgrade_app_environment_stack(id, app_environment_stack_upgrade_input)
        print("The response of AppEnvironmentsApi->upgrade_app_environment_stack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppEnvironmentsApi->upgrade_app_environment_stack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_environment_stack_upgrade_input** | [**AppEnvironmentStackUpgradeInput**](AppEnvironmentStackUpgradeInput.md)|  | 

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
**200** | Upgrade result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

